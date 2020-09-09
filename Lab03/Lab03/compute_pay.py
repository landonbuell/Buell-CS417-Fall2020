"""
Landon Buell
Alejo Hausner
CS417.01 - L03
8 Spet 2020
"""

import sys

def compute_payroll(timesheet_file_name,
                    payroll_file_name):
    # ITEM 6 follows this line
    timesheet = open(timesheet_file_name, 'r')

    #ITEM 12 follows this line
    payroll = open(payroll_file_name,mode="w")

    while True:
        line = timesheet.readline()
        if len(line) == 0:
            break
        line = line.rstrip("\n\r")
        print (line) # ITEM 2

    # ITEMS 2, 3 follow this line
        fields = line.split(":")
        print(fields)

    # ITEMS 4, 5 follow this line
        lastName = fields[0]
        firstName = fields[1]
        try:
            hoursWorked = float(fields[2])
            hourlyPay = float(fields[3])
        except ValueError:
            hoursWorked = 0.0
            hourlyPay = 0.0 
            sys.stderr.write("Bad Number in timesheet!"+line+"\n")

    # ITEM 7 follows this line
        grossPay = ComputeGrossPay(hoursWorked,hourlyPay)

    # ITEM 8 follows this line
        TAXRATE = 0.2           # these are some wildtaxes here!
        tax = TAXRATE * grossPay

    # ITEM 9 follows this line
        netPay = grossPay - tax
        print("{}:{}:{}:{}:{}".format(lastName,firstName,grossPay,tax,netPay))

    # ITEMS 10, 11, 12, 13 follow this line       
        payroll.write("{}:{}:{}:{}:{}\n".format(lastName,firstName,grossPay,tax,netPay))

    payroll.close()
    timesheet.close()

    # ITEM 14 follows this line

def ComputeGrossPay(hours,pay):
    """ Compute Gross Pay for Part 7 """
    if hours <= 40:         # 40 hr. week?
        return hours * pay
    else:
        overtime = hours - 40   # overtime
        time = 40 * pay
        timeHalf = overtime * (1.5) * pay
        return time + timeHalf

def main():
    timesheet_file = "timesheet.txt"
    payroll_file = "payroll.txt"
    compute_payroll(timesheet_file, payroll_file)

if __name__ == '__main__':
    main()

