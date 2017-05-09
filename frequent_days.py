# solution by Roman Frolov 2017
from datetime import date, timedelta
def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)
            
def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
            
day = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday', 3 : 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}
order = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
def most_frequent_days(year):
    days = {'Monday' : 0, 'Tuesday' : 0, 'Wednesday' : 0, 'Thursday' : 0, 'Friday' : 0, 'Saturday' : 0, 'Sunday' : 0}
    result = list()
    start_date = date(year, 1, 1)
    end_date = date(year+1, 1, 1)
    for single_date in daterange(start_date, end_date):
        single_dayasdf = single_date.strftime("%Y, %m, %d")
        single_year = int(single_date.strftime("%Y"))
        single_month = int(single_date.strftime("%m"))
        single_day = int(single_date.strftime("%d"))
        if day[date(single_year, single_month, single_day).weekday()] == 'Monday':
            days['Monday'] +=1
        elif day[date(single_year, single_month, single_day).weekday()] == 'Tuesday':
            days['Tuesday'] +=1
        elif day[date(single_year, single_month, single_day).weekday()] == 'Wednesday':
            days['Wednesday'] +=1
        elif day[date(single_year, single_month, single_day).weekday()] == 'Thursday':
            days['Thursday'] +=1
        elif day[date(single_year, single_month, single_day).weekday()] == 'Friday':
            days['Friday'] +=1
        elif day[date(single_year, single_month, single_day).weekday()] == 'Saturday':
            days['Saturday'] +=1
        elif day[date(single_year, single_month, single_day).weekday()] == 'Sunday':
            days['Sunday'] +=1
   
    result.append(keywithmaxval(days))
    value = days[keywithmaxval(days)]
    for d in days:
        if days[d] == value and d not in result:
            result.append(d)
    result = sorted(result, key=order.index)
    print(result)
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
    assert most_frequent_days(212) == ["Wednesday","Thursday"]
