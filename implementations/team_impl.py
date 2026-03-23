import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db")
import json, uuid, datetime
from team_base import TeamBase

class TeamAPI(TeamBase):

    def create_team(self, request: str) -> str:
        data = json.loads(request)

        if len(data["name"]) > 64:
            raise Exception("Name too long")

        teams = json.load(open(os.path.join(DB_PATH, "teams.json")))
        open(os.path.join(DB_PATH, "teams.json"))

        if any(t["name"] == data["name"] for t in teams):
            raise Exception("Team exists")

        team = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "description": data["description"],
            "admin": data["admin"],
            "users": [],
            "creation_time": str(datetime.datetime.now())
        }

        teams.append(team)
        json.dump(teams,open(os.path.join(DB_PATH, "teams.json"),"w"))
        

        return json.dumps({"id": team["id"]})

    def list_teams(self) -> str:
        return json.dumps(json.load(open(os.path.join(DB_PATH, "teams.json"))))

    def describe_team(self, request: str) -> str:
        data = json.loads(request)
        teams = json.load(open(os.path.join(DB_PATH, "teams.json")))

        for t in teams:
            if t["id"] == data["id"]:
                return json.dumps(t)

        raise Exception("Team not found")

    def update_team(self, request: str) -> str:
        data = json.loads(request)
        teams = json.load(open(os.path.join(DB_PATH, "teams.json")))

        for t in teams:
            if t["id"] == data["id"]:
                t["name"] = data["team"]["name"]
                t["description"] = data["team"]["description"]

        json.dump(teams,open(os.path.join(DB_PATH, "teams.json"),"w"))
        return json.dumps({"status": "updated"})

    def add_users_to_team(self, request: str):
        data = json.loads(request)
        teams = json.load(open(os.path.join(DB_PATH, "teams.json")))

        for t in teams:
            if t["id"] == data["id"]:
                if len(t["users"]) + len(data["users"]) > 50:
                    raise Exception("Max 50 users allowed")

                t["users"].extend(data["users"])

        json.dump(teams,open(os.path.join(DB_PATH, "teams.json"),"w"))
        return json.dumps({"status": "users added"})

    def remove_users_from_team(self, request: str):
        data = json.loads(request)
        teams = json.load(open(os.path.join(DB_PATH, "teams.json")))

        for t in teams:
            if t["id"] == data["id"]:
                t["users"] = [u for u in t["users"] if u not in data["users"]]

        json.dump(teams,open(os.path.join(DB_PATH, "teams.json"),"w"))
        return json.dumps({"status": "users removed"})

    def list_team_users(self, request: str):
        data = json.loads(request)

        teams = json.load(open(os.path.join(DB_PATH, "teams.json")))
        users = json.load(open(os.path.join(DB_PATH, "users.json")))

        for t in teams:
            if t["id"] == data["id"]:
                return json.dumps([u for u in users if u["id"] in t["users"]])

        raise Exception("Team not found")