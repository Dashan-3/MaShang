import pytest


def setup_module():
    print('在每个模块之前执行')


def teardown_module():
    print('在每个模块之后执行')


class TestApi:

    def setup_class(self):
        print('在每个类之前执行，创建日志对象（创建多个日志对象，那么日志会出现重复)，创建数据库连接')

    def teardown_class(self):
        print('在每个类之后执行，销毁日志对象，关闭数据库连接')

    def setup(self):
        print('在每个用例之前执行，web自动化：打开浏览器，加载网页，接口自动化：日志开始')

    def teardown_class(self):
        print('在每个用例之后执行，日志结束，关闭浏览器')

    @pytest.mark.smoke
    def test_baidu(self):
        print('百度一下')
        # raise Exception('自定义异常')

    @pytest.mark.productmanage
    def test_sougou(self):
        print('搜狗输入法')

    def test_tengxun(self):
        print('腾讯新闻')