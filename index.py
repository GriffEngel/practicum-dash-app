from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from app import app
from pages import intro, year19_20

app.layout = dbc.Nav(
    html.Div(
        [
            dcc.Location(id="url", refresh=False),
            html.Div(
                [
                    dcc.Link("Home", href="/"),
                    html.Br(),
                    dcc.Link("2019-20", href="/year19_20"),
                    html.Br(),
                    dcc.Link("2020-21", href="/"),
                    html.Br(),
                    dcc.Link("2021-22", href="/"),
                    html.Br(),
                    dcc.Link("2022-23", href="/"),
                    html.Br(),
                    dcc.Link("2023-24", href="/"),
                ],
                style={"padding": 10, "flex": 1},
                className="navbar d-flex justify-content-center gap-2 fs-4 link-offset-2",
            ),
            html.Div(id="page-content", style={"padding": 10}),
        ]
    )
)


@callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return intro.layout
    elif pathname == "/year19_20":
        return year19_20.layout
    elif pathname == "/":
        return year20_21.layout
    elif pathname == "/":
        return year21_22.layout
    elif pathname == "/":
        return year22_23.layout
    elif pathname == "/":
        return year23_24.layout
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
