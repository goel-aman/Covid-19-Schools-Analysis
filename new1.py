import pandas as pd 
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 

df = pd.read_csv("C:/Users/hp/Desktop/Aman Goel/Python_Codes/datavisualization_lab_da/covid_impact_education.csv")

import pandas as pd 
import numpy as np
optionss=[]
df = pd.read_csv("C:/Users/hp/Desktop/Aman Goel/Python_Codes/datavisualization_lab_da/covid_impact_education.csv")
print(df.head())
df['Date'] = df['Date'].astype(str)
unique_date = df.Date.unique()
df['val'] = 0
for i in unique_date:
    dict = {
        "label": i,
        "value":i
    }
    optionss.append(dict)
    df.loc[(df["Date"] == i) & (df['Status'] == 'Fully open'),'val'] = 0
    df.loc[(df["Date"] == i) & (df['Status'] == 'Partially open'),'val'] = 1
    df.loc[(df["Date"] == i) & (df['Status'] == 'Academic break'),'val'] = 2
    df.loc[(df["Date"] == i) & (df['Status'] == 'Closed due to COVID-19'),'val'] = 3

print(df.head())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Web Application Dashboards With Dash", style={'text-align': 'center'}),
   
    dcc.Dropdown(id = 'slct_year',
    options = optionss,
        multi=False,
        value=2015,
        style={'width': "40%"}
    ),
    html.Div(id='output_container',children=[]),
    html.Br(),
    html.Div('0 -> Fully Open Schools   1 ->  Partially Open    2 -> Academic Break  3 -> Closed due to COVID - 19'),
    dcc.Graph(id='my_bee_map',figure={})
    ])

@app.callback(
    [Output(component_id = 'output_container',component_property='children'),
    Output(component_id='my_bee_map',component_property = 'figure')],
    [Input(component_id='slct_year',component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was : {}".format(option_slctd)
    dfff = df[df['Date'] == option_slctd]

    #plotly Express
    fig = px.choropleth(
        data_frame=dfff,
        locationmode='ISO-3',
        locations='ISO',
        color='val',
        hover_name='Country',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        width=1300,
        height =700,
    )

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
