from fastapi import APIRouter
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from config.mongo import connection
from bson import json_util
from json import loads

euro = APIRouter()

@euro.get("/stages/{teams}/{stage}")
def all_stages(teams:bool = True,stage=None):
    if teams == True:
        if stage != None:
            results =  connection.databaseEuro2020.EurocupData.find({"stage":stage},{"_id":0,"team_name_home":1,"team_name_away":1})
        else:
          results =  connection.databaseEuro2020.EurocupData.find({},{"_id":0,"team_name_home":1,"team_name_away":1})  

    else:
        results =  connection.databaseEuro2020.EurocupData.find({},{"_id":0,"stage":1})
    return loads(json_util.dumps(results))

@euro.get("/stage/{stage}/{home}/{away}")
def one_stage(stage,home = None,away = None):
    if home and away  != None:
        results = connection.databaseEuro2020.EurocupData.find({"stage":stage,"team_name_home":home,"team_name_away":away},{"_id":0})
        
    elif home == None:
        results = connection.databaseEuro2020.EurocupData.find({"stage":stage,"team_name_away":away},{"_id":0})
    elif away == None:
        results = connection.databaseEuro2020.EurocupData.find({"stage":stage,"team_name_home":home},{"_id":0})
    
    return loads(json_util.dumps(results))

@euro.get("/stage_teams/{stage}")
def stage_teams(stage):
    results =  connection.databaseEuro2020.EurocupData.find({"stage":stage},{"_id":0,"team_name_home":1,"team_name_away":1})
    return loads(json_util.dumps(results))

@euro.get("/stats/{stage}/{home}")
def stats(stage,home):
    results = connection.databaseEuro2020.EurocupData.find({"stage":stage,"team_name_home":home},{"_id":0,"team_name_home":0,"team_name_away":0,"stage":0,"pens":0,})
    return loads(json_util.dumps(results))

