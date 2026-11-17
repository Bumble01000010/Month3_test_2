from db.database import get_db
from db.queries import INSERT_TASK, GET_ALL_TASKS, UPDATE_TASKS_STATUS

def create_task(task: str):
    conn = get_db()
    conn.execute(INSERT_TASK, (task,))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = get_db()
    tasks =conn.execute(GET_ALL_TASKS).fetchall() 
    conn.close()
    return tasks

def toggle_task_status(task_id: int):
    conn = get_db()
    conn.execute(UPDATE_TASKS_STATUS, (task_id,))
    conn.commit()
    conn.close()