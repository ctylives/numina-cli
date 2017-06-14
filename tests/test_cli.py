"""Tests for our main numina CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase
import os
import json

from numina import __version__ as VERSION
from numina.commands import utils 

test_token = os.environ["TEST_TOKEN"]

class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['numina', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)
        self.assertTrue('Options:' in output)
        self.assertTrue('Examples:' in output)

        output = popen(['numina', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)
        self.assertTrue('Options:' in output)
        self.assertTrue('Examples:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['numina', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)

class TestAuthenticate(TestCase):
    def test_authentication_token(self):
        output = popen(['numina', 'authenticate', test_token], stdout=PIPE).communicate()[0]
        self.assertTrue(output.strip() == 'Authentication token has been saved for future use: "' + test_token + '"')
        token_in_file = utils.get_saved_token()
        self.assertTrue(test_token == token_in_file)

class TestUtils(TestCase):
    def test_get_saved_token(self):
        # Assert that the token still matches the value from the previous test
        token_in_file = utils.get_saved_token()
        self.assertTrue(test_token == token_in_file)
        # Assert that changing directories does not break the token, as it gest saved to home
        os.chdir('..')
        token_in_file = utils.get_saved_token()
        self.assertTrue(test_token == token_in_file)
        # Assert that changing directories does not break the token, as it gest saved to home
        os.chdir('./numina-cli')
        token_in_file = utils.get_saved_token()
        self.assertTrue(test_token == token_in_file)

    # def test_if_token_expired(self):
    #     # Test if the server returns an expired status, or response with no text the function returns True
    #     mock_response = { "status" : 'Token is expired'  }
    #     is_expired = utils.check_if_expired(mock_response)
    #     self.assertTrue(is_expired)
    #     mock_response = {}
    #     is_expired = utils.check_if_expired(mock_response)
    #     self.assertTrue(is_expired)

    #     # Test if the response returns a text field thats json parsable, then return false
    #     mock_response['text'] = json.dumps({'result' : 'Success!'})
    #     is_expired = utils.check_if_expired(mock_response)
    #     self.assertFalse(is_expired)

class TestCounts(TestCase):
    def test_failing_to_provide_input(self):
        # Test fail cases for count command
        token_in_file = utils.get_saved_token()
        output = popen(['numina', 'counts', '5840a3f6ffe95e4003030e34'], stdout=PIPE).communicate()[0]
        j_output = json.loads(output)
        self.assertTrue( 'result' in j_output )
        self.assertTrue( 'status' in j_output )
        self.assertTrue( 'code' in j_output )
