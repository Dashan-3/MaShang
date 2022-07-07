import pytest

class TestApi:

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_baidu(self):
        print('百度一下')
        # raise Exception('自定义异常')


    @pytest.mark.skip(reason = '无条件跳过' )
    @pytest.mark.run(order=1)
    @pytest.mark.productmanage
    def test_sougou(self):
        print('搜狗输入法')

    @pytest.mark.run(order=2)
    def test_tengxun(self):
        print('腾讯新闻')



