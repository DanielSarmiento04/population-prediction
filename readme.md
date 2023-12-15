---
title : Predicción de poblaciones.
date : 2023-02-25
excerpt : Porfolio
description : Estimación de una población
tags :
 - python
 - pandas
 - prediction
---

# **Population Prediction**


## Resumen

The objective of this repository is make a research about growth/decrease population using some data analysis techniques. To do it We use the oficial data provided by [The world bank](https://data.worldbank.org/indicator/SP.POP.TOTL?end=2022&locations=BM&start=1960&view=chart) is an international financial institution that provides loans and grants to governments of low- and middle-income countries for various development purposes, its mission is to help developing countries achieve sustainable growth by financing investment, mobilizing capital in international financial markets, and providing advisory services



<!-- [DANE](https://www.dane.gov.co), that is the oficial entity responsible for the planning, collection, processing, analysis and dissemination of official statistics of Colombia. -->

> The dataset can be accessed by the follow [link](https://www.dane.gov.co/files/investigaciones/poblacion/proyepobla06_20/ProyeccionMunicipios2005_2020.xls)


## Table of contents
1. [Set Up](#set-up)
2. [Selected population](#selected-population)

## Set Up

Create the python environment and download the necessary dependencies

```
conda create --name populations python=3.10 -y
conda activate populations
pip install -r requirements.txt
```


## Selected population (Ukraine)

The algorithm are design to work with some tendency, but for developer reason we selected Ukraine as the default population


## References

[1] Gramalote (2023) Wikipedia. Available at: https://es.wikipedia.org/wiki/Gramalote (Accessed: 13 December 2023). 

<!-- [Data Colombian municipalities](https://www.dane.gov.co/files/investigaciones/poblacion/proyepobla06_20/ProyeccionMunicipios2005_2020.xls) -->
<!-- 
[Data Colombia](https://datosmacro.expansion.com/demografia/poblacion/colombia)

[Manipulation pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

[Methods arithmetic](https://ccp.ucr.ac.cr/cursos/demografia_03/materia/5_crecimiento.htm) -->