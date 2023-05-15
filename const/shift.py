class Constantes:

    @property
    def day(self):
        return 'DAY'

    @property
    def night(self):
        return 'NIGHT'

    @property
    def midnight(self):
        return 'MIDNIGHT'



    @staticmethod
    def midnight_shift() -> dict:
        return {
            'start': 0,
            'end': 9,
            'price': {
                "LV": 25,
                "SD": 30
            }

        }

    @staticmethod
    def day_shift() -> dict:
        return {
            'start': 9,
            'end': 18,
            'price': {
                "LV": 15,
                "SD": 20
            }
        }

    @staticmethod
    def night_shift() -> dict:
        return {
            'start': 18,
            'end': 24,
            'price': {
                "LV": 20,
                "SD": 25
            }
        }
