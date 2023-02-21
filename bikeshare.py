import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv','CHIGAGO': 'chicago.csv',
             'New York City': 'new_york_city.csv', 'New york city': 'new_york_city.csv',
              'new york city': 'new_york_city.csv', 'washington': 'washington.csv',
             'Washington': 'washington.csv','WASHINGTON': 'washington.csv'  }

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
    city='X'

    while city not in CITY_DATA.keys():      
      city = input("\nWould you like to see data for Chicago , New York, or Washington? (Accepted input: e.g. chicago,Chicago or CHICAGO) ").lower()

      if city not in CITY_DATA.keys():
        print("\nPlease check your input, Try again please..")


    print("\nYour choice city : {city.title()} ")


    # TO DO: get user input for month (all, january, february, ... , june)
    # 2. Would you like to filter the data by month, day, or not at all?
    # 3. (If they chose month) Which month - January, February, March, April, May, or June?
    MONTH_LIST = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_LIST.keys():
        print("\nPlease enter the month, between January to June")
        print("\nAccepted input:e.g. january,January or JANUARY).")
        print("\n(For all months, please type 'all' or 'All' or 'ALL' for that.)")
        month = input("\nWould you like to filter the data by month, day, or not at all? ").lower()
        
        if month not in MONTH_LIST.keys():
            print("\nPlease check your input, Try again please..")

    print("\nYour choice month : {month.title()} ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # 4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week. ")
        print("\nAccepted input:\nDay name: (e.g. monday,Monday or MONDAY).")
        print("\n(You can also put 'all' or 'All' to view data for all days in a week.)")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nPlease check your input, Try again please..")

    print("\nYour choice day : {day.title()} ")
    print("\nYour choice city: {city.upper()}, Your choice months: {month.upper()} and Your choice days: {day.upper()}.")

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

    #Convert the Start Time column 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week

    #Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print("Most Popular Month (1 = January,2 = February..): {popular_month}")

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    popular_day = df['day_of_week'].mode()[0]
    print("\nMost Popular Day: {popular_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"\nMost Popular Hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    #Displays statistics on the most popular stations and trip. 

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: {start_station}")

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    print("\nThe most commonly used end station: {end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print("\nThe most frequent combination of trips : {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration. 

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    #Finds out the duration in minutes and seconds format
    minute, second = divmod(total_time, 60)
    #Finds out the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print("The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time
    average_trip = round(df['Trip Duration'].mean())
    #Finds the average duration in minutes and seconds format
    mins, sec = divmod(average_trip, 60)
    #This filter prints the time in hours, mins, sec format
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print("\nThe average trip duration : {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print("\nThe average trip duration : {mins} minutes and {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
<<<<<<< HEAD
    #Displays statistics on bikeshare users.
=======
    #Displays statistics on bikeshare users. 
>>>>>>> documentation

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    print("\nThe counts of user types :\n\n{user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nThe counts of gender types :\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column. ")
        print("\nPlease Try again. ")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])        
        print("\nThe earliest year of birth: {earliest}")
        print("\nThe most recent year of birth: {recent}")
        print("\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_lists(df):
    #Displays 5 rows of data from the csv file for the selected city.
    DISPLAY_LIST = ['yes', 'no']
    list_data = ''
    counter = 0
    while list_data not in DISPLAY_LIST:
        print("\nDo you want to view raw data? (Yes,yes,No or no) ")
        list_data = input().lower()
        if list_data == "yes":
            print(df.head())
        elif list_data not in DISPLAY_LIST:
            print("\nPlease check your input.Try again.")

    while list_data == 'yes':
        print("Do you want to view more raw data?")
        counter += 5
        list_data = input().lower()

        if list_data == "yes":
             print(df[counter:counter+5])
        elif list_data != "yes":
             break

    print('-'*40)

# main function 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # Display Lists functions..
        display_lists(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? (yes or no).\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
