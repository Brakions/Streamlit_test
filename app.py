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
from client import *
import plotly.graph_objects as go
import math



#API IMPORT -------------------------------------------------------------------------------------------------------------------
st.set_page_config(
    page_title="Indata", layout="wide",
    page_icon="💚",
)
import base64

main_bg = "earth-leaf-greenery-wallpaper-preview.jpg"
main_bg_ext = "jpg"

side_bg = "earth-leaf-greenery-wallpaper-preview.jpg"
side_bg_ext = "jpg"

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://user-images.githubusercontent.com/93687273/217873392-7fee4e67-6c2e-401b-bb81-229509cdca67.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
def sidebar_bg(side_bg):

   side_bg_ext = 'gif'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'giphy.gif'
sidebar_bg(side_bg)
   
def main():
    techo=[" ","🔲 model"]
    choice = st.sidebar.selectbox("🔺Prediction",techo,index=0)
    with st.sidebar:
         add_radio = st.radio(
            "Choose :",
            ("Mostrar", "No Mostrar")
         )
    
    
    if choice == " ":
      st.title("")
    if add_radio == "No Mostrar":
       choice = " "
    
    ##-------------------------------------------------------------------------------------------------------------------------
      # Path del modelo preentrenado
    MODEL_PATH = 'pickle_model2020.pkl'
    
    #Funcion st.write para slides
    def fin(x):
      if x <0:
         st.write("Disminuir en ", (abs(x)*100/3),"%")
      elif x==0:
            st.write("Sin cambios")
      else:
            st.write("Aumentar en",(abs(x)*100/3),"%")

    def model_prediction(x_in, model):

               x = np.asarray(x_in).reshape(1,-1)
               preds=model.predict(x)

               return preds
    
    if choice == "🔲 model":
        st.title("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Cinzel&size=27&pause=100000&color=F79213&width=435&lines=Life+Expentancy+Predict)](https://git.io/typing-svg)")
        st.write("Este apartado se utiliza para predecir la espectativa de vida en años, para el entrenamiento se estadarizaron los datos numericos en una escala de :","-3.00 a 3.00 , en color 'verde' se puede indentificar a las variables que su valor es directamente proporcional a la expectativa de vida y en color 'rojo' su contraparte.")
        
        st.write(" ")
        st.write(" ")
        # Se carga el modelo
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    
            
      # Lecctura de datos
      #Datos = st.text_input
        st.write(" ")
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=Current+health+expenditure+per+capita+(current+US%24))](https://git.io/typing-svg)")
        A = st.slider("",min_value =-3.00,max_value=3.00,step= 0.01,value=0.00)
        fin(A)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=Current+health+expenditure+(%25)+of+GDP%3A)](https://git.io/typing-svg)")
        B = st.slider(" ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(B)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=F70000&background=000000&vCenter=true&width=438&height=24&lines=Adolescent+fertility+rate+%3A)](https://git.io/typing-svg)")
        C = st.slider("   ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(C)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=F70000&background=000000&vCenter=true&width=438&height=24&lines=Population%2C+total+%3A)](https://git.io/typing-svg)")
        D = st.slider("    ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(D)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=F70000&background=000000&vCenter=true&width=438&height=24&lines=Birth+rate%2C+crude+(per+1000+people)%3A)](https://git.io/typing-svg)")
        E = st.slider("     ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(E)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=F70000&background=000000&vCenter=true&width=438&height=24&lines=Fertility+rate%2C+total+(births+per+woman)%3A)](https://git.io/typing-svg)")
        F = st.slider("      ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(F)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=F70000&background=000000&vCenter=true&width=438&height=24&lines=Mortality+rate%2C+infant+(per+1%2C000+live+births)%3A)](https://git.io/typing-svg)")
        G = st.slider("       ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(G)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=Suicide+mortality+rate%3A)](https://git.io/typing-svg)")
        H = st.slider("             ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(H)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=Prevalence+of+overweight+among+adults+%3A)](https://git.io/typing-svg)")
        I = st.slider("              ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(I)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=GDP+per+capita%3A)](https://git.io/typing-svg)")
        J = st.slider("               ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(J)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=GDP+current(%24))](https://git.io/typing-svg)")
        K = st.slider("                  ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(K)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=F70000&background=000000&vCenter=true&width=438&height=24&lines=Prevalence+of+hypertension)](https://git.io/typing-svg)")
        L = st.slider("                   ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(L)
        st.write(" ")
        st.write("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Rajdhani&size=16&pause=100000&color=00F7E4FF&background=000000&vCenter=true&width=438&height=24&lines=Population+growth(%25))](https://git.io/typing-svg)")
        M = st.slider("                    ",min_value =-3.00,max_value=3.00,step= 0.01,value =0.00)
        fin(M)
       
    
      
      # El botón predicción se usa para iniciar el procesamiento
        if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
            x_in =[np.float_(A),
                    np.float_(B),
                    np.float_(C),
                    np.float_(D),
                    np.float_(E),
                    np.float_(F),
                    np.float_(G),
                    np.float_(H),
                    np.float_(I),
                    np.float_(J),
                    np.float_(K),
                    np.float_(L),
                    np.float_(M),]
                    
            predictS = model_prediction(x_in, model)
            st.success('La Esperanza de vida es: {}'.format(predictS[0]).upper())
        
 
    ##-------------------------------------------------------------------------------------------------------------------------

    casa=[" ","🔲 Series","🔲 Series (Final)"]
    choice = st.sidebar.selectbox("🔺Stats Explorer",casa)
    
    if choice == " ":
      st.title("")
      
    if choice == "🔲 Series":
         st.title("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Cinzel&size=35&pause=100000&color=F79213&width=435&lines=Series+Stats+Explorer)](https://git.io/typing-svg)")
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

    if choice == "🔲 Series (Final)":
            st.title("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Cinzel&size=35&pause=100000&color=F79213&width=435&lines=Series+Stats+Explorer)](https://git.io/typing-svg)")
            st.markdown('''
            Esta aplicación realiza una exploracion simple de datos estadísticos que tienen impacto en la  esperanza de vida !
            * **Python libraries:** pandas, streamlit, wbgapi 
            * **Data source:** https://www.worldbank.org/en/home''')
            st.subheader("Datasets (Region)")
            with st.form(key="searchform2"):
                nav1,nav2,nav3 = st.columns([3,2,1])
                Rgnes=["Latin America & Caribeann","Africa","European Union","South Asia","World"]

                Paises=[]
            with nav1:
                    search_term2 =st.selectbox("Select Region :",Rgnes)
                    def result():  
                     if search_term2 =="Latin America & Caribeann":
                           return(CLA4)
                     if search_term2 =="Africa":
                           return(AFR4)
                     if search_term2 =="European Union":
                           return(EUU4)
                     if search_term2 =="South Asia":
                           return(SAS4)
                     if search_term2 =="World":
                           return(WLD4)
            st.write(result())
            with nav2:
               
               submit_search = st.form_submit_button()
         #----------------------------------------------------------------------------------------------------------------------
    menu = [" ","🔲 Life Expectancy-Regions","🔲 Info","🔲 Datasets"]
    choice = st.sidebar.selectbox("🔺Proyeccion + Datasets (Semana 1)",menu)
    
    if choice == " ":
      st.title("")
    if choice == "🔲 Life Expectancy-Regions":
            st.title("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Cinzel&size=35&pause=100000&color=F79213&width=435&lines=Life+Expectancy)](https://git.io/typing-svg)")
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
    
        
            
    if choice == "🔲 Info":

            st.subheader("Info")
            if st.checkbox("Regions"):
                st.write(wb.region.info())
            if st.checkbox("Countries"):
                st.write(wb.economy.info())
            
            if st.checkbox("Series"):
                st.write(wb.series.info())

    if choice == "🔲 Datasets":

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
                        "Suicide mortality rate (per 100,000 population)"]
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
   
    menu2 = [" ","🔲 Series x Region"]
    choice = st.sidebar.selectbox("🔺Graficas x Series",menu2)
    if choice == "🔲 Series x Region":

            st.subheader("[![Typing SVG](https://readme-typing-svg.demolab.com?font=Cinzel&size=25&pause=100000&color=F79213&width=435&lines=Select+Serie+%3A)](https://git.io/typing-svg)")
            # Nav Search Form
            with st.form(key="searchformZ"):
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
                        "(constant LCU)"]
                Regiones=["World(WLD)","Latin America and the Caribbean(CLA)",
                            "Africa(AFR)","European Union(EUU)","South Asia(SAS)"]
                with nav1:
                    search_term =st.selectbox("Select Serie :",Series)
                    Regions3=["World(WLD)","Latin America and the Caribbean(CLA)",
                            "Africa(AFR)","European Union(EUU)","South Asia(SAS)"]
                    #Adolescent fertility rate (ages 15-19)
                    def result():
                        
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regiones == "World(WLD)":
                           return WLDgZ() 
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagZ()
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regiones == "Africa(AFR)":
                           return AfrgZ()
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regiones == "European Union(EUU)":
                           return EUUgZ()
                        if search_term =="Adolescent fertility rate (ages 15-19)" and Regiones == "South Asia(SAS)":
                           return SASgZ()
                    #Birth rate, crude (per 1000 people)
                   
                        if search_term =="Birth rate, crude (per 1000 people)" and Regiones == "World(WLD)":
                           return WLDbgZ() 
                        if search_term =="Birth rate, crude (per 1000 people)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagbZ()
                        if search_term =="Birth rate, crude (per 1000 people)" and Regiones == "Africa(AFR)":
                           return AfrbgZ()
                        if search_term =="Birth rate, crude (per 1000 people)" and Regiones == "European Union(EUU)":
                           return EUUbgZ()
                        if search_term =="Birth rate, crude (per 1000 people)" and Regiones == "South Asia(SAS)":
                           return SASbgZ()

                    #Births attended by skilled health staff (%)
                   
                        if search_term =="Births attended by skilled health staff (%)" and Regiones == "World(WLD)":
                           return BashWLD() 
                        if search_term =="Births attended by skilled health staff (%)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return BashCLA()
                        if search_term =="Births attended by skilled health staff (%)" and Regiones == "Africa(AFR)":
                           return BashAFR()
                        if search_term =="Births attended by skilled health staff (%)" and Regiones == "European Union(EUU)":
                           return BashEUU()
                        if search_term =="Births attended by skilled health staff (%)" and Regions == "South Asia(SAS)":
                           return BashSAS()

                    #Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total
                   
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regiones == "World(WLD)":
                           return CodpnWLD() 
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regiones == "Latin America and the Caribbean(CLA)":
                           return CodpnCLA()
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regiones == "Africa(AFR)":
                           return CodpnAFR()
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regiones == "European Union(EUU)":
                           return CodpnEUU()
                        if search_term =="Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (%) of total" and Regiones == "South Asia(SAS)":
                           return CodpnSAS()
                    
                    
                    #Current health expenditure (%) of GDP
                   
                        if search_term =="Current health expenditure (%) of GDP" and Regiones == "World(WLD)":
                           return WLDchZ() 
                        if search_term =="Current health expenditure (%) of GDP" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagchZ()
                        if search_term =="Current health expenditure (%) of GDP" and Regiones == "Africa(AFR)":
                           return AfrchZ()
                        if search_term =="Current health expenditure (%) of GDP" and Regiones == "European Union(EUU)":
                           return EUUchZ()
                        if search_term =="Current health expenditure (%) of GDP" and Regiones == "South Asia(SAS)":
                           return SASchZ()
                    
                    #Current health expenditure per capita (current US$)
                   
                        if search_term =="Current health expenditure per capita (current US$)" and Regiones == "World(WLD)":
                           return WLDchcZ() 
                        if search_term =="Current health expenditure per capita (current US$)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagchcZ()
                        if search_term =="Current health expenditure per capita (current US$)" and Regiones == "Africa(AFR)":
                           return AfrchcZ()
                        if search_term =="Current health expenditure per capita (current US$)" and Regiones == "European Union(EUU)":
                           return EUUchcZ()
                        if search_term =="Current health expenditure per capita (current US$)" and Regiones == "South Asia(SAS)":
                           return SASchcZ()

                    #Fertility rate, total (births per woman)
                   
                        if search_term =="Fertility rate, total (births per woman)" and Regiones == "World(WLD)":
                           return WLDfrZ() 
                        if search_term =="Fertility rate, total (births per woman)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagfrZ()
                        if search_term =="Fertility rate, total (births per woman)" and Regiones == "Africa(AFR)":
                           return AfrfrZ()
                        if search_term =="Fertility rate, total (births per woman)" and Regiones == "European Union(EUU)":
                           return EUUfrZ()
                        if search_term =="Fertility rate, total (births per woman)" and Regiones == "South Asia(SAS)":
                           return SASfrZ()

                    

                    #Life expectancy at birth, total (years)
                   
                        if search_term =="Life expectancy at birth, total (years)" and Regiones == "World(WLD)":
                           return WLDleZ()
                        if search_term =="Life expectancy at birth, total (years)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagleZ()
                        if search_term =="Life expectancy at birth, total (years)" and Regiones == "Africa(AFR)":
                           return Afrle()
                        if search_term =="Life expectancy at birth, total (years)" and Regiones == "European Union(EUU)":
                           return EUUleZ()
                        if search_term =="Life expectancy at birth, total (years)" and Regiones == "South Asia(SAS)":
                           return SASleZ()

      

                    

                    #Mortality rate, infant (per 1,000 live births)
                   
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regiones == "World(WLD)":
                           return WLDmrZ() 
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagmrZ()
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regiones == "Africa(AFR)":
                           return AfrmrZ()
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regiones == "European Union(EUU)":
                           return EUUmrZ()
                        if search_term =="Mortality rate, infant (per 1,000 live births)" and Regiones == "South Asia(SAS)":
                           return SASmrZ()
                    

                    #Population growth (annual %)
                   
                        if search_term =="Population growth (annual %)" and Regiones == "World(WLD)":
                           return WLDpwZ() 
                        if search_term =="Population growth (annual %)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagpwZ()
                        if search_term =="Population growth (annual %)" and Regiones == "Africa(AFR)":
                           return AfrpwZ()
                        if search_term =="Population growth (annual %)" and Regiones == "European Union(EUU)":
                           return EUUpwZ()
                        if search_term =="Population growth (annual %)" and Regiones == "South Asia(SAS)":
                           return SASpwZ()


                    



                #Population, total
                   
                        if search_term =="Population, total" and Regiones == "World(WLD)":
                           return WLDptZ() 
                        if search_term =="Population, total" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClaptZ()
                        if search_term =="Population, total" and Regiones == "Africa(AFR)":
                           return AfrptZ()
                        if search_term =="Population, total" and Regiones == "European Union(EUU)":
                           return EUUptZ()
                        if search_term =="Population, total" and Regiones == "South Asia(SAS)":
                           return SASptZ()

                
                #Suicide mortality rate (per 100,000 population)
                   
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regiones == "World(WLD)":
                           return WLDsmZ() 
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClasmZ()
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regiones == "Africa(AFR)":
                           return AfrsmZ()
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regiones == "European Union(EUU)":
                           return EUUsmZ()
                        if search_term =="Suicide mortality rate (per 100,000 population)" and Regiones == "South Asia(SAS)":
                           return SASsmZ()


            


                #(constant LCU)
                   
                        if search_term =="(constant LCU)" and Regiones == "World(WLD)":
                           return WLDgdpZ() 
                        if search_term =="(constant LCU)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return ClagdpZ()
                        if search_term =="(constant LCU)" and Regiones == "Africa(AFR)":
                           return AFRgdpZ()
                        if search_term =="(constant LCU)" and Regiones == "European Union(EUU)":
                           return EUUgdpZ()
                        if search_term =="(constant LCU)" and Regiones == "South Asia(SAS)":
                           return SASgdpZ()


                #Wanted fertility rate (births per woman)
                   
                        if search_term =="Wanted fertility rate (births per woman)" and Regiones == "World(WLD)":
                           return WfrWLD() 
                        if search_term =="Wanted fertility rate (births per woman)" and Regiones == "Latin America and the Caribbean(CLA)":
                           return WfrCLA()
                        if search_term =="Wanted fertility rate (births per woman)" and Regiones == "Africa(AFR)":
                           return WfrAFR()
                        if search_term =="Wanted fertility rate (births per woman)" and Regiones == "European Union(EUU)":
                           return WfrEUU()
                        if search_term =="Wanted fertility rate (births per woman)" and Regiones == "South Asia(SAS)":
                           return WfrSAS()
                
                with nav3:    
                    submit_search = st.form_submit_button()
                #st.write(result())
                with nav2:
                        Regiones = st.selectbox("Regions :",Regions3)
                st.write(result())        
                        
   
if __name__ =="__main__":
    main()
