from src.member_database import MemberDatabase

def test_メンバーの名前一覧を取得する():
    db = MemberDatabase()
    members = db.get_members()
    assert members[1].name == '伊藤'
    assert members[5].name == '田中'

def test_メンバーのasanaプロジェクトID一覧を取得する():
    db = MemberDatabase()
    members = db.get_members()
    assert members[0].asana_project_id == 1202070137346385
    assert members[1].asana_project_id == 1202120929387877

def test_asana_user_idを取得する():
    db = MemberDatabase()
    members = db.get_members()
    assert members[0].asana_user_id == 1202070004740146
    assert members[1].asana_user_id == 1202106958339202