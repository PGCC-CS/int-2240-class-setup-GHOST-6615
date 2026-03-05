# Employee Payroll Calculator
# This program calculates an employee's gross pay including overtime


def calcPayWithOvertime(hours, rate):

    overtime_hours = hours - 40
    regular_pay = 40 * rate
    overtime_pay = overtime_hours * rate * 1.5

    gross_pay = regular_pay + overtime_pay

    print("\nRegular hours:", 40)
    print("Overtime hours:", overtime_hours)
    print("Gross pay (including overtime): $", format(gross_pay, ".2f"))


def calcRegularPay(hours, rate):

    gross_pay = hours * rate

    print("\nRegular hours:", hours)
    print("Overtime hours:", 0)
    print("Gross pay: $", format(gross_pay, ".2f"))


def main():

    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly pay rate: "))

    if hours > 40:
        calcPayWithOvertime(hours, rate)
    else:
        calcRegularPay(hours, rate)


main()