from django.test import TestCase
from unittest import mock
import datetime
from .utils import add_miles_to_lat_lng, get_month_intervals, get_month_intervals_as_tuple
from freezegun import freeze_time

class CommonUtilsTest(TestCase):
    @freeze_time("2019-02-02")
    def test_get_month_intervals(self):
        expectedintervalnum=48
        expectedfirstinterval="2019-01"
        expectedsecondinterval="2018-12"
        expectedlastinterval="2015-02"

        intervals=get_month_intervals()

        self.assertTrue(intervals[0]==expectedfirstinterval,f"actual:{intervals[0]} expected:{expectedfirstinterval}")
        self.assertTrue(intervals[expectedintervalnum-1]==expectedlastinterval, f"actual:{intervals[expectedintervalnum-1]} expected:{expectedlastinterval}")
        self.assertTrue(intervals[1]==expectedsecondinterval, f"actual:{intervals[1]} expected:{expectedsecondinterval}")

    @freeze_time("2019-02-02")
    def test_get_month_intervals_as_tuple_list(self):
        expectedintervalnum=48
        expectedfirstinterval=("2019-01","2019-01")
        expectedsecondinterval=("2018-12","2018-12")
        expectedlastinterval=("2015-02","2015-02")

        intervals=get_month_intervals_as_tuple()

        self.assertTupleEqual(intervals[0],expectedfirstinterval,f"actual:{intervals[0]} expected:{expectedfirstinterval}")
        self.assertTupleEqual(intervals[expectedintervalnum-1],expectedlastinterval, f"actual:{intervals[expectedintervalnum-1]} expected:{expectedlastinterval}")
        self.assertTupleEqual(intervals[1],expectedsecondinterval, f"actual:{intervals[1]} expected:{expectedsecondinterval}")


    def test_add_miles_to_lat_lng(self):
        expectedLatLng=(52,-2.5)

        # point should be around 21.5 miles to the left of the original point (ie bearing 270).
        actualLatLng=add_miles_to_lat_lng(52,-2,270,21.5)

        # the new points position doesn't need to be completely accurate for current use case, so testing within a range is fine.
        self.assertTrue(51.9 <= actualLatLng[0] <= 52.1)
        self.assertTrue(-2.51 <= actualLatLng[1] <= -2.49)
        
