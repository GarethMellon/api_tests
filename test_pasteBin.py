import requests, unittest
import env


class PasteBinTest(unittest.TestCase):
    def test_post(self):
        """ set up a test post to the pastebin api"""
        pasteBin_api = "https://pastebin.com/api/api_post.php"

        header = {"Content-Type": "application/json; charset=utf8"}
        params = {"api_dev_key": env.pasteBin_api, "api_user_name": env.username, "api_user_password": env.pasteBin_api,
                  'api_option': 'paste', 'api_paste_format': 'python', 'api_paste_code': 'This is a test post'}

        r = requests.post(pasteBin_api, params, header)

        """ check the API responded as we expect it to """
        try:
            self.assertTrue(r.ok)
            self.assertEqual(r.request.method, "POST")
            self.assertEqual(r.status_code, 200)
        except AssertionError:
            raise AssertionError


if __name__ == "__main__":
    unittest.main()
