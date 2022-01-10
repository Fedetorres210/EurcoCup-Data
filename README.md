
# Instructive system of Euro2020 Data
### A basic api and dashboard about the data of the Eurocope2020. 
### This dashboard uses the stages and the teams to locate the stats of the match.

 <img src="https://ichef.bbci.co.uk/news/800/cpsprodpb/E6E3/production/_118870195_gettyimages-1321658511.jpg.webp" width="580"/>


 ## Table of content
 -----------------
 * Goals completed
 * Data cleaning
 * Mongo Database
 * Streamlit Dashboard
 * Requests API



## Goals completed
------
### L1
* L1: Crear api 
* L1: Crear dashboard en streamlit
* L1: Base de datos en MongoDB o PostgreSQL
### L2
* L2: Tener la base de datos en el Cloud (Hay servicios gratis en MongoDB Atlas, Heroku Postgres, dentre otros)
#
-------

## Data cleaning
#
### Match data

For this project the required information was about every single match of the Eurcup 2020. For the comfort of the developer it was decided to use only stadistic of the game and not the specific events in each game.


<img src="documents\img\Datacleaning.png">

###### Especfic image of the datacleaning


----- 

## Mongo Database
---
### For this project it was decided to use the free databases of Atlas MongoDB.

<img src="documents\img\mongo.png">






## Streamlit Dashboard
------
To run the dashboard use the command:
```python
streamlit run main.py
```
### What you can get with the dashboard
----
* The aim of the dashboard is to show the stats of the specific match with the stage and home stage that you choose.
* You can also look for every game in the selected stage with the sidebar stage

 
    <img src="documents\img\stream.png">

#
----
### Requests API

Every single one of the API requests.

* URL/stages
* URL/stage
* URL/stage_teams
* URL/team
* URL/stats















 

