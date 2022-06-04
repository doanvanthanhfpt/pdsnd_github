"""
Please be noted versions of Pandas and Numpy
Name: numpy; Version: 1.12.1
Name: pandas; Version: 0.23.3
"""

import time
import pandas as pd
import numpy as np

# from input_from_user import get_user_input

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

# define cities
CITIES = ['chicago', 'newyork', 'washington']

# define months
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

# define days of week
DAYS = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

def get_user_input(typed_mess, user_list):
    
    while True:
        typed_data = input(typed_mess).lower()
        if typed_data in user_list:
            break
        if typed_data == 'all':
            break
    
    return typed_data

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
        city = input('Typing the city? \n').lower()
        if city in CITIES:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_user_input('Now select a month of jan, feb, mar, apr, may, jun \n: ', MONTHS)
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_input('Now select a day of week or "all"\n: ', DAYS)

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
    # read data from selected city and time
    df = pd.read_csv(CITY_DATA[city])
    
    # convert data type - datetime type on column Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract time unit from converted Start Time column
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    
    # handle for month
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
    
    # handle for day
    if day != 'all':
        df = df[ df['day_of_week'] == day.title() ]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("Most common month is: \n", most_common_month)


    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most day of the week is: \n", most_common_day_of_week)


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is: \n", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = 'Doing --- The most commonly used start station is: {} \n'.format(df['Start Station'].mode()[0])
    print(most_common_used_start_station)


    # TO DO: display most commonly used end station
    most_common_used_end_station = 'Doing --- The most commonly used end station is: {} \n'.format(df['End Station'].mode()[0])
    print(most_common_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + 'come to ' + df['End Station']
    most_combination_of_start_to_end = '\nDoing --- The most frequent combination of start station to end station is: {}\n'.format(df['trip'].mode()[0])
    print(most_common_used_start_station + most_common_used_end_station + most_combination_of_start_to_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: \n", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].max()
    print("Mean travel time is: \n",mean_travel_time)
    
    print("Travel time for each user type: \n")
    # To DO: display travel time for each user type
    groupby_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(groupby_user_trip):
        print(" {}: {}".format(groupby_user_trip.index[index], user_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: \n')
    count_of_user_types = df['User Type'].value_counts()
    print(count_of_user_types)
    
    #for index, count_of_user_types in enumerate(count_of_user_types):
    #    print("  {}: {}".format(count_of_user_types.index[index], count_of_user_types))
    
    # try for my self explaination
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "/n")
    print()
    


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_stats = df['Gender'].value_counts()
        print(gender_stats)
        print('\n')


    # TO DO: Display earliest, most recent, and most common year of birth     
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
    
        earliest_b_y = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        print('Earliest birth year is: \n',earliest_b_y)
        print('\n')
        earliest_b_y = birth_year.min()
        print('Earliest birth year by min: \n',earliest_b_y)
        print('\n')
        
        most_recent_b_y = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        print('Most recent birth year is: \n',most_recent_b_y)
        print('\n')
        most_recent_b_y = birth_year.max()
        print('Most recent birth year by max: \n',most_recent_b_y)
        print('\n')
        
        most_common_b_y = df['Birth Year'].mode()[0]
        print('Most common birth year is: \n',most_common_b_y)
        print('\n')
        most_common_b_y = birth_year.value_counts().idxmax()
        print('Most common birth year by valueCount and idxmax: \n',most_common_b_y)
        print('\n')
        
        #group_of_b_y = df.groupby('Birth Year')
        #print('Birth year distribution: \n',group_of_b_y)
        #print('\n')
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    raw_amount = 5
    print(df.head(raw_amount))
    while True:
        display_more = input("\nDo you want to list more raw data? 'Yes' or 'No'\n").lower()
        if display_more == 'yes':
            raw_amount = raw_amount + 5
            print(df.iloc[raw_amount - 5:raw_amount, :])
        elif display_more == 'no':
            break
        else:
            print('\nWrong input')
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
