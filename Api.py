import datetime
from unicodedata import decimal
import wbgapi as wb

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plotly.subplots import make_subplots

## Adolescent fertility rate (births per 1,000 women ages 15-19)---------------------------------------------------------------
#World(WLD)
def AfrWLD():
    AfrWLD=wb.data.DataFrame('SP.ADO.TFRT', wb.region.members('WLD'), range(2010, 2023, 1))
    return AfrWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def AfrCLA():
    AfrCLA=wb.data.DataFrame('SP.ADO.TFRT', wb.region.members('CLA'), range(2010, 2023, 1))
    return AfrCLA
#Africa(AFR)
def AfrAFR():
    AfrAFR=wb.data.DataFrame('SP.ADO.TFRT', wb.region.members('AFR'), range(2010, 2023, 1))
    return AfrAFR
#European Union(EUU)
def AfrEUU():
    AfrEUU=wb.data.DataFrame('SP.ADO.TFRT', wb.region.members('EUU'), range(2010, 2023, 1))
    return AfrEUU
#South Asia(IFC classification)(SAS)
def AfrSAS():
    AfrSAS=wb.data.DataFrame('SP.ADO.TFRT', wb.region.members('SAS'), range(2010, 2023, 1))
    return AfrSAS

## Birth rate, crude (per 1000 people)-----------------------------------------------------------------------------------------
#World(WLD)
def BrcWLD():
    BrcWLD=wb.data.DataFrame('SP.DYN.CBRT.IN', wb.region.members('WLD'), range(2010, 2023, 1))
    return BrcWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def BrcCLA():
    BrcCLA=wb.data.DataFrame('SP.DYN.CBRT.IN', wb.region.members('CLA'), range(2010, 2023, 1))
    return BrcCLA
#Africa(AFR)
def BrcAFR():
    BrcAFR=wb.data.DataFrame('SP.DYN.CBRT.IN', wb.region.members('AFR'), range(2010, 2023, 1))
    return BrcAFR
#European Union(EUU)
def BrcEUU():
    BrcEUU=wb.data.DataFrame('SP.DYN.CBRT.IN', wb.region.members('EUU'), range(2010, 2023, 1))
    return BrcEUU
#South Asia(IFC classification)(SAS)
def BrcSAS():
    BrcSAS=wb.data.DataFrame('SP.DYN.CBRT.IN', wb.region.members('SAS'), range(2010, 2023, 1))
    return BrcSAS

## Births attended by skilled health staff (% of total)--------------------------------------------------------------------------
#World(WLD)
def BashWLD():
    BashWLD=wb.data.DataFrame('SH.STA.BRTC.ZS', wb.region.members('WLD'), range(2010, 2023, 1))
    return BashWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def BashCLA():
    BashCLA=wb.data.DataFrame('SH.STA.BRTC.ZS', wb.region.members('CLA'), range(2010, 2023, 1))
    return BashCLA
#Africa(AFR)
def BashAFR():
    BashAFR=wb.data.DataFrame('SH.STA.BRTC.ZS', wb.region.members('AFR'), range(2010, 2023, 1))
    return BashAFR
#European Union(EUU)
def BashEUU():
    BashEUU=wb.data.DataFrame('SH.STA.BRTC.ZS', wb.region.members('EUU'), range(2010, 2023, 1))
    return BashEUU
#South Asia(IFC classification)(SAS)
def BashSAS():
    BashSAS=wb.data.DataFrame('SH.STA.BRTC.ZS', wb.region.members('SAS'), range(2010, 2023, 1))
    return BashSAS

## Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total)-------------------------
#World(WLD)
def CodpnWLD():
    CodpnWLD=wb.data.DataFrame('SH.DTH.COMM.ZS', wb.region.members('WLD'), range(2010, 2023, 1))
    return CodpnWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def CodpnCLA():
    CodpnCLA=wb.data.DataFrame('SH.DTH.COMM.ZS', wb.region.members('CLA'), range(2010, 2023, 1))
    return CodpnCLA
