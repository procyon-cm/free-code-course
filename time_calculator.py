def add_time(start, duration, arg=None):
    start = start.split()
    am_pm = start[1]
    time = start[0].split(':')
    hour = time[0]
    minute = time[1]
    duration = duration.split(":")
    hour_duration = duration[0]
    minute_duration = duration[1]

    new_minute = int(minute_duration) + int(minute)
    new_hour = int(hour) + int(hour_duration)
   
    week = {'monday' : 1, 'tuesday' : 2, 'wednesday' : 3, 'thursday' : 4, 'friday' : 5, 'saturday' : 6, 'sunday' : 7}
    day = 0
    
    
    if new_minute > 59:
        new_hour = new_hour + (new_minute // 60)
        new_minute = new_minute % 60

    while new_hour > 12:                            
        new_hour = new_hour - 12
        if am_pm == 'PM':
            am_pm = 'AM'
            day += 1
        else:
            am_pm = 'PM'
    
    if new_minute > 0 and new_hour == 12:               # for example 12:05 
        if am_pm == 'PM':
            am_pm = 'AM'
            day += 1
        else:
            am_pm = 'PM'   
   
    if len(str(new_minute)) == 1:                       # 12:5 -> 12:05
        new_minute = "0" + str(new_minute)
    
    if day == 0:
        day_text = ''
    elif day == 1:
        day_text = '(next day)'
    else:
        day_text = f'({day} days later)'


    if arg:                                             # optional argument
        arg = arg.lower()
        number_of_day = week[arg] + day
        while number_of_day > 7:
            number_of_day = number_of_day - 7
        
        def get_key(val): 
            for key, value in week.items(): 
                if val == value: 
                    return key 
        day_result = get_key(number_of_day)
        day_result = str(day_result).capitalize()
        if day == 0:
            new_time = str(new_hour) + ":" + str(new_minute) + " " + am_pm + ", " + str(day_result)
        else:
            new_time = str(new_hour) + ":" + str(new_minute) + " " + am_pm + ", " + str(day_result) + " " + day_text
        return new_time


    if day == 0:
        new_time = str(new_hour) + ":" + str(new_minute) + " " + am_pm
    else:
        new_time = str(new_hour) + ":" + str(new_minute) + " " + am_pm + " " + day_text
    return new_time
    
    