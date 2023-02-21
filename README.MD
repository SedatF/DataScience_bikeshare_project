WITH PANDAS on Bikeshare Data

PROJECT OVERVIEW :
------------------
This project uses the panda polarity and simple statistical methods to see the most popular days and the most common stations with the bicycle sharing data of Chicago, Washington and New York cities.

Running the program : 
---------------------
You can input 'python bikeshare.py' on your terminal to run this program. I used Google Colab.

Program Details : 
-----------------
I will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. 
I will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

Statistics Computed: 
---------------------
#1 Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day

#2 Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration
- total travel time
- average travel time

#4 User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

Requirements : 
---------------
Language: Python 3.6 or above
Libraries: pandas, numpy, time

Project DataSet : 
------------------
chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity.
Note: This does not include the 'Gender' or 'Birth Year' data.

Built with : 
-------------
Python 3.6.6 - The language used to develop this.
pandas - One of the libraries used for this.
numpy - One of the libraries used for this.
time - One of the libraries used for this.

Author :
------------
Sedat FINDIK 

Acknowledgements:
-------------------
Udacity - Udacity's Data Analyst Nanodegree program and their instructors were extremely helpful while I was pursuing this project.

pandas docs - pandas documentation was immensely helpful in understanding the implemention of pandas methods used in this project.
https://pandas.pydata.org/

