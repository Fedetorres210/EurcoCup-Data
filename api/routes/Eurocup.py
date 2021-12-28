from fastapi import APIRouter
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from config.mongo import connection
from bson import json_util
from json import loads

euro = APIRouter()

@euro.get("/stages")
def information():
    results =  connection.Mid_project.Eurocup.find({},{"_id":0,"stage":1})
    return loads(json_util.dumps(results))

@euro.get("/stage")
def information(stage):
    results =  connection.Mid_project.Eurocup.find({"stage":stage},{"_id":0})

    return loads(json_util.dumps(results))

@euro.get("/home_teams")
def information():
    results =  connection.Mid_project.Eurocup.find({},{"_id":0,"team_name_home":1,"stage":1})
    return loads(json_util.dumps(results))

@euro.get("/visit_teams")
def information():
    results =  connection.Mid_project.Eurocup.find({},{"_id":0,"team_name_away":1,"stage":1})
    return loads(json_util.dumps(results))


@euro.get("/Home_team")
def information(home_team):
    results =  connection.Mid_project.Eurocup.find({"team_name_home":home_team},{"_id":0})
    return loads(json_util.dumps(results))

@euro.get("/visit_team")
def information(visit_team):
    results =  connection.Mid_project.Eurocup.find({"team_name_away":visit_team},{"_id":0})
    return loads(json_util.dumps(results))