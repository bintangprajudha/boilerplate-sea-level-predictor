import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    years_extended = pd.Series(range(1880, 2051))
    sea_level_predicted = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_predicted, color='red', label='Best Fit Line')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Create second line of best fit
    # Filter data for the last 20 years
    recent_df = df[df['Year'] >= 2000] 
    x_recent = recent_df['Year']
    y_recent = recent_df['CSIRO Adjusted Sea Level']
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(x_recent, y_recent)
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_level_recent_predicted = slope_recent * years_recent_extended + intercept_recent
    plt.plot(years_recent_extended, sea_level_recent_predicted, color='green', label='Best Fit Line (2000 onwards)')
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()