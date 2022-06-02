from src.member_database import MemberDatabase
from src.scrum_master import ScrumMaster
from src.task_storage import FailedTaskStorage

class AsanaAlart():
    def main():
        member_database = MemberDatabase()
        members = member_database.get_members()
        task_storage = FailedTaskStorage()
        scrumMaster = ScrumMaster(members, task_storage)
        scrumMaster.start_check_progress_cycle(5)

if __name__ == '__main__':
    asana_alart = AsanaAlart()
    asana_alart.main()