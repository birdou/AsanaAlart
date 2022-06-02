from src.slack import SlackBroadcaster
from src.asana_client import AsanaTask
from src.member_database import Member
import os
from dotenv import load_dotenv
import pytest

load_dotenv()
is_use_proxy = os.getenv('IS_USE_PROXY')
if is_use_proxy == 'True':
    os.environ['http_proxy'] = os.getenv('HTTP_PROXY')
    os.environ['https_proxy'] = os.getenv('HTTPS_PROXY')
else:
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)

@pytest.mark.slack
def test_メッセージ送信後の応答ステータスがokであることを確認する():
    broadcaster = SlackBroadcaster()
    channel_id = 'C03HQJRTXN1'
    message = 'testメッセージ'
    is_ok = broadcaster.broadcast_message(channel_id, message)
    assert is_ok == True

@pytest.mark.slack
def test_送信メッセージの内容が次のような形式になっていることを確認する():
    broadcaster = SlackBroadcaster()

    member = Member(0, '鳥越', '1202070137346385', 'C03HQJRTXN1')
    task = AsanaTask(0, '推薦書を提出する', member, '2021-06-01', None, "Today's Todo")
    expected_message = '[鳥越]: 「推薦書を提出する」が未完了。'

    assert broadcaster.broadcaset_alart(task) == expected_message