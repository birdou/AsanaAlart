from src.asana import AsanaAPIClient, AsanaSectionNameValidator

def test_セクション名からtoday_todoセクションかどうかを判断する():
    validator = AsanaSectionNameValidator()

    is_today = validator.is_today_task_name("Today's Todo")
    assert is_today == True

    is_today = validator.is_today_task_name("Todo")
    assert is_today == False

def test_タスク名を取得する():
    asana = AsanaAPIClient()
    project_id='1202070137346385'
    tasks = asana.get_today_tasks(project_id)
    task_name = tasks[0].name
    assert task_name == '[院試] 344円切手購入'

def test_タスクの期限に日付のみが指定されている時のタスク期限を取得する():
    asana = AsanaAPIClient()
    project_id='1202070137346385'
    tasks = asana.get_today_tasks(project_id)
    due_on = tasks[0].due_on
    assert due_on.strftime('%Y-%m-%d %H:%M:%S') == '2022-06-04 00:00:00'

def test_タスクの期限が切れているかどうかを判断する():
    asana = AsanaAPIClient()
    project_id='1202070137346385'
    tasks = asana.get_today_tasks(project_id)

    assert tasks[0].is_passed_deadline() == False
