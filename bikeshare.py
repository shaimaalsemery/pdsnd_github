import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city=input('Enter City Name ').lower().strip()
        if city !='chicago' and city!= 'new york city' and city!='washington'and city!='all':
            print('name not vaild')
        else:
            break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter Month Name ').lower().strip()
        if month!='january'and month!='february'and month!='march'and month!='april'and month!='may'and month!='june'and month!='july'and month!='august'and month!='september'and month!='october'and month!='november'and month!='december'and month!='all':
            print('month not vaild')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         day=input('Enter Day Name ').lower().strip()
         if day!='monday' and day!='tuesday'and day!='wednesday' and day!='thursday'and day!='friday'and day!='saturday'and day!='sunday'and day!='all':
            print('day not vaild')
         else:
             break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df =pd.read_csv(CITY_DATA[city])

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
       
        df =df[df['month']==month]

    
    if day != 'all':
        
        df = df =df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=CITY_DATA['month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day=CITY_DATA['day_of_week'].mode()[0]


    # TO DO: display the most common start hour 
    most_common_start_time=CITY_DATA['Start Time'].mode()[0]
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=CITY_DATA['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_common_end_station=CITY_DATA['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=CITY_DATA.grouppy['Start Station','End Station'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=CITY_DATA['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel_time=CITY_DATA['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of 
    user_types=CITY_DATA['User Type'].value_counts()
    


    # TO DO: Display counts of gender
    try:
        gender=CITY_DATA['Gender'].value_counts().to_string()
    except KeyError:
        print('there is no gender distribution  data for this city') 
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        print('    Year of Birth...')
        print('        Earliest:        ', int(df['Birth Year'].min()))
        print('        Most recent:     ', int(df['Birth Year'].max()))
        print('        Most common:     ', int(df['Birth Year'].mode()))

    
        
        
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_data=input('Do you want to see the raw date?').lower().strip()
        
        start=0
        end=5
        while(True):
            temp=df.iloc[start:end]
            start +=5
            end +=5
            print(temp)
            
            raw_data=input('Do you want to see the raw data?').lower().strip()
            if(raw_data=='no'):
                break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