#Africa(AFR)
def CodpnAFR():
    CodpnAFR=wb.data.DataFrame('SH.DTH.COMM.ZS', wb.region.members('AFR'), range(2010, 2023, 1))
    return CodpnAFR
#European Union(EUU)
def CodpnEUU():
    CodpnEUU=wb.data.DataFrame('SH.DTH.COMM.ZS', wb.region.members('EUU'), range(2010, 2023, 1))
    return CodpnEUU
#South Asia(IFC classification)(SAS)
def CodpnSAS():
    CodpnSAS=wb.data.DataFrame('SH.DTH.COMM.ZS', wb.region.members('SAS'), range(2010, 2023, 1))
    return CodpnSAS


## Current health expenditure (% of GDP)------------------------------------------------------------------------------------------
#World(WLD)
def CuheWLD():
    CuheWLD=wb.data.DataFrame('SH.XPD.CHEX.GD.ZS', wb.region.members('WLD'), range(2010, 2023, 1))
    return CuheWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def CuheCLA():
    CuheCLA=wb.data.DataFrame('SH.XPD.CHEX.GD.ZS', wb.region.members('CLA'), range(2010, 2023, 1))
    return CuheCLA
#Africa(AFR)
def CuheAFR():
    CuheAFR=wb.data.DataFrame('SH.XPD.CHEX.GD.ZS', wb.region.members('AFR'), range(2010, 2023, 1))
    return CuheAFR
#European Union(EUU)
def CuheEUU():
    CuheEUU=wb.data.DataFrame('SH.XPD.CHEX.GD.ZS', wb.region.members('EUU'), range(2010, 2023, 1))
    return CuheEUU
#South Asia(IFC classification)(SAS)
def CuheSAS():
    CuheSAS=wb.data.DataFrame('SH.XPD.CHEX.GD.ZS', wb.region.members('SAS'), range(2010, 2023, 1))
    return CuheSAS

## Current health expenditure per capita (current US$)-----------------------------------------------------------------------------
#World(WLD)
def CuhepcWLD():
    CuhepcWLD=wb.data.DataFrame("SH.XPD.CHEX.PC.CD", wb.region.members('WLD'), range(2010, 2023, 1))
    return CuhepcWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def CuhepcCLA():
    CuhepcCLA=wb.data.DataFrame("SH.XPD.CHEX.PC.CD", wb.region.members('CLA'), range(2010, 2023, 1))
    return CuhepcCLA
#Africa(AFR)
def CuhepcAFR():
    CuhepcAFR=wb.data.DataFrame("SH.XPD.CHEX.PC.CD", wb.region.members('AFR'), range(2010, 2023, 1))
    return CuhepcAFR
#European Union(EUU)
def CuhepcEUU():
    CuhepcEUU=wb.data.DataFrame("SH.XPD.CHEX.PC.CD", wb.region.members('EUU'), range(2010, 2023, 1))
    return CuhepcEUU
#South Asia(IFC classification)(SAS)
def CuhepcSAS():
    CuhepcSAS=wb.data.DataFrame("SH.XPD.CHEX.PC.CD", wb.region.members('SAS'), range(2010, 2023, 1))
    return CuhepcSAS

