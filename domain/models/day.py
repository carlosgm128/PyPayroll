from datetime import datetime

from domain.const.DaysOfTheWeek import DayOfTheWeekEnum


class Day:
    def __init__(self, start: datetime, end: datetime, day: DayOfTheWeekEnum) -> None:
        self.__start = start
        self.__end = end
        self.__name = day

    def get_day(self) -> DayOfTheWeekEnum:
        return self.__name.value

    def get_start(self) -> datetime:
        return self.__start

    def get_end(self):
        return self.__end

    def set_start(self, new_start: datetime) -> datetime:
        if self.__start >= self.__end:
            raise Exception("Asignacion invalida de la hora de inicio de jornada")
        else:
            self.__start == new_start

    def set_end(self, new_end: datetime) -> datetime:
        if self.__end <= self.__start:
            raise Exception("Asignacion invalida de la hora de finalizacion de jornada")
        else:
            self.__end = new_end
