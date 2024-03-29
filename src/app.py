from dash import Dash
import dash_bootstrap_components as dbc


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0",
        }
    ],
)
