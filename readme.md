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

# Population Prediction

This repository contains the analysis of growth/decrease in a real population, The information was extracted from the public source of the [DANE](https://www.dane.gov.co) the document extracted is ProyeccionMunicipios2005_2020.xls


note that the document has data from a wide variety of municipalities, for practical purposes the analysis will be carried out on the municipality of gramalote

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



# Referencias
[Manipulation Excel municipios](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

[Manipulation Colombia](https://datosmacro.expansion.com/demografia/poblacion/colombia)