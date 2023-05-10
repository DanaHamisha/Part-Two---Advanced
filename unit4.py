from datetime import datetime


# ex1
def gen_secs():
    """Generator that yields all possible seconds ranges (0-59) - seconds"""
    for s in range(60):
        yield s


# ex2
def gen_minutes():
    """Generator that yields all possible seconds ranges (0-59) - minutes"""
    for s in range(60):
        yield s


# ex3
def gen_hours():
    """Generator that yields all possible seconds ranges (0-59) - hours"""
    for s in range(24):
        yield s


# ex4
def gen_time():
    """Generator that yields all possible times (hour:minutes:second)"""
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)


# ex5
def gen_years(start=datetime.now().year):
    """Generator that yields all possible years from given year"""
    year = start
    while True:
        yield year
        year += 1


# ex6
def gen_months():
    """Generator that yields all the months"""
    for m in range(1, 13):
        yield m


# ex7
def gen_days(month, leap_year=True):
    """Generator that yields the number of days in a given month"""
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31,
        4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    days = days_in_month[month]
    return (x for x in range(1, days + 1))


# ex8
def gen_date():
    for year in gen_years():
        # Check if the current year is a leap year
        for month in gen_months():
            # the number of days depend on the given mouth
            for day in gen_days(month, leap_year=(year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield " {}/{}/{} {:02d}:{:02d}:{:02d}".format(day, month, year, hour, minute, second)


def main():
    # ex9
    fun = gen_date()
    for i in range(1000000):
        print(next(fun))


if __name__ == '__main__':
    main()
