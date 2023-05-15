from unittest import TestCase
from unittest.mock import patch, mock_open
from datetime import datetime

from util.utils import Utils


class TestUtils(TestCase):

    def setUp(self) -> None:
        self.payload1 = 'RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00'
        self.payload2 = "JHON=10:00-12:00,TH01:00-03:00"
        self.payload3 = "MARIO=SU00:00-23:59"
        self.day_MO = 'MO10:00-12:00'
        self.day_TU = 'TU10:00-12:00'
        self.time1 = '21:00'

    def test_get_days_worked(self):
        expected_output = ['10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00']
        self.assertEqual(Utils.get_days_worked(self.payload1), expected_output)

        expected_output = ['10:00-12:00', 'TH01:00-03:00']
        self.assertEqual(Utils.get_days_worked(self.payload2), expected_output)

        expected_output = ['SU00:00-23:59']
        self.assertEqual(Utils.get_days_worked(self.payload3), expected_output)

    def test_get_name(self):
        expected_output = 'RAMON'
        self.assertEqual(Utils.get_name(self.payload1), expected_output)

        expected_output = 'JHON'
        self.assertEqual(Utils.get_name(self.payload2), expected_output)

        expected_output = 'MARIO'
        self.assertEqual(Utils.get_name(self.payload3), expected_output)

    def test_get_hour_worked_by_day(self):
        expected_output = ['10:00', '12:00']
        self.assertEqual(Utils.get_hour_worked_by_day(self.day_MO), expected_output)

        expected_output = ['10:00', '12:00']
        self.assertEqual(Utils.get_hour_worked_by_day(self.day_TU), expected_output)

    def test_check_extension(self):
        payload = "document.txt"
        self.assertIsNone(Utils.check_extension(payload))

    def test_check_extension_invalid(self):
        payload = "document.pdf"
        self.assertRaises(IOError, Utils.check_extension, payload)

        payload = "image.png"
        self.assertRaises(IOError, Utils.check_extension, payload)

        payload = "data.csv"
        self.assertRaises(IOError, Utils.check_extension, payload)

    @patch('builtins.input', return_value="file.txt")
    @patch('sys.argv', ['main.py', '--path=file.txt'])
    @patch('builtins.open', new_callable=mock_open,
           read_data=f'RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00')
    def test_get_data_from_archive(self, mock_file_open, mock_input):
        expected_path = "file.txt"
        expected_data = ['RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00']

        data = Utils.get_data_from_archive()

        # mock_input.assert_called_once_with("inserte la ruta del archivo de pagos para procesar ")
        mock_file_open.assert_called_once_with(expected_path, 'rt', encoding='UTF-8')
        self.assertEqual(data, expected_data)

    @patch('builtins.input', return_value="file.txt")
    @patch('sys.argv', ['utils.py', '--path=file.txt'])
    @patch('builtins.open', new_callable=mock_open,
           read_data=f'RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00')
    def test_get_data_from_archive_by_sys_argv(self, mock_file_open, mock_input):
        expected_path = "file.txt"
        expected_data = ['RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00']

        data = Utils.get_data_from_archive()

        mock_file_open.assert_called_once_with(expected_path, 'rt', encoding='UTF-8')
        self.assertEqual(data, expected_data)

    def test_get_time(self):
        expected_output = datetime.strptime(self.time1, '%H:%M')
        self.assertEqual(Utils.get_time(self.time1), expected_output)

    def test_get_time_invalid(self):
        payload = "not_a_time"
        expected_output = None
        with self.assertRaises(ValueError):
            Utils.get_time(payload)

    def test_clean_data(self):
        self.fail()

    def test_get_price_per_day(self):
        self.fail()

    def test_format_input(self):
        self.fail()

    def test_get_day_by_str(self):
        self.fail()

    def test_set_time(self):
        self.fail()

    def test_get_worked_time(self):
        self.fail()

    def test_get_price_per_shift(self):
        self.fail()

    def test_get_day_type(self):
        self.fail()

    def test_generate_days_worked(self):
        self.fail()
