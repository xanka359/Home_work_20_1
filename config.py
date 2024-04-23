import os

from appium.options.android.common import app
from dotenv import load_dotenv
from selene.support.shared import config
from selene_in_action import resources, utils

load_dotenv()

#context = os.getenv('context', 'bstack')
bstack_userName = os.getenv('LOGIN')
bstack_accessKey = os.getenv('KEY')
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723/wd/hub')
deviceName = os.getenv('deviceName')
app = os.getenv('app', './app-alpha-universal-release.apk')
appWaitActivity = os.getenv('AppWaitActivity', 'org.wikipedia.*')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'

def to_driver_options():
    from appium.options.android import UiAutomator2Options
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or runs_on_bstack)
        else resources.file.abs_path_from_project(app)
    ))

    if runs_on_bstack:
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options