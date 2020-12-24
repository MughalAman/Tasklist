import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM tasks")
        rows = self.cur.fetchall()
        return rows

    def insert(self, task):
        self.cur.execute("INSERT INTO tasks VALUES (NULL, ?)", (task,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, task):
        self.cur.execute("UPDATE tasks SET task = ? WHERE id = ?",
                         (task, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
