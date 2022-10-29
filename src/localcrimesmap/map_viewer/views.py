from django.shortcuts import render
import logging

from common.utils import get_month_intervals

logger = logging.getLogger(__name__)

def render_map(request):
    months = get_month_intervals()
    logger.info("Rendering map...")
    return render(request, "map_viewer/map.html", {'monthIntervals':months, 'map':'active'})
