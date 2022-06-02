from src.member_database import MemberDatabase
from src.scrum_master import ScrumMaster
from src.task_storage import FailedTaskStorage
from src.proxy import ProxySwitch

class AsanaAlart():
    def main(self):
        member_database = MemberDatabase()
        members = member_database.get_members()
        task_storage = FailedTaskStorage()
        scrumMaster = ScrumMaster(members, task_storage)
        scrumMaster.start_check_progress_cycle(5)

if __name__ == '__main__':
    proxy = ProxySwitch()

    asana_alart = AsanaAlart()
    asana_alart.main()