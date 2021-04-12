import requests
from bs4 import BeautifulSoup as soup
import pandas as pd 
import numpy as np 




class Formula:
        
    def get_drivers(self, year):
        
        """Get drivers for a specific year 

        Returns:
            list : dictionnary in a list
            
        """
        
        driver_pos = 1
        
        drivers_standings = []
        
        url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
        
        content = requests.get(url)
        soups = soup(content.text, 'html.parser', from_encoding="iso-8859-8")
        
        drivers_first_name = soups.find_all('span', attrs = {'class':'hide-for-tablet'})
        drivers_last_name = soups.find_all('span', attrs = {'class':'hide-for-mobile'})
        driver_nationality = soups.find_all('td', class_ = 'dark semi-bold uppercase')
        driver_car = soups.find_all('a', class_ = 'grey semi-bold uppercase ArchiveLink')
        driver_points = soups.find_all('td', attrs = {'class' : 'dark bold'})

        for first, last, nation, car, points in zip(drivers_first_name, drivers_last_name, driver_nationality, driver_car, driver_points):
            
            data = {}
            
            data['Position'] = driver_pos
            data['First Name'] = first.text
            data['Last Name'] = last.text
            data['Nationality'] = nation.text
            data['Car'] = car.text
            data['Points'] = points.text
            
            drivers_standings.append(data)  
            
            driver_pos += 1          
        
        return drivers_standings
            
############
    
    def teams_in_formula(self, year):
        
        """Get every team from a specifiy year

        Returns:
            list: dictionary in a list
        """
    
        team_standings = []
        
        team_pos = 1
        
        url = f'https://www.formula1.com/en/results.html/{year}/team.html'
        
        content = requests.get(url)
        soups = soup(content.text, 'lxml')
        
        team = soups.find_all('a', class_ = 'dark bold uppercase ArchiveLink')
        point = soups.select('td.dark.bold')
        length = soups.find_all(class_ = 'resultsarchive-table')
        

        for teams, points in zip(team, point):

            data = {}
            
            data['Position'] = index
            data['Team'] = teams.text
            data['Points'] = points.text  
            
            team_pos += 1          
            
            team_list.append(data)
           
        
        return team_standings

###########


    def race_results_specific_year(self,year):
        
        """Get race results from specific year

        Returns:
            list: dictionnary in a list
        """
        
        results_url = f'http://www.formula1.com/en/results.html/{year}/races.html'
        
        content = requests.get(results_url)
        soups = soup(content.text, 'html.parser')
        
        race_results = []
        
        grand_prix = soups.find_all(class_ = 'dark bold ArchiveLink')
        date = soups.find_all(class_ = 'dark hide-for-mobile')
        winner_first_name = soups.find_all('span', class_ = 'hide-for-tablet')
        winner_last_name = soups.find_all('span', class_ = 'hide-for-mobile')
        abbreviation_name = soups.find_all('span', class_ = 'uppercase hide-for-desktop')
        car = soups.find_all('td', class_ = 'semi-bold uppercase')
        laps = soups.find_all(class_ = 'bold hide-for-mobile')
        lap_time = soups.find_all(class_ = 'dark bold hide-for-tablet')
        
        for gp, dates, first, last, abb, cars, lap, laps_time in zip(grand_prix, date, winner_first_name, winner_last_name, abbreviation_name, car, laps, lap_time):
            
            results = {}
            results['Grand Prix'] = gp.text.strip()
            results['Date'] = dates.text
            results['First Name'] = first.text
            results['Last Name'] = last.text
            results['Abbreviation'] = abb.text
            results['Car'] = cars.text
            results['Lap'] = lap.text
            results['Lap Time'] = laps_time.text
            
            race_results.append(results)

        return race_results


    def get_live_coverage_data(self):
        pass
        
            








