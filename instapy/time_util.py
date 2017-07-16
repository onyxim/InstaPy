"""Helper module to handle time related stuff"""
from random import gauss
from time import sleep as original_sleep
import arrow
import re

# Amount of variance to be introduced
# i.e. random time will be in the range: TIME +/- STDEV %
STDEV = 0.5


def randomize_time(mean):
    allowed_range = mean * STDEV
    stdev = allowed_range / 3  # 99.73% chance to be in the allowed range

    t = 0
    while abs(mean - t) > allowed_range:
        t = gauss(mean, stdev)

    return t


def sleep(t):
    original_sleep(randomize_time(t))


class Schedule(object):
    def __init__(self, schedule={}):
        self.schedule = schedule.copy()
        self.machine_schedule = {}
        for code, value in self.schedule:
            for str_interval in value["intervals"]:
                re_str = re.search('(.+)-(.+)',str_interval)
                time_format = 'HH:MM'
                interval = [arrow.get(re_str.group(0), time_format), arrow.get(re_str.group(1), time_format)]
                for day in code:
                    self.machine_schedule[day] = interval

    def add(self, days="", intervals=[], logic=""):
        pass

    def get(self):
        """Return your schedule dict"""
        pass

    # todo write this function
    # todo write logical optional operator fo this function
    def check_moment_in_ranges(self, now):
        """Use day codes from link https://registrar.gmu.edu/topics/days-of-the-week-codes/"""
        print(arrow.get('16:30', 'YYYY-MM-DD HH:mm:ss'))
