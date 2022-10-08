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
    ##BMU(Bermuda)-CRI(Costa Rica)-CHL(Chile)-PRI(Puerto Rico)-VIR(Virgins Islands)-BRB(Barbados)
    #Bermudas
def BMU():
    BMU=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"BMU",range(1990,2021,1))
    return BMU

    #Costa Rica
def CRI():
    CRI=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"CRI",range(1990,2021,1))
    return CRI

    #Chile
def CHL():
    CHL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"CHL",range(1990,2021,1))
    return CHL

    #Puerto Rico
def PIR():
    PIR=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"PRI",range(1990,2021,1))
    return PIR

    #Virgin Islands
def VIR():
    VIR=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"VIR",range(1990,2021,1))
    return VIR

    #Barbados
def BRB1():
    BRB1=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"BRB",range(1990,2021,1))
    return BRB1



    ### Africa
    ##SYC(Seychelles)-DZA(Algeria)-MAR(Morocco)-TUN(Tunisia)-MUS(Mauritius)-CPV(Cabo Verde)

    #Seychelles
def SYC():
    SYC=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"SYC",range(1990,2021,1))
    return SYC


    #Algeria
def DZA():
    DZA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"DZA",range(1990,2021,1))
    return DZA


#Morocco
def MAR():
    MAR=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"MAR",range(1990,2021,1))
    return MAR


#Tunisia
def TUN():
    TUN=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"TUN",range(1990,2021,1))
    return TUN


#Mauritius
def MUS():
    MUS=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"MUS",range(1990,2021,1))
    return MUS


#Cabo Verde
def CPV():
    CPV=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"CPV",range(1990,2021,1))
    return CPV



    ### European Union
    ##MLT(Malta)-SWE(Suecia)-ITA(Italia)-ESP(España)-IRL-FRA(Francia)
    #Malta
def MLT():
    MLT=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"MLT",range(1990,2021,1))
    return MLT


    #Suecia
def SWE():
    SWE=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"SWE",range(1990,2021,1))
    return SWE


    #Italia
def ITA():
    ITA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"ITA",range(1990,2021,1))
    return ITA


    #España
def ESP():
    ESP=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"ESP",range(1990,2021,1))
    return ESP


    #Irlanda
def IRL():
    IRL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"IRL",range(1990,2021,1))
    return IRL


    #Francia
def FRA():
    FRA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"FRA",range(1990,2021,1))
    return FRA



    ### South Asia
    ##MDV(Maldives)-LKA(Sri Lanka)-BGD(Bangladesh)-BTN(Bhutan)-NLP(Nepal)-IND(India)
    #Maldives
def MDV():
    MDV=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"MDV",range(1990,2021,1))
    return MDV


    #Sri Lanka
def LKA():
    LKA=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"LKA",range(1990,2021,1))
    return LKA


    #Bangladesh
def BGD():
    BGD=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"BGD",range(1990,2021,1))
    return BGD


    #Bhutan
def BTN():
    BTN=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"BTN",range(1990,2021,1))
    return BTN


    #Nepal
def NPL():
    NPL=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"NPL",range(1990,2021,1))
    return NPL


    #India
def IND():
    IND=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"IND",range(1990,2021,1))
    return IND



    ### World
    ## HKG(Hong Kong SAR, China)-JPN(Japon)-MAC(Macao SAR, China)-SGP(Singapur)-KOR(Korea)-CHI(China)
    #Hong Kong(china)
def HKG():
    HKG=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"HKG",range(1990,2021,1))
    return HKG


    #Japon
def JPN():
    JPN=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"JPN",range(1990,2021,1))
    return JPN


    #Macao SAR(China)
def MAC():
    MAC=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"MAC",range(1990,2021,1))
    return MAC


    #Singapur
def SGP():
    SGP=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"SGP",range(1990,2021,1))
    return SGP


    #Korea
def KOR():
    KOR=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"KOR",range(1990,2021,1))
    return KOR


    #China
def CHI():
    CHI=wb.data.DataFrame(['SP.ADO.TFRT',
    'SP.DYN.CBRT.IN',
    'SH.STA.BRTC.ZS',
    'SH.DTH.COMM.ZS',
    'SH.XPD.CHEX.GD.ZS',
    "SH.XPD.CHEX.PC.CD",
    "SP.DYN.CDRT.IN",
    "SP.DYN.TFRT.IN",
    "SP.DYN.LE00.FE.IN",
    "SP.DYN.LE00.MA.IN",
    "SP.DYN.LE00.IN",
    "SH.STA.BRTW.ZS",
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
    "SP.DYN.WFRT"],"CHI",range(1990,2021,1))
    return CHI
    
    ##DATASETS------------------------------------------------------------------------------------------------------------------