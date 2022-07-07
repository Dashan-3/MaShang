import pytest


@pytest.fixture(scope='function')
def user_login():
    print('用户登录')
