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
    message = '<@U02PNA3JPKN> @U02PNA3JPKN>' #'<!channel>'
    # ブラウザ data-message-senderを探せばよい
    is_ok = broadcaster.broadcast_message(channel_id, message)
    assert is_ok == True

import os
from dotenv import load_dotenv
import requests

def broadcast_user_id_list():
    load_dotenv()
    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    url = "https://slack.com/api/users.list"
    headers = {"Authorization": "Bearer " + SLACK_TOKEN}
    CHANNEL = 'C03HQJRTXN1'
    r = requests.post(url, headers=headers)
    response = r.json()
    return response

@pytest.mark.slack
def test_メンバーのユーザーidを取得する():
    res = broadcast_user_id_list()
    print(res)

#@pytest.mark.slack
def test_メッセージが送信できることを確認する():
    broadcaster = SlackBroadcaster()

    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task = AsanaTask(0, '推薦書を提出する', member, '2021-06-01', None, "Today's Todo", False)
    expected_message = '田中: 「推薦書を提出する」が未完了。Help me!'

    assert broadcaster.broadcaset_alart(task) == expected_message

def test_送信メッセージの内容が次のような形式になっていることを確認する():
    broadcaster = SlackBroadcaster()

    member = Member(0, '田中', asana_project_id='1202120929387852', asana_user_id='1202098038140491', slack_id='C03HQJRTXN1')
    task = AsanaTask(0, '推薦書を提出する', member, '2021-06-01', None, "Today's Todo", False)
    expected_message = '田中: 「推薦書を提出する」が未完了。Help me!'

    assert broadcaster.create_alart_message(task) == expected_message