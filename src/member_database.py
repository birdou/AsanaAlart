import sqlite3

class MemberDatabase():
    def __init__(self):        
        self.dbname = '../resources/asana_alart.db'
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS member(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, asana_project_id STRING, slack_channel_id STRING)')
        conn.commit()
        conn.close()

    def get_members(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM member')

        member_datas = cur.fetchall()
        members = []
        for member_data in member_datas:
            user_id = member_data[0]
            name = member_data[1]
            asana_id = member_data[2]
            slack_id = member_data[3]
            member = Member(user_id, name, asana_id, slack_id)
            members.append(member)
        conn.close()
        return members


class Member():
    def __init__(self, user_id, name, asana_id, slack_id):
        self.user_id = user_id
        self.name = name
        self.asana_id = asana_id
        self.slack_id = slack_id

    def __str__(self):
        return self.name
