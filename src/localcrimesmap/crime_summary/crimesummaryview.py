from django.views import View
from django.shortcuts import render, HttpResponse
import logging

from police_api.police_api_service import get_crimes_within_area, save_crimes_JSON
from .forms import CrimeSummaryForm
from common.models import Crime
from common.utils import add_miles_to_lat_lng

logger = logging.getLogger(__name__)

class CrimeSummaryView(View):
    def get_square_from_centre_point(self, centerlat, centerlng, lengthinmiles):
        corners = [45, 135, 225, 315]
        cornercoords = []
        polystring = ""

        for corner in corners:
            cornercoords.append(add_miles_to_lat_lng(centerlat, centerlng, corner, lengthinmiles))

        for cornerCood in cornercoords:
            polystring += f'{cornerCood[0]},{cornerCood[1]}:'

        return polystring.rstrip(':')

    def get(self, request):
        return render(request, 'crime_summary/summary.html', {'form': CrimeSummaryForm(auto_id="summaryform_%s"),'crime_summary':'active'})

    def post(self, request):
        form = CrimeSummaryForm(request.POST)
        if form.is_valid():
            enteredlat = form.cleaned_data['lat']
            enteredlng = form.cleaned_data['lng']
            entereddate = form.cleaned_data['date']
            entermiles = float(form.cleaned_data['radius'])

            poly = self.get_square_from_centre_point(enteredlat, enteredlng, entermiles / 2)
            crimes = get_crimes_within_area(poly, entereddate)
            crimesSaved = save_crimes_JSON(crimes)
            crime_type_list = Crime.calculate_crimeType_count(crimesSaved)

            return render(request, 'crime_summary/report.html', {'crime_type_list':crime_type_list, 'detected_crimes':crimesSaved })

        else:
            formerrors=""
            for error in form.errors():
                formerrors += f"{error},"
            logger.error(f"crime summary form is not valid:{formerrors}")
            # return 404 template with message.
