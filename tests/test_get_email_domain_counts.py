import unittest
import email_transform

class TestGetEmailDomainCounts(unittest.TestCase):

    def test_with_empty_list(self):
        email_transform.get_email_domain_counts([])


    def test_with_one_email(self):
        test_data = [
            {
                'email': 'asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_email_domain_counts(test_data)

        self.assertEqual(result, {})


    def test_with_multiple_emails(self):
        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'asdf2@asd.com',
                'login_date': '2014-06-24T09:19:49+00:00'
            },
            {
                'email': 'test@gmail.com',
                'login_date': '2014-01-24T09:19:49+00:00'
            },
        ]

        result = email_transform.get_email_domain_counts(test_data)

        self.assertEqual(result, {'asd.com': 2})


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
                'email': 'test3@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_email_domain_counts(test_data)

        self.assertEqual(result, {'asd.com': 3})


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
                'email': 'test3@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_email_domain_counts(test_data)

        self.assertEqual(result, {'asd.com': 3})


    def test_junk_data_email(self):
        test_data = [
            {
                'email': 'asdfeefhasdfh',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test3@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_email_domain_counts(test_data)

        self.assertEqual(result, {'asd.com': 3})


    def test_missing_tld_email(self):
        test_data = [
            {
                'email': 'asdf@asdf',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test3@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_email_domain_counts(test_data)

        self.assertEqual(result, {'asd.com': 3})