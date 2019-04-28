import unittest, requests, json
from env import *


class apiTest(unittest.TestCase):
    def test_sw_api_get(self):
        """ makes a request to api and store data json """
        req = requests.get("https://swapi.co/api/people/")
        json_data = json.loads(req.content)

        try:
            """ Check the API responds correctly """
            self.assertTrue(req.ok)
            self.assertEqual(req.status_code, 200)
            self.assertEqual(str(req.request), "<PreparedRequest [GET]>")

            """ iterate over our data and check that information is present """
            for person in json_data["results"]:
                self.assertTrue(person["name"])
                self.assertTrue(person["height"])
                self.assertTrue(person["mass"])
                self.assertTrue(person["hair_color"])
                assert "https://swapi.co/api/planets" in person["homeworld"]
        except AssertionError:
            raise AssertionError

    def test_pastBin_post(self):
        """ make post to pastBin api"""
        pasteBin_api_url = "https://pastebin.com/api/api_post.php"
        data = {
            'api_dev_key': pasteBin_api,
            'api_option': 'paste',
            'api_paste_code': 'Test_Data',
            'api_paste_format': 'python'
        }
        api_post = requests.post(pasteBin_api_url, data)

        """ validate api POST """
        try:
            self.assertTrue(api_post.ok)
            self.assertEqual(str(api_post.request), "<PreparedRequest [POST]>")
            self.assertEqual(api_post.status_code, 200)
            self.assertEqual(api_post.reason, "OK")

        except AssertionError:
            raise AssertionError


if __name__ == "__name__":
    unittest.main()
