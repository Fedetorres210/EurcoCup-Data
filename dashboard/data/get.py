import requests
url = "http://127.0.0.1:8000"

def list_of_stages(teams=False,stage=None):
    q= {'teams': teams,"stage":stage}
    return requests.get(url+"/stages",params=q).json()

def teams_stages(stage):
    q = {
        "stage":stage
    }
    return requests.get(url+"/stage_teams",params=q).json()

def info_stage(stage,home):
    q = {
        "stage":stage,
        "home":home
    }
    return requests.get(url+"/stats",params=q).json()

def away_stage(away):
    q = {
        "away":away
        
    }
    return requests.get(url+"/team",params=q).json()


