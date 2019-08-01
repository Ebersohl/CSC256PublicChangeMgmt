import datetime

#
# test cases are birth year, (year of fra, month within fra year)
#
from changedoc.full_retirement_calc import full_retirement_age, full_retirement_date

TEST_RETIREMENT_AGE = {1899: (-1, -1),
                       1900: (65, 0),
                       1937: (65, 0),
                       1938: (65, 2),
                       1942: (65, 10),
                       1943: (66, 0),
                       1954: (66, 0),
                       1955: (66, 2),
                       1959: (66, 10),
                       1960: (67, 0),
                       }

TRA_TUPLE_YEAR = 0
TRA_TUPLE_MONTH = 1

TEST_RETIREMENT_DATE = {(1899, 12): (-1, 'invalid'),
                        (1900, -1): (-1, 'invalid'),
                        (1900, 13): (-1, 'invalid'),
                        (1900, 1): (1965, 'January'),
                        (1937, 2): (1937 + 65, 'February'),
                        (1938, 1): (1938 + 65, 'March'),
                        (1942, 2): (1942 + 65, 'December'),
                        (1942, 3): (1942 + 65 + 1, 'January'),
                        (1942, 4): (1942 + 65 + 1, 'February'),
                        (1942, 5): (1942 + 65 + 1, 'March'),
                        (1942, 6): (1942 + 65 + 1, 'April'),
                        (1943, 5): (1943 + 66, 'May'),
                        (1954, 6): (1954 + 66, 'June'),
                        (1955, 5): (1955 + 66, 'July'),
                        (1960, 8): (1960 + 67, 'August'),
                        (1939, 5): (1939 + 65, 'September'),
                        (1940, 4): (1940 + 65, 'October'),
                        (1958, 3): (1958 + 66, 'November'),
                        (1959, 2): (1959 + 66, 'December'),
                        (1955, 1): (1955 + 66, 'March'),
                        }

TRD_BIRTH_YEAR = 0
TRD_BIRTH_MONTH = 1
TRD_FRA_YEAR = 0
TRD_FRA_MONTH = 1

CURRENT_YEAR = datetime.date.today().year


def test_retirement_0():
    year, month = full_retirement_age(CURRENT_YEAR)
    assert year == 67 and month == 0, "Failed for year {} ".format(CURRENT_YEAR)


def test_retirement_1():
    year, month = full_retirement_age(CURRENT_YEAR + 1)
    assert year == -1 and month == -1, "Failed for year {} ".format(CURRENT_YEAR)


def test_retirement_2():
    for birth_year in TEST_RETIREMENT_AGE:
        actual_year, actual_month = full_retirement_age(birth_year)
        assert actual_year == TEST_RETIREMENT_AGE[birth_year][TRA_TUPLE_YEAR] and actual_month == \
            TEST_RETIREMENT_AGE[birth_year][TRA_TUPLE_MONTH], \
            "Failed for birth year {} actual year {}  month {}".format(birth_year, actual_year, actual_month)


def test_retirement_date_0():
    for birth_info in TEST_RETIREMENT_DATE:
        actual_year, actual_month = full_retirement_date(birth_info[TRD_BIRTH_YEAR], birth_info[TRD_BIRTH_MONTH])
        assert actual_year == TEST_RETIREMENT_DATE[birth_info][TRD_FRA_YEAR] \
            and actual_month == TEST_RETIREMENT_DATE[birth_info][TRD_FRA_MONTH], \
            "Failed for birth info {} actual year {}  month {}".format(birth_info, actual_year, actual_month)
