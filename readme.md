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

The objective of this repository is make a research about growth/decrease population using some data analysis techniques. To do it We use the oficial data provided by [DANE](https://www.dane.gov.co), that is the oficial entity responsible for the planning, collection, processing, analysis and dissemination of official statistics of Colombia.

> The dataset can be accessed by the follow [link](https://www.dane.gov.co/files/investigaciones/poblacion/proyepobla06_20/ProyeccionMunicipios2005_2020.xls)

## Steps

1. Create virtual enviaroments:

    Win
 ```
 python -m venv .venv
 ```
linux/MacOs
 ```
 python3 -m virtualenv .venv
 ```
Or using anaconda 
 ```
 conda create --name .venv python=3.10
 ```

2. Activate the virtual environment

    Win
 ```
 .venv/Scripts/activate
 ```
 linux/MacOs
 ```
 source .venv/bin/activate
 ```
Or using anaconda 
 ```
 conda ativate .venv
 ```

3. Download the requirements  from requirements.txt if you are in windows or Linux and


    Win/Conda
 ```
 python -m pip install -r requirements.txt
 ```
 MacOs/Linux
 ```
 python3 -m pip install -r requirements.txt
 ```


4. Visualize the data mun/ProyeccionMunicipios2005_2020.xls

In more cases is important see the documentation, what kind of data is available here.

> The xls contains 2 important columns Municipios and Departamentos.

5. Generate sample population. (mun/First.ipynb)

6. (Optional) in the folder Colombia is generated the same process for the population


## Referencias

[1] 

<!-- [Data Colombian municipalities](https://www.dane.gov.co/files/investigaciones/poblacion/proyepobla06_20/ProyeccionMunicipios2005_2020.xls) -->

[Data Colombia](https://datosmacro.expansion.com/demografia/poblacion/colombia)

[Manipulation pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

[Methods arithmetic](https://ccp.ucr.ac.cr/cursos/demografia_03/materia/5_crecimiento.htm)