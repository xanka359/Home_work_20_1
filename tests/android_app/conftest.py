import allure
import pytest
from dotenv import load_dotenv
from selene import browser

import config
from selene_in_action.resources import allure_attachment

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local_real",
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
    #with allure.step('init app session'):
    options = config.to_driver_options(context=context)
    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'),
        options=options)

    browser.config.timeout = '10.0'

    # browser.config._wait_decorator = support._logging.wait_with(
    #     context=allure_commons._allure.StepContext
    # )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if context == 'bstack':
        allure_attachment.attach_bstack_video(session_id)