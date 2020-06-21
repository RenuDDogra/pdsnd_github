import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
week_days = [0,1,2,3,4,5,6]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while(True):
        print("Would you like to see the data for: Chicago,new york city,washington")
        city=input().lower()
        if city in cities:
          break
        else:
            print("Please enter valid city name")


    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        print("Which month you would like to see data for : 'january', 'february', 'march', 'april', 'may', 'june'")
        month=input().lower()
        if month in monthsinyear:
            break
        else:
            print("Please enter valid month name")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("Which day you would like to check EX 0=Sunday,1= monday .. etc")
    while(True):
        day=int(input())
        if day in week_days:
            break
        else:
            print("Please enter valid day")
    


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
    
    
    # columns
    
    df['day_of_week'] = df['Start Time'].dt.weekday
    
    df['month']=df['Start Time'].dt.month
    
    df['hour'] = df['Start Time'].dt.hour
    
    df['start_end'] = df['Start Station'].astype(str) + ' to ' + df['End Station']
    
    
    #filter by month
    if month != 'all':
         # use the index of the months list to get the corresponding in
        monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june']
        monthIndx = monthsinyear.index(month) + 1
        
        df = df[df['month'] == monthIndx]
    #filter by day 
    if day != 'all':
       #filter by day of week to create the new dataframe
       df = df[df['day_of_week'] == day]
       
        
        
    return df

def display_data(df):
    j=0
    i=5
    raw_input=input("Would you like to see raw data , enter yes or no \n")
    while(raw_input == 'yes'):
        if raw_input.lower() == 'yes':
            raw_data=df.iloc[j:i,:]
            j=i+1
            i=i+5
            print(raw_data)
            raw_input=input("do you want to view more raw data..? enter 'yes' or 'no' \n")
        else:
            print("I believe you want to continuing viewing the statistical data")
       

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_index = df["month"].mode()[0] - 1
    The_most_common_month = monthsinyear[month_index].title()
    print( f"The month {The_most_common_month} is the most common month")
    


    # TO DO: display the most common day of week
    The_most_common_day_of_week = df["day_of_week"].mode()[0]
    print( f" The most common day of week is  {The_most_common_day_of_week} ")
    
    

    # TO DO: display the most common start hour

    The_most_common_hour = df["hour"].mode()[0]
    print( f" The most common hour is {The_most_common_hour}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    The_most_common_start_station=df['Start Station'].mode()[0]
    print( f" The most common start station is : {The_most_common_start_station}")
    # TO DO: display most commonly used end station
    The_most_common_used_end_station =df['End Station'].mode()[0]
    print( f" The most common end station is : {The_most_common_used_end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    start_end_station=df['start_end'].mode()[0]
    print( f" The most common 'start' and 'end' station is : {start_end_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print( f" The total time travel is : {total_travel_time}")
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print( f" The mean time travel is : {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df["User Type"].value_counts()
    print( f" The counts of user types is : {user_types}")

    # TO DO: Display counts of gender
    if "Gender" in df:
        
        print("male counts are : ", df.query("Gender == 'Male'").Gender.count())
        print("female counts are: ", df.query("Gender == 'Female'").Gender.count())
    else:
        print("No 'Gender' column present in this city csv file data")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "birth Year" in df:    
        earliest=df["Birth Year"].min()
        most_recent=df["Birth Year"].max()
        most_common_year=df["Birth Year"].value_counts().idxmax()
    
        print( f" The most earliest years is  : {earliest} ")
        print( f" The most recent years is  : {most_recent} ")
        print( f" The most common years is  : {most_common_year} ")
    
    else:
        print("No 'birth' year column present in this city csv file data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        # This filters the date into three variable via city,month,day
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
