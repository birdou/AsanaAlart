from src.task_storage import FailedTaskStorage

def test_タスクをデータベースに追加_削除する間にタスクの有り無しの出力が変化することを確認する():
    storage = FailedTaskStorage()
    task_id = 132132133
    storage.add_failed_task_id(task_id)
    assert storage.is_failed_task_id(task_id) == True
    storage.remove_failed_task_id(task_id)
    assert storage.is_failed_task_id(task_id) == False

def test_タスクが完了のときにタスクストレージからが削除されることを確認する():
    storage = FailedTaskStorage()
    task_id = 132132133
    storage.add_failed_task_id(task_id)
    assert storage.is_failed_task_id(task_id) == True
    storage.remove_done_tasks()
    assert storage.is_failed_task_id(task_id) == True
    storage.set_done_labels()
    storage.set_undone_label(task_id)
    storage.remove_done_tasks()
    assert storage.is_failed_task_id(task_id) == True
    storage.set_done_labels()
    storage.remove_done_tasks()
    assert storage.is_failed_task_id(task_id) == False