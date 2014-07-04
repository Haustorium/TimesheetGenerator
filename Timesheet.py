


def sequence(date,month):
    """
    Creates a list based on the startdate varible in the function Hours

    Returns a list of the dates of the week for a fortnight,
    not including weekends, starting from the startdate.
    """

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] * 2
    list1 = (list(range(1,32))) * 2
    list2 = (list(range(1,31))) * 2
    list3 = (list(range(1,29))) * 2
    
    dates = ()
    new_list = []
    dateList = []
    
    i = 0

    if date > 31:
        date = int(input("Invalid date. Pick a valid date between 1-31.\n"))
    
    if month in [1,3,5,7,8,10,12]:
        new_list = ((list1[(date-1):(date+4)]) + (list1[(date+6):(date+12)]))
        
    elif month in [4,6,9,11]:
        new_list = (list2[(date-1):(date+4)]) + (list2[(date+6):(date+12)])
        
    elif month == (2):
        new_list = ((list3[(date-1):(date+4)]) + (list3[(date+6):(date+12)]))
        
    while i < 10:
        dates = (days[i],new_list[i])
        (day, date) = dates
        dateList += [day + ' ' + str(date)]
        i+=1

    return dateList
        
        
        
def Hours():
    """
    Creates a form to email given information about the date and times worked

    Returns: A copiable form to email with accurate times of hours worked
    """
    
    hours = []
    times = []
    startDate = int(input("What is the start date of this timesheet?\n"))
    month = int(input("What month is it?\n"))

    dates = sequence(startDate,month)
    
    i = 0
    total1 = 0
    total2 = 0
    grandTotal = 0

    
    while i < 10:
        startTime = float(input("What time did you start work on " + dates[i] + "?\n"))
        hoursWorked = float(input("How many hours did you work?\n"))
        endTime = float(startTime + hoursWorked)

        if hoursWorked > 7.5:
            hoursWorked = hoursWorked - 0.5
        
        if endTime >= 13:
            endTime = endTime - 12

        if (endTime % 1) != 0:
            endTime = (endTime // 1) + .30
            
        times += [(startTime, endTime)]
        hours += [hoursWorked]
        
        if  i < 5:
            total1 += hoursWorked

        if 5 <= i < 10:
            total2 += hoursWorked

        grandTotal += hoursWorked

        i += 1



    for i in range(0,len(dates)):
        print("\n" + "\n" + dates[i] + " " + str(times[i][0]) + "0 - " + str(times[i][1]) + "0 " + str(hours[i]) + " hours")
        if i == 4:
            print("Total: " + str(total1) + " Hours" + "\n")

        if i == 9:
            print("Total: " + str(total2) + " Hours" + "\n")

    print("Grand Total:" + str(grandTotal))

    
    
    
