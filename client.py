import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import wbgapi as wb


#df=pd.read_csv("life_expectancy.csv")
fig=go.Figure()
#Adolescent fertility rate======================================================================================================
def Afr():
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
                        x=GAF.index,
                        name="Brazil",
                        y=GAF["BRA"],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=GAF.index,
                        name="Argentina",
                        y=GAF["ARG"],
                        line = dict(color='skyblue')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GAF.index,
                        name="Colombia",
                        y=GAF["COL"],
                        line = dict(color='green')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GAF.index,
                        name="Peru",
                        y=GAF["PER"],
                        line = dict(color='red')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GAF.index,
                        name="Mexico",
                        y=GAF["MEX"],
                        line = dict(color='blueviolet')
                    )

    )
    fig.add_trace(
                    go.Scatter(
                        x=GAF.index,
                        name="Chile",
                        y=GAF["CHL"],
                        line = dict(color='black')
                    )  
    )                  
    return fig


#Life Expectancy in America=====================================================================================================
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

    #Graph Adolescent fertility rate
GAFR=wb.data.DataFrame('SP.ADO.TFRT',wb.region.members('WLD'),range(1990,2020,1))
GA=GAFR.transpose()

GAF=GA.rename(index={"YR1990":"1990","YR1991":"1991","YR1992":"1992","YR1993":"1993","YR1994":"1994","YR1995":"1995","YR1996":"1996","YR1997":"1997","YR1998":"1998","YR1999":"1999","YR2000":"2000","YR2001":"2001","YR2002":"2002","YR2003":"2003","YR2004":"2004","YR2005":"2005","YR2006":"2006","YR2007":"2007","YR2008":"2008","YR2009":"2009","YR2010":"2010","YR2011":"2011","YR2012":"2012","YR2013":"2013","YR2014":"2014","YR2015":"2015","YR2016":"2016","YR2017":"2017","YR2018":"2018","YR2019":"2019","YR2020":"2020","YR2021":"2021"})
GAF.index=GAF.index.map(int)

    #Graph Birth rate, crude
GBR=wb.data.DataFrame('SP.DYN.CBRT.IN',wb.region.members('WLD'),range(1990,2020,1))
GB=GBR.transpose()

GBF=GB.rename(index={"YR1990":"1990","YR1991":"1991","YR1992":"1992","YR1993":"1993","YR1994":"1994","YR1995":"1995","YR1996":"1996","YR1997":"1997","YR1998":"1998","YR1999":"1999","YR2000":"2000","YR2001":"2001","YR2002":"2002","YR2003":"2003","YR2004":"2004","YR2005":"2005","YR2006":"2006","YR2007":"2007","YR2008":"2008","YR2009":"2009","YR2010":"2010","YR2011":"2011","YR2012":"2012","YR2013":"2013","YR2014":"2014","YR2015":"2015","YR2016":"2016","YR2017":"2017","YR2018":"2018","YR2019":"2019","YR2020":"2020","YR2021":"2021"})
GBF.index=GBF.index.map(int)

#DATASETS(FINALES)
CLA4=pd.read_csv("CLA4.csv")
AFR4=pd.read_csv("AFR4.csv")
EUU4=pd.read_csv("EUU4.csv")
SAS4=pd.read_csv("SAS4.csv")
WLD4=pd.read_csv("WLD4.csv")

#GRAPH FINAL
fig=go.Figure()
#Adolescent fertility rate===============================CLA======================================================================
def ClagZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Adolescent fertility rate",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,4],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,4],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,4],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,4],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,4],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,4],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.ADO.TFRT'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Adolescent fertility rate===============================AFR======================================================================
def AfrgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Adolescent fertility rate",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,4],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,4],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,4],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,4],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,4],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,4],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.ADO.TFRT'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Adolescent fertility rate===============================EUU======================================================================
def EUUgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Adolescent fertility rate",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,4],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,4],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,4],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,4],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,4],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,4],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.ADO.TFRT'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Adolescent fertility rate===============================SAS======================================================================
def SASgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Adolescent fertility rate",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,4],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,4],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,4],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,4],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,4],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,4],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.ADO.TFRT'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Adolescent fertility rate===============================WLD======================================================================
def WLDgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Adolescent fertility rate",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,4],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,4],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,4],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,4],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,4],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,4],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.ADO.TFRT'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Birth rate, crude (per 1000 people)===============================CLA======================================================================
def ClagbZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Birth rate, crude",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,7],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,7],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,7],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,7],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,7],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,7],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.DYN.CBRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Birth rate, crude (per 1000 people)===============================AFR======================================================================
def AfrbgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Birth rate, crude",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,7],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,7],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,7],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,7],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,7],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,7],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.DYN.CBRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Birth rate, crude (per 1000 people)===============================EUU======================================================================
def EUUbgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Birth rate, crude",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,7],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,7],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,7],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,7],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,7],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,7],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.DYN.CBRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Birth rate, crude (per 1000 people)===============================SAS======================================================================
def SASbgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Birth rate, crude",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,7],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,7],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,7],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,7],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,7],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,7],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.DYN.CBRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Birth rate, crude (per 1000 people)===============================WLD======================================================================
def WLDbgZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Birth rate, crude ",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,7],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,7],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,7],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,7],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,7],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,7],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.DYN.CBRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig

#Current health expenditure (% of GDP)===============================CLA======================================================================
def ClagchZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure (%) of GDP",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,3],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,3],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,3],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,3],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,3],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,3],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.DYN.CBRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure (% of GDP)===============================AFR======================================================================
def AfrchZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure (%) of GDP",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,3],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,3],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,3],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,3],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,3],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,3],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SH.XPD.CHEX.GD.ZS'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure (% of GDP)===============================EUU======================================================================
def EUUchZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure (%) of GDP",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,3],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,3],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,3],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,3],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,3],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,3],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SH.XPD.CHEX.GD.ZS'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure (% of GDP)===============================SAS======================================================================
def SASchZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure (%) of GDP",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,3],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,3],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,3],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,3],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,3],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,3],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SH.XPD.CHEX.GD.ZS'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure (% of GDP)===============================WLD======================================================================
def WLDchZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure (%) of GDP",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,3],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,3],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,3],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,3],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,3],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,3],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SH.XPD.CHEX.GD.ZS'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure per capita (current US$)===============================CLA======================================================================
def ClagchcZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure per capita (current US$)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,2],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,2],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,2],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,2],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,2],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,2],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SH.XPD.CHEX.PC.CD'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure per capita (current US$)===============================AFR======================================================================
def AfrchcZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure per capita (current US$)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,2],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,2],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,2],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,2],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,2],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,2],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SH.XPD.CHEX.PC.CD'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure per capita (current US$)===============================EUU======================================================================
def EUUchcZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure per capita (current US$)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,2],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,2],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,2],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,2],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,2],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,2],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SH.XPD.CHEX.PC.CD'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure per capita (current US$)===============================SAS======================================================================
def SASchcZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure per capita (current US$)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,2],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,2],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,2],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,2],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,2],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,2],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SH.XPD.CHEX.PC.CD'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Current health expenditure per capita (current US$)===============================WLD======================================================================
def WLDchcZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Current health expenditure per capita (current US$)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,2],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,2],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,2],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,2],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,2],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,2],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SH.XPD.CHEX.PC.CD'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Fertility rate, total (births per woman)===============================CLA======================================================================
def ClagfrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Fertility rate, total (births per woman)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,8],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,8],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,8],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,8],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,8],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,8],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.DYN.TFRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Fertility rate, total (births per woman)===============================AFR======================================================================
def AfrfrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Fertility rate, total (births per woman)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,8],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,8],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,8],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,8],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,8],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,8],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.DYN.TFRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Fertility rate, total (births per woman)===============================EUU======================================================================
def EUUfrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Fertility rate, total (births per woman)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,8],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,8],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,8],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,8],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,8],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,8],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.DYN.TFRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Fertility rate, total (births per woman)===============================SAS======================================================================
def SASfrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Fertility rate, total (births per woman)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,8],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,8],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,8],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,8],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,8],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,8],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.DYN.TFRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Fertility rate, total (births per woman)===============================WLD======================================================================
def WLDfrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Fertility rate, total (births per woman)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,8],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,8],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,8],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,8],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,8],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,8],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.DYN.TFRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig



#Life expectancy at birth, total (years)===============================CLA======================================================================
def ClagleZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Life expectancy at birth, total (years)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,9],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,9],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,9],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,9],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,9],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,9],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.DYN.LE00.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Life expectancy at birth, total (years)===============================AFR======================================================================
def Afrle():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Life expectancy at birth, total (years)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,9],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,9],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,9],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,9],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,9],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,9],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.DYN.LE00.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Life expectancy at birth, total (years)===============================EUU======================================================================
def EUUleZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Life expectancy at birth, total (years)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,9],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,9],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,9],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,9],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,9],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,9],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.DYN.LE00.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Life expectancy at birth, total (years)===============================SAS======================================================================
def SASleZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Life expectancy at birth, total (years)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,9],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,9],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,9],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,9],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,9],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,9],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.DYN.LE00.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Life expectancy at birth, total (years)===============================WLD======================================================================
def WLDleZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Life expectancy at birth, total (years)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,9],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,9],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,9],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,9],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,9],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,9],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.DYN.LE00.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig



#Mortality rate, infant (per 1,000 live births)===============================CLA======================================================================
def ClagmrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Mortality rate, infant (per 1,000 live births)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,10],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,10],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,10],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,10],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,10],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,10],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.DYN.IMRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Mortality rate, infant (per 1,000 live births)===============================AFR======================================================================
def AfrmrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Mortality rate, infant (per 1,000 live births)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,10],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,10],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,10],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,10],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,10],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,10],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.DYN.IMRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Mortality rate, infant (per 1,000 live births)===============================EUU======================================================================
def EUUmrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Mortality rate, infant (per 1,000 live births)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,10],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,10],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,10],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,10],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,10],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,10],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.DYN.IMRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Mortality rate, infant (per 1,000 live births)===============================SAS======================================================================
def SASmrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Mortality rate, infant (per 1,000 live births)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,10],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,10],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,10],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,10],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,10],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,10],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.DYN.IMRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Mortality rate, infant (per 1,000 live births)===============================WLD======================================================================
def WLDmrZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Mortality rate, infant (per 1,000 live births)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,10],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,10],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,10],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,10],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,10],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,10],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.DYN.IMRT.IN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig



#Population growth (annual %)===============================CLA======================================================================
def ClagpwZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population growth (annual %)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,5],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,5],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,5],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,5],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,5],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,5],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.POP.GROW'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population growth (annual %)===============================AFR======================================================================
def AfrpwZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population growth (annual %)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,5],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,5],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,5],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,5],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,5],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,5],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.POP.GROW'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population growth (annual %)===============================EUU======================================================================
def EUUpwZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population growth (annual %)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,5],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,5],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,5],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,5],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,5],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,5],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.POP.GROW'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population growth (annual %)===============================SAS======================================================================
def SASpwZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population growth (annual %)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,5],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,5],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,5],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,5],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,5],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,5],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.POP.GROW'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population growth (annual %)===============================WLD======================================================================
def WLDpwZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population growth (annual %)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,5],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,5],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,5],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,5],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,5],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,5],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.POP.GROW'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig



#Population, total===============================CLA======================================================================
def ClaptZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population, total",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,6],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,6],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,6],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,6],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,6],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,6],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SP.POP.TOTL'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population, total===============================AFR======================================================================
def AfrptZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population, total",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,6],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,6],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,6],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,6],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,6],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,6],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SP.POP.TOTL'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population, total===============================EUU======================================================================
def EUUptZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population, total",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,6],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,6],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,6],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,6],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,6],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,6],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SP.POP.TOTL'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population, total===============================SAS======================================================================
def SASptZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population, total",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,6],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,6],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,6],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,6],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,6],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,6],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SP.POP.TOTL'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Population, total===============================WLD======================================================================
def WLDptZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Population, total",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,6],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,6],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,6],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,6],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,6],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,6],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SP.POP.TOTL'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig



#Suicide mortality rate (per 100,000 population)===============================CLA======================================================================
def ClasmZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Suicide mortality rate (per 100,000 population)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,11],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,11],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,11],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,11],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,11],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,11],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['SH.STA.SUIC.P5'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Suicide mortality rate (per 100,000 population)===============================AFR======================================================================
def AfrsmZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Suicide mortality rate (per 100,000 population)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,11],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,11],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,11],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,11],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,11],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,11],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['SH.STA.SUIC.P5'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Suicide mortality rate (per 100,000 population)===============================EUU======================================================================
def EUUsmZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Suicide mortality rate (per 100,000 population)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,11],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,11],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,11],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,11],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,11],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,11],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['SH.STA.SUIC.P5'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Suicide mortality rate (per 100,000 population)===============================SAS======================================================================
def SASsmZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Suicide mortality rate (per 100,000 population)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,11],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,11],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,11],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,11],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,11],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,11],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['SH.STA.SUIC.P5'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#Suicide mortality rate (per 100,000 population)===============================WLD======================================================================
def WLDsmZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"Suicide mortality rate (per 100,000 population)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,11],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,11],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,11],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,11],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,11],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,11],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['SH.STA.SUIC.P5'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig



#GDP(constant LCU)===============================CLA======================================================================
def ClagdpZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"GDP(constant LCU)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="BRA"].date,
                        name="Brazil",
                        y=CLA4[CLA4["countryiso3code"]=="BRA"].iloc[:,13],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="ARG"].date,
                        name="Argentina",
                        y=CLA4[CLA4["countryiso3code"]=="ARG"].iloc[:,13],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="PER"].date,
                        name="Perú",
                        y=CLA4[CLA4["countryiso3code"]=="PER"].iloc[:,13],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="MEX"].date,
                        name="Mexico",
                        y=CLA4[CLA4["countryiso3code"]=="MEX"].iloc[:,13],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="COL"].date,
                        name="Colombia",
                        y=CLA4[CLA4["countryiso3code"]=="COL"].iloc[:,13],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=CLA4[CLA4["countryiso3code"]=="CHL"].date,
                        name="Chile",
                        y=CLA4[CLA4["countryiso3code"]=="CHL"].iloc[:,13],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=CLA4['date'],
                        y=CLA4['NY.GDP.MKTP.KN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#GDP(constant LCU)===============================AFR======================================================================
def AFRgdpZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"GDP(constant LCU)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="NER"].date,
                        name="Nigeria",
                        y=AFR4[AFR4["countryiso3code"]=="NER"].iloc[:,13],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ETH"].date,
                        name="Ethiopia",
                        y=AFR4[AFR4["countryiso3code"]=="ETH"].iloc[:,13],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="EGY"].date,
                        name="Egipto",
                        y=AFR4[AFR4["countryiso3code"]=="EGY"].iloc[:,13],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="COD"].date,
                        name="Congo",
                        y=AFR4[AFR4["countryiso3code"]=="COD"].iloc[:,13],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="TZA"].date,
                        name="Tanzania",
                        y=AFR4[AFR4["countryiso3code"]=="TZA"].iloc[:,13],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=AFR4[AFR4["countryiso3code"]=="ZAF"].date,
                        name="South Africa",
                        y=AFR4[AFR4["countryiso3code"]=="ZAF"].iloc[:,13],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=AFR4['date'],
                        y=AFR4['NY.GDP.MKTP.KN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#GDP(constant LCU)===============================EUU======================================================================
def EUUgdpZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"GDP(constant LCU)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="DEU"].date,
                        name="Germany",
                        y=EUU4[EUU4["countryiso3code"]=="DEU"].iloc[:,13],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="FRA"].date,
                        name="Francia",
                        y=EUU4[EUU4["countryiso3code"]=="FRA"].iloc[:,13],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ITA"].date,
                        name="Italia",
                        y=EUU4[EUU4["countryiso3code"]=="ITA"].iloc[:,13],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ESP"].date,
                        name="España",
                        y=EUU4[EUU4["countryiso3code"]=="ESP"].iloc[:,13],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="POL"].date,
                        name="Polonia",
                        y=EUU4[EUU4["countryiso3code"]=="POL"].iloc[:,13],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=EUU4[EUU4["countryiso3code"]=="ROU"].date,
                        name="Romania",
                        y=EUU4[EUU4["countryiso3code"]=="ROU"].iloc[:,13],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=EUU4['date'],
                        y=EUU4['NY.GDP.MKTP.KN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#GDP(constant LCU)===============================SAS======================================================================
def SASgdpZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"GDP(constant LCU)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="IND"].date,
                        name="India",
                        y=SAS4[SAS4["countryiso3code"]=="IND"].iloc[:,13],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="PAK"].date,
                        name="Pakistan",
                        y=SAS4[SAS4["countryiso3code"]=="PAK"].iloc[:,13],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="BGD"].date,
                        name="Bangladesh",
                        y=SAS4[SAS4["countryiso3code"]=="BGD"].iloc[:,13],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="AFG"].date,
                        name="Afghanistan",
                        y=SAS4[SAS4["countryiso3code"]=="AFG"].iloc[:,13],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="NPL"].date,
                        name="Nepal",
                        y=SAS4[SAS4["countryiso3code"]=="NPL"].iloc[:,13],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=SAS4[SAS4["countryiso3code"]=="LKA"].date,
                        name="Sri Lanka",
                        y=SAS4[SAS4["countryiso3code"]=="LKA"].iloc[:,13],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=SAS4['date'],
                        y=SAS4['NY.GDP.MKTP.KN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig


#GDP(constant LCU)===============================WLD======================================================================
def WLDgdpZ():
    fig=go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.13, subplot_titles=('', ''), 
               row_width=[0.2, 0.7])
    fig.update_layout(
            title={
                "text":"GDP(constant LCU)",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Volumen",
            yaxis_title = "quantity",
            xaxis_rangeslider_visible=False
        )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="CHN"].date,
                        name="China",
                        y=WLD4[WLD4["countryiso3code"]=="CHN"].iloc[:,13],
                        line = dict(color="gold")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="AUS"].date,
                        name="Australia",
                        y=WLD4[WLD4["countryiso3code"]=="AUS"].iloc[:,13],
                        line = dict(color="skyblue")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="USA"].date,
                        name="United States",
                        y=WLD4[WLD4["countryiso3code"]=="USA"].iloc[:,13],
                        line = dict(color="red")
                    )
            )
    
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="IDN"].date,
                        name="Indonesia",
                        y=WLD4[WLD4["countryiso3code"]=="IDN"].iloc[:,13],
                        line = dict(color="brown")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="GBR"].date,
                        name="Gran Bretaña",
                        y=WLD4[WLD4["countryiso3code"]=="GBR"].iloc[:,13],
                        line = dict(color="black")
                    )
            )
    fig.add_trace(
                    go.Scatter(
                        x=WLD4[WLD4["countryiso3code"]=="RUS"].date,
                        name="Rusia",
                        y=WLD4[WLD4["countryiso3code"]=="RUS"].iloc[:,13],
                        line = dict(color="green")
                    )
    
            )
    
    fig.add_trace(
                        go.Bar(
                        x=WLD4['date'],
                        y=WLD4['NY.GDP.MKTP.KN'],
                        name="Volumen",
                        showlegend=False),
                        row=2, col=1
    
)
                    
    return fig