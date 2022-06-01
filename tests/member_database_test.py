from src.member_database import MemberDatabase

def test_メンバーの名前一覧を取得する():
    db = MemberDatabase()
    members = db.get_members()
    assert members[0].name == 'Torikoshi'
    assert members[1].name == 'Segawa'

def test_メンバーのasanaプロジェクトID一覧を取得する():
    db = MemberDatabase()
    members = db.get_members()
    assert members[0].asana_id == 1202070137346385
    assert members[1].asana_id == 1202070137346378