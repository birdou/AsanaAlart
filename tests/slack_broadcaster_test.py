from src.slack import SlackBroadcaster
from src.asana_client import AsanaTask
from src.member_database import Member
import pytest
from src.proxy import ProxySwitch

proxy = ProxySwitch()

@pytest.mark.slack
def test_メッセージ送信後の応答ステータスがokであることを確認する():
    broadcaster = SlackBroadcaster()
    channel_id = 'C03HQJRTXN1'
    message = 'testメッセージ'
    is_ok = broadcaster.broadcast_message(channel_id, message)
    assert is_ok == True

@pytest.mark.slack
def test_メッセージが送信できることを確認する():
    broadcaster = SlackBroadcaster()

    member = Member(0, '田中', '1202070137346385', 'C03HQJRTXN1')
    task = AsanaTask(0, '推薦書を提出する', member, '2021-06-01', None, "Today's Todo", False)
    expected_message = '田中: 「推薦書を提出する」が未完了。Help me!'

    assert broadcaster.broadcaset_alart(task) == expected_message

def test_送信メッセージの内容が次のような形式になっていることを確認する():
    broadcaster = SlackBroadcaster()

    member = Member(0, '田中', '1202070137346385', 'C03HQJRTXN1')
    task = AsanaTask(0, '推薦書を提出する', member, '2021-06-01', None, "Today's Todo", False)
    expected_message = '田中: 「推薦書を提出する」が未完了。Help me!'

    assert broadcaster.create_alart_message(task) == expected_message