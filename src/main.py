from libs import czech_holidays
from datetime import datetime, timedelta, time

WORKING_DAYS = [
    [time(0, 0, 0), time(23, 59, 59)],   # Monday
    [time(0, 0, 0), time(23, 59, 59)],   # Tuesday
    [time(0, 0, 0), time(23, 59, 59)],   # Wednesday
    [time(0, 0, 0), time(15, 00, 00)],   # Thursday
    None,                                # Friday
    None,                                # Saturday
    None,                                # Sunday
]

TODAY = datetime.now()


def not_holiday():
    holidays = czech_holidays.Holidays(year=TODAY.year)
    tomorrow = TODAY.date() + timedelta(days=1)
    # if TODAY.date() in holidays or tomorrow in holidays:
    #     print("Holiday conditions not met.")
    #     return False
    return True


def is_working_time():
    working_day = WORKING_DAYS[TODAY.weekday()]
    if working_day:
        if working_day[0] < TODAY.time() < working_day[1]:
            return True
    print("Working time conditions not met.")
    return False


def main():
    if is_working_time() and not_holiday():
        print('Succeeded')
        exit(0)
    else:
        print('Failed')
        exit(1)


if __name__ == '__main__':
    main()
