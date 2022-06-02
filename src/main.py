import sys
import os
from . import member_database as md
from . import scrum_master as sm
from . import task_storage as ts

class AsanaAlart():
    def main(self):
        member_database = md.MemberDatabase()
        members = member_database.get_members()
        task_storage = ts.FailedTaskStorage()
        scrumMaster = sm.ScrumMaster(members, task_storage)
        scrumMaster.start_check_progress_cycle(5)

if __name__ == '__main__':
    sys.path.append('../src')
    os.environ['http_proxy'] = 'http://proxy.uec.ac.jp:8080/'
    os.environ['https_proxy'] = 'http://proxy.uec.ac.jp:8080/'

    asana_alart = AsanaAlart()
    asana_alart.main()