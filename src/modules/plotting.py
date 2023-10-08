import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Trend for specific country

# Make function to visualize trend of any country
def visualize_country_trend(df=None, country=None):
    if country is None:
        print('Please provide a proper country name.')
        return
    country = country.title()
    
    data = df[df['Country'].str.contains(country, case=False)]
    
    if len(data) == 0:
        print('Country name does not match any records.')
        return
    
    country = data['Country'].unique()[0]
    
    plt.figure(figsize=(11, 5))
    sns.lineplot(data=data, x='Year', y='CO2EmissionRate')
    plt.xticks(rotation=0)
    plt.title(f'Global CO2 Emission Trend of {country}')
    plt.xlabel('')
    plt.ylabel('CO2 Emission in mt')
    plt.show()

# Example usage:
# visualize_country_trend('United States')  # Replace 'United States' with the desired country




# Trend for specific year

# Function to visualize trend of any country
def visualize_year_trend(df, year=None):
    try:
        year = int(year)
        if year < 1991 or year > 2018:
            print('Please enter a year between 1991 and 2018.')
            return
        data = df[df['Year'] == year]
        data = data.sort_values(by='CO2EmissionRate', ascending=False).head(10)
        plt.figure(figsize=(11, 5))
        sns.barplot(data=data, y='Country', x='CO2EmissionRate')
        plt.xticks(rotation=0)
        plt.title(f'Top 10 CO2 Emission Contributors in {year}')
        plt.ylabel('')
        plt.xlabel('CO2 Emission in mt')
        plt.show()
    except ValueError:
        print('Please enter a valid year.')

# Example usage:
# visualize_year_trend(2015)  # Replace 2015 with the desired year