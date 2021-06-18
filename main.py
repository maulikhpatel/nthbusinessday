import math
import numpy
import datetime


def get_user_input(msg):
    return input(msg)


def is_number(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False


def is_date(input):
    try:
        month, day, year = input.split('/')
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        try:
            year, month, day = input.split('-')
            datetime.datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False


def to_date(input):
    try:
        month, day, year = input.split('/')
        return datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        year, month, day = input.split('-')
        return datetime.datetime(int(year), int(month), int(day))



def calc_nth_business_day(idate, ndays):
    vDate = idate
    vSign = int(numpy.sign(ndays))
    vWeekend = datetime.datetime.isoweekday(vDate)

    # consider weekend (SAT + SUN) as 1 day
    if vSign == -1 and vWeekend == 7:  # SUN
        vDate = vDate + datetime.timedelta(days=vSign)
    elif vSign == 1 and vWeekend == 6:  # SAT
        vDate = vDate + datetime.timedelta(days=vSign)

    # Calculate remaining days in current week
    if vSign == -1:
        remaining_weekdays = 5 if vWeekend == 7 else vWeekend - 1
    else:
        remaining_weekdays = 5 if vWeekend == 7 else 5 - vWeekend

    # Calculate remaining days using which we will calculate number of weekends in betweeen
    diffdays = abs(ndays) - remaining_weekdays
    daysratio = (diffdays - 1) / 5.00

    # Calculate number of weekends to add
    noofweekends = math.floor(daysratio) + 1

    # Calculate number of weekends Days to add
    weekenddays = noofweekends * 2 * vSign

    return vDate + datetime.timedelta(days=ndays + weekenddays)


if __name__ == '__main__':
    in_input_date = '2021-06-09'
    in_no_of_days = 10
    # in_input_date = get_user_input("Enter Input Date (mm/dd/yyyy): ")
    if not is_date(in_input_date):
        print("Please enter date value(mm/dd/yyyy)")
        exit(1)
    # in_no_of_days = get_user_input("Enter # of Days to Add/Deduct: ")
    if not is_number(in_no_of_days):
        print("Please enter numeric value")
        exit(1)

    while in_no_of_days != 0:
        output_date = calc_nth_business_day(to_date(in_input_date), in_no_of_days)
        print("Output :", in_input_date, ":: Days : ", in_no_of_days, ":: Output :", output_date)
        in_no_of_days = in_no_of_days - int(numpy.sign(in_no_of_days))

