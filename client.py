import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


df=pd.read_csv("life_expectancy.csv")
fig=go.Figure()

def lifexp():
    fig=go.Figure()
    fig.update_layout(
            title={
                "text":"LifeExpectancy",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title =" ",
            yaxis_title = "Esperanza de años",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Peru",
                        y=df["Peru"],
                        line = dict(color='red')
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Argentina",
                        y=df["Argentina"],
                        line = dict(color='skyblue')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Colombia",
                        y=df["Colombia"],
                        line = dict(color='goldenrod')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Alemania",
                        y=df["Germany"],
                        line = dict(color='black')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="China",
                        y=df["China"],
                        line = dict(color='green')
                    )

    )
        
    return fig