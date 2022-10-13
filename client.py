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
                        x=GF.index,
                        name="Brazil",
                        y=GF["BRA"],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Argentina",
                        y=GF["ARG"],
                        line = dict(color='skyblue')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Colombia",
                        y=GF["COL"],
                        line = dict(color='green')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Peru",
                        y=GF["PER"],
                        line = dict(color='red')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Mexico",
                        y=GF["MEX"],
                        line = dict(color='blueviolet')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Chile",
                        y=GF["CHL"],
                        line = dict(color='black')
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
                        x=GF.index,
                        name="España",
                        y=GF["ESP"],
                        line = dict(color='black')
                    )
            )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Francia",
                        y=GF["FRA"],
                        line = dict(color='skyblue')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Alemania",
                        y=GF["DEU"],
                        line = dict(color='goldenrod')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Italia",
                        y=GF["ITA"],
                        line = dict(color='red')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Polonia",
                        y=GF["POL"],
                        line = dict(color='green')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Romania",
                        y=GF["ROU"],
                        line = dict(color='green')
                    )

    )
        
    return fige

#Life Expectancy in South Asia
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
                        x=GF.index,
                        name="Afghanistan",
                        y=GF["AFG"],
                        line = dict(color='black')
                    )
            )
    figa.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Bangladesh",
                        y=GF["BGD"],
                        line = dict(color='skyblue')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Nepal",
                        y=GF["NPL"],
                        line = dict(color='goldenrod')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="India",
                        y=GF["IND"],
                        line = dict(color='red')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Pakistan",
                        y=GF["PAK"],
                        line = dict(color='green')
                    )

    )
    figa.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Sri Lanka",
                        y=GF["LKA"],
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
                        x=GF.index,
                        name="Egipto",
                        y=GF["EGY"],
                        line = dict(color='black')
                    )
            )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Congo",
                        y=GF["COD"],
                        line = dict(color='skyblue')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Tanzania",
                        y=GF["TZA"],
                        line = dict(color='goldenrod')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Nigeria",
                        y=GF["NGA"],
                        line = dict(color='red')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Ethiopia",
                        y=GF["ETH"],
                        line = dict(color='green')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="South Africa",
                        y=GF["ZAF"],
                        line = dict(color='green')
                    )

    )
        
    return fige

#Life Expectancy in World
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
                        x=GF.index,
                        name="USA",
                        y=GF["USA"],
                        line = dict(color='black')
                    )
            )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="China",
                        y=GF["CHN"],
                        line = dict(color='skyblue')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Pakistan",
                        y=GF["PAK"],
                        line = dict(color='goldenrod')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="India",
                        y=GF["IND"],
                        line = dict(color='red')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Brazil",
                        y=GF["BRA"],
                        line = dict(color='green')
                    )

    )
    fige.add_trace(
                    go.Scatter(
                        x=GF.index,
                        name="Indonesia",
                        y=GF["IDN"],
                        line = dict(color='green')
                    )

    )
        
    return fige




    ##DATASETS------------------------------------------------------------------------------------------------------------------
    ### Latin America & Caribeann
    ##BRA(Brazil)-MEX(Mexico)-COL(Colombia)-ARG(Argentina)-PER(Peru)-VEN(Venezuela)
    #Brazil
def BRA():
    BRA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"BRA",range(1990,2021,1))
    return BRA

    #Mexico
def MEX():
    MEX=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"MEX",range(1990,2021,1))
    return MEX

    #Colombia
def COL():
    COL=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"COL",range(1990,2021,1))
    return COL

    #Argentina
def ARG():
    ARG=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"ARG",range(1990,2021,1))
    return ARG

    #Perú
def PER():
    PER=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"PER",range(1990,2021,1))
    return PER

    #Chile
def CHL():
    CHL=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"CHL",range(1990,2021,1))
    return CHL



    ### Africa
    ##NGA(Nigeria)-ETH(Ethiopia)-EGY(Egipto)-COD(Congo)-TZA(Tanzania)-ZAF(South Africa)

    #Nigeria
def NGA():
    NGA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"NGA",range(1990,2021,1))
    return NGA


    #Ethiopia
def ETH():
    ETH=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"ETH",range(1990,2021,1))
    return ETH


