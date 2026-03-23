
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db")
import json, uuid, datetime, os
from project_board_base import ProjectBoardBase

class BoardAPI(ProjectBoardBase):

    def create_board(self, request: str):
        data = json.loads(request)

        boards = json.load(open(os.path.join(DB_PATH, "boards.json")))

        for b in boards:
            if b["name"] == data["name"] and b["team_id"] == data["team_id"]:
                raise Exception("Board exists")

        board = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "description": data["description"],
            "team_id": data["team_id"],
            "status": "OPEN",
            "creation_time": data["creation_time"]
        }

        boards.append(board)
        json.dump(boards, open(os.path.join(DB_PATH, "boards.json"),"w"))

        return json.dumps({"id": board["id"]})

    def add_task(self, request: str) -> str:
        data = json.loads(request)

        tasks = json.load(open(os.path.join(DB_PATH, "tasks.json")))
        

        task = {
            "id": str(uuid.uuid4()),
            "title": data["title"],
            "description": data["description"],
            "user_id": data["user_id"],
            "board_id": data["board_id"],   # ✅ ADD THIS
            "status": "OPEN"
        }

        tasks.append(task)
        json.dump(tasks, open(os.path.join(DB_PATH, "tasks.json"),"w"))
        

        return json.dumps({"id": task["id"]})

    def update_task_status(self, request: str):
        data = json.loads(request)
        tasks = json.load(open(os.path.join(DB_PATH, "tasks.json")))

        for t in tasks:
            if t["id"] == data["id"]:
                t["status"] = data["status"]

        json.dump(tasks, open(os.path.join(DB_PATH, "tasks.json"),"w"))
        return json.dumps({"status": "updated"})

    def close_board(self, request: str) -> str:
        data = json.loads(request)

        boards = json.load(open(os.path.join(DB_PATH, "boards.json")))
        tasks = json.load(open(os.path.join(DB_PATH, "tasks.json")))

        for b in boards:
            if b["id"] == data["id"]:

                # ✅ Only check tasks of THIS board
                if any(t["status"] != "COMPLETE" and t["board_id"] == b["id"] for t in tasks):
                    raise Exception("All tasks must be complete")

                b["status"] = "CLOSED"
                b["end_time"] = str(datetime.datetime.now())

        json.dump(boards, open(os.path.join(DB_PATH, "boards.json"),"w"))
        return json.dumps({"status": "closed"})

    def list_boards(self, request: str) -> str:
        data = json.loads(request)
        boards = json.load(open(os.path.join(DB_PATH, "boards.json")))

        return json.dumps([
            {"id": b["id"], "name": b["name"]}
            for b in boards if b["team_id"] == data["id"] and b["status"] == "OPEN"
        ])

    def export_board(self, request: str) -> str:
        data = json.loads(request)

        boards = json.load(open(os.path.join(DB_PATH, "boards.json")))
        tasks = json.load(open(os.path.join(DB_PATH, "tasks.json")))

        for b in boards:
            if b["id"] == data["id"]:
                filename = f"out/board_{b['id']}.txt"

                with open(filename, "w") as f:
                    f.write(f"Board: {b['name']}\n")
                    f.write(f"Description: {b['description']}\n\n")
                    f.write("Tasks:\n")

                    for t in tasks:
                        f.write(f"- {t['title']} [{t['status']}]\n")

                return json.dumps({"out_file": filename})

        raise Exception("Board not found")


