from src.scrum_master import ScrumMaster
from src.member_database import MemberDatabase
from src.task_storage import FailedTaskStorage

def test_全員の遅れている今日のスケジュールを取得する():
    memberDB = MemberDatabase()
    members = memberDB.get_members()
    task_storage = FailedTaskStorage()
    master = ScrumMaster(members, task_storage)
    tasks = master.get_all_delayed_tasks()
    assert tasks[0].name == "[院試] 検定料3万振込み"
