from datetime import datetime, timedelta, date, time


def get_departure_date():
    departure_date_str = input('Enter estimate departure date (YYYY-MM-DD): ')
    departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d')
    return departure_date
    

def get_travel_time():
    departure_time_str = input('Estimated time of departure (HH:MM AM/PM): ')
    departure_time = datetime.strptime(departure_time_str, '%I:%M %p')
    return departure_time



def main():
    print('Welcome to the trip duration calculator program!')
    print()
    print('Arrival Time Estimator')
    while True:
        departure_date = get_departure_date()
        departure_time = get_travel_time()
        miles = int(input('Enter miles: '))
        miles_per_hour = int(input('Enter miles per hour: '))
        time_traveled = miles / miles_per_hour
        hours_traveled = time_traveled // 1
        minutes_traveled = (time_traveled % 1) * 60
        
        arrival_time = departure_time + timedelta(hours = hours_traveled, minutes = minutes_traveled)
        arrival_date = departure_date + timedelta(hours = hours_traveled, minutes = minutes_traveled) # fix the date issue
        
        print()
        print('Estimated travel time')
        print("Hours:", int(hours_traveled))
        print("Minutes:", int(minutes_traveled))
        print('Estimated date of arrival:', arrival_date.strftime('%Y-%m-%d')) 
        print('Estimated time of arrival:', arrival_time.strftime('%I:%M %p'))
        print()
        #check wheather the user wants to continue
        result = input('Continue? (y/n): ')
        print()
        if result.lower() != 'y':
           print('Bye!')
           break
       
       
if __name__=='__main__':
    main()

