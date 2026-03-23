import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db")
import json, uuid, datetime
from user_base import UserBase

class UserAPI(UserBase):

    def create_user(self, request: str) -> str:
        data = json.loads(request)

        if len(data["name"]) > 64:
            raise Exception("Name too long")

        try:
            users = json.load(open(os.path.join(DB_PATH, "users.json")))
        except:
            users = []

        if any(u["name"] == data["name"] for u in users):
            raise Exception("User already exists")

        user = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "display_name": data["display_name"],
            "creation_time": str(datetime.datetime.now())
        }

        users.append(user)
        json.dump(users,open(os.path.join(DB_PATH, "users.json"),"w"))

        return json.dumps({"id": user["id"]})

    def list_users(self) -> str:
        return json.dumps(json.load(open(os.path.join(DB_PATH, "users.json"))))

    def describe_user(self, request: str) -> str:
        data = json.loads(request)
        users = json.load(open(os.path.join(DB_PATH, "users.json")))

        for u in users:
            if u["id"] == data["id"]:
                return json.dumps(u)

        raise Exception("User not found")

    def update_user(self, request: str) -> str:
        data = json.loads(request)
        users = json.load(open(os.path.join(DB_PATH, "users.json")))

        for u in users:
            if u["id"] == data["id"]:
                u["display_name"] = data["user"]["display_name"]

        json.dump(users, open(os.path.join(DB_PATH, "users.json"),"w"))
        return json.dumps({"status": "updated"})

    def get_user_teams(self, request: str) -> str:
        data = json.loads(request)

        teams = json.load(open("db/teams.json"))

        result = []
        for t in teams:
            if data["id"] in t["users"]:
                result.append(t)

        return json.dumps(result)