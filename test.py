from implementations.user_impl import UserAPI
from implementations.team_impl import TeamAPI
from implementations.board_impl import BoardAPI

import json, datetime

u = UserAPI()
t = TeamAPI()
b = BoardAPI()

# create user
user = json.loads(u.create_user('{"name":"chirag","display_name":"Chirag"}'))
user_id = user["id"]

# create team
team = json.loads(t.create_team(f'{{"name":"team1","description":"test","admin":"{user_id}"}}'))
team_id = team["id"]

# create board
board = json.loads(b.create_board(json.dumps({
    "name": "board1",
    "description": "test board",
    "team_id": team_id,
    "creation_time": str(datetime.datetime.now())
})))

print("Board created:", board)

# add task
task = json.loads(b.add_task(json.dumps({
    "title": "Task1",
    "description": "First Task",
    "user_id": user_id,
    "board_id": board["id"],
    "creation_time": str(datetime.datetime.now())
})))

task_id = task["id"]
print("Task created:", task)

# complete task
b.update_task_status(json.dumps({
    "id": task_id,
    "status": "COMPLETE"
}))

# close board
res = b.close_board(json.dumps({
    "id": board["id"]
}))

print("Board closed:", res)

# export board
export = b.export_board(json.dumps({
    "id": board["id"]
}))

print(export)