import unittest
from ..instapy.time_util import Schedule

import json
import arrow


class TestSchedule(unittest.TestCase):
    def test_check_date(self):
        json_file = open('/code/instabot/bot_settings.json', encoding='utf-8')
        settings = json.load(json_file)
        schedule = Schedule(settings["schedule"])
        test_datetime = arrow.get(2017,7,14,13,0,0)
        self.assertTrue(schedule.check_moment_in_ranges(test_datetime))
        test_datetime = arrow.get(2017, 7, 14, 3, 0, 0)
        self.assertFalse(schedule.check_moment_in_ranges(test_datetime))
        print(schedule.schedule)
