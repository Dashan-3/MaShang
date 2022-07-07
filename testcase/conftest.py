import pytest


def read_yaml():
    return ['张三', '李四', '王二']


@pytest.fixture(scope='session', autouse=True)
def execute_sql():
    print('执行数据库的验证，查询数据库。')
    yield
    print('关闭数据库链接')


# @pytest.fixture(scope='function', params=read_yaml())
# def execute_sql(request):
#     print(request.param)
#     print('执行数据库的验证，查询数据库。')
#     yield request.param
#     print('关闭数据库链接')
