import unittest
from ..instapy.time_util import Schedule

import json
import arrow
import time


class TestSchedule(unittest.TestCase):
    def setUp(self):
        json_file = open('/code/instabot/bot_settings.json', encoding='utf-8')
        settings = json.load(json_file)
        self.schedule = Schedule(settings["schedule"])

    def test_check_date(self):
        test_datetime = arrow.get(2017,7,14,13,0,0)
        self.assertTrue(self.schedule.check_moment_in_ranges(test_datetime))
        test_datetime = arrow.get(2017, 7, 14, 3, 0, 0)
        self.assertFalse(self.schedule.check_moment_in_ranges(test_datetime))
        print(self.schedule.schedule)

    def test_get_time_to_start_stop(self):
        test_datetime = arrow.get(2017, 7, 14, 13, 0, 0)