
class TestApi1:

    def test_baidu(self, execute_sql, user_login):
        print(f'百度一下：{execute_sql}')
        print(user_login)
        assert '1' in '1234'

    def test_sougou(self):
        print('搜狗输入法')

    def test_tengxun(self):
        print('腾讯新闻')


class TestApi2:

    def test_duo_class(self):
        print('多个类的情况')
