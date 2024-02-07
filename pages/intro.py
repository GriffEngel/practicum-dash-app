from dash import html

layout = html.Div(
    [
        html.H1("OpenHawks OER Report", className="fs-1"),
        html.P(
            "Click on the corresponding link to see cost savings data for each academic year"
        ),
    ],
    className="text-center min-vw-100",
)
