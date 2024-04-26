import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene_in_action.resources import file

load_dotenv()

class Config:
    remote_url = os.getenv('REMOTE_URL')
    app_wait_activity = os.getenv('APP_WAIT_ACTIVITY')
    app = os.getenv('APP')
    app_real = os.getenv('APP_REAL')
    device_name = os.getenv('DEVICE_NAME')
    platform_name = os.getenv('PLATFORM_NAME')
    platform_version = os.getenv('PLATFORM_VERSION')
    login = os.getenv('LOGIN')
    key = os.getenv('KEY')
    udid = os.getenv('UDID')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('udid', self.udid)
            options.set_capability('app', file.path(self.app))
            print(self.app)

        if context == 'local_real':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', file.path(self.app_real))

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',
                    'userName': self.login,
                    'accessKey': self.key,
                },
            )

        return options


config_app = Config()

