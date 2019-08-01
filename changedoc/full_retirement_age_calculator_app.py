from changedoc.full_retirement_calc import full_retirement_age, full_retirement_date


def calculator():
    print("Social Security Full Retirement Age Calculator");
    birth_year_str = str(input("Enter the year of birth or <enter> to exit ")).strip()
    while birth_year_str != '':
        birth_year = int(birth_year_str)
        birth_month = int(input("Enter the month of birth (<Enter> implies 0)"))
        fra_age_years, fra_age_months = full_retirement_age(birth_year)
        fra_date_year, fra_date_month = full_retirement_date(birth_year, birth_month)
        print("your full retirement age is ", fra_age_years, " and ", fra_age_months, " months")
        print("this will be in ", fra_date_month, " of ", fra_date_year, "\n")
        birth_year_str = input("Enter the year of birth or <enter> to exit ")


def main():
    calculator()


main()

