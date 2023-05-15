"""
    calculadora para determinar el salario de un empleado basado en bloques de jornadas con diferentes y
    pagos por hora de jornada y dia de la jornada
"""
import logging
from util.utils import Utils
from models.User import User
from models.day import Day
from payment.Payment import Payment


def main():
    archive = Utils.get_data_from_archive()
    data = Utils.clean_data(archive)
    for user in data:
        user_name = Utils.get_name(user)
        days: list[Day] = Utils.generate_days_worked(Utils.get_days_worked(user))
        user_instance = User(user_name, days)
        payment = Payment.process_payment(user_instance)
        print(f"EL monto a para a {user_instance.get_name()} es : {'{:.2f}'.format(payment)} USD")


if __name__ == '__main__':
    main()
