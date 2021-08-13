import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#combining the two datasets 
employ_df = pd.read_csv('employment_clean.csv')
covid_df = pd.read_csv('covid_clean.csv')

employ_df = employ_df.head(14)

employ_df['Case/Day'] = covid_df['Case/Day']

#COVID Timeline
FIRST_RESTRICTIONS = 3.52-1 #March 16
FIRST_STAGE_3 = 3.97-1 #March 30
EASE_OF_RESTRICTIONS = 5.35-1 #May 11
SECOND_RESTRICTIONS = 7-1 #June 30
STAGE_OF_DISASTER = 8.07-1 #August 2
SECOND_EMERGENCY = 11.27-1 #Novermber 8

#Color Patches
red_patch = mpatches.Patch(alpha = 0.3, color='red', label='First Restriction')
green_patch = mpatches.Patch(alpha = 0.3, color='green', label='Tougher Restrictions')
blue_patch = mpatches.Patch(alpha = 0.3, color='blue', label='Ease of Restrictions')
turquoise_patch = mpatches.Patch(alpha = 0.3, color='turquoise', label='State of Disaster')

#setting x and y values
x = employ_df['Month/Year']
line1 = employ_df['Employed']
line2 = employ_df['Case/Day']
  
#plotting the line 
fig, ax = plt.subplots(figsize = (12, 5))
plt.title('Comparison of Employment and New-Cases Per Month in Victoria')
  
# use twiinx to make secondary y-axis
ax2 = ax.twinx()
ax.plot(x, line1, color = 'r')
ax2.plot(x, line2, color = 'g')
plt.axvspan(FIRST_RESTRICTIONS, FIRST_STAGE_3, alpha = 0.3, color = 'red') #First Lockdown
plt.axvspan(FIRST_STAGE_3, EASE_OF_RESTRICTIONS, alpha = 0.3, color = 'green') #First Tougher Restriction
plt.axvspan(EASE_OF_RESTRICTIONS, SECOND_RESTRICTIONS, alpha = 0.3, color = 'blue') #First Ease of Restriction
plt.axvspan(SECOND_RESTRICTIONS, STAGE_OF_DISASTER, alpha = 0.3, color = 'green') #Second Restriction
plt.axvspan(STAGE_OF_DISASTER, SECOND_EMERGENCY, alpha = 0.3, color = 'turquoise') #Stage 4
plt.legend(handles=[red_patch, green_patch, blue_patch, turquoise_patch])
# giving labels to the axis
ax.set_xlabel('Month/Year', color = 'black')
ax.set_ylabel("Number of persons employed ('000units)", color = 'r')
ax2.set_ylabel('Case/Day', color = 'g')

#saving the plot
plt.savefig('line.png')