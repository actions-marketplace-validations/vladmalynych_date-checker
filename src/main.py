from libs import czech_holidays
from datetime import datetime

today = datetime.now()


def main():
    holidays = czech_holidays.Holidays(year=today.year)
    print(holidays)


if __name__ == '__main__':
    main()