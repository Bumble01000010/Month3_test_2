CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT
    )
'''

CREATE_TASKS_TABLE = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        is_done BOOL DEFAULT 0
    )
'''

INSERT_USER = 'INSERT OR IGNORE INTO user (telegram_id, username) VALUES (?, ?)'
GET_USER_BY_TG_ID = 'SELECT * FROM user WHERE telegram_id = ?'

INSERT_TASK = 'INSERT INTO TASKS (task, is_done) VALUES (?, 0)'


GET_ALL_TASKS = 'SELECT id, task, is_done FROM tasks'
UPDATE_TASKS_STATUS = "UPDATE tasks SET is_done = CASE WHEN is_done = 0 THEN 1 ELSE 0 END WHERE id = ?"
MARK_TASK_DONE = "UPDATE tasks SET is_done = 1 WHERE id = ?"
