from infra.config.shift import Constantes
from domain.models.User import User
from application.util.utils import Utils


class Payment:

    @staticmethod
    def process_payment(user: User):
        if user is None:
            raise Exception("usuario no puede ser indefinido")

        total_to_pay = 0
        total_hours_work = 0
        for day in user.get_worked():
            day_hours = Utils.get_worked_time(day, Constantes.day_shift())
            night_hours = Utils.get_worked_time(day, Constantes.night_shift())
            midnight_hours = Utils.get_worked_time(day, Constantes.midnight_shift())

            payment_block_day = Utils.get_price_per_shift(day, Constantes.day)
            payment_block_night = Utils.get_price_per_shift(day, Constantes.night)
            payment_block_midnight = Utils.get_price_per_shift(day, Constantes.midnight)

            produced_day = day_hours * payment_block_day
            produced_night = night_hours * payment_block_night
            produced_midnight = midnight_hours * payment_block_midnight

            total_to_pay += produced_day + produced_night + produced_midnight
            total_hours_work += day_hours + night_hours + midnight_hours

        return total_to_pay
