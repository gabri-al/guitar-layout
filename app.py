from dash import Dash, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash
from dash import html

_font = "https://fonts.googleapis.com/css2?family=Lato&display=swap"
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, _font],
		   suppress_callback_exceptions=True, prevent_initial_callbacks=True)
app._favicon = ("assets/img/favicon.ico") # custom path to favicon
server = app.server

############################################################################################
# Import shared components
from assets.sidebar import _sidebar

############################################################################################
# App Layout
app.layout = dbc.Container([
	dbc.Row([
        dbc.Col([
			_sidebar
        ], width = 5),
        dbc.Col([
            dbc.Row([dash.page_container])
	    ], className = 'page-content', width = 7),
    ])
], fluid=True)

############################################################################################
# Run App
if __name__ == '__main__':
	app.run_server(debug=False)