import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import wbgapi as wb


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
                        name="Angola",
                        y=df["Angola"],
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




    ##DATASETS------------------------------------------------------------------------------------------------------------------
    ### Latin America & Caribeann
    ##BRA(Brazil)-MEX(Mexico)-COL(Colombia)-ARG(Argentina)-PER(Peru)-VEN(Venezuela)
    #Brazil
def BRA():
    BRA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"BRA",range(1990,2021,1))
    return BRA

    #Mexico
def MEX():
    MEX=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"MEX",range(1990,2021,1))
    return MEX

    #Colombia
def COL():
    COL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"COL",range(1990,2021,1))
    return COL

    #Argentina
def ARG():
    ARG=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"ARG",range(1990,2021,1))
    return ARG

    #Perú
def PER():
    PER=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"PER",range(1990,2021,1))
    return PER

    #Venezuela
def CHL():
    CHL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"CHL",range(1990,2021,1))
    return CHL



    ### Africa
    ##SYC(Seychelles)-DZA(Algeria)-MAR(Morocco)-TUN(Tunisia)-MUS(Mauritius)-CPV(Cabo Verde)

    #Seychelles
def SYC():
    SYC=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"SYC",range(1990,2021,1))
    return SYC


    #Algeria
def DZA():
    DZA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"DZA",range(1990,2021,1))
    return DZA


#Morocco
def MAR():
    MAR=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"MAR",range(1990,2021,1))
    return MAR


#Tunisia
def TUN():
    TUN=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"TUN",range(1990,2021,1))
    return TUN


#Mauritius
def MUS():
    MUS=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"MUS",range(1990,2021,1))
    return MUS


#Cabo Verde
def CPV():
    CPV=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"CPV",range(1990,2021,1))
    return CPV



    ### European Union
    ##MLT(Malta)-SWE(Suecia)-ITA(Italia)-ESP(España)-IRL-FRA(Francia)
    #Malta
def MLT():
    MLT=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"MLT",range(1990,2021,1))
    return MLT


    #Suecia
def SWE():
    SWE=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"SWE",range(1990,2021,1))
    return SWE


    #Italia
def ITA():
    ITA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    "SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"ITA",range(1990,2021,1))
    return ITA


    #España
def ESP():
    ESP=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5",
    
"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"ESP",range(1990,2021,1))
    return ESP


    #Irlanda
def IRL():
    IRL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"IRL",range(1990,2021,1))
    return IRL


    #Francia
def FRA():
    FRA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"FRA",range(1990,2021,1))
    return FRA



    ### South Asia
    ##IND(India)-PAK(Pakistan)-BGD(Bangladesh)-AFG(Afghanistan)-NLP(Nepal)-LKA(Sri Lanka)
    #Pakistán
def PAK():
    PAK=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"PAK",range(1990,2021,1))
    return PAK


    #Sri Lanka
def LKA():
    LKA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"LKA",range(1990,2021,1))
    return LKA


    #Bangladesh
def BGD():
    BGD=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"BGD",range(1990,2021,1))
    return BGD


    #Afghanistan
def AFG():
    AFG=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"BTN",range(1990,2021,1))
    return AFG


    #Nepal
def NPL():
    NPL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"NPL",range(1990,2021,1))
    return NPL


    #India
def IND():
    IND=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"IND",range(1990,2021,1))
    return IND



    ### World
    ## World CHN(China)-IND(India)-USA(United States)-IDN(Indonesia)-PAK(Pakistan)-BRA(Brasil)
    #USA
def USA():
    USA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"USA",range(1990,2021,1))
    return USA


    #Indonesia
def IDN():
    IDN=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
 
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.DYN.NCOM.ZS","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"
],"IDN",range(1990,2021,1))
    return IDN




    #Singapur
def SGP():
    SGP=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"],"SGP",range(1990,2021,1))
    return SGP





    #China
def CHN():
    CHN=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    
    
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    
    "SP.DYN.AMRT.FE",
    "SP.DYN.AMRT.MA",
    "SP.DYN.IMRT.IN",
    "SP.POP.GROW",
    "SP.POP.TOTL.FE.IN",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL",
    "SH.STA.SUIC.P5",
    "SH.STA.SUIC.FE.P5",
    "SH.STA.SUIC.MA.P5"
    
,"SH.XPD.CHEX.GD.ZS","SH.XPD.CHEX.PC.CD","SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD","NY.GDP.MKTP.KD","NY.GDP.MKTP.KN",
"SH.STA.TRAF.P5","SH.HTN.PREV.ZS","SH.STA.OWAD.ZS"
],"CHN",range(1990,2021,1))
    return CHN
    
    ##DATASETS------------------------------------------------------------------------------------------------------------------