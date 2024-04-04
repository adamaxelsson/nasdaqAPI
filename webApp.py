import pandas as pd
import nasdaqdatalink
import functions
import classes
nasdaqdatalink.read_key(filename="/home/adam/Documents/nasdaqAPI/nasdaqAPI/.corporatenasdaqdatalinkapikey")
"""basic Flask app - demo of using a variable in a route"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/available_stocks/<country>')
def available_stocks(country):
    data = request.args.getlist('data') 
    data_str = ', '.join(data)  # Join the list items into a string
    return f"Available stocks: {data_str}"

@app.route('/')
def home():
    df = nasdaqdatalink.get_table('MER/F1', qopts={"columns": ["countrycode", "longname"]}, paginate=True)
    country_dict = pd.DataFrame(df).to_dict()['countrycode' ]
    name_dict = pd.DataFrame(df).to_dict()['longname']
    name_dict = functions.remove_dups(name_dict)
    companies_per_country_dict = functions.get_companies_from_country(name_dict, country_dict)
 
    return render_template('basic_table.html', 
                           title='Available Countries',
                           countries=(companies_per_country_dict.items()))

if __name__ == '__main__':
    app.run(debug=True)

#API KEY = nTqbqZnZBKDHvpTxas41