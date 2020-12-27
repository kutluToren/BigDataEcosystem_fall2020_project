import pandas as pd
import numpy as np
import random



df = pd.read_csv("bank_prospects.csv")

#Rename 2 columns to make the data more like account information
df.rename(columns={'Purchased':'Premium','Salary':'Balance'},inplace=True)


country_array = ["France","Germany","Belgium","England","Spain","Italy","Denmark","Austria","Holland"];
random_data_size = 100

for i in range(random_data_size):
    random.seed(52+i)
    bal = random.randrange(5000,55000)
    age = random.randrange(18,75)
    gender = random.choice(["Male","Female"])
    country = random.choice(country_array)
    premium = random.choice(["N","Y"])
    tmp=pd.DataFrame([{'Age':age,'Balance':bal,'Gender':gender,'Country':country,'Premium':premium}])
    df = pd.concat([df,tmp], ignore_index=True)
    

#add 10 wrong NaN numbers for balance
for i in range(10):
    random.seed(10+i)
    age = random.randrange(18,75)
    gender = random.choice(["Male","Female"])
    country = random.choice(country_array)
    premium = random.choice(["N","Y"])
    tmp=pd.DataFrame([{'Age':age,'Balance':np.nan,'Gender':gender,'Country':country,'Premium':premium}])
    df = pd.concat([df,tmp], ignore_index=True)

# add 10 countries with unknown value
for i in range(10):
    random.seed(25+i)
    bal = random.randrange(5000,55000)
    age = random.randrange(18,75)
    gender = random.choice(["Male","Female"])
    premium = random.choice(["N","Y"])
    tmp=pd.DataFrame([{'Age':age,'Balance':bal,'Gender':gender,'Country':"unknown",'Premium':premium}])
    df = pd.concat([df,tmp], ignore_index=True)  


df = df.sample(frac=1)

df.to_csv("bank_data_{}.csv".format(random_data_size),index=False)