import dash
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc
import random
import time
import numpy as np
from dash.exceptions import PreventUpdate

dash.register_page(__name__, path='/', name='Home',
                   title='Guitar Layout Renderer',
                   description = 'Tool designed to render the guitar fretboard layout with dynamic css')

############################################################################################
# Page layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2(['Guitar Fretboard Layout Renderer'])
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.P(['A 2-fret sample is displayed below, based on the css style properties on the left'], style={"text-align":"center", "margin-top":"20px"})
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([], width = 4),
        dbc.Col([
            html.Div(id = 'guitar-fret-headers', children = [
                html.Div(id = 'fret1-header-column', children = [
                    html.Div(id = 'fret1-header', children = 'fr-1')
                ]),
                html.Div(id = 'fret2-header-column', children = [
                    html.Div(id = 'fret2-header', children = 'fr-2')
                ])
            ]),
            html.Div(id = 'guitar-neck', children = [
                html.Div(id = 'fret1-column', children = [
                    html.Div(id = 'fr1-string-6'),
                    html.Div(id = 'fret1-element-5'),
                    html.Div(id = 'fr1-string-5'),
                    html.Div(id = 'fret1-element-4'),
                    html.Div(id = 'fr1-string-4'),
                    html.Div(id = 'fret1-element-3'),
                    html.Div(id = 'fr1-string-3'),
                    html.Div(id = 'fret1-element-2'),
                    html.Div(id = 'fr1-string-2'),
                    html.Div(id = 'fret1-element-1'),
                    html.Div(id = 'fr1-string-1')
                ]),
                html.Div(id = 'fret2-column', children = [
                    html.Div(id = 'fr2-string-6'),
                    html.Div(id = 'fret2-element-5'),
                    html.Div(id = 'fr2-string-5'),
                    html.Div(id = 'fret2-element-4'),
                    html.Div(id = 'fr2-string-4'),
                    html.Div(id = 'fret2-element-3'),
                    html.Div(id = 'fr2-string-3'),
                    html.Div(id = 'fret2-element-2'),
                    html.Div(id = 'fr2-string-2'),
                    html.Div(id = 'fret2-element-1'),
                    html.Div(id = 'fr2-string-1')
                ]),
            ])
        ], width=4),
        dbc.Col([], width = 4),
    ])
])

############################################################################################
# Guitar Neck Styling
@callback(Output('guitar-neck', 'style'),
          Output('guitar-fret-headers', 'style'),
          Input('input-neck-background', 'value'))
def apply_style(neck_background):
    style_ = {"margin" : "30px 0px 0px 0px",
              "display" : "flex",
              "background-repeat" : "repeat-x",
              "border-radius" : "0.5%",
              "padding" : "3px 0px 3px 0px",
              "text-align" : "center"}
    style_neck = style_.copy()
    style_neck["background"] = neck_background
    style_neck["box-shadow"] = "0 0 0.6em #A9A9A9"
    style_neck["margin"] = "5px 0px 0px 0px"
    return style_neck, style_

# Guitar Fret Styling - External Div
@callback(Output('fret1-column', 'style'),
          Output('fret2-column', 'style'),
          Output('fret1-header-column', 'style'),
          Output('fret2-header-column', 'style'),
          Input('input-fret-width', 'value'))
def apply_style(width):
    style_ = {"width" : width}
    return style_, style_, style_, style_

# Guitar Fret Styling - Internal Fret Element div
@callback(Output('fret1-element-5', 'style'),
          Output('fret1-element-4', 'style'),
          Output('fret1-element-3', 'style'),
          Output('fret1-element-2', 'style'),
          Output('fret1-element-1', 'style'),
          Output('fret2-element-5', 'style'),
          Output('fret2-element-4', 'style'),
          Output('fret2-element-3', 'style'),
          Output('fret2-element-2', 'style'),
          Output('fret2-element-1', 'style'),
          Input('input-fret-elem-height', 'value'),
          Input('input-fret-elem-border-right', 'value'),
          Input('input-fret-elem-border-image', 'value'),
          Input('input-fret-elem-box-shadow', 'value'),
          Input('input-fret-dot-background-image', 'value'))
def apply_style(height, border_right, border_image, box_shadow, dot_background_image):
    style_ = {"height" : height,
              "border" : "0px",
              "border-right": border_right,
              "border-image": border_image,
              "box-shadow": box_shadow              
              }
    style_dotted = style_.copy()
    style_dotted["background-image"] = dot_background_image
    return style_, style_, style_, style_, style_,   style_, style_, style_dotted, style_, style_

# Guitar Strings Styling
@callback(Output('fr1-string-6', 'style'),
          Output('fr1-string-5', 'style'),
          Output('fr1-string-4', 'style'),
          Output('fr1-string-3', 'style'),
          Output('fr1-string-2', 'style'),
          Output('fr1-string-1', 'style'),
          Output('fr2-string-6', 'style'),
          Output('fr2-string-5', 'style'),
          Output('fr2-string-4', 'style'),
          Output('fr2-string-3', 'style'),
          Output('fr2-string-2', 'style'),
          Output('fr2-string-1', 'style'),
          Input('input-string-height', 'value'),
          Input('input-string-height-reduction', 'value'),
          Input('input-string-background', 'value'),
          Input('input-string-box-shadow', 'value'))
def apply_style(height, height_red, background, box_shadow):
    style_6 = {
        "margin" : "0px 0px 0px 0px",
        "border" : "none",
        "position" : "relative",
        "height" : height,
        "background" : background,
        "box-shadow" : box_shadow}
    style_5 = style_6.copy(); style_4 = style_6.copy(); style_3 = style_6.copy(); style_2 = style_6.copy(); style_1 = style_6.copy()
    if height_red == '' or not height_red:
        height_red = '0.00em'
    style_5["height"] = str(float(height[:-2]) - float(height_red[:-2]))+'em'
    style_4["height"] = str(float(height[:-2]) - 2*float(height_red[:-2]))+'em'
    style_3["height"] = str(float(height[:-2]) - 3*float(height_red[:-2]))+'em'
    style_2["height"] = str(float(height[:-2]) - 4*float(height_red[:-2]))+'em'
    style_1["height"] = str(float(height[:-2]) - 5*float(height_red[:-2]))+'em'
    return style_6,style_5,style_4,style_3,style_2,style_1,   style_6,style_5,style_4,style_3,style_2,style_1