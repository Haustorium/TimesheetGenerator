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
    startDate = int(input("What is the start date of this timesheet?\n"))
    month = int(input("What month is it?\n"))
    hoursPerFortnight = int(input("How many hours did you work over these two weeks?\n"))

    hoursPerDay = (hoursPerFortnight / 10)

    dates = sequence(startDate,month)

    for i in range(0,len(dates)):
        print(dates[i])

    
    
    """
    Mon 12: 10 - 1:30 3.5 hours
    Tue 13: 2:00 - 4:30 2.5 Hours
    Wed 14: 12 - 4:00 4 Hours
    Thur 15: 8:00-4:00 7.5 Hours
    Fri 16: 9:30 - 1:30 4 Hours
    Total: 21.5 Hours

    Mon 19: 10:30 - 1:30 3 hours
    Tue 20: 1:30 - 4:30 3 hours
    Wed 21: 12 - 3:30 3.5 hours
    Thur 22: 12 - 3:30 3.5 hours
    Fri 23: 12 - 3:30 3.5 hours

    Total: 16.5 Hours

    Grand total: 38 Hours

    """
