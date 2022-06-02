import sqlite3
from pathlib import Path

class FailedTaskStorage():
    def __init__(self):        
        self.dbname = str(Path(__file__).resolve().parents[1] / 'resources/asana_alart.db')
        print(self.dbname)
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS failed_tasks(task_id INTEGER PRIMARY KEY, is_done INTEGER)')
        conn.commit()
        conn.close()

    def add_failed_task_id(self, task_id):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = """
        insert into failed_tasks (task_id, is_done)
        select ?, ?
        where NOT EXISTS (select 1 from failed_tasks where task_id=?)
        """
        data = (task_id, 0, task_id)
        cur.execute(sql, data)

        conn.commit()
        conn.close

    def is_failed_task_id(self, task_id):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'SELECT * FROM failed_tasks WHERE task_id = ? LIMIT 1'
        data = (task_id,)
        cur.execute(sql, data)

        conn.close

        result = cur.fetchall()
        return len(result) == 1

    def remove_failed_task_id(self, task_id):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'DELETE FROM failed_tasks WHERE task_id = ?'
        data = (task_id,)
        cur.execute(sql, data)

        conn.commit()
        conn.close
    
    def set_done_labels(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'UPDATE failed_tasks SET is_done = 1'
        cur.execute(sql)

        conn.commit()
        conn.close

    def set_undone_label(self, task_id):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'UPDATE failed_tasks SET is_done = 0 WHERE task_id = ?'
        data = (task_id,)
        cur.execute(sql, data)

        conn.commit()
        conn.close
    
    def remove_done_tasks(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'DELETE FROM failed_tasks WHERE is_done = 1'
        cur.execute(sql)

        conn.commit()
        conn.close

