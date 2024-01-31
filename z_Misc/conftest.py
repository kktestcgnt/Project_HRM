# Common Fixtures are present here.
import pytest


@pytest.fixture(autouse=True, scope="function")
def display():
    print("call from pytest")





