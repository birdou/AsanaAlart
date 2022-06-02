import sys
from member_database import MemberDatabase
from scrum_master import ScrumMaster
from task_storage import FailedTaskStorage

class AsanaAlart():
    def main(self):
        member_database = MemberDatabase()
        members = member_database.get_members()
        task_storage = FailedTaskStorage()
        scrumMaster = ScrumMaster(members, task_storage)
        scrumMaster.start_check_progress_cycle(5)

if __name__ == '__main__':
    sys.path.append('../src')

    asana_alart = AsanaAlart()
    asana_alart.main()