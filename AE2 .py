#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1 - Voting System (Working With Files)


import pandas as pd

#Creates a dataframe with two columns
df = pd.DataFrame({
    "Favourite Location": [],
})


#Asks user what their fav location is

favLocation = str(input("What is your location in London? "))
new_row = {'Favourite Location':favLocation, '# of votes':1}

#append row to the dataframe
df = df.append(new_row, ignore_index=True)
print("Location added! ")

#Makes a loop until all values added to dataframe
moreLocations = True

while (moreLocations == True):
    question = input("Would you like to add more? Type yes to add more")
    
    if(question == "yes"):
        
        favLocation = str(input("What is your location in London? "))
        new_row = {'Favourite Location':favLocation, '# of votes':1}

        #append row to the dataframe
        df = df.append(new_row, ignore_index=True)
    
    else:
        moreLocations = False
        
#Counts votes and removes duplicates       
df['# of Votes'] = df.groupby(['Favourite Location']).transform('count')

df = df.drop_duplicates()

#Converts to CSV file called London
df.to_csv("London.csv",sep='\t')

dframe = pd.read_table("file_name.csv", sep="\t")

#Prints out results using a for loop and zip
print("Here are the results so far... ")

for v, x in zip(df['Favourite Location'], df["# of Votes"]):
    print(v, x)

df.drop('# of votes', inplace=True, axis=1)

print(df)


# 

# 

# In[ ]:


#Question 2 - Booking System (OOP)

class Booking:
    def __init__(self, name, location, duration, breakfast):
        self.name = name
        self.location = location
        self.duration = duration
        self.breakfast = breakfast
        
    def sayConfirmation(self):
        print("Hello my name is " + str(self.name) + " and I want to stay in " + str(self.location) + " for " + str(self.duration) + " with " + str(self.breakfast))
   
        
class longBooking(Booking):
    
    def __init__(self, name, location, duration, breakfast):
        duration = "2 months"
        super().__init__(name,location, duration, breakfast)
        


class shortBooking(Booking):
    
    def __init__(self, name, location, duration, breakfast):
        duration = "2 weeks"
        super().__init__(name, location, breakfast)
        
Ella = longBooking("Ella", "London", "long", "breakfast included")
Ella.sayConfirmation()

Jacob = longBooking("Jacob", "London", "short", "breakfast not included")
Jacob.sayConfirmation()


# In[1]:


#Question 3 - Analyzing Data (Charts)

import matplotlib.pyplot as plt
import numpy as np
   
#Makes set x values and randomized y values 
xValues = [1, 2, 3, 4, 5]
yValues = [np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]
secondYValues = [np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]
thirdYValues = [np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]


X_axis = np.arange(len(xValues))

#Makes bar charts and allows them to not overlap. 
plt.bar(X_axis +.2, yValues,width = .2 ,label = yValues)
plt.bar(X_axis -.2,secondYValues, width = .2, label = secondYValues)
plt.bar(X_axis,thirdYValues, width = .2, label = thirdYValues)


plt.title('Random values')
plt.xlabel('Random x values')
plt.ylabel('Random y values')
plt.show()



# In[2]:


#Question 4 - Scraping Data From Wikipedia  (Pandas)

import matplotlib.pyplot as plt
import pandas as pd

#Retreive data 

url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

#Reads HTML File 

df_list = pd.read_html(url)

#[0]Finds the table on the wiki page'

df = pd.read_html(url)[2]

# convert list to dataframe
df = pd.DataFrame(df)

#Makes a dataframe removing all billionares who are not from the US
UsaBillionares = df[(df["Nationality"] == "United States")]

print(UsaBillionares)

#Divider
print("-" *100)

#Makes a new dataframe with only billionares under 30. There are none
youngBillionares = df[(df["Age"] < 30)]

print(youngBillionares)

#Divider
print("-" *100)

#Plots the data with x being the rank and y being the age
df.plot(
   x='No.', 
   y='Age', 
   kind='scatter'
)


# In[2]:


# Question  5 - Analysing Data (Matplot Lib, Pandas & Requests)

# accept input from user on which site they want to search on
# request site content
# parse out bad/useless words
# throw word count into dictionary
# use bar plot to showcase top 5 words
# use https://www.microsoft.com/en-us/

import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame({
    "Word": ["Frequency"],
})


url = input("Enter a website to analyse: ")

source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')

#Creates a list of words to go over and also asks user if they want to add any
stopWords = ['are', 'is', 'her', '\xa0', 'has', 'at', 'from', 'as', '|', 'you', 'of', 'how', 'on', 'i', 'for', 'and', 'they','-', 'his', 'in', 'with', 'the', 'to', 'him', 'a', 'be', '&', 'was', 'that']

answer = True

print("This is a list of words currently being filtered: \n {'are', 'is', 'her', '\xa0', 'has', 'at', 'from', 'as', '|', 'you', 'of', 'how', 'on', 'i', 'for', 'and', 'they','-', 'his', 'in', 'with', 'the', 'to', 'him', 'a', 'be', '&', 'was', 'that'}")
while (answer == True):
    moreStopWords = input("Would you like to add a word/character to filter out? Type yes or no")
    
    if (moreStopWords == 'yes'):
        newStop = input("What word/chracter? ")
        stopWords.append(newStop)
    else:
        break

#Breaks up the website into words that are gonna be used 
all_words = soup.get_text(" ", strip=True).lower().split()

newWord = []

#Makes the rows of the dataframe
for word in all_words:
    if word not in stopWords:
        newWord.append(word)
        new_row = {'Word':word, 'Frequency':1}

        #append row to the dataframe
        df = df.append(new_row, ignore_index=True)
        
    
#Removes duplicate rows
df['Frequency'] = df.groupby(['Word']).transform('count')
df = df.drop_duplicates()

sort_data = df.sort_values('Frequency', ascending = False)

#Gets just the top 5 results
topFive = sort_data.head()

print("The top word is: " + (sort_data['Word'].iloc[df.index[0]]))
print(topFive)

plot = topFive.plot.bar(x="Word", y="Frequency", rot=70, title="Analyzing Top Words from " + url)

#Saves the plot and data
savePlot = input("Would you like to save this graph? Type yes to save ")

if(savePlot == "yes"):
    fileName = input("What would you like to name it? ")
    plot.get_figure().savefig(fileName)
    
saveFile = input("Would you like to save this file? Type yes to save ")

if(saveFile == "yes"):
    fileName = input("What would you like to name it? ")
    topFive.to_csv(fileName + ".csv",sep='\t')


# 

# In[ ]:





# In[ ]:




