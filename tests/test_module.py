import unittest
from unittest.mock import patch
import pySimpleSQL  # Replace with the actual name of your library module

class TestDatabaseFunctions(unittest.TestCase):

    @patch('pySimpleSQL.getpass.getpass')  # Mocking getpass
    @patch('builtins.input')  # Mocking input
    def test_setup_database(self, mock_input, mock_getpass):
        # Mock responses for user input
        mock_getpass.return_value = 'test_password'
        mock_input.side_effect = ['test_user', 'test_host', 'test_db']

        pySimpleSQL.setup_database()

        expected_config = {
            'user': 'sql11681093',
            'password': 'jaEdRY336t',
            'host': 'sql11.freesqldatabase.com',
            'database': 'sql11681093',
        }
        self.assertEqual(pySimpleSQL.get_db_config(), expected_config)

    def test_set_db_config(self):
        test_config = {
            'user': 'sql11681093',
            'password': 'jaEdRY336t',
            'host': 'sql11.freesqldatabase.com',
            'database': 'sql11681093',
        }
        pySimpleSQL.set_db_config(test_config)
        self.assertEqual(pySimpleSQL.get_db_config(), test_config)

# Add more tests as needed

if __name__ == '__main__':
    unittest.main()