#Egipto
def EGY():
    EGY=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"EGY",range(1990,2021,1))
    return EGY


#Congo
def COD():
    COD=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"COD",range(1990,2021,1))
    return COD


#Tanzania
def TZA():
    TZA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"TZA",range(1990,2021,1))
    return TZA


#South Africa
def ZAF():
    ZAF=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"ZAF",range(1990,2021,1))
    return ZAF



    ### European Union
    ##MLT DEU(Germany)-FRA(Francia)-ITA(Italia)-ESP(España)-POL(Polonia)-ROU(Romania)
    #Germany
def DEU():
    DEU=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"DEU",range(1990,2021,1))
    return DEU


    #Romania
def ROU():
    ROU=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"ROU",range(1990,2021,1))
    return ROU


    #Italia
def ITA():
    ITA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"ITA",range(1990,2021,1))
    return ITA


    #España
def ESP():
    ESP=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"ESP",range(1990,2021,1))
    return ESP


    #Polonia
def POL():
    POL=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"POL",range(1990,2021,1))
    return POL


    #Francia
def FRA():
    FRA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"FRA",range(1990,2021,1))
    return FRA



    ### South Asia
    ##IND(India)-PAK(Pakistan)-BGD(Bangladesh)-AFG(Afghanistan)-NLP(Nepal)-LKA(Sri Lanka)
    #Pakistán
def PAK():
    PAK=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"PAK",range(1990,2021,1))
    return PAK


    #Sri Lanka
def LKA():
    LKA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"LKA",range(1990,2021,1))
    return LKA


    #Bangladesh
def BGD():
    BGD=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"BGD",range(1990,2021,1))
    return BGD


    #Afghanistan
def AFG():
    AFG=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"BTN",range(1990,2021,1))
    return AFG


    #Nepal
def NPL():
    NPL=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"NPL",range(1990,2021,1))
    return NPL


    #India
def IND():
    IND=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"IND",range(1990,2021,1))
    return IND



    ### World
    ## World CHN(China)-IND(India)-USA(United States)-IDN(Indonesia)-PAK(Pakistan)-BRA(Brasil)
    #USA
def USA():
    USA=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"USA",range(1990,2021,1))
    return USA


    #Indonesia
def IDN():
    IDN=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"
],"IDN",range(1990,2021,1))
    return IDN




    #Singapur
def SGP():
    SGP=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"],"SGP",range(1990,2021,1))
    return SGP





    #China
def CHN():
    CHN=wb.data.DataFrame(["SP.ADO.TFRT",
"SP.DYN.CBRT.IN",
"SH.XPD.CHEX.GD.ZS",
"SH.XPD.CHEX.PC.CD",
"SP.DYN.TFRT.IN",
"SP.DYN.LE00.IN",
"SP.DYN.IMRT.IN",
"SP.POP.GROW",
"SP.POP.TOTL",
"SH.STA.SUIC.P5",
"SP.DYN.CDRT.IN",
"NY.GDP.MKTP.KD",
"NY.GDP.MKTP.KN"
],"CHN",range(1990,2021,1))
    return CHN
    
    ##DATASETS------------------------------------------------------------------------------------------------------------------

    #Graph Expectativa de vida(WORLD)
GEVW=wb.data.DataFrame("SP.DYN.LE00.IN",wb.region.members('WLD'),range(1990,2020,1))
GW=GEVW.transpose()

GF=GW.rename(index={"YR1990":"1990","YR1991":"1991","YR1992":"1992","YR1993":"1993","YR1994":"1994","YR1995":"1995","YR1996":"1996","YR1997":"1997","YR1998":"1998","YR1999":"1999","YR2000":"2000","YR2001":"2001","YR2002":"2002","YR2003":"2003","YR2004":"2004","YR2005":"2005","YR2006":"2006","YR2007":"2007","YR2008":"2008","YR2009":"2009","YR2010":"2010","YR2011":"2011","YR2012":"2012","YR2013":"2013","YR2014":"2014","YR2015":"2015","YR2016":"2016","YR2017":"2017","YR2018":"2018","YR2019":"2019","YR2020":"2020","YR2021":"2021"})
GF.index=GF.index.map(int)