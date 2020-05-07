from flask import request, Flask, render_template
import requests
import json
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def home():
    resp = requests.get('https://pomber.github.io/covid19/timeseries.json')
    results = json.loads(resp.text)
    options = sorted(list(results.keys()))

    return render_template('home.html', options=options)

@app.route('/', methods=['POST'])
def confirmed_graph():
    country = request.form['options']
    country2 = request.form['options2']
    
    resp = requests.get('https://pomber.github.io/covid19/timeseries.json')

    results = json.loads(resp.text)

    c1_x_vals = [each['date'] for each in results[f'{country}']]
    c1_y_vals = [each['confirmed'] for each in results[f'{country}']]
    c2_x_vals = [each['date'] for each in results[f'{country2}']]
    c2_y_vals = [each['confirmed'] for each in results[f'{country2}']]
        
    df = pd.DataFrame(data=[c1_x_vals, 
                            c1_y_vals, 
                            c2_x_vals, 
                            c2_y_vals,]).T

    df.columns = [f'{country}X', 
                  f'{country}Y', 
                  f'{country2}X', 
                  f'{country2}Y']
        
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=c1_x_vals, y=c1_y_vals,
                        mode='lines',
                        name=f'{country}')
                 )
    
    fig.add_trace(go.Scatter(x=c2_x_vals, y=c2_y_vals,
                        mode='lines',
                        name=f'{country2}')
                 )
    
    fig.update_layout(title= f"{country} vs {country2} Coronavirus",
                      xaxis_title="Date",
                      yaxis_title="Number of confirmed cases",
                     )

    return home(), fig.show()
