import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    df = df.rename({'CSIRO Adjusted Sea Level': 'CSIRO_Adjusted_Sea_Level'}, axis=1)
    plt.scatter(df.Year, df.CSIRO_Adjusted_Sea_Level, c ="blue", s = 40, alpha = 0.5)

    # Create first line of best fit
    res = linregress(df.Year, df.CSIRO_Adjusted_Sea_Level)
    plt.figure(figsize=(15,6))
    plt.plot(np.arange(df.Year.min(),2050,1), np.arange(df.Year.min(),2050,1) * res.slope + res.intercept, 'o', label = 'original data')
    plt.plot(df.Year, res.intercept + res.slope * df.Year, 'r', label = 'fitted line')
    plt.grid()
    plt.legend()
    plt.show()
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    lineB = linregress(df_2000['Year'], df_2000['CSIRO_Adjusted_Sea_Level'])
    xB = np.arange(2000,2050,1)
    yB = xB*lineB.slope + lineB.intercept
    plt.plot(xB,yB)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()