from behave import given, when, then
import time
from AppObjects import Notepad


@given('we have behave installed')
def step_impl(context):
    Notepad.start_notepad_app(context)
    time.sleep(5)


@when('we implement a test')
def step_impl2(context):
    time.sleep(2)


@then('behave will test it for us!')
def step_impl3(context):
    time.sleep(3)