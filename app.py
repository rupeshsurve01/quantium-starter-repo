import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load cleaned data
df = pd.read_csv("final_output.csv")
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    children=[

        # HEADER (tests expect this exact text)
        html.H1("Pink Morsel Sales Visualiser"),

        # REGION PICKER WRAPPER
        html.Div([
            html.Label("Select Region:"),
            dcc.RadioItems(
                id="region-picker",
                options=[
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                    {"label": "All", "value": "all"}
                ],
                value="all",
                inline=True
            )
        ]),

        # MAIN GRAPH (tests expect id="line-chart")
        dcc.Graph(id="line-chart")
    ]
)

# Callback to update the chart
@app.callback(
    Output("line-chart", "figure"),
    Input("region-picker", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == selected_region]

    fig = px.line(
        filtered,
        x="date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        title_x=0.5
    )

    return fig


# Only run server if file executed directly (not during tests)
if __name__ == "__main__":
    app.run(debug=True)
