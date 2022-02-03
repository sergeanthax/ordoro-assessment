import unittest
import email_transform

class TestGetAprilLogins(unittest.TestCase):

    def test_empty_list(self):
        result = email_transform.get_april_logins([])

        self.assertEqual(result, [])

    def test_no_april_logins(self):
        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-06-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_april_logins(test_data)

        self.assertEqual(result, [])


    def test_one_april_login(self):
        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-01-24T09:19:49+00:00'
            }
        ]


        result = email_transform.get_april_logins(test_data)

        self.assertEqual(result, ['asdf@asd.com'])


    def test_empty_login_date(self):
        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': ''
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_april_logins(test_data)

        self.assertEqual(result, ['test2@asd.com'])


    def test_none_login_date(self):
        test_data = [
            {
                'email': 'asdf@asd.com',
                'login_date': None
            },
            {
                'email': 'test@asd.com',
                'login_date': '2014-05-24T09:19:49+00:00'
            },
            {
                'email': 'test2@asd.com',
                'login_date': '2014-04-24T09:19:49+00:00'
            }
        ]

        result = email_transform.get_april_logins(test_data)

        self.assertEqual(result, ['test2@asd.com'])

