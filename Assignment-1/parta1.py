import pandas as pd
import argparse
import numpy as np


parser = argparse.ArgumentParser(description = "Create CSV file output")
parser.add_argument('Filename', metavar = 'filename', type=str)
args = parser.parse_args()
output_filename = args.Filename

def alt_sum(elements):
    if elements.isnull().all():
        return np.nan
    else:
        return elements.sum()

covid_data = pd.read_csv('owid-covid-data.csv')
covid_data['date'] = pd.to_datetime(covid_data['date'], format = "%Y-%m-%d")
covid_data['year'] = covid_data['date'].dt.strftime('%Y')
covid_data['month'] = covid_data['date'].dt.strftime('%m')
covid_year = covid_data.loc[covid_data['year']=="2020"]
covid_year = covid_year[['location','month','total_cases','new_cases','total_deaths','new_deaths','date','year']]
output_data = covid_year.groupby(['location', 'month']).aggregate({'total_cases':max,
    'new_cases' : alt_sum, 'total_deaths' : max, 'new_deaths': alt_sum})
output_data['case_fatality_rate'] = output_data['new_deaths']/output_data['new_cases']
case_fatality_rate = output_data['case_fatality_rate']
output_data.drop(columns = 'case_fatality_rate', inplace=True)
output_data.insert(2, 'case_fatality_rate', case_fatality_rate)

output_data.to_csv(output_filename)
print(output_data.head)

