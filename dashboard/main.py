from requests.api import get
import streamlit as st
from streamlit.errors import Error
from data.get import list_of_stages, teams_stages, info_stage, away_stage
import pandas as pd

st.sidebar.title("Detailed Info")
st.title('Eurocup2020')

st.text('A streamlit page to visualize the Eurocup data')

# 2 Columns for stage and home team
column1,column2 = st.columns(2)
with column1:
    st.header("Select the Stage")
    st.image('https://images6.alphacoders.com/312/thumbbig-312319.webp')
    select_stage = st.selectbox("Select the Stage",set([stage["stage"] for stage in list_of_stages()]))
with column2:
    st.subheader("Pick the home team for the stadistics")
    st.image("https://images3.alphacoders.com/657/thumbbig-657637.webp",width=315)

    team = st.selectbox("Select your home-team for the stats",[team["team_name_home"]for team in teams_stages(select_stage)])
    



match = st.sidebar.checkbox("Checkout the list of the games in this stage")
st.sidebar.caption("All the matches in the selected stage with home and away team")
games = list_of_stages(match,select_stage)
if match:
    st.selectbox("Games with home and away teams",games)
st.sidebar.image('https://www.diez.hn/binrepository/951x680/0c0/0d0/none/3014757/GHDU/000-9vg9k3_677991_20220102171136.jpg')


#select_stage = st.selectbox("Select the Stage",set([stage["stage"] for stage in list_of_stages()]))








        
#st.text([elem.values() for elem in list_of_stages(match,select_stage)])

#team = st.selectbox("Select your home-team for the stats",[team["team_name_home"]for team in teams_stages(select_stage)])

# date and list of stats

lst_of_stats = []
for stats in info_stage(select_stage,team):
    for keys, values in stats.items():
        lst_of_stats.append(keys)
    

#Comparaision Columns
def same_stat(*stats):
    count = 0
    for elem in stats:
        if elem[count] == elem[count+1]:
            raise Error("You can't choose the same stat for 2 columns")
            count += 1
column4, column5,column6, column7 = st.columns(4)


with column4:
    first_stadistic = st.selectbox("Select your 1 stadistics",lst_of_stats)
    st.metric(first_stadistic,stats[first_stadistic])
    


with column5:
    second_stadistic = st.selectbox("Select your 2 stadistics",lst_of_stats)
    if second_stadistic != first_stadistic:
        st.metric(second_stadistic,stats[second_stadistic])
    else:
        raise Error("You can't choose the same stadistic")

with column6:
    third_stadistic = st.selectbox("Select your 3 stadistics",lst_of_stats)
    if third_stadistic != second_stadistic:
        st.metric(third_stadistic,stats[third_stadistic])
    else:
        raise Error("You can't choose the same stadistic between pairs ")

with column7:
    fourth_stadistic = st.selectbox("Select your 4 stadistics",lst_of_stats)
    if fourth_stadistic != third_stadistic:
        st.metric(fourth_stadistic,stats[fourth_stadistic])
    else: 
        raise Error("You can't choose the same stadistic between pairs ")











  









