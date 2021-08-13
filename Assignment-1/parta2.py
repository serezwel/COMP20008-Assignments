import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description = "Create PNG file output")
parser.add_argument('Filename', metavar = 'filename', type=str, nargs = 2)
args = parser.parse_args()
output_filename = args.Filename

def alt_sum(output_data):
    if output_data.isnull().all():
        return np.nan
    else:
        return output_data.sum()

plot_data = pd.read_csv("owid-covid-data.csv")
plot_data['date'] = pd.to_datetime(plot_data['date'], format = "%Y-%m-%d")
plot_data['year'] = plot_data['date'].dt.strftime('%Y')
plot_year = plot_data.loc[plot_data['year']=="2020"]
aggregated_data = plot_year.groupby(['location']).aggregate({
    'new_cases' : alt_sum,'new_deaths': alt_sum}).reset_index()
aggregated_data['case_fatality_rate'] = aggregated_data['new_deaths']/aggregated_data['new_cases']
plt.figure()
plt.scatter(aggregated_data["new_cases"],aggregated_data["case_fatality_rate"],c=aggregated_data.
    location.astype('category').cat.codes,cmap='hsv',s=10)
plt.xlabel("New Cases")
plt.ylabel("Case Fatality Rate")
plt.title("Case Fatality Rate vs New Cases")
for i, country in enumerate(aggregated_data['location']):
    if aggregated_data['case_fatality_rate'][i] >= 0.075 or aggregated_data['new_cases'][i] >= 2e7:
        plt.annotate(country, xy=(aggregated_data['new_cases'][i], aggregated_data['case_fatality_rate'][i]))
plt.savefig(output_filename[0], format='png')
plt.figure()
plt.scatter(aggregated_data["new_cases"],aggregated_data["case_fatality_rate"],c=aggregated_data.
    location.astype('category').cat.codes,cmap='hsv',s=10)
plt.xscale("log")
plt.xlabel("New Cases (log base 10)")
plt.ylabel("Case Fatality Rate")
plt.title("Case Fatality Rate vs New Cases (log base 10)")
for i, country in enumerate(aggregated_data['location']):
    if (aggregated_data['case_fatality_rate'][i] >= 0.055 or aggregated_data['new_cases'][i] <= 5e2
        or aggregated_data['new_cases'][i] >= 2e7):
        plt.annotate(country, xy=(aggregated_data['new_cases'][i], aggregated_data['case_fatality_rate'][i]))
plt.savefig(output_filename[1], format='png')


