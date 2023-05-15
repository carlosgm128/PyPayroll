from domain.models.day import Day


class User:

    def __init__(self, name: str, worked: list[Day]) -> None:
        self.__name = name
        self.__worked = worked

    def get_name(self) -> str:
        return self.__name

    def get_worked(self) -> list[Day]:
        return self.__worked
