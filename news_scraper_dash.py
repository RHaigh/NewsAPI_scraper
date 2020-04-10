from newsapi.newsapi_client import NewsApiClient
from pandas.io.json import json_normalize
import dash_table
import pandas as pd
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State

# Define dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# Enter in news API key and grab all articles from chosen sources using get_everything function
api = NewsApiClient(api_key='INSERT KEY')
all_articles = api.get_everything(sources='bbc-news, abc-news, al-jazeera-english',
                                  from_param=yesterday,
                                  to=today,
                                  page_size=100)
# A comprehensive guide to the newsAPI python client can be found at: https://newsapi.org/docs/client-libraries/python

# Normalize the json and convert to data frame format
df = json_normalize(all_articles['articles'], max_level=1)
df = pd.DataFrame.from_records(df)
df = df[['title', 'publishedAt', 'source.name', 'description']].copy()
# Rename columns
df.columns = ['Title', 'Date', 'Source', 'Summary']
# Convert date/time format to standard dd-mm-yy
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')

# Bring in external stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Be aware that bootstrap themes often slice off sections and require edited padding and wrapping

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H4("News API Scraper"),

    dcc.Input(
        id='text_input',
        placeholder='Enter search...',
        type='text',
        value=''
    ),

    html.Br(),
    html.Br(),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'BBC News', 'value': 'BBC News'},
            {'label': 'ABC News', 'value': 'ABC News'},
            {'label': 'Al Jazeera English', 'value': 'Al Jazeera English'}
        ],
        value='BBC News'
    ),

    html.Br(),
    html.Button('Update', id='button'),
    html.Br(),
    html.Br(),

    dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in df.columns.values],
        data=df.to_dict('records'),
        style_header={
            'textAlign': 'left',
        },
        # Universal styling rules
        style_data={
            'minWidth': '5px', 'maxWidth': '180px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'textAlign': 'left',
        },
        # Individual column styling rules
        style_data_conditional=[
            {'if': {'column_id': 'Date'},
             'width': '5%'},
            {'if': {'column_id': 'Source'},
             'width': '5%'},
            {'if': {'column_id': 'Title'},
             'width': '20%'},
            {'if': {'column_id': 'Summary'},
             'width': '20%'},
        ]
    )
])

# Callback rendering on button click requires one Input and multiple States
@app.callback(Output('table', 'data'),
              [Input('button', 'n_clicks')],
              [State('dropdown', 'value'),
               State('text_input', 'value')])
def update_rows(n_clicks, value1, value2):
    if n_clicks is None:
        return dash.no_update
    f1 = (df['Source'] == value1) # If string is equal to source
    f2 = (df['Title'].str.contains(value2)) # If string contains text input
    dff = df[f1 & f2]
    return dff.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
