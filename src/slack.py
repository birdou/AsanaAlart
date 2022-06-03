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

    def create_alart_message(self, task):
        alart = "%s: 「%s」が未完了。Help me!" % (task.member.name, task.name)
        return alart

    def broadcaset_alart(self, task):
        channel_id = task.member.slack_id
        alart = self.create_alart_message(task)
        self.broadcast_message(channel_id, alart)
        return alart
