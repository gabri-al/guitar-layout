from dash import html, dcc
import dash_bootstrap_components as dbc

############################################################################################
# Import shared components

from assets.footer import _footer
from assets.nav import _nav

############################################################################################

_sidebar = html.Div([
    dbc.Row([
        dbc.Col([_nav], width = 12)
    ]),
    ## Guitar Neck layout filters
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([html.H4(['Configure the Guitar Layout'], className = 'filter-title')], width = 10),
        dbc.Col([], width = 1),
    ]),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([
            "Background: ", dcc.Input(type = 'text', id = 'input-neck-background', 
                                      value = '-webkit-gradient(linear, left top, right top, color-stop(0%,rgba(233,223,196,1)), color-stop(1%,rgba(233,223,196,1)), color-stop(2%,rgba(237,227,200,1)), color-stop(24%,rgba(237,227,200,1)), color-stop(25%,rgba(235,221,195,1)), color-stop(48%,rgba(233,223,196,1)), color-stop(49%,rgba(235,221,195,1)), color-stop(52%,rgba(230,216,189,1)), color-stop(53%,rgba(230,216,189,1)), color-stop(54%,rgba(233,219,192,1)), color-stop(55%,rgba(230,216,189,1)), color-stop(56%,rgba(230,216,189,1)), color-stop(57%,rgba(233,219,192,1)), color-stop(58%,rgba(230,216,189,1)), color-stop(73%,rgba(230,216,189,1)), color-stop(74%,rgba(233,219,192,1)), color-stop(98%,rgba(233,219,192,1)), color-stop(100%,rgba(235,221,195,1)))')
        ], width = 10),
        dbc.Col([], width = 1),
    ]),
    ## Frets layout filters
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([html.H4(['Frets Layout'], className = 'filter-title')], width = 10),
        dbc.Col([], width = 1),
    ]),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col(["Width : ", dcc.Input(type = 'text', id = 'input-fret-width', value = '4.3em')], width = 5),
        dbc.Col(["Fret element height : ", dcc.Input(type = 'text', id = 'input-fret-elem-height', value = '3.1em')], width = 6),
    ]),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col(["Border-right : ", dcc.Input(type = 'text', id = 'input-fret-elem-border-right', value = '0.38em solid')], width = 5),
        dbc.Col(["Border-image : ", dcc.Input(type = 'text', id = 'input-fret-elem-border-image', value = 'linear-gradient(75deg, #686868, #d0d0d0) 1')], width = 6),
    ]),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col(["Box-shadow : ", dcc.Input(type = 'text', id = 'input-fret-elem-box-shadow', value = '0.045em 0.045em 0.2em #686868')], width = 5),
        dbc.Col(["Dotted fret background-image : ", dcc.Input(type = 'text', id = 'input-fret-dot-background-image', value = 'radial-gradient(#4646464b 20%, transparent 20%)')], width = 6),
        dbc.Col([], width = 6),
    ]),    
    ## Strings layout filters
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([html.H4(['Strings Layout'], className = 'filter-title')], width = 10),
        dbc.Col([], width = 1),
    ]),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col(["Height : ", dcc.Input(type = 'text', id = 'input-string-height', value = '0.2em')], width = 5),
        dbc.Col(["Reduce each string height of : ", dcc.Input(type = 'text', id = 'input-string-height-reduction', value = '0.02em')], width = 6),
     ]),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col(["Background : ", dcc.Input(type = 'text', id = 'input-string-background', value = 'linear-gradient(#202020, #686868, #A9A9A9)')], width = 5),
        dbc.Col(["Box-shadow : ", dcc.Input(type = 'text', id = 'input-string-box-shadow', value = '0.05em 0.05em 0.2em #202020')], width = 6),
        dbc.Col([], width = 6),
     ]),
    ## Footer
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([html.Hr([], className = 'hr-footer')], width = 10),
        dbc.Col([], width = 1)
    ]),
    dbc.Row([
        dbc.Col([_footer], width = 12)
    ])
], className = 'sidebar-div')