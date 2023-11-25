from dash import html
import dash_bootstrap_components as dbc
import dash

_nav = dbc.Container([
	dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([html.Img(disable_n_clicks = True, src = 'assets/img/Guitar_001.png', height = '90em')],
                width = 10, className = 'nav-col-img'),
        dbc.Col([], width = 1)
    ])
])