from unittest import result
from matplotlib.backend_bases import key_press_handler
import streamlit as st
import wbgapi as wb
import numpy as np
from Api import *
from secrets import choice
import pandas as pd
import pickle
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from client import DEU, EGY, ETH, NGA, ROU, TZA, ZAF, lifexp,lifexpe,lifexpa,lifexpaf,lifexpo
from client import BRA,COL,MEX,PER,CHL,ARG
from client import ETH,ZAF,COD,TZA,EGY,NGA
from client import POL,DEU,ESP,ITA,ROU,FRA
from client import LKA,BGD,NPL,IND
from client import CHN,USA,PAK,IDN,AFG
#API IMPORT -------------------------------------------------------------------------------------------------------------------
## Adolescent fertility rate (births per 1,000 women ages 15-19)
from Api import AfrAFR,AfrCLA,AfrEUU,AfrSAS,AfrWLD
## Birth rate, crude (per 1000 people)
#from Api import BrcAFR,BrcCLA,BrcEUU,BrcSAS,BrcWLD
## Births attended by skilled health staff (% of total)
from Api import BashAFR,BashCLA,BashEUU,BashSAS,BashWLD
## Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total)
from Api import CodpnAFR,CodpnCLA,CodpnEUU,CodpnSAS,CodpnWLD
## Current health expenditure (% of GDP)
from Api import CuheAFR,CuheCLA,CuheEUU,CuheSAS,CuheWLD
## Current health expenditure per capita (current US$)
from Api import CuhepcAFR,CuhepcCLA,CuhepcEUU,CuhepcSAS,CuhepcWLD
## Death rate, crude (per 1,000 people)
from Api import DrcmAFR,DrcmCLA,DrcmWLD,DrcmEUU,DrcmSAS
## Fertility rate, total (births per woman)
from Api import FrtbAFR,FrtbCLA,FrtbEUU,FrtbSAS,FrtbWLD
## Life expectancy at birth, female (years)
from Api import LebfCLA,LebfAFR,LebfEUU,LebfSAS,LebfWLD
## Life expectancy at birth, male (years)
from Api import LebmAFR,LebmCLA,LebmEUU,LebmSAS,LebmWLD
## Life expectancy at birth, total (years)
from Api import LebCLA,LebAFR,LebEUU,LebSAS,LebWLD
## Low-birthweight babies (% of births)
from Api import LbbAFR,LbbCLA,LbbEUU,LbbSAS,LbbWLD
## Mortality rate, adult, female (per 1,000 female adults)
from Api import MrafAFR,MrafCLA,MrafEUU,MrafSAS,MrafWLD
## Mortality rate, adult, male (per 1,000 male adults)
from Api import MramAFR,MramCLA,MramEUU,MramSAS,MramWLD
## Mortality rate, infant (per 1,000 live births)
from Api import MriAFR,MriCLA,MriEUU,MriSAS,MriWLD
## Population growth (annual %)
from Api import PgaAFR,PgaCLA,PgaEUU,PgaSAS,PgaWLD
## Population, female
from Api import PfAFR,PfCLA,PfEUU,PfSAS,PfWLD
# Population, male
from Api import PmAFR,PmCLA,PmEUU,PmSAS,PmWLD
## Population, total
from Api import PtAFR,PtCLA,PtEUU,PtSAS,PtWLD
## Suicide mortality rate (per 100,000 population)
from Api import SmrEUU,SmrAFR,SmrCLA,SmrSAS,SmrWLD
## Suicide mortality rate, female (per 100,000 female population)
from Api import SmrfAFR,SmrfCLA,SmrfEUU,SmrfSAS,SmrfWLD
## Suicide mortality rate, male (per 100,000 male population)
from Api import SmrmAFR,SmrmCLA,SmrmEUU,SmrmSAS,SmrmWLD
## Wanted fertility rate (births per woman)
from Api import WfrAFR,WfrCLA,WfrEUU,WfrSAS,WfrWLD
#API IMPORT -------------------------------------------------------------------------------------------------------------------
def main():
    techo=["Off","model"]
    choice = st.sidebar.selectbox("Prediction",techo)
    if choice == "Off":
      st.title("")
    
    ##-------------------------------------------------------------------------------------------------------------------------
      # Path del modelo preentrenado
    MODEL_PATH = 'pickle_model.pkl'
    
            
    def model_prediction(x_in, model):

               x = np.asarray(x_in).reshape(1,-1)
               preds=model.predict(x)

               return preds
    
    if choice == "model":
        st.title("Life Expentancy Predict")
        # Se carga el modelo
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    

      # Lecctura de datos
      #Datos = st.text_input
        A = st.text_input("GDP (constant 2015 US$):")
        B = st.text_input("GDP (constant LCU):")
        C = st.text_input("Suicide mortality rate (per 100,000 population):")
        D = st.text_input("Current health expenditure (%) of GDP:")
        E = st.text_input("Current health expenditure per capita (current US$)")
        F = st.text_input("Adolescent fertility rate :")
        G = st.text_input("Birth rate, crude (per 1000 people):")
        H = st.text_input("Mortality rate, infant (per 1,000 live births):")
        I = st.text_input("Fertility rate, total :")
        J = st.text_input("Population growth (annual %):")
        K = st.text_input("Population, total")
       
    
      
      # El botón predicción se usa para iniciar el procesamiento
        if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
            x_in =[np.float_(A.title()),
                    np.float_(B.title()),
                    np.float_(C.title()),
                    np.float_(D.title()),
                    np.float_(E.title()),
                    np.float_(F.title()),
                    np.float_(G.title()),
                    np.float_(H.title()),
                    np.float_(I.title()),
                    np.float_(J.title()),
                    np.float_(K.title()),]
                    
            predictS = model_prediction(x_in, model)
            st.success('La Esperanza de vida es: {}'.format(predictS[0]).upper())
        
 
    ##-------------------------------------------------------------------------------------------------------------------------

    casa=["Off","Series"]
    choice = st.sidebar.selectbox("Stats Explorer",casa)
    if choice == "Off":
      st.title(" ")
    if choice == "Series":
         st.title("Series Stats Explorer")
         st.markdown('''
         Esta aplicación realiza una exploracion simple de datos estadísticos que tienen impacto en la  esperanza de vida !
         * **Python libraries:** pandas, streamlit, wbgapi 
         * **Data source:** https://www.worldbank.org/en/home''')
         st.subheader("Datasets")
         #----------------------------------------------------------------------------------------------------------------------
         with st.form(key="searchform2"):
                nav1,nav2,nav3 = st.columns([3,2,1])
                Rgnes=["Latin America & Caribeann","Africa","European Union","South Asia","World"]

                Paises=[]
         with nav1:
                    search_term2 =st.selectbox("Select Region :",Rgnes)
                    if search_term2 =="Latin America & Caribeann":
                        Paises=["Brazil","Mexico","Colombia","Argentina","Perú","Chile"]
                    if search_term2 =="Africa":
                        Paises=["Congo","Nigeria","Ethiopia","Egipto","Tanzania","South Africa"]
                    if search_term2 =="European Union":
                        Paises=["Polonia","Alemania","Italia","España","Romania","Francia"]
                    if search_term2 =="South Asia":
                        Paises=["Pakistán","Sri Lanka","Bangladesh","Afghanistan","Nepal","India"]
                    if search_term2 =="World":
                        Paises=["United States","Pakistán","Indonesia","India","China","Brazil"]
                     
            
         with nav2:
                        Rg = st.selectbox("Paises :",Paises)
                           
         with nav3:
                        submit_search = st.form_submit_button()
         with nav1:
                     def result():
                        #Latin America & Caribeann
                        if Rg=="Brazil":
                           return BRA()
                        if Rg== "Mexico":
                           return MEX()
                        if Rg== "Colombia":
                           return COL()
                        if Rg== "Argentina":
                           return ARG()
                        if Rg== "Perú":
                           return PER()
                        if Rg== "Chile":
                           return CHL()
                        #Africa
                        if Rg =="Congo":
                           return COD()
                        if Rg =="Nigeria":
                           return NGA()
                        if Rg =="South Africa":
                           return ZAF()
                        if Rg =="Ethiopia":
                           return ETH()
                        if Rg =="Tanzania":
                           return TZA()
                        if Rg =="Egipto":
                           return EGY() 
                        #European Union
                        if Rg =="Polonia":
                           return POL()
                        if Rg =="Romania":
                           return ROU()
                        if Rg =="Italia":
                           return ITA()
                        if Rg =="España":
                           return ESP()
                        if Rg =="Alemania":
                           return DEU()
                        if Rg =="Francia":
                           return FRA()
                        #South Asia
                        #if Rg =="Pakistán":
                           #return MDV()
                        if Rg =="Sri Lanka":
                           return LKA()
                        if Rg =="Bangladesh":
                           return BGD()
                        if Rg =="Afghanistan":
                           return AFG()
                        if Rg =="Nepal":
                           return NPL()
                        if Rg =="India":
                           return IND()
                        #World
                        if Rg =="United States":
                           return USA()
                        #if Rg =="Japon":
                           #return JPN()
                        if Rg =="Pakistán":
                           return PAK()
                        if Rg =="Indonesia":
                           return IDN()
                        #if Rg =="Korea":
                         #  return KOR()
                        if Rg =="China":
                           return CHN()

         st.write(result())   

         
         #----------------------------------------------------------------------------------------------------------------------
    menu = ["Off","Life Expectancy-Regions","Info","Datasets"]
    choice = st.sidebar.selectbox("Proyeccion + Datasets (Semana 1)",menu)
    
    if choice == "Off":
      st.title(" ")
    if choice == "Life Expectancy-Regions":
            st.title("Life Expectancy")
            st.subheader("Regiones")
            if st.checkbox("Latin America & Caribeann"):
                st.write(lifexp())
            if st.checkbox("European Union"):
                st.write(lifexpe())
            if st.checkbox("South Asia"):
                st.write(lifexpa())
            if st.checkbox("Africa"):
                st.write(lifexpaf())
            if st.checkbox("World"):
                st.write(lifexpo())
    
        
            
    if choice == "Info":

            st.subheader("Info")
            if st.checkbox("Regions"):
                st.write(wb.region.info())
            if st.checkbox("Countries"):
                st.write(wb.economy.info())
            
            if st.checkbox("Series"):
                st.write(wb.series.info())

    if choice == "Datasets":

            st.subheader("Datasets")
            # Nav Search Form
            with st.form(key="searchform"):
                nav1,nav2,nav3 = st.columns([3,2,1])
                Series=["Adolescent fertility rate (ages 15-19)"
                        ,"Birth rate, crude (per 1000 people)",
                        "Current health expenditure (%) of GDP",
                        "Current health expenditure per capita (current US$)",
                        "Fertility rate, total (births per woman)",
                        "Life expectancy at birth, total (years)",
                        "Mortality rate, infant (per 1,000 live births)",
                        "Population growth (annual %)",
                        "Population, total",
                        "Suicide mortality rate (per 100,000 population)",
                        "(constant 2015 US$)",
                        "GDP(constant LCU)"]
                Regiones=["World(WLD)","Latin America and the Caribbean(CLA)",
                            "Africa(AFR)","European Union(EUU)","South Asia(SAS)"]
                with nav1:
                    search_term =st.selectbox("Select Serie :",Series)
                    #Adolescent fertility rate (ages 15-19)
                    def result():
                        
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regions == "World(WLD)":
                           return AfrWLD() 
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regions == "Latin America and the Caribbean(CLA)":
                           return AfrCLA()
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regions == "Africa(AFR)":
                           return AfrAFR()
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regions == "European Union(EUU)":
                           return AfrEUU()
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regions == "South Asia(SAS)":
                           return AfrSAS()
                    #Birth rate, crude (per 1000 people)
                   
                        if search_term =="Birth rate, crude (per 1000 people)" and Regions == "World(WLD)":
                           return BrcWLD() 
                        if search_term =="Birth rate, crude (per 1000 people)" and Regions == "Latin America and the Caribbean(CLA)":
                           return BrcCLA()
                        if search_term =="Birth rate, crude (per 1000 people)" and Regions == "Africa(AFR)":
                           return BrcAFR()
                        if search_term =="Birth rate, crude (per 1000 people)" and Regions == "European Union(EUU)":
                           return BrcEUU()
                        if search_term =="Birth rate, crude (per 1000 people)" and Regions == "South Asia(SAS)":
                           return BrcSAS()

                    #Births attended by skilled health staff (%)
                   
                        if search_term =="Births attended by skilled health staff (%)" and Regions == "World(WLD)":
                           return BashWLD() 
                        if search_term =="Births attended by skilled health staff (%)" and Regions == "Latin America and the Caribbean(CLA)":
                           return BashCLA()
                        if search_term =="Births attended by skilled health staff (%)" and Regions == "Africa(AFR)":
                           return BashAFR()
                        if search_term =="Births attended by skilled health staff (%)" and Regions == "European Union(EUU)":
                           return BashEUU()
                        if search_term =="Births attended by skilled health staff (%)" and Regions == "South Asia(SAS)":
                           return BashSAS()

                    #Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total
                   
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regions == "World(WLD)":
                           return CodpnWLD() 
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regions == "Latin America and the Caribbean(CLA)":
                           return CodpnCLA()
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regions == "Africa(AFR)":
                           return CodpnAFR()
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regions == "European Union(EUU)":
                           return CodpnEUU()
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regions == "South Asia(SAS)":
                           return CodpnSAS()
                    
                    
                    #Current health expenditure (%) of GDP
                   
                        if search_term =="Current health expenditure (%) of GDP" and Regions == "World(WLD)":
                           return CuheWLD() 
                        if search_term =="Current health expenditure (%) of GDP" and Regions == "Latin America and the Caribbean(CLA)":
                           return CuheCLA()
                        if search_term =="Current health expenditure (%) of GDP" and Regions == "Africa(AFR)":
                           return CuheAFR()
                        if search_term =="Current health expenditure (%) of GDP" and Regions == "European Union(EUU)":
                           return CuheEUU()
                        if search_term =="Current health expenditure (%) of GDP" and Regions == "South Asia(SAS)":
                           return CuheSAS()
                    
                    #Current health expenditure per capita (current US$)
                   
                        if search_term =="Current health expenditure per capita (current US$)" and Regions == "World(WLD)":
                           return CuhepcWLD() 
                        if search_term =="Current health expenditure per capita (current US$)" and Regions == "Latin America and the Caribbean(CLA)":
                           return CuhepcCLA()
                        if search_term =="Current health expenditure per capita (current US$)" and Regions == "Africa(AFR)":
                           return CuhepcAFR()
                        if search_term =="Current health expenditure per capita (current US$)" and Regions == "European Union(EUU)":
                           return CuhepcEUU()
                        if search_term =="Current health expenditure (%) of GDP" and Regions == "South Asia(SAS)":
                           return CuhepcSAS()

                    #Death rate, crude (per 1,000 people)
                   
                        if search_term =="Death rate, crude (per 1,000 people)" and Regions == "World(WLD)":
                           return DrcmWLD() 
                        if search_term =="Death rate, crude (per 1,000 people)" and Regions == "Latin America and the Caribbean(CLA)":
                           return DrcmCLA()
                        if search_term =="Death rate, crude (per 1,000 people)" and Regions == "Africa(AFR)":
                           return DrcmAFR()
                        if search_term =="Death rate, crude (per 1,000 people)" and Regions == "European Union(EUU)":
                           return DrcmEUU()
                        if search_term =="Death rate, crude (per 1,000 people)" and Regions == "South Asia(SAS)":
                           return DrcmSAS()

                    #Fertility rate, total (births per woman)
                   
                        if search_term =="Fertility rate, total (births per woman)" and Regions == "World(WLD)":
                           return FrtbWLD() 
                        if search_term =="Fertility rate, total (births per woman)" and Regions == "Latin America and the Caribbean(CLA)":
                           return FrtbCLA()
                        if search_term =="Fertility rate, total (births per woman)" and Regions == "Africa(AFR)":
                           return FrtbAFR()
                        if search_term =="Fertility rate, total (births per woman)" and Regions == "European Union(EUU)":
                           return FrtbEUU()
                        if search_term =="Fertility rate, total (births per woman)" and Regions == "South Asia(SAS)":
                           return FrtbSAS()

                    #Life expectancy at birth, female (years)
                   
                        if search_term =="Life expectancy at birth, female (years)" and Regions == "World(WLD)":
                           return LebfWLD() 
                        if search_term =="Life expectancy at birth, female (years)" and Regions == "Latin America and the Caribbean(CLA)":
                           return LebfCLA()
                        if search_term =="Life expectancy at birth, female (years)" and Regions == "Africa(AFR)":
                           return LebfAFR()
                        if search_term =="Life expectancy at birth, female (years)" and Regions == "European Union(EUU)":
                           return LebfEUU()
                        if search_term =="FLife expectancy at birth, female (years)" and Regions == "South Asia(SAS)":
                           return LebfSAS()

                    #Life expectancy at birth, male (years)
                   
                        if search_term =="Life expectancy at birth, male (years)" and Regions == "World(WLD)":
                           return LebmWLD() 
                        if search_term =="Life expectancy at birth, male (years)" and Regions == "Latin America and the Caribbean(CLA)":
                           return LebmCLA()
                        if search_term =="Life expectancy at birth, male (years)" and Regions == "Africa(AFR)":
                           return LebmAFR()
                        if search_term =="Life expectancy at birth, male (years)" and Regions == "European Union(EUU)":
                           return LebmEUU()
                        if search_term =="Life expectancy at birth, male (years)" and Regions == "South Asia(SAS)":
                           return LebmSAS()

                    #Life expectancy at birth, total (years)
                   
                        if search_term =="Life expectancy at birth, total (years)" and Regions == "World(WLD)":
                           return LebWLD()
                        if search_term =="Life expectancy at birth, total (years)" and Regions == "Latin America and the Caribbean(CLA)":
                           return LebCLA()
                        if search_term =="Life expectancy at birth, total (years)" and Regions == "Africa(AFR)":
                           return LebAFR()
                        if search_term =="Life expectancy at birth, total (years)" and Regions == "European Union(EUU)":
                           return LebEUU()
                        if search_term =="Life expectancy at birth, total (years)" and Regions == "South Asia(SAS)":
                           return LebSAS()

                    #Low-birthweight babies (%) of births
                   
                        if search_term =="Low-birthweight babies (%) of births" and Regions == "World(WLD)":
                           return LbbWLD() 
                        if search_term =="Low-birthweight babies (%) of births" and Regions == "Latin America and the Caribbean(CLA)":
                           return LbbCLA()
                        if search_term =="Low-birthweight babies (%) of births" and Regions == "Africa(AFR)":
                           return LbbAFR()
                        if search_term =="Low-birthweight babies (%) of births" and Regions == "European Union(EUU)":
                           return LbbEUU()
                        if search_term =="Low-birthweight babies (%) of births" and Regions == "South Asia(SAS)":
                           return LbbSAS()

                    #Mortality rate, adult, female (per 1,000 female adults)
                   
                        if search_term =="Mortality rate, adult, female (per 1,000 female adults)" and Regions == "World(WLD)":
                           return MrafWLD() 
                        if search_term =="Mortality rate, adult, female (per 1,000 female adults)" and Regions == "Latin America and the Caribbean(CLA)":
                           return MrafCLA()
                        if search_term =="Mortality rate, adult, female (per 1,000 female adults)" and Regions == "Africa(AFR)":
                           return MrafAFR()
                        if search_term =="Mortality rate, adult, female (per 1,000 female adults)" and Regions == "European Union(EUU)":
                           return MrafEUU()
                        if search_term =="Mortality rate, adult, female (per 1,000 female adults)" and Regions == "South Asia(SAS)":
                           return MrafSAS()

                    #Mortality rate, adult, male (per 1,000 male adults)
                   
                        if search_term =="Mortality rate, adult, male (per 1,000 male adults)" and Regions == "World(WLD)":
                           return MramWLD() 
                        if search_term =="Mortality rate, adult, male (per 1,000 male adults)" and Regions == "Latin America and the Caribbean(CLA)":
                           return MramCLA()
                        if search_term =="Mortality rate, adult, male (per 1,000 male adults)" and Regions == "Africa(AFR)":
                           return MramAFR()
                        if search_term =="Mortality rate, adult, male (per 1,000 male adults)" and Regions == "European Union(EUU)":
                           return MramEUU()
                        if search_term =="Mortality rate, adult, male (per 1,000 male adults)" and Regions == "South Asia(SAS)":
                           return MramSAS()

                    #Mortality rate, infant (per 1,000 live births)
                   
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regions == "World(WLD)":
                           return MriWLD() 
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regions == "Latin America and the Caribbean(CLA)":
                           return MriCLA()
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regions == "Africa(AFR)":
                           return MriAFR()
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regions == "European Union(EUU)":
                           return MriEUU()
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regions == "South Asia(SAS)":
                           return MriSAS()
                    

                    #Population growth (annual %)
                   
                        if search_term =="Population growth (annual %)" and Regions == "World(WLD)":
                           return PgaWLD() 
                        if search_term =="Population growth (annual %)" and Regions == "Latin America and the Caribbean(CLA)":
                           return PgaCLA()
                        if search_term =="Population growth (annual %)" and Regions == "Africa(AFR)":
                           return PgaAFR()
                        if search_term =="Population growth (annual %)" and Regions == "European Union(EUU)":
                           return PgaEUU()
                        if search_term =="Population growth (annual %)" and Regions == "South Asia(SAS)":
                           return PgaSAS()


                    #Population, female
                   
                        if search_term =="Population, female" and Regions == "World(WLD)":
                           return PfWLD() 
                        if search_term =="Population, female" and Regions == "Latin America and the Caribbean(CLA)":
                           return PfCLA()
                        if search_term =="Population, female" and Regions == "Africa(AFR)":
                           return PfAFR()
                        if search_term =="Population, female" and Regions == "European Union(EUU)":
                           return PfEUU()
                        if search_term =="Population, female" and Regions == "South Asia(SAS)":
                           return PfSAS()


                #Population, male
                   
                        if search_term =="Population, male" and Regions == "World(WLD)":
                           return PmWLD() 
                        if search_term =="Population, male" and Regions == "Latin America and the Caribbean(CLA)":
                           return PmCLA()
                        if search_term =="Population, male" and Regions == "Africa(AFR)":
                           return PmAFR()
                        if search_term =="Population, male" and Regions == "European Union(EUU)":
                           return PmEUU()
                        if search_term =="Population, male" and Regions == "South Asia(SAS)":
                           return PmSAS()


                #Population, total
                   
                        if search_term =="Population, total" and Regions == "World(WLD)":
                           return PtWLD() 
                        if search_term =="Population, total" and Regions == "Latin America and the Caribbean(CLA)":
                           return PtCLA()
                        if search_term =="Population, total" and Regions == "Africa(AFR)":
                           return PtAFR()
                        if search_term =="Population, total" and Regions == "European Union(EUU)":
                           return PtEUU()
                        if search_term =="Population, total" and Regions == "South Asia(SAS)":
                           return PtSAS()

                
                #Suicide mortality rate (per 100,000 population)
                   
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regions == "World(WLD)":
                           return SmrWLD() 
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regions == "Latin America and the Caribbean(CLA)":
                           return SmrCLA()
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regions == "Africa(AFR)":
                           return SmrAFR()
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regions == "European Union(EUU)":
                           return SmrEUU()
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regions == "South Asia(SAS)":
                           return SmrSAS()


                #Suicide mortality rate, female (per 100,000 female population)
                   
                        if search_term =="Suicide mortality rate, female (per 100,000 female population)" and Regions == "World(WLD)":
                           return SmrfWLD() 
                        if search_term =="Suicide mortality rate, female (per 100,000 female population)" and Regions == "Latin America and the Caribbean(CLA)":
                           return SmrfCLA()
                        if search_term =="Suicide mortality rate, female (per 100,000 female population)" and Regions == "Africa(AFR)":
                           return SmrfAFR()
                        if search_term =="Suicide mortality rate, female (per 100,000 female population)" and Regions == "European Union(EUU)":
                           return SmrfEUU()
                        if search_term =="Suicide mortality rate, female (per 100,000 female population)" and Regions == "South Asia(SAS)":
                           return SmrfSAS()


                #Suicide mortality rate, male (per 100,000 male population)
                   
                        if search_term =="Suicide mortality rate, male (per 100,000 male population)" and Regions == "World(WLD)":
                           return SmrmWLD() 
                        if search_term =="Suicide mortality rate, male (per 100,000 male population)" and Regions == "Latin America and the Caribbean(CLA)":
                           return SmrmCLA()
                        if search_term =="Suicide mortality rate, male (per 100,000 male population)" and Regions == "Africa(AFR)":
                           return SmrmAFR()
                        if search_term =="Suicide mortality rate, male (per 100,000 male population)" and Regions == "European Union(EUU)":
                           return SmrmEUU()
                        if search_term =="Suicide mortality rate, male (per 100,000 male population)" and Regions == "South Asia(SAS)":
                           return SmrmSAS()


                #Wanted fertility rate (births per woman)
                   
                        if search_term =="Wanted fertility rate (births per woman)" and Regions == "World(WLD)":
                           return WfrWLD() 
                        if search_term =="Wanted fertility rate (births per woman)" and Regions == "Latin America and the Caribbean(CLA)":
                           return WfrCLA()
                        if search_term =="Wanted fertility rate (births per woman)" and Regions == "Africa(AFR)":
                           return WfrAFR()
                        if search_term =="Wanted fertility rate (births per woman)" and Regions == "European Union(EUU)":
                           return WfrEUU()
                        if search_term =="Wanted fertility rate (births per woman)" and Regions == "South Asia(SAS)":
                           return WfrSAS()

                
                    with nav2:
                            Regions = st.selectbox("Regions :",Regiones)

                    
                    
                         
                st.write(result())
                with nav3:    
                    submit_search = st.form_submit_button()
   
   
   
if __name__ =="__main__":
    main()
