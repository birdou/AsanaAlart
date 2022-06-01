from src.asana import AsanaAPIClient, AsanaSectionNameValidator
from src.member_database import Member

def test_セクション名からtoday_todoセクションかどうかを判断する():
    validator = AsanaSectionNameValidator()

    is_today = validator.is_today_task_name("Today's Todo")
    assert is_today == True

    is_today = validator.is_today_task_name("Todo")
    assert is_today == False

def test_タスク名を取得する():
    asana = AsanaAPIClient()
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    tasks = asana.get_today_tasks(member)
    task_name = tasks[0].name
    assert task_name == '[院試] 344円切手購入'

def test_タスクの期限に日付のみが指定されている時のタスク期限を取得する():
    asana = AsanaAPIClient()
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    tasks = asana.get_today_tasks(member)
    due_on = tasks[0].due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-04 00:00:00'

def test_タスクの期限が切れているかどうかを判断する():
    asana = AsanaAPIClient()
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    tasks = asana.get_today_tasks(member)

    assert tasks[0].is_passed_deadline() == False
