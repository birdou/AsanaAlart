import asana
import datetime
from dotenv import load_dotenv
import os

from src.member_database import MemberDatabase

class AsanaAPIClient():
    def __init__(self):
        load_dotenv()
        PERSONAL_ACCESS_TOKEN=os.getenv('PERSONAL_ACCESS_TOKEN')
        self.client = asana.Client.access_token(PERSONAL_ACCESS_TOKEN)
        self.section_validator = AsanaSectionNameValidator()

        self.member_db = MemberDatabase()

    def get_tasks_json(self, project_id):
        tasks = self.client.tasks.get_tasks(
            {
                'opt_fields' : [
                    'this.name', 
                    'this.due_on',
                    'this.due_at',
                    'this.start_on',
                    'this.memberships.section.name',
                    'this.completed',
                    'this.assignee',
                ],
                'project': project_id
            }
        )
        return tasks

    def get_today_tasks(self, member, is_delayed_task_only=False):
        project_id = member.asana_project_id
        tasks_json = self.get_tasks_json(project_id)
        tasks = []
        for task_json in tasks_json:
            section = task_json['memberships'][0]['section']['name']
            if self.section_validator.is_today_task_name(section):
                task = self.convert2task(task_json, member, section)
                if is_delayed_task_only:
                    if task.is_passed_deadline():
                        tasks.append(task)
                else:
                    tasks.append(task)
        return tasks

    def convert2task(self, task_json, project_member, section):
        task_id = task_json['gid']
        name = task_json['name']
        due_on = task_json['due_on']
        due_at = task_json['due_at']
        is_completed = task_json['completed']
        try:
            assignee_id = int(task_json['assignee']['gid'])
            member = self.member_db.get_member(assignee_id)
            if member is None:
                member = project_member
        except TypeError:
            member = project_member
        task = AsanaTask(task_id, name, member, due_on, due_at, section, is_completed) 
        return task

class AsanaTask():
    def __init__(self, task_id, name, member, due_on, due_at, section, is_completed):
        self.task_id = task_id
        self.name = name
        self.member = member
        self.due_on = self.convert2datetime(due_on, due_at)
        self.section = section
        self.is_completed = is_completed

    def convert2datetime(self, due_on, due_at):
        if due_on is None:
            # 日付が設定されていない場合
            date = datetime.datetime.max
        else:
            if due_at is None:
                # 日付のみが期限に設定されている場合
                date = datetime.datetime.strptime(due_on, '%Y-%m-%d')
                weekday = date.weekday()
                days = 1
                # 金曜日から日曜日の場合
                if 4 <= weekday: 
                    days = 7 - weekday
                # 翌日の13時が期限に設定されるようにした
                date = date + datetime.timedelta(days=days) + datetime.timedelta(hours=13)
            else:
                # 時刻まで期限に設定されている場合
                date = datetime.datetime.strptime(due_at, '%Y-%m-%dT%H:%M:%S.000Z')
                # 時差を考慮。サマータイムは考慮していない
                date = date + datetime.timedelta(hours=9)
        return date

    def is_passed_deadline(self):
        if self.is_completed:
            return False
        now = datetime.datetime.now()
        return self.due_on < now

class AsanaSectionNameValidator():
    def is_today_task_name(self, section_name):
        return 'today' in section_name.lower()