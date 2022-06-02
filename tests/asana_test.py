from src.asana_client import AsanaAPIClient, AsanaSectionNameValidator, AsanaTask
from src.member_database import Member
import os
from dotenv import load_dotenv
import pytest

load_dotenv()
is_use_proxy = os.getenv('IS_USE_PROXY')
print(is_use_proxy)
if is_use_proxy == 'True':
    os.environ['http_proxy'] = os.getenv('HTTP_PROXY')
    os.environ['https_proxy'] = os.getenv('HTTPS_PROXY')
else:
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)

def test_セクション名からtoday_todoセクションかどうかを判断する():
    validator = AsanaSectionNameValidator()

    is_today = validator.is_today_task_name("Today's Todo")
    assert is_today == True

    is_today = validator.is_today_task_name("Todo")
    assert is_today == False

@pytest.mark.asana
def test_タスク名を取得する():
    asana = AsanaAPIClient()
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    tasks = asana.get_today_tasks(member)
    task_name = tasks[0].name
    assert task_name == '[院試] 344円切手購入'

@pytest.mark.asana
def test_タスクの期限に日付のみが指定されている時のタスク期限を取得する():
    asana = AsanaAPIClient()
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    tasks = asana.get_today_tasks(member)
    due_on = tasks[0].due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-04 00:00:00'

def test_タスクの期限が切れているかどうかを判断する():
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    task = AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", False)

    assert task.is_passed_deadline() == True

@pytest.mark.asana
def test_遅れている今日のタスク一覧を取得する():
    asana = AsanaAPIClient()
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    tasks = asana.get_today_tasks(member, is_delayed_task_only=True)

    assert tasks[0].name == "[院試] 検定料3万振込み"

def test_タスクが完了していた時に期限が切れているかどうかを判断する():
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')

    task = AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", True)
    assert task.is_passed_deadline() == False

def test_タスクが完了していない時に期限が切れているかどうかを判断する():
    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')

    task = AsanaTask(0, 'テストタスク', member, '2022-06-02', None, "Today's Task", False)
    assert task.is_passed_deadline() == True
