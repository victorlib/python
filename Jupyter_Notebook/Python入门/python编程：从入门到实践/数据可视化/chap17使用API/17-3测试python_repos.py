import requests
import unittest


class StatusTestCase(unittest.TestCase):
    """测试返回状态码是否正确.py"""

    def test_python_repos(self):
        """能够正确返回Github中python项目吗"""
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)


unittest.main()
