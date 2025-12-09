import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the CSV
df = pd.read_csv("final_output.csv")

# Convert date column properly
df["date"] = pd.to_datetime(df["date"])

# Convert Sales to number (just to be safe)
df["Sales"] = pd.to_numeric(df["Sales"])

# Sort by date
df = df.sort_values("date")

# OPTIONAL: Group by date (if multiple entries per day exist)
df = df.groupby("date", as_index=False)["Sales"].sum()

# Create the line chart
fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "Sales": "Sales ($)"}
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