## Death rate, crude (per 1,000 people)---------------------------------------------------------------------------------------------
#World(WLD)
def DrcmWLD():
    DrcmWLD=wb.data.DataFrame("SP.DYN.CDRT.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return DrcmWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def DrcmCLA():
    DrcmCLA=wb.data.DataFrame("SP.DYN.CDRT.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return DrcmCLA
#Africa(AFR)
def DrcmAFR():
    DrcmAFR=wb.data.DataFrame("SP.DYN.CDRT.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return DrcmAFR
#European Union(EUU)
def DrcmEUU():
    DrcmEUU=wb.data.DataFrame("SP.DYN.CDRT.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return DrcmEUU
#South Asia(IFC classification)(SAS)
def DrcmSAS():
    DrcmSAS=wb.data.DataFrame("SP.DYN.CDRT.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return DrcmSAS

## Fertility rate, total (births per woman)-----------------------------------------------------------------------------------------
#World(WLD)
def FrtbWLD():
    FrtbWLD=wb.data.DataFrame("SP.DYN.TFRT.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return FrtbWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def FrtbCLA():
    FrtbCLA=wb.data.DataFrame("SP.DYN.TFRT.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return FrtbAFR
#Africa(AFR)
def FrtbAFR():
    FrtbAFR=wb.data.DataFrame("SP.DYN.TFRT.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return FrtbAFR
#European Union(EUU)
def FrtbEUU():
    FrtbEUU=wb.data.DataFrame("SP.DYN.TFRT.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return FrtbEUU
#South Asia(IFC classification)(SAS)
def FrtbSAS():
    FrtbSAS=wb.data.DataFrame("SP.DYN.TFRT.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return FrtbSAS

## Life expectancy at birth, female (years)------------------------------------------------------------------------------------------
#World(WLD)
def LebfWLD():
    LebfWLD=wb.data.DataFrame("SP.DYN.LE00.FE.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return LebfWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def LebfCLA():
    LebfCLA=wb.data.DataFrame("SP.DYN.LE00.FE.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return LebfCLA
#Africa(AFR)
def LebfAFR():
    LebfAFR=wb.data.DataFrame("SP.DYN.LE00.FE.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return LebfAFR
#European Union(EUU)
def LebfEUU():
    LebfEUU=wb.data.DataFrame("SP.DYN.LE00.FE.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return LebfEUU
#South Asia(IFC classification)(SAS)
def LebfSAS():
    LebfSAS=wb.data.DataFrame("SP.DYN.LE00.FE.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return LebfSAS

## Life expectancy at birth, male (years)--------------------------------------------------------------------------------------------
#World(WLD)
def LebmWLD():
    LebmWLD=wb.data.DataFrame("SP.DYN.LE00.MA.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return LebmWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def LebmCLA():
    LebmCLA=wb.data.DataFrame("SP.DYN.LE00.MA.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return LebmCLA
#Africa(AFR)
def LebmAFR():
    LebmAFR=wb.data.DataFrame("SP.DYN.LE00.MA.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return LebmAFR
#European Union(EUU)
def LebmEUU():
    LebmEUU=wb.data.DataFrame("SP.DYN.LE00.MA.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return LebmEUU
#South Asia(IFC classification)(SAS)
def LebmSAS():
    LebmSAS=wb.data.DataFrame("SP.DYN.LE00.MA.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return LebmSAS

## Life expectancy at birth, total (years)--------------------------------------------------------------------------------------------
#World(WLD)
def LebWLD():
    LebWLD=wb.data.DataFrame("SP.DYN.LE00.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return LebWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def LebCLA():
    LebCLA=wb.data.DataFrame("SP.DYN.LE00.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return LebCLA
#Africa(AFR)
def LebAFR():
    LebAFR=wb.data.DataFrame("SP.DYN.LE00.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return LebAFR
#European Union(EUU)
def LebEUU():
    LebEUU=wb.data.DataFrame("SP.DYN.LE00.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return LebEUU
#South Asia(IFC classification)(SAS)
def LebSAS():
    LebSAS=wb.data.DataFrame("SP.DYN.LE00.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return LebSAS

## Low-birthweight babies (% of births)------------------------------------------------------------------------------------------------
#World(WLD)
def LbbWLD():
    LbbWLD=wb.data.DataFrame("SH.STA.BRTW.ZS", wb.region.members('WLD'), range(2010, 2023, 1))
    return LbbWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def LbbCLA():
    LbbCLA=wb.data.DataFrame("SH.STA.BRTW.ZS", wb.region.members('CLA'), range(2010, 2023, 1))
    return LbbCLA
#Africa(AFR)
def LbbAFR():
    LbbAFR=wb.data.DataFrame("SH.STA.BRTW.ZS", wb.region.members('AFR'), range(2010, 2023, 1))
    return LbbAFR
#European Union(EUU)
def LbbEUU():
    LbbEUU=wb.data.DataFrame("SH.STA.BRTW.ZS", wb.region.members('EUU'), range(2010, 2023, 1))
    return LbbEUU
#South Asia(IFC classification)(SAS)
def LbbSAS():
    LbbSAS=wb.data.DataFrame("SH.STA.BRTW.ZS", wb.region.members('SAS'), range(2010, 2023, 1))
    return LbbSAS

## Mortality rate, adult, female (per 1,000 female adults)-----------------------------------------------------------------------------
#World(WLD)
def MrafWLD():
    MrafWLD=wb.data.DataFrame("SP.DYN.AMRT.FE", wb.region.members('WLD'), range(2010, 2023, 1))
    return MrafWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def MrafCLA():
    MrafCLA=wb.data.DataFrame("SP.DYN.AMRT.FE", wb.region.members('CLA'), range(2010, 2023, 1))
    return MrafCLA
#Africa(AFR)
def MrafAFR():
    MrafAFR=wb.data.DataFrame("SP.DYN.AMRT.FE", wb.region.members('AFR'), range(2010, 2023, 1))
    return MrafAFR
#European Union(EUU)
def MrafEUU():
    MrafEUU=wb.data.DataFrame("SP.DYN.AMRT.FE", wb.region.members('EUU'), range(2010, 2023, 1))
    return MrafEUU
#South Asia(IFC classification)(SAS)
def MrafSAS():
    MrafSAS=wb.data.DataFrame("SP.DYN.AMRT.FE", wb.region.members('SAS'), range(2010, 2023, 1))
    return MrafSAS

## Mortality rate, adult, male (per 1,000 male adults)----------------------------------------------------------------------------------
#World(WLD)
def MramWLD():
    MramWLD=wb.data.DataFrame("SP.DYN.AMRT.MA", wb.region.members('WLD'), range(2010, 2023, 1))
    return MramWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def MramCLA():
    MramCLA=wb.data.DataFrame("SP.DYN.AMRT.MA", wb.region.members('CLA'), range(2010, 2023, 1))
    return MramCLA
#Africa(AFR)
def MramAFR():
    MramAFR=wb.data.DataFrame("SP.DYN.AMRT.MA", wb.region.members('AFR'), range(2010, 2023, 1))
    return MramAFR
#European Union(EUU)
def MramEUU():
    MramEUU=wb.data.DataFrame("SP.DYN.AMRT.MA", wb.region.members('EUU'), range(2010, 2023, 1))
    return MramEUU
#South Asia(IFC classification)(SAS)
def MramSAS():
    MramSAS=wb.data.DataFrame("SP.DYN.AMRT.MA", wb.region.members('SAS'), range(2010, 2023, 1))
    return MramSAS

## Mortality rate, infant (per 1,000 live births)---------------------------------------------------------------------------------------
#World(WLD)
def MriWLD():
    MriWLD=wb.data.DataFrame("SP.DYN.IMRT.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return MriWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def MriCLA():
    MriCLA=wb.data.DataFrame("SP.DYN.IMRT.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return MriCLA
#Africa(AFR)
def MriAFR():
    MriAFR=wb.data.DataFrame("SP.DYN.IMRT.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return MriAFR
#European Union(EUU)
def MriEUU():
    MriEUU=wb.data.DataFrame("SP.DYN.IMRT.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return MriEUU
#South Asia(IFC classification)(SAS)
def MriSAS():
    MriSAS=wb.data.DataFrame("SP.DYN.IMRT.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return MriSAS

## Population growth (annual %)----------------------------------------------------------------------------------------------------------
#World(WLD)
def PgaWLD():
    PgaWLD=wb.data.DataFrame("SP.POP.GROW", wb.region.members('WLD'), range(2010, 2023, 1))
    return PgaWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def PgaCLA():
    PgaCLA=wb.data.DataFrame("SP.POP.GROW", wb.region.members('CLA'), range(2010, 2023, 1))
    return PgaCLA
#Africa(AFR)
def PgaAFR():
    PgaAFR=wb.data.DataFrame("SP.POP.GROW", wb.region.members('AFR'), range(2010, 2023, 1))
    return PgaAFR
#European Union(EUU)
def PgaEUU():
    PgaEUU=wb.data.DataFrame("SP.POP.GROW", wb.region.members('EUU'), range(2010, 2023, 1))
    return PgaEUU
#South Asia(IFC classification)(SAS)
def PgaSAS():
    PgaSAS=wb.data.DataFrame("SP.POP.GROW", wb.region.members('SAS'), range(2010, 2023, 1))
    return PgaSAS

## Population, female---------------------------------------------------------------------------------------------------------------------
#World(WLD)
def PfWLD():
    PfWLD=wb.data.DataFrame("SP.POP.TOTL.FE.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return PfWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def PfCLA():
    PfCLA=wb.data.DataFrame("SP.POP.TOTL.FE.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return PfCLA
#Africa(AFR)
def PfAFR():
    PfAFR=wb.data.DataFrame("SP.POP.TOTL.FE.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return PfAFR
#European Union(EUU)
def PfEUU():
    PfEUU=wb.data.DataFrame("SP.POP.TOTL.FE.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return PfEUU
#South Asia(IFC classification)(SAS)
def PfSAS():
    PfSAS=wb.data.DataFrame("SP.POP.TOTL.FE.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return PfSAS

# Population, male-------------------------------------------------------------------------------------------------------------------------
#World(WLD)
def PmWLD():
    PmWLD=wb.data.DataFrame("SP.POP.TOTL.MA.IN", wb.region.members('WLD'), range(2010, 2023, 1))
    return PmWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def PmCLA():
    PmCLA=wb.data.DataFrame("SP.POP.TOTL.MA.IN", wb.region.members('CLA'), range(2010, 2023, 1))
    return PmCLA
#Africa(AFR)
def PmAFR():
    PmAFR=wb.data.DataFrame("SP.POP.TOTL.MA.IN", wb.region.members('AFR'), range(2010, 2023, 1))
    return PmAFR
#European Union(EUU)
def PmEUU():
    PmEUU=wb.data.DataFrame("SP.POP.TOTL.MA.IN", wb.region.members('EUU'), range(2010, 2023, 1))
    return PmEUU
#South Asia(IFC classification)(SAS)
def PmSAS():
    PmSAS=wb.data.DataFrame("SP.POP.TOTL.MA.IN", wb.region.members('SAS'), range(2010, 2023, 1))
    return PmSAS

## Population, total-------------------------------------------------------------------------------------------------------------------------
#World(WLD)
def PtWLD():
    PtWLD=wb.data.DataFrame("SP.POP.TOTL", wb.region.members('WLD'), range(2010, 2023, 1))
    return PtWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def PtCLA():
    PtCLA=wb.data.DataFrame("SP.POP.TOTL", wb.region.members('CLA'), range(2010, 2023, 1))
    return PtCLA
#Africa(AFR)
def PtAFR():
    PtAFR=wb.data.DataFrame("SP.POP.TOTL", wb.region.members('AFR'), range(2010, 2023, 1))
    return PtAFR
#European Union(EUU)
def PtEUU():
    PtEUU=wb.data.DataFrame("SP.POP.TOTL", wb.region.members('EUU'), range(2010, 2023, 1))
    return PtEUU
#South Asia(IFC classification)(SAS)
def PtSAS():
    PtSAS=wb.data.DataFrame("SP.POP.TOTL", wb.region.members('SAS'), range(2010, 2023, 1))
    return PtSAS

## Suicide mortality rate (per 100,000 population)--------------------------------------------------------------------------------------------
#World(WLD)
def SmrWLD():
    SmrWLD=wb.data.DataFrame("SH.STA.SUIC.P5", wb.region.members('WLD'), range(2010, 2023, 1))
    return SmrWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def SmrCLA():
    SmrCLA=wb.data.DataFrame("SH.STA.SUIC.P5", wb.region.members('CLA'), range(2010, 2023, 1))
    return SmrCLA
#Africa(AFR)
def SmrAFR():
    SmrAFR=wb.data.DataFrame("SH.STA.SUIC.P5", wb.region.members('AFR'), range(2010, 2023, 1))
    return SmrAFR
#European Union(EUU)
def SmrEUU():
    SmrEUU=wb.data.DataFrame("SH.STA.SUIC.P5", wb.region.members('EUU'), range(2010, 2023, 1))
    return SmrEUU
#South Asia(IFC classification)(SAS)
def SmrSAS():
    SmrSAS=wb.data.DataFrame("SH.STA.SUIC.P5", wb.region.members('SAS'), range(2010, 2023, 1))
    return SmrSAS


## Suicide mortality rate, female (per 100,000 female population)-----------------------------------------------------------------------------
#World(WLD)
def SmrfWLD():
    SmrfWLD=wb.data.DataFrame("SH.STA.SUIC.FE.P5", wb.region.members('WLD'), range(2010, 2023, 1))
    return SmrfWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def SmrfCLA():
    SmrfCLA=wb.data.DataFrame("SH.STA.SUIC.FE.P5", wb.region.members('CLA'), range(2010, 2023, 1))
    return SmrfCLA
#Africa(AFR)
def SmrfAFR():
    SmrfAFR=wb.data.DataFrame("SH.STA.SUIC.FE.P5", wb.region.members('AFR'), range(2010, 2023, 1))
    return SmrfAFR
#European Union(EUU)
def SmrfEUU():
    SmrfEUU=wb.data.DataFrame("SH.STA.SUIC.FE.P5", wb.region.members('EUU'), range(2010, 2023, 1))
    return SmrfEUU
#South Asia(IFC classification)(SAS)
def SmrfSAS():
    SmrfSAS=wb.data.DataFrame("SH.STA.SUIC.FE.P5", wb.region.members('SAS'), range(2010, 2023, 1))
    return SmrfSAS

## Suicide mortality rate, male (per 100,000 male population)---------------------------------------------------------------------------------
#World(WLD)
def SmrmWLD():
    SmrmWLD=wb.data.DataFrame("SH.STA.SUIC.MA.P5", wb.region.members('WLD'), range(2010, 2023, 1))
    return SmrmWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def SmrmCLA():
    SmrmCLA=wb.data.DataFrame("SH.STA.SUIC.MA.P5", wb.region.members('CLA'), range(2010, 2023, 1))
    return SmrmCLA
#Africa(AFR)
def SmrmAFR():
    SmrmAFR=wb.data.DataFrame("SH.STA.SUIC.MA.P5", wb.region.members('AFR'), range(2010, 2023, 1))
    return SmrmAFR
#European Union(EUU)
def SmrmEUU():
    SmrmEUU=wb.data.DataFrame("SH.STA.SUIC.MA.P5", wb.region.members('EUU'), range(2010, 2023, 1))
    return SmrmEUU
#South Asia(IFC classification)(SAS)
def SmrmSAS():
    SmrmSAS=wb.data.DataFrame("SH.STA.SUIC.MA.P5", wb.region.members('SAS'), range(2010, 2023, 1))
    return SmrmSAS

## Wanted fertility rate (births per woman)---------------------------------------------------------------------------------------------------
#World(WLD)
def WfrWLD():
    WfrWLD=wb.data.DataFrame("SP.DYN.WFRT", wb.region.members('WLD'), range(2010, 2023, 1))
    return WfrWLD
#Latin America and the Caribbean(IFC classification)(CLA)
def WfrCLA():
    WfrCLA=wb.data.DataFrame("SP.DYN.WFRT", wb.region.members('CLA'), range(2010, 2023, 1))
    return WfrCLA
#Africa(AFR)
def WfrAFR():
    WfrAFR=wb.data.DataFrame("SP.DYN.WFRT", wb.region.members('AFR'), range(2010, 2023, 1))
    return WfrAFR
#European Union(EUU)
def WfrEUU():
    WfrEUU=wb.data.DataFrame("SP.DYN.WFRT", wb.region.members('EUU'), range(2010, 2023, 1))
    return WfrEUU
#South Asia(IFC classification)(SAS)
def WfrSAS():
    WfrSAS=wb.data.DataFrame("SP.DYN.WFRT", wb.region.members('SAS'), range(2010, 2023, 1))
    return WfrSAS




