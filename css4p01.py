# -*- coding: utf-8 -*-

import pandas as pd

# read the file
df = pd.read_csv("data/movie_dataset.csv")

# display statistics about the file
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""

# display a full description of the file
print(df.describe())
"""
              Rank         Year  ...  Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000

[8 rows x 7 columns]
"""

"""
Clean the data by:
    1. Changing the Runtime (Minutes) column to Runtime(Minutes)
    2. Changing the Revenue (Millions) column to Revenue(Millions)
    3. Appropriating average values to null Revenues
    4. Appropriating average values to null Metascore
"""
df.rename(columns={'Runtime (Minutes)':'Runtime(Minutes)','Revenue (Millions)':'Revenue(Millions)'}, inplace=True)

avg_revenue = df['Revenue(Millions)'].mean()
df['Revenue(Millions)'].fillna(round(avg_revenue,2), inplace=True)

avg_metascore = df['Metascore'].mean()
df['Metascore'].fillna(round(avg_metascore,0), inplace=True)

# display information about the new file
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Rank               1000 non-null   int64  
 1   Title              1000 non-null   object 
 2   Genre              1000 non-null   object 
 3   Description        1000 non-null   object 
 4   Director           1000 non-null   object 
 5   Actors             1000 non-null   object 
 6   Year               1000 non-null   int64  
 7   Runtime(Minutes)   1000 non-null   int64  
 8   Rating             1000 non-null   float64
 9   Votes              1000 non-null   int64  
 10  Revenue(Millions)  1000 non-null   float64
 11  Metascore          1000 non-null   float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""

# display description of the new file
print(df.describe()) 
"""
              Rank         Year  ...  Revenue(Millions)    Metascore
count  1000.000000  1000.000000  ...        1000.000000  1000.000000
mean    500.500000  2012.783000  ...          82.956840    58.986000
std     288.819436     3.205962  ...          96.412043    16.634859
min       1.000000  2006.000000  ...           0.000000    11.000000
25%     250.750000  2010.000000  ...          17.442500    47.750000
50%     500.500000  2014.000000  ...          60.375000    59.000000
75%     750.250000  2016.000000  ...          99.177500    71.000000
max    1000.000000  2016.000000  ...         936.630000   100.000000

[8 rows x 7 columns]
"""

# determine moving with the highest rating
highest_rating = df['Rating'].max()
highest_rated_movie =  df.loc[df['Rating']==highest_rating,'Title'] #get the title of the movie  with the highest rating

# display the average revenue
print("Average revenue is ",round(avg_revenue, 2))

# get the sum revenue of 2015
tot_revenue_2015 = df.loc[df['Year']==2015,'Revenue(Millions)'].sum()
print("Total revenue of 2015 is ", round(tot_revenue_2015, 2))
tot_revenue_2016 = df.loc[df['Year']==2016,'Revenue(Millions)'].sum()
print("Total revenue of 2016 is ", round(tot_revenue_2016, 2))
tot_revenue_2017 = df.loc[df['Year']==2017,'Revenue(Millions)'].sum()
print("Total revenue of 2017 is ", round(tot_revenue_2017, 2)) #there was no revenue in 2017

avg_revenue_2015_2016 = (tot_revenue_2015 + tot_revenue_2016)/2.0
print("Average revenue btw years is ", round(avg_revenue_2015_2016,2))
"""
Average revenue is  82.96
Total revenue of 2015 is  10015.56
Total revenue of 2016 is  18843.97
Total revenue of 2017 is  0.0
Average revenue btw years is  14429.76
"""

# number of movies released in 2016
number_of_movies_2016 =  df['Year'].value_counts()[2016]
print("Number of movies released in 2016: ", number_of_movies_2016)
"""
Number of movies released in 2016:  297
"""

# number of movies directed by Christopher Nolan
number_of_movies_by_nolan =  df['Director'].value_counts()['Christopher Nolan']
print("Number of movies directed by Christopher Nolan: ", number_of_movies_by_nolan)
"""
Number of movies directed by Christopher Nolan:  5
"""

# number of movies with a rating of 8, the least
number_of_movies_with_rating_8_plus =  (df['Rating'] >=8).value_counts()
print("Number of movies weith a rating from 8: ", number_of_movies_with_rating_8_plus)
"""
Number of movies weith a rating from 8:  Rating
False    922
True      78
Name: count, dtype: int64
"""

tot_ratings_of_movies_by_nolan =  (df.loc[df['Director']=='Christopher Nolan','Rating']).sum()
rating_median_of_movies_by_nolan = tot_ratings_of_movies_by_nolan / number_of_movies_by_nolan
print("Median rankings of movies by Christopher Nolan: ", round(rating_median_of_movies_by_nolan,1))
"""
Median rankings of movies by Christopher Nolan:  8.7
"""

# determine year with the highest average rating
avg_rating_2016 = (df.loc[df['Year']==2016,'Rating']).mean()
avg_rating_2006 = (df.loc[df['Year']==2006,'Rating']).mean()
avg_rating_2008 = (df.loc[df['Year']==2008,'Rating']).mean()
avg_rating_2007 = (df.loc[df['Year']==2007,'Rating']).mean()
print("Average rating in 2016: ", round(avg_rating_2016, 1))
print("Average rating in 2006: ", round(avg_rating_2006,1))
print("Average rating in 2008: ", round(avg_rating_2008,1))
print("Average rating in 2007: ", round(avg_rating_2007, 1))
"""
Average rating in 2016:  6.4
Average rating in 2006:  7.1
Average rating in 2008:  6.8
Average rating in 2007:  7.1
"""

number_of_movies_by_2006 = (df['Year'] < 2007).value_counts()
number_of_movies_by_2016 = (df['Year'] > 2006).value_counts()
increase = number_of_movies_by_2016 - number_of_movies_by_2006
percentage_increase = (increase / number_of_movies_by_2006)*100

