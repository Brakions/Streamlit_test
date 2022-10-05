import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


df=pd.read_csv("life_expectancy.csv")
fig=go.Figure()

#Life Expectancy in America
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
                        name="U.S.A",
                        y=df["United States"],
                        line = dict(color='black')
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
                        name="Peru",
                        y=df["Peru"],
                        line = dict(color='red')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Mexico",
                        y=df["Mexico"],
                        line = dict(color='green')
                    )

    )
        
    return fig
#Life Expectancy in Europa
def lifexpe():
    fige=go.Figure()
    fige.update_layout(
            title={
                "text":"LifeExpectancy",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title =" ",
            yaxis_title = "Esperanza de años",
            xaxis_rangeslider_visible=False
        )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="España",
                        y=df["Spain"],
                        line = dict(color='black')
                    )
            )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Francia",
                        y=df["France"],
                        line = dict(color='skyblue')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Alemania",
                        y=df["Germany"],
                        line = dict(color='goldenrod')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Italia",
                        y=df["Italy"],
                        line = dict(color='red')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Portugal",
                        y=df["Portugal"],
                        line = dict(color='green')
                    )

    )
        
    return fige

#Life Expectancy in Asia
def lifexpa():
    figa=go.Figure()
    figa.update_layout(
            title={
                "text":"LifeExpectancy",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title =" ",
            yaxis_title = "Esperanza de años",
            xaxis_rangeslider_visible=False
        )
    figa.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="China",
                        y=df["China"],
                        line = dict(color='black')
                    )
            )
    figa.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Japón",
                        y=df["Japan"],
                        line = dict(color='skyblue')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Corea del sur",
                        y=df["South Korea"],
                        line = dict(color='goldenrod')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="India",
                        y=df["India"],
                        line = dict(color='red')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Tailandia",
                        y=df["Thailand"],
                        line = dict(color='green')
                    )

    )
        
    return figa

#Life Expectancy in Africa
def lifexpaf():
    fige=go.Figure()
    fige.update_layout(
            title={
                "text":"LifeExpectancy",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title =" ",
            yaxis_title = "Esperanza de años",
            xaxis_rangeslider_visible=False
        )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Egipto",
                        y=df["Egypt"],
                        line = dict(color='black')
                    )
            )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Argelia",
                        y=df["Algeria"],
                        line = dict(color='skyblue')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Alemania",
                        y=df["Germany"],
                        line = dict(color='goldenrod')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Nigeria",
                        y=df["Nigeria"],
                        line = dict(color='red')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Botsuana",
                        y=df["Botswana"],
                        line = dict(color='green')
                    )

    )
        
    return fige

#Life Expectancy in Oceanía
def lifexpo():
    fige=go.Figure()
    fige.update_layout(
            title={
                "text":"LifeExpectancy",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title =" ",
            yaxis_title = "Esperanza de años",
            xaxis_rangeslider_visible=False
        )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Nueva Zelanda",
                        y=df["New Zealand"],
                        line = dict(color='black')
                    )
            )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Australia",
                        y=df["Australia"],
                        line = dict(color='skyblue')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Fiji",
                        y=df["Fiji"],
                        line = dict(color='goldenrod')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Tonga",
                        y=df["Tonga"],
                        line = dict(color='red')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=df["Year"],
                        name="Islas Salomón",
                        y=df["Solomon Islands"],
                        line = dict(color='green')
                    )

    )
        
    return fige