from flask import Flask, jsonify, request, render_template, url_for
from datetime import datetime
from data import Formula


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



### HOME PAGE ###

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


### GET DRIVERS LIST ###

@app.route('/f1/drivers/<int:year>', methods = ['GET'])    
def get_driver_standings_by_year(year):
    main = Formula()

    drivers = main.get_drivers(year)
    print(drivers)
    
    return jsonify({f'Driver Standings ({year})' : drivers})


### GET TEAM LIST ###

@app.route('/f1/teams/<int:year>', methods = ['GET'])
def get_teams_standings_by_year(year):
    
    data = Formula()
    
    teams = data.teams_in_formula(year)
    if year < 1958:
        return jsonify({'Not available' : 'The Constructors Championship was not awarded until 1958'})

    else:
        return jsonify({f'Constructor Standings ({year})': teams})
    

### RACES BY YEAR ###    

@app.route('/f1/races/<int:year>')
def race_results_by_year(year):
    
    date = datetime.now()
    date_year = date.year
    
    race_results = Formula()
    results = race_results.race_results_specific_year(year)
    
    if year > date_year:
        return jsonify({'Error' : f'No data is available for the year {year} unless you create a time machine'})
    else:
        return jsonify({f'Race ({year})': results})
    

@app.errorhandler(404)
def error_handling(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_handling(error):
    return render_template('500.html'), 500
 

    
if __name__ == '__main__':
    app.run(host = 'localhost', port = '5000', debug = True)

    

    