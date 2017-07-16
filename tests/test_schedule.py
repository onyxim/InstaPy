import unittest
from ..instapy.time_util import Schedule

import json


class TestSchedule(unittest.TestCase):
    def test_check_date(self):
        json_file = open('/code/instabot/bot_settings.json', encoding='utf-8')
        settings = json.load(json_file)
        schedule = Schedule(settings["schedule"])
        print(schedule.machine_schedule)
