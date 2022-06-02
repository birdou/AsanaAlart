from asana_client import AsanaAPIClient
from slack import SlackBroadcaster
import time

class ScrumMaster():
    def __init__(self, members, task_storage):
        self.members = members
        self.task_storage = task_storage
        self.asanaClient = AsanaAPIClient()
        self.slackBroadcaster = SlackBroadcaster()
    
    def get_all_delayed_tasks(self):
        tasks = []
        for member in self.members:
            tasks = tasks + self.asanaClient.get_today_tasks(member, is_delayed_task_only=True)
        return tasks

    def start_check_progress_cycle(self, interval_minute):
        while(True):
            tasks = self.get_all_delayed_tasks()
            for task in tasks:
                self.deal_with_task_problem(task)
            time.sleep(60*interval_minute)

    def deal_with_task_problem(self, task):
        if self.is_new_delayed_task(task):
            self.slackBroadcaster.broadcaset_alart(task)
            self.task_storage.add_failed_task_id(task.task_id)
        else:
            pass

    def is_new_delayed_task(self, task):
        return not self.task_storage.is_failed_task_id(task.task_id)