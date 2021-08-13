from datetime import datetime
import pandas as pd


covid_dataset = pd.read_csv("Transmission sources Victoria.csv")
covid_dataset.rename({"Unnamed: 0":"Date"}, axis = 1, inplace=True)
covid_cases = list(covid_dataset)
covid_cases.remove("Date")
covid_dataset['Case/Day'] = covid_dataset[covid_cases].sum(axis=1)
covid_dataset = covid_dataset[["Date", "Case/Day"]]
i = 0
while covid_dataset["Date"][i] != "01/01":
    covid_dataset.at[i,"Date"] = covid_dataset["Date"][i]+"/2020"
    i = i+1
while i<len(covid_dataset):
    covid_dataset.at[i,"Date"] = covid_dataset["Date"][i]+"/2021"
    i = i+1
covid_dataset["Date"] = pd.to_datetime(covid_dataset["Date"], format= "%d/%m/%Y")
covid_dataset["Month/Year"] = covid_dataset["Date"].dt.strftime('%m/%Y') 
covid_dataset = covid_dataset.groupby(['Month/Year'],as_index=False).aggregate({'Case/Day':sum})
covid_dataset["Month/Year"] = pd.to_datetime(covid_dataset["Month/Year"], format="%m/%Y")
covid_dataset = covid_dataset.sort_values(by='Month/Year')
covid_dataset["Month/Year"] = covid_dataset["Month/Year"].dt.strftime('%m/%Y')
covid_dataset = covid_dataset.reset_index(drop=True)

covid_dataset.to_csv("covid_clean.csv")