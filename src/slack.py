from numpy import broadcast
import requests
from dotenv import load_dotenv
import os

class SlackBroadcaster():
    def __init__(self):
        load_dotenv()
        self.SLACK_TOKEN = os.getenv('SLACK_TOKEN')
        self.url = "https://slack.com/api/chat.postMessage"
        self.headers = {"Authorization": "Bearer " + self.SLACK_TOKEN}
        CHANNEL = 'C03HQJRTXN1'

    def broadcast_message(self, channel_id, message):
        data  = {
        'channel': channel_id,
        'text': message
        }
        r = requests.post(self.url, headers=self.headers, data=data)
        response = r.json()
        is_ok = response['ok']
        return is_ok

    def broadcaset_alart(self, task):
        alart = "[%s]: 「%s」が未完了。" % (task.member.name, task.name)
        channel_id = task.member.slack_id
        self.broadcast_message(channel_id, alart)
        return alart
