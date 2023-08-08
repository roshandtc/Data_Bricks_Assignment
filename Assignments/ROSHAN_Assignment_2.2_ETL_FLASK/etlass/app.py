### intergrate html with flask
###  http 
from flask import Flask, render_template 
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# to Create a connection b/w the SQLite database
engine = create_engine('sqlite:///etl_database.db')  # adding 'new_database.db' as my file

@app.route('/tips')
def indextips():
    #  to Read the Iris and Tips tables 
   
    tips_df = pd.read_sql_table('tips_data', engine)

    # Convert dataframes to HTML tables
    
    tips = tips_df.to_html(classes='table table-striped')
    #print(tips)
    return tips
@app.route('/iris')
def indexiris():
    #  to Read the Iris and Tips tables 
    iris_df = pd.read_sql_table('iris_data', engine)
    

    # Convert dataframes to HTML tables
    iris = iris_df.to_html(classes='table table-striped') 
    
    #print(tips)
    return iris
    #return render_template('iris.html','tips.html',iris_table=iris, tips_table=tips)
if __name__ == '__main__':
    app.run(debug=True)
