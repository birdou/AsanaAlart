from src.asana_client import AsanaAPIClient, AsanaSectionNameValidator, AsanaTask
from src.member_database import Member
import pytest
from src.proxy import ProxySwitch
import json

proxy = ProxySwitch()

def test_セクション名からtoday_todoセクションかどうかを判断する():
    validator = AsanaSectionNameValidator()

    is_today = validator.is_today_task_name("Today's Todo")
    assert is_today == True

    is_today = validator.is_today_task_name("Todo")
    assert is_today == False

@pytest.mark.asana
def test_asanaサーバーから応答があるかをテストする():
    asana = AsanaAPIClient()
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    try:
        tasks = asana.get_today_tasks(member)
    except:
        assert False

def test_タスク名を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", False)
    task_name = task.name
    assert task_name == 'テストタスク'

def test_タスクの期限に日付のみが指定されている時のタスク期限を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", False)
    due_on = task.due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-03 13:00:00'

def test_タスクの期限に時刻指定されている時のタスク期限を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-07-07', '2022-07-07T04:00:00.000Z', "Today's Task", False)
    due_on = task.due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-07-07 13:00:00'

def test_タスクの期限に時刻指定されていなくて金曜日の時のタスク期限を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-06-10', None, "Today's Task", False)
    due_on = task.due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-13 13:00:00'

def test_タスクの期限に時刻指定されていなくて日曜日の時のタスク期限を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-06-12', None, "Today's Task", False)
    due_on = task.due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-13 13:00:00'

def test_タスクの期限に時刻指定されていなくて月曜日の時のタスク期限を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-06-13', None, "Today's Task", False)
    due_on = task.due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-14 13:00:00'

def test_タスクの期限に時刻指定されていて金曜日の時のタスク期限を取得する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task= AsanaTask(0, 'テストタスク', member, '2022-06-10', '2022-06-10T05:00:00.000Z', "Today's Task", False)
    due_on = task.due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-10 14:00:00'

def test_タスクの期限が切れているかどうかを判断する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    
    task = AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", False)
    assert task.is_passed_deadline() == True

@pytest.mark.asana
def test_遅れている今日のタスク一覧を取得する():
    asana = AsanaAPIClient()
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    tasks = asana.get_today_tasks(member, is_delayed_task_only=True)

    assert tasks[0].name == "[院試] 検定料3万振込み"

def test_タスクが完了していた時に期限が切れているかどうかを判断する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    
    task = AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", True)
    assert task.is_passed_deadline() == False

def test_タスクが完了していない時に期限が切れているかどうかを判断する():
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    
    task = AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", False)
    assert task.is_passed_deadline() == True

def test_担当者を取得する():
    task_json = '{"gid": "1202335027082060", "assignee": {"gid": "1202048128573552", "resource_type": "user"}, "completed": false, "due_at": null, "due_on": null, "memberships": [{"section": {"gid": "1202120929387868", "name": "To-Do"}}, {"section": {"gid": "1202070137346379", "name": "To-Do"}}], "name": "1章の本文を書く 参考文献を探す", "start_on": null}'
    task_dict = json.loads(task_json)
    asana = AsanaAPIClient()
    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task = asana.convert2task(task_dict, member, "Today's task")
    assert task.member.name == '瀨川'
