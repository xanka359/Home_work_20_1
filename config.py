import os

import pytest
from dotenv import load_dotenv

@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()

context = os.getenv('context', 'bstack')
bstack_userName = os.getenv('bstack_userName', 'oksanabondareva_4dJCBH')
bstack_accessKey = os.getenv('bstack_accessKey', 'EVxh5GDxEpqoJBmkGytA')

user_name = f"'bstack_userName', {bstack_userName}"
accessKey = f"'bstack_accessKey', {bstack_accessKey}"