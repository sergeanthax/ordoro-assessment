import unittest
import email_transform

class TestGetDistinctEmailAddresses(unittest.TestCase):

    def test_empty_data(self):
        result = email_transform.get_distinct_email_addresses([])

        self.assertEqual(result, [])


    def test_single_email(self):
        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['asdf@asd.com'])


    def test_duplicate_email(self):

        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['asdf@asd.com'])


    def test_multiple_duplicate_emails(self):

        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test@test.com',
                'login_date': '2014-01-24T09:19:49+00:00'
            },
            {
                'email': 'test@test.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['asdf@asd.com', 'test@test.com'])



    def test_empty_email(self):
        test_data = [
            {
                'email': '',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['test@asd.com', 'test2@asd.com'])


    def test_nonetype_email(self):
        test_data = [
            {
                'email': None,
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['test@asd.com', 'test2@asd.com'])


    def test_junk_data_email(self):
        test_data = [
            {
                'email': 'asdasdfasdfrefa',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['test@asd.com', 'test2@asd.com'])


    def test_missing_tld_email(self):
        test_data = [
            {
                'email': 'asasdfasdf@asdf',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_distinct_email_addresses(test_data)

        self.assertEqual(result, ['test@asd.com', 'test2@asd.com'])