from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
import test_swapi_io
import test_api_request

test_swapi = TestLoader().loadTestsFromTestCase(test_swapi_io.swapiTest)
test_request = TestLoader().loadTestsFromTestCase(test_api_request.apiTest)

suite = TestSuite([test_swapi, test_request])

runner = HTMLTestRunner(output='reports', report_title="API Test", combine_reports=True, report_name="API_Tests")

runner.run(suite)