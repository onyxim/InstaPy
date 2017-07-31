import arrow
import re

class Schedule(object):
    day_code_resolve = {'M': 1, 'T': 2, 'W': 3, 'R': 4, 'F': 5, 'S': 6, 'U': 7}

    def __init__(self, schedule={}):
        """Use day codes from link https://registrar.gmu.edu/topics/days-of-the-week-codes/"""
        self.schedule = schedule.copy()
        self.machine_schedule = {}
        for code, value in self.schedule.items():
            for str_interval in value["intervals"]:
                re_str = re.findall('(..:..)', str_interval)
                time_format = 'hh:mm'
                interval = [arrow.get(re_str[0], time_format), arrow.get(re_str[1], time_format)]
                for one_letter in code:
                    day = self.day_code_resolve[one_letter]
                    self.machine_schedule[day] = self.machine_schedule.get(day, []) + [interval]

    def add(self, days="", intervals=[], logic=""):
        pass

    def get(self):
        """Return your schedule dict"""
        pass

    # todo write this function
    # todo write logical optional operator fo this function
    def check_moment_in_ranges(self, moment=arrow.get()):
        """Return True when passed date in schedule ranges for the of the passed date"""
        day = moment.isoweekday()
        for range in self.machine_schedule[day]:
            if range[0].time() < moment.time() < range[1].time():
                return True
        return False

    def sum_all_time(self, moment=arrow.get()):
        pass

    def get_time_to_start_stop(self, moment=arrow.get()):
        """Return start and stop time for current time range"""
        day = moment.isoweekday()
        moment = arrow.get(1, 1, 1, moment.time().hour, moment.time().minute, moment.time().second)
        # Ranges for a day
        ranges = self.machine_schedule[day].copy()
        for n in range(0, len(ranges) - 1):
            if moment < ranges[n][0]:
                start = (ranges[n][0] - moment).total_seconds()
                stop = ranges[n][1]
            elif ranges[n][0] < moment < ranges[n][1]:
                # Start right now. The moment is within ranges.
                start = 0
                stop = ranges[n][1]
            elif ranges[n][1] < moment < ranges[n + 1][0]:
                start = ranges[n][0] - moment
                stop = ranges[n][1]
            elif ranges[n + 1][1] < moment:
                start = ranges[n][0] - moment
                stop = ranges[n][1]
        return start, stop
