# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': '#E84A27',
    'text': '#13294b'}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Eric',
	style={
            'textAlign': 'center',
            'color': colors['text']
        }
		),

    html.Div(children='''
        Dash: A world where Illinois is good at sports.
    ''', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2], 'y': [24, 14], 'type': 'bar', 'name': 'Opponent'},
                {'x': [1, 2], 'y': [31, 34], 'type': 'bar', 'name': u'Illinois'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
	
	html.Div(children ='This is the bottom of the page', style={'color': colors['text'],
			'textAlign': 'center'})
	])

if __name__ == '__main__':
    app.run_server(debug=True)