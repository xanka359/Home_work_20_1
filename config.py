import os

from dotenv import load_dotenv

load_dotenv()

context = os.getenv('context', 'bstack')
bstack_userName = os.getenv('LOGIN')
bstack_accessKey = os.getenv('KEY')
