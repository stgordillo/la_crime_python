# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head()

# Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
crime_time = crimes['TIME OCC'].value_counts()
print(crime_time)

# We can see that 12pm is the time of the most frequent committed crimes. Let's extract just the hours, as I can see that while the majority of crime is reported hourly, some crime is reported by minute instead 
crimes['HOUR OCC'] = crimes['TIME OCC'].str[:2].astype(int)
crime_time2 = crimes['HOUR OCC'].value_counts()
print(crime_time2)

# Here we can see that there was indeed quite a bit of crime reported by minute, adding roughly 7000 more entries. Next we'll plot the data using seaborn.
sns.countplot(data=crimes, x='HOUR OCC')
plt.show()

peak_crime_hour = 12

# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59)? Save as a string variable called peak_night_crime_location.
night_hours = crimes[crimes['HOUR OCC'].isin([22,23,0,1,2,3])]
peak_night_crime_location = night_hours.groupby('AREA NAME', as_index=False)['HOUR OCC'].count().sort_values('HOUR OCC', ascending=False).iloc[0]['AREA NAME']
print(peak_night_crime_location)


# Identify the number of crimes committed against victims of different age groups. Save as a pandas Series called victim_ages, with age group label "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+" as the index and the frequency of crims as the values.
age_bin = [0,17,25,34,44,54,64, np.inf]
age_label = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']
crimes['Age Bracket'] = pd.cut(crimes['Vict Age'], bins=age_bin, labels=age_label)

victim_ages = crimes['Age Bracket'].value_counts()
print(victim_ages)
