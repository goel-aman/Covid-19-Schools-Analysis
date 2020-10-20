
import pandas as pd 
import numpy as np

df = pd.read_csv("C:/Users/hp/Desktop/Aman Goel/Python_Codes/datavisualization_lab_da/covid_impact_education.csv")
print(df.head())
unique_date = df.Date.unique()
dict =  {
    'date': unique_date,
    'fully_open' : [],
    'partially_open' : [],
    'closed': []
}

for i in unique_date:
    new_df = df[df["Date"] == i]
    val = len(new_df[new_df["Status"] == "Fully open"].index)
    dict['fully_open'].append(val)
    partially_open = len(new_df[new_df["Status"] == 'Partially open'].index)
    closed = len(new_df[new_df["Status"] == 'Closed due to COVID-19'].index)
    dict['partially_open'].append(partially_open)
    dict['closed'].append(closed)

final_data = pd.DataFrame(dict)

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children= [
    html.H1('Affect On Schools Due To Covid - 19'),
    dcc.Graph(
        id = 'example',
        figure = {
            'data': [
                {'x': final_data["date"].to_numpy() , 'y': final_data["fully_open"].to_numpy(), 'type': 'line', 'name':'Country Count With Schools Open'}
                ],
                'layout':{
                    'title':'Number Of Countries Where Schools Were Open Vs Date (World Data)'
                }
        }
    ),
    dcc.Graph(
        id = 'example-1',
        figure = {
            'data': [
                {'x' : final_data["date"].to_numpy(), 'y':final_data['closed'].to_numpy(),'type':'line','name': 'Country Count With School Closed'}
            ],
            'layout': {
                'title': 'Number Of Countries Where Schools Were Closed Vs Date (World Data)'
            }
        }
    ),
    dcc.Graph(
        id = 'example-2',
        figure = {
            'data':[
                {'x': final_data["date"].to_numpy(),'y':final_data['partially_open'].to_numpy(),'type':'line','name': 'Country Count With Schools Patially Open'}
            ],
            'layout':{
                'title': 'Number Of Countries Where Schools Were Patially Open Vs Date (World Data)'
            }
        }
    ),
    dcc.Graph(
        id = 'example-3',
        figure = {
            'data': [
                {'x': final_data["date"].to_numpy() , 'y': final_data["fully_open"].to_numpy(), 'type': 'line', 'name':'Country Count With Schools Open'},
                {'x' : final_data["date"].to_numpy(), 'y':final_data['closed'].to_numpy(),'type':'line','name': 'Country Count With School Closed'},
                {'x': final_data["date"].to_numpy(),'y':final_data['partially_open'].to_numpy(),'type':'line','name': 'Country Count With Schools Patially Open'}
            ],
            'layout':{
                'title': 'Comparision Of Open Vs Closed Vs Patially Open (World Data)' 
            }
        }
    )
    ])


if __name__ == '__main__':
    app.run_server(debug = True)
