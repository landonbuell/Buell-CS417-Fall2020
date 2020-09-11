"""
Landon Buell
Alejo Hausner
CS 417.01 - Lab04
10 Sept 2020
"""

import sys

TAX_RATE = 0.20

def safe_open(filename, mode):
    '''Tries to open the given file.
    If successful, returns the file handle.
    If not, complains and exits'''

    try:
        handle = open(filename, mode)
    except Exception as e:
        sys.stderr.write('Can\'t open ' + filename + ':' + str(e) + '\n')
        sys.exit(1)
    return handle

def get_hourly_rates(filename):
    # ITEM 2: read the employee file and get the hourly rates,
    # keyed by employee ID
    hourly_rates = dict()
    employee_data = safe_open(filename,mode='r')
    while True:
        line = employee_data.readline()
        if len(line) == 0:
            break
        line = line.rstrip("\n\r")
        fields = line.split(':')
        # Read the rates from the employee file
        employeeID = int(fields[0])
        rate = float(fields[3])
        hourly_rates.update({employeeID:rate})
        
    return hourly_rates


def compute_pay(timesheet_filename,employee_filename, payroll_filename):
    # ITEM 1: compute_pay() has THREE arguments now:
    #         timesheet_filename, employee_filename, payroll_filename
    timesheet = safe_open(timesheet_filename, 'r')
    payroll = safe_open(payroll_filename, 'w')

    hourly_rates = get_hourly_rates(employee_filename)

    while True:
        line = timesheet.readline()
        if len(line) == 0:
            break
        line = line.rstrip("\n\r")
        fields = line.split(':')

        # ITEM 3: only fields 0 and 1 have data in the new file format

        employeeID = int(fields[0])
        hours_worked = 0
        hourly_rate = 0
        try:
            hours_worked = float(fields[1])
            hourly_rate = float(hourly_rates[employeeID])
        except ValueError:
            sys.stderr.write('bad number in timesheet file: ' + line)

        if hours_worked <= 40:
            regular_hours = hours_worked
            overtime_hours = 0
        else:
            regular_hours = 40
            overtime_hours = hours_worked - 40
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        gross_pay = regular_pay + overtime_pay
        tax = gross_pay * TAX_RATE
        net_pay = gross_pay - tax

        # ITEM 4: The format for the payroll file has changed too!

        payroll.write("{}:{:.2f}:{:.2f}:{:.2f}\n".format(employeeID,gross_pay, tax, net_pay))

    timesheet.close()
    payroll.close()

def main():
    # ITEM 1: Check sys.argv for THREE filenames,
    # sys.argv[1] has the timesheet file, sys.argv[2] the employee file,
    # and sys.argv[2] the payroll file.
    #
    # If len(sys.argv) is not 4, prompt the user for the three file names.
    if len(sys.argv) != 4:
        print("\n\tERROR! - Wrong Number of Arguments Passed!")
        fileTimesheet = input("Time Sheet File? :")
        fileEmployee = input("Employee File? :")
        filePayroll = input("Payroll File? :")
    else:
        fileTimesheet = sys.argv[1]
        fileEmployee = sys.argv[2]
        filePayroll = sys.argv[3]

    # compute_pay() will now have 3 arguments, and they should be variables,
    # not these two strings.
    compute_pay(fileTimesheet,fileEmployee,filePayroll)

if __name__ == '__main__':
    main()
