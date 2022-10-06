import streamlit as st
from Api import *
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from client import lifexp,lifexpe,lifexpa,lifexpaf,lifexpo
#API IMPORT -------------------------------------------------------------------------------------------------------------------
## Adolescent fertility rate (births per 1,000 women ages 15-19)
from Api import AfrAFR,AfrCLA,AfrEUU,AfrSAS,AfrWLD
## Birth rate, crude (per 1000 people)
#from Api import BrcAFR,BrcCLA,BrcEUU,BrcSAS,BrcWLD
## Births attended by skilled health staff (% of total)
from Api import BashAFR,BashCLA,BashEUU,BashSAS,BashWLD
## Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total)
from Api import CodpnAFR,CodpnCLA,CodpnEUU,CodpnSAS,CodpnWLD
## Capital health expenditure (% of GDP)
from Api import CheAFR,CheCLA,CheEUU,CheSAS,CheWLD
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
    menu = ["Life Expectancy","Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)

    st.title("Life Expectancy")

    if choice == "Life Expectancy":
            st.subheader("Continentes")
            if st.checkbox("America"):
                st.write(lifexp())
            if st.checkbox("Europa"):
                st.write(lifexpe())
            if st.checkbox("Asia"):
                st.write(lifexpa())
            if st.checkbox("Africa"):
                st.write(lifexpaf())
            if st.checkbox("Oceania"):
                st.write(lifexpo())
    else :
            
            st.subheader("Dataset")
            if st.checkbox("Dataset"):
                df=pd.read_csv("life_expectancy.csv")
                st.dataframe(df)
        
            if st.checkbox("AFR"):
                st.dataframe(AfrAFR())


if __name__ =="__main__":
    main()
