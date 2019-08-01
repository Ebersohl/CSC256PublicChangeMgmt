from datetime import datetime

EARLIEST_YEAR = 1900
CURRENT_YEAR = datetime.today().year

LAST_65_YEAR = 1937

FIRST_66_YEAR = 1943
LAST_66_YEAR = 1954

FIRST_67_YEAR = 1960

MONTH_NAMES = {0: 'january',
               1: 'January',
               2: 'February',
               3: 'March',
               4: 'April',
               5: 'May',
               6: 'June',
               7: 'July',
               8: 'August',
               9: 'September',
               10: 'October',
               11: 'November',
               12: 'December',
               }

# Don't want to use len(MONTH_NAMES) because it's one element
# too long
YEAR_LENGTH = 12

# Return the age at which a person born in a given year
# is entitled to full Social Security benefits.
#
# Age is expressed in years and number of months
# within that year.
#
# For example,
#
# age_in_years, month_within_yearly_age = full_retirement_age(1955)
# will result in age_in_years == 66
# and month_within_yearly_age == 2
#
# Birth years may range from 1900 to the present year.
#
# Invalid birth years return -1 -1
#
# See https://www.ssa.gov/planners/retire/agereduction.html
#
def full_retirement_age(birth_year):
    if birth_year >= CURRENT_YEAR:
        return -1, -1
    if birth_year < EARLIEST_YEAR:
        return -1, -1
    if birth_year <= LAST_65_YEAR:
        return 65, 0
    if birth_year >= FIRST_67_YEAR:
        return 67, 0
    if FIRST_66_YEAR <= birth_year <= LAST_66_YEAR:
        return 66, 0
    if birth_year < FIRST_66_YEAR:
        return 65, (birth_year - LAST_65_YEAR) * 2
    return 66, ((birth_year - LAST_66_YEAR) * 2)


# Return the year and month a person with a given birth year
# is entitled to full retirement benefits from social security
# The year is returned as an int value, the month as a string ('January', for example)
# The birth year must be between 1900 and the current year.
# The birth month must be 0 or 1 for January, 2 for February, 12 for December
#
# Invalid birth year or month will result in -1 being returned for the year,
# and "invalid" for the month.
#
def full_retirement_date(birth_year, birth_month):
    birth_month_normalized = birth_month
    # if birth_month == 0:
    #   birth_month_normalized = 1
    age, month_offset = full_retirement_age(birth_year)
    if age == -1 or birth_month_normalized < 0 or birth_month > 12:
        return -1, 'invalid'
    fra_month = birth_month_normalized + month_offset
    fra_year = birth_year + age
    if fra_month > YEAR_LENGTH:
        fra_month -= YEAR_LENGTH
        fra_year += 1
    return fra_year, MONTH_NAMES[fra_month]
