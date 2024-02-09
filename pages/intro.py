from dash import html, dcc
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


# *========== Keep for Later if Needed ============
# df = pd.read_csv("./Cleaned_Datasets/1fall_2019.csv")
# df2 = pd.read_csv("./Cleaned_Datasets/1spring_2020.csv")
# df3 = pd.read_csv("./Cleaned_Datasets/2summer_2020.csv")
# df4 = pd.read_csv("./Cleaned_Datasets/3fall_2020.csv")
# df5 = pd.read_csv("./Cleaned_Datasets/3spring_2021.csv")
# df6 = pd.read_csv("./Cleaned_Datasets/4fall_2021.csv")
# df7 = pd.read_csv("./Cleaned_Datasets/4spring_2022.csv")
# df8 = pd.read_csv("./Cleaned_Datasets/5fall_2022.csv")
# df9 = pd.read_csv("./Cleaned_Datasets/5spring_2023.csv")
# df10 = pd.concat([df,df2,df3,df4,df5,df6,df7,df8,df9])

data = {
    "Academic Year": ["2019-20", "2020-21", "2021-22", "2022-23"],
    "Total Cost Savings ($)": [191196.90, 301354.38, 300769.68, 466356.72],
}
df11 = pd.DataFrame(data)

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df11["Academic Year"],
        y=df11["Total Cost Savings ($)"],
        mode="lines+markers",
        marker=dict(
            size=10,
            color="#FFCD00",
            symbol="circle",
        ),
        line=dict(color="FireBrick", width=4, dash="dash"),
    )
)
fig.update_layout(
    title="Total Cost Savings by Academic Year",
    xaxis_title="Academic Year",
    yaxis_title="Cost Savings ($)",
)
fig.update_yaxes(range=[0, 500000])
# fig = px.line(df11, x="Academic Year", y="Total Cost Savings ($)")

layout = (
    html.Div(
        [
            html.H1("OpenHawks OER Report", className="fs-1 text-center"),
            html.P(
                "Click on the corresponding link to see cost savings data for each academic year"
            ),
            # TODO: Make this look better
            html.Div([dcc.Graph(figure=fig)]),
        ],
    ),
)
