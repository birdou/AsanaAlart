import sys
import os
from dotenv import load_dotenv
from src.member_database import MemberDatabase
from src.scrum_master import ScrumMaster
from src.task_storage import FailedTaskStorage

class AsanaAlart():
    def main(self):
        member_database = MemberDatabase()
        members = member_database.get_members()
        task_storage = FailedTaskStorage()
        scrumMaster = ScrumMaster(members, task_storage)
        scrumMaster.start_check_progress_cycle(5)

if __name__ == '__main__':
    sys.path.append('../src')

    load_dotenv()
    is_use_proxy = os.getenv('IS_USE_PROXY')
    if is_use_proxy == 'True':
        os.environ['http_proxy'] = os.getenv('HTTP_PROXY')
        os.environ['https_proxy'] = os.getenv('HTTPS_PROXY')
    else:
        os.environ.pop('http_proxy', None)
        os.environ.pop('https_proxy', None)

    asana_alart = AsanaAlart()
    asana_alart.main()