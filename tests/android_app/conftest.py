import allure
import pytest
from dotenv import load_dotenv
from selene import browser

from selene_in_action.resources import allure_attachment
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local_emulator",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    dotenv_path = f".env.{context}"

    load_dotenv(dotenv_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    from  config import config_app
    # with allure.step('init app session'):
    options = config_app.to_driver_options(context=context)
    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'),
                                             options=options)

    browser.config.timeout = 10.0

    yield

    allure_attachment.attach_screenshot(browser)

    allure_attachment.attach_xml(browser)

    if context == 'bstack':
        session_id = browser.driver.session_id

        with allure.step('tear down app session with id' + session_id):
            browser.quit()

        allure_attachment.attach_bstack_video(config_app, session_id)

    browser.quit()