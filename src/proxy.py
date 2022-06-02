import os
from dotenv import load_dotenv

class ProxySwitch():
    def __init__(self):
        self.set_up()
        
    def set_up(self):
        load_dotenv()
        is_use_proxy = os.getenv('IS_USE_PROXY')
        if is_use_proxy == 'True':
            self.turn_on_proxy(os.getenv('HTTP_PROXY'), os.getenv('HTTPS_PROXY'))
        else:
            self.turn_off_proxy()

    def turn_on_proxy(self, http_proxy, https_proxy):
        os.environ['http_proxy'] = http_proxy
        os.environ['https_proxy'] = https_proxy
    
    def turn_off_proxy(self):
        os.environ.pop('http_proxy', None)
        os.environ.pop('https_proxy', None)
