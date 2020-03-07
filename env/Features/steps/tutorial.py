from behave import given, when, then
from pywinauto.application import Application
import time


@given('we have behave installed')
def step_impl(context):
    Application(backend="uia").start('notepad.exe')
    time.sleep(10)


@when('we implement a test')
def step_impl2(context):
    time.sleep(2)


@then('behave will test it for us!')
def step_impl3(context):
    time.sleep(3)
