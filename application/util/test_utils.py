from unittest import TestCase
from unittest.mock import patch, mock_open
from datetime import datetime, timedelta

from domain.const.DaysOfTheWeek import DayOfTheWeekEnum
from infra.config.shift import Constantes
from infra.filemanager import FileManager
from domain.models.day import Day
from application.util.utils import Utils


class TestUtils(TestCase):

    def setUp(self) -> None:
        self.payload1 = 'RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00'
        self.payload2 = "JHON=10:00-12:00,TH01:00-03:00"
        self.payload3 = "MARIO=SU00:00-23:59"
        self.day_MO = 'MO10:00-12:00'
        self.day_TU = 'TU10:00-12:00'
        self.time1 = '21:00'
        self.day_MO_Obj = Day(datetime.now(), datetime.now() + timedelta(hours=3), DayOfTheWeekEnum.MONDAY)
        self.day_SU_Obj = Day(datetime.now(), datetime.now() + timedelta(hours=3), DayOfTheWeekEnum.SUNDAY)

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
    @patch('sys.argv', ['PyPayroll.py', '--path=file.txt'])
    @patch('builtins.open', new_callable=mock_open,
           read_data=f'RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00')
    def test_get_data_from_archive(self, mock_file_open, mock_input):
        expected_path = "file.txt"
        expected_data = ['RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00']

        data = FileManager.get_data_from_archive()

        mock_file_open.assert_called_once_with(expected_path, 'rt', encoding='UTF-8')
        self.assertEqual(data, expected_data)

    @patch('builtins.input', return_value="file.txt")
    @patch('sys.argv', ['utils.py', '--path=file.txt'])
    @patch('builtins.open', new_callable=mock_open,
           read_data=f'RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00')
    def test_get_data_from_archive_by_sys_argv(self, mock_file_open, mock_input):
        expected_path = "file.txt"
        expected_data = ['RAMON=10:00-12:00,TU10:00-12:00,TH01:00-03:00']

        data = FileManager.get_data_from_archive()

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
        dirty = ["data1\n", "data2\n", "data3\n"]
        expected_output = ["data1", "data2", "data3"]
        self.assertEqual(Utils.clean_data(dirty), expected_output)

    def test_get_price_per_day(self):
        expected_output = 15
        price = Utils.get_price_per_day(self.day_MO_Obj, Constantes.day_shift())
        self.assertEqual(price, expected_output)

    def test_format_input(self):
        payload = 'MO03:00-13:00'
        expected_output = ['03:00', '13:00']
        formatted_input = Utils.format_input(payload)
        self.assertEqual(formatted_input, expected_output)

    def test_get_day_by_str_monday(self):
        payload = 'MO'
        expected_output = DayOfTheWeekEnum.MONDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_tuesday(self):
        payload = 'TU'
        expected_output = DayOfTheWeekEnum.TUESDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_wednesday(self):
        payload = 'WE'
        expected_output = DayOfTheWeekEnum.WENDSDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_thursday(self):
        payload = 'TH'
        expected_output = DayOfTheWeekEnum.THURSDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_friday(self):
        payload = 'FR'
        expected_output = DayOfTheWeekEnum.FRIDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_saturday(self):
        payload = 'SA'
        expected_output = DayOfTheWeekEnum.SATURDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_sunday(self):
        payload = 'SU'
        expected_output = DayOfTheWeekEnum.SUNDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_get_day_by_str_default(self):
        payload = 'XX'
        expected_output = DayOfTheWeekEnum.MONDAY
        day = Utils.get_day_by_str(payload)
        self.assertEqual(day, expected_output)

    def test_set_time(self):
        payload = 10
        expected_output = datetime.strptime('10', '%H')
        time = Utils.set_time(payload)
        self.assertEqual(time, expected_output)

    def test_set_time_midnight(self):
        payload = 24
        expected_output = datetime.strptime('23:59', '%H:%M')
        time = Utils.set_time(payload)
        self.assertEqual(time, expected_output)

    def test_set_time_invalid_type(self):
        payload = "HOLA"
        with self.assertRaises(ValueError):
            Utils.set_time(payload)

    def test_get_price_per_shift_day_LV(self):
        shift = Constantes.day
        expected_output = Constantes.day_shift()['price'][Utils.get_day_type(self.day_MO_Obj)]
        price = Utils.get_price_per_shift(self.day_MO_Obj, shift)
        self.assertEqual(price, expected_output)

    def test_get_price_per_shift_night_LV(self):
        shift = Constantes.night
        expected_output = Constantes.night_shift()['price'][Utils.get_day_type(self.day_MO_Obj)]
        price = Utils.get_price_per_shift(self.day_MO_Obj, shift)
        self.assertEqual(price, expected_output)

    def test_get_price_per_shift_midnight_LV(self):
        shift = Constantes.midnight
        expected_output = Constantes.midnight_shift()['price'][Utils.get_day_type(self.day_MO_Obj)]
        price = Utils.get_price_per_shift(self.day_MO_Obj, shift)
        self.assertEqual(price, expected_output)

    def test_get_price_per_shift_day_SD(self):
        shift = Constantes.day
        expected_output = Constantes.day_shift()['price'][Utils.get_day_type(self.day_SU_Obj)]
        price = Utils.get_price_per_shift(self.day_SU_Obj, shift)
        self.assertEqual(price, expected_output)

    def test_get_price_per_shift_night_SD(self):
        shift = Constantes.night
        expected_output = Constantes.night_shift()['price'][Utils.get_day_type(self.day_SU_Obj)]
        price = Utils.get_price_per_shift(self.day_SU_Obj, shift)
        self.assertEqual(price, expected_output)

    def test_get_price_per_shift_midnight_SD(self):
        shift = Constantes.midnight
        expected_output = Constantes.midnight_shift()['price'][Utils.get_day_type(self.day_SU_Obj)]
        price = Utils.get_price_per_shift(self.day_SU_Obj, shift)
        self.assertEqual(price, expected_output)

    def test_get_day_type(self):
        payload = Day(datetime.now(), datetime.now() + timedelta(hours=3), DayOfTheWeekEnum.MONDAY)
        expected_output = "LV"
        day_type = Utils.get_day_type(payload)
        self.assertEqual(day_type, expected_output)

        payload = Day(datetime.now(), datetime.now() + timedelta(hours=3), DayOfTheWeekEnum.SUNDAY)
        expected_output = "SD"
        day_type = Utils.get_day_type(payload)
        self.assertEqual(day_type, expected_output)
