from datetime import datetime

from infra.config.shift import Constantes
from domain.const.DaysOfTheWeek import DayOfTheWeekEnum
from domain.models.day import Day


class Utils:

    @staticmethod
    def get_days_worked(payload: str):
        """
            return a list of days worked
        """
        return payload.rsplit("=")[1].rsplit(',')

    @staticmethod
    def get_name(payload):
        """
            return the name of the user
        """
        return payload.rsplit('=')[0]

    @staticmethod
    def get_hour_worked_by_day(payload):
        """
            method to tread a payload and separate working hours:
            expected: MO09:00-17:00,TU09:00-17:00,FR09:00-17:00,SA09:00-17:00,SU09:00-17:00
        """
        return payload[2:].rsplit('-')

    @staticmethod
    def check_extension(payload):
        """
            check file extension otherwise raise an exception
        """
        if '.txt' not in payload:
            raise IOError("extencion invalida de archivo, solo soportada .txt")

    @staticmethod
    def get_time(payload):
        """
            function to convert a string into a date time
            Input example 21:00
        """
        try:
            return datetime.strptime(str(payload), '%H:%M')
        except ValueError:
            raise ValueError(f'conversion erronea de: {payload}')

    @staticmethod
    def clean_data(payload: list[str]) -> list[str]:
        """
            method created to clean '\\n' from the archive read
        """
        res = []
        for sub in payload:
            res.append(sub.replace("\n", ""))
        return res

    @staticmethod
    def get_price_per_day(payload: str, shift: dict) -> str:
        """
            method created to received price depending on the day schema set up
            payload expected is
            shift expected format is {
                        'start': 9,
                        'end': 18,
                        'price': {
                            "LV": 15,
                            "SD": 20
                        }
                    }
        """
        day_type = Utils.get_day_type(payload)
        return shift['price'][day_type]

    @staticmethod
    def format_input(payload):
        """
            formatter input type must be in this format 'MO03:00-13:00'
        """
        start = payload[2:].rsplit('-')[0]
        end = payload[2:].rsplit('-')[1]
        return [start, end]

    @staticmethod
    def get_day_by_str(payload: str) -> DayOfTheWeekEnum:
        match payload[:2]:
            case 'MO':
                return DayOfTheWeekEnum.MONDAY
            case 'TU':
                return DayOfTheWeekEnum.TUESDAY
            case 'WE':
                return DayOfTheWeekEnum.WENDSDAY
            case 'TH':
                return DayOfTheWeekEnum.THURSDAY
            case 'FR':
                return DayOfTheWeekEnum.FRIDAY
            case 'SA':
                return DayOfTheWeekEnum.SATURDAY
            case 'SU':
                return DayOfTheWeekEnum.SUNDAY
            case _:
                print("No se ha podido determinar el dia de la semana, por defecto Lunes sera asignado")
                return DayOfTheWeekEnum.MONDAY

    @staticmethod
    def set_time(payload: str) -> datetime:
        """
            create a time based on int hour provided
            espected payload format is 10:00
        """
        try:
            if type(payload) != int:
                raise ValueError("type provided not supported")
            if payload == 24:
                return datetime.strptime('23:59', '%H:%M')
            return datetime.strptime(str(payload), '%H')
        except ValueError:
            raise ValueError(f"Hora invalida proporcionada {payload}")

    @staticmethod
    def get_worked_time(payload: Day, shift: dict):
        start: datetime = Utils.set_time(shift['start'])
        end: datetime = Utils.set_time(shift['end'])
        worked_start: datetime = payload.get_start()
        worked_end: datetime = payload.get_end()

        if start > worked_start:
            worked_start = start

        if worked_end > end:
            worked_end = end

        delta = worked_end - worked_start
        hours = delta.total_seconds() / 3600

        if hours <= 0:
            return 0

        return hours

    @staticmethod
    def get_price_per_shift(payload: Day, shift: property):
        str_pay_block = Utils.get_day_type(payload)
        if Constantes.day == shift:
            return Constantes.day_shift()['price'][str_pay_block]
        elif Constantes.night == shift:
            return Constantes.night_shift()['price'][str_pay_block]
        elif Constantes.midnight == shift:
            return Constantes.midnight_shift()['price'][str_pay_block]
        else:
            raise Exception("No se pudo determinar el precio por type de jornada laboral")

    @staticmethod
    def get_day_type(payload: Day) -> str:
        if payload.get_day() == DayOfTheWeekEnum.SATURDAY.value or payload.get_day() == DayOfTheWeekEnum.SUNDAY.value:
            return "SD"
        else:
            return "LV"

    @staticmethod
    def generate_days_worked(payload: list[str]) -> list[Day]:
        days_out: list[Day] = []
        for day in payload:
            str_date_formatted = Utils.format_input(day)
            start = Utils.get_time(str_date_formatted[0])
            end = Utils.get_time(str_date_formatted[1])
            current = Day(start, end, Utils.get_day_by_str(day))
            days_out.append(current)
        return days_out
