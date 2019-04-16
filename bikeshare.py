import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITY_SELECT = ['chicago', 'new york city', 'washington']
MONTH_SELECT = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
WEEKDAY = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
        city = input('What city do you want to explore: Chicago, New York City, or Washington? \n' ).lower()
        if city in CITY_SELECT:
            break
        else:
            print('Please enter one of the following: Chicago, New York City, or Washington? Make sure to check your spelling. \n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('You\'ve selected {}. Select one of the following months would you like to see data for: January, February, March, April, May, or June? Type \'all\' for no filter. \n'.format(city.title())).lower()
        if month in MONTH_SELECT:
            break
        else:
            print('Incorrect input. Please enter one of the following if you would like to filter: January, February, March, April, May, or June. If you want to see all months, type \'all\'. \n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Now select a day of the week you would like to see data for. If you would like to see all days, type \'all\'. \n').lower()
        if day in WEEKDAY:
            break
        else:
            print('Incorrect input. Please enter one of days of the week and make sure you\'re using the correct spelling. If you would like to not filter, type \'all\. \n')

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
           month = MONTH_SELECT.index(month) + 1
           df = df[df['month'] == month]
    if day != 'all':
            df = df[df['day_of_week'] ==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', calendar.month_name[most_common_month])

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combo_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most common combination of start and end station is: {}, {}'.format(most_common_combo_station[0], most_common_combo_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time using bikeshare is:', total_travel_time,'seconds')

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The average travel time using bikeshare is:', average_travel_time,'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(user_type_count, '\n')

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print(gender_count, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    earliest_year = birth_year.min()
    latest_year = birth_year.max()
    most_common_year = birth_year.mode()[0]
    print('The oldest user was born in', int(earliest_year))
    print('The youngest user was born in', int(latest_year))
    print('The average user was born in', int(most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    row_length = df.shape[0]
    for i in range(0, row_length, 5):
        question = input('Would you like to view the raw data? Please type \'Yes\' or \'No\'. \n')
        if question.lower() != 'yes':
            break
        row_data = df.iloc[i: i + 5]
        print(row_data,'\n\nType \'Yes\' to view the next five rows.')

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
