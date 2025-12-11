import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the cleaned CSV
df = pd.read_csv("final_output.csv")

# Convert date properly
df["date"] = pd.to_datetime(df["date"])

# Group by date and region
df = df.groupby(["date", "region"], as_index=False)["Sales"].sum()

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(className="container", children=[

    html.H1("Pink Morsel Sales Visualiser", className="title"),

    html.Div("Filter by Region:", className="label"),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        className="radio"
    ),

    dcc.Graph(id="sales-line-chart")

])

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df.groupby("date", as_index=False)["Sales"].sum()
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "Sales": "Sales"}
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
