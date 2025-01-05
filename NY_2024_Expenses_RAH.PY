# NY 2024 Fuel_Cost
'''
Assumptions etc //
* I don't really know what efficiency the surf actually consumes fuel at, I've just googled and then estimated
* In reality, I payed a varied fuel price across the country, across different stations
* Distance is estimated by Google Maps
'''

# Imports
import pandas as pd

# Trip Dataframe
data = {
"Trip": ["Masterton to Hamilton", "Hamilton to Raglan", "Raglan to Hamilton", "Hamilton to Whitianga", "Whitianga to Hamilton", "Hamilton to Raglan", "Raglan to Masterton"], 
"Persons(s)": ["Kay + Russ + Olivia", "Kayleigh + Russell", "Kayleigh + Russell", "Kay + Russ + Sita + Allan", "Kay + Russ + Sita + Allan", "Kay + Russ + Olivia", "Kay + Russ + Olivia"],
"no_people_in_trip": [3, 2, 2, 4, 4, 3, 3],
"Distance": [482, 43.8, 43.8, 181.7, 181.7, 43.8, 482],
"Fuel_Efficiency": [14, 14, 14, 14, 14, 14, 14],
"Gas_Cost": [2.65, 2.65, 2.65, 2.65, 2.65, 2.65, 2.65],
}

# Creating df
df = pd.DataFrame(data)

# Calculating Fuel Amount
df["Fuel_Amount"] = df.Distance / df.Fuel_Efficiency
df["Fuel_Amount_Rounded"] = df["Fuel_Amount"].round(2)

# Calculating Total Fuel Cost
df["Total_Fuel_Cost"] = df.Fuel_Amount * df.Gas_Cost
df["Total_Fuel_Cost_Rounded"] = df["Total_Fuel_Cost"].round(2)

# Calculating Cost Per Person
df["Cost_Per_Person"] = df.Total_Fuel_Cost / df.no_people_in_trip
df["Cost_Per_Person_Rounded"] = df["Cost_Per_Person"].round(2)

# Printing Final Df
print(df)

# Exporting to CSV
df.to_csv('NY_2024_Expenses.csv', index=False)
