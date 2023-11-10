# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:47:03 2023

@author: bhavin
"""


import pandas as pd
import matplotlib.pyplot as plt

def create_line_plot(dataframe, countries):
    """
    Create a line plot for the specified countries from the given DataFrame.
    Parameters:
    - dataframe: DataFrame containing the data.
    - countries: List of country names to plot.
    """
    # Transpose DataFrame
    dataf_t = pd.DataFrame.transpose(dataframe)

    # Set the country names as columns
    dataf_t.columns = dataf_t.iloc[0]

    # Remove the first line (not containing numerical data)
    dataf_t = dataf_t.iloc[1:]

    # Clean data, drop NaN values
    dataf_clean = dataf_t[countries].dropna()

    # Plotting the Line Graph
    dataf_clean.plot(marker = 'o', linestyle = '-')

    plt.legend(countries)
    plt.title('Fuel Imports Over Years')
    plt.xlabel('Year')
    plt.ylabel('Fuel Imports')

    # Save the plot to a file
    plt.savefig("LineGraph.png")

    # Show the plot
    plt.show()

# Read data from CSV
fdata = pd.read_csv("Fuel imports_Data.csv")

# Select relevant data for the line plot
dfdata = fdata.loc[:6, ['Country Name', '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]', '2022 [YR2022]']]

# List of countries to plot
countries_to_plot = ["Japan", "China", "India", "United States", "Germany"]

# Calling Function to create Line Plot, Pie Plot 
create_line_plot(dfdata, countries_to_plot)

# Pie Chart
def pie_chart(dataframe, value_column, label_column, figsize=(8, 8), colors=None):
    
    """
    Create a pie chart from the given DataFrame.
    Parameters:
    - dataframe: DataFrame containing the data.
    - value_column: The column representing the values for the pie chart.
    - label_column: The column containing labels for the pie chart.
    - figsize: Figure size.
    - colors: List of colors for the pie chart.
    """
    
    # Plotting the pie chart
    ax = dataframe.plot.pie(
        y=value_column,
        labels=dataframe[label_column],
        autopct='%1.0f%%',
        figsize=figsize,
        colors=colors
    )

    # Show the plot
    plt.show()

    # Save the plot to a file
    plt.savefig("piechart.png")

# DataFrame of each country and its population in 2022
dataframe_country_population = pd.DataFrame({
    'Country Name': ['India', 'China', 'United States', 'Indonesia'],
    'population_in_2022': [1417173173.0, 1412175000.0, 333287557.0, 275501339.0]
})

# List of colors for the pie chart
pie_colors = ['orange', 'lightblue', 'yellow', 'red']

# Calling Function to create and display the pie chart
pie_chart(dataframe_country_population, 'population_in_2022', 'Country Name', figsize=(8, 8), colors=pie_colors)



# Bar Chart Data
years = ['2018', '2019', '2020', '2021', '2022']
india_population = [1369003306.0, 1383112050.0, 1396387127.0, 1407563842.0, 1417173173.0]
china_population = [1402760000.0, 1407745000.0, 1411100000.0, 1412360000.0, 1412175000.0]

# Defining UDF For Comparing India And China's Population
def comparison_bar_chart(x_values, y1_values, y2_values, label1, label2, title, x_label, y_label):
    bar_width = 0.25
    index = range(len(x_values))

    plt.bar(index, y1_values, width=bar_width, label=label1, color='lightblue')
    plt.bar(index, y2_values, width=bar_width, label=label2, color='orange', align='edge')

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(index, x_values)
    plt.legend()
    plt.show()
    
    # Save BarChart as file
    plt.savefig('barchart.png')

# Call the function with India and China's population data
comparison_bar_chart(years, india_population, china_population, 'India', 'China',
                            'India vs China Population Over the Years', 'Year', 'Population')
