from dash import Dash, html, dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ["https://codepen.io/dilums/pen/ZEBowxX.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}],
            'layout':{'title': 'Dash Data Visualization'}
        }
    ),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}],
            'layout':{'title': 'Dash Data Visualization'}
        }
    )
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
