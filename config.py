import os

from appium.options.android import UiAutomator2Options
from appium.options.android.common import app
from dotenv import load_dotenv
from selene_in_action import resources

#load_dotenv()


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        load_dotenv('.env.local_emulator')
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', resources.file.abs_path_from_project(os.getenv('APP')))

    if context == 'local_real':
        load_dotenv('.env.local_real')
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', resources.file.abs_path_from_project(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        load_dotenv(dotenv_path=resources.file.abs_path_from_project('.env.credentials'))
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': os.getenv('LOGIN'),
                'accessKey': os.getenv('KEY'),
            },
        )

    return options