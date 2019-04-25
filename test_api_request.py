import unittest, requests, json

"""
simple tests to check API calls.
"""


class apiTest(unittest.TestCase):

    def test_api_get(self):
        req = requests.get("https://swapi.co/api/people/")
        json_data = json.loads(req.text)

        """ Check the API responds correctly """
        self.assertEqual(req.status_code, 200)
        self.assertEqual(str(req.request), "<PreparedRequest [GET]>")

        """ Check that data is present in some fields """
        for person in json_data["results"]:
            self.assertTrue(person["name"])
            self.assertTrue(person["height"])
            self.assertTrue(person["mass"])
            self.assertTrue(person["hair_color"])
            assert "https://swapi.co/api/planets" in person["homeworld"]

if __name__ == "__name__":
    unittest.main()
