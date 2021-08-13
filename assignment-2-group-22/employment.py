import pandas as pd
df = pd.read_excel("unemployment vic  (2).xls",sheet_name = "Data1")

employment = df.loc[75:]["Victoria ;  Employed total ;  Persons ;"]
date = df.loc[75:]["Unnamed: 0"]
date = date.dt.strftime('%m/%Y')

output = pd.concat([date, employment], axis = 1, join = 'inner')
output = output.rename({"Unnamed: 0" : "Month/Year"}, axis = 1)
output = output.rename({"Victoria ;  Employed total ;  Persons ;":"Employed"}, axis = 1)

output = output.set_index('Month/Year')

output.to_csv("employment_clean.csv")