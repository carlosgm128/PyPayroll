"""
    calculadora para determinar el salario de un empleado basado en bloques de jornadas con diferentes y
    pagos por hora de jornada y dia de la jornada
"""
import logging
from util.utils import get_data_from_archive, clean_data, get_name, get_days_worked, generate_days_worked
from models.User import User
from models.day import Day
from payment.Payment import Payment


def main():
    archive = get_data_from_archive()
    data = clean_data(archive)
    for user in data:
        user_name = get_name(user)
        days: list[Day] = generate_days_worked(get_days_worked(user))
        user_instance = User(user_name, days)
        payment = Payment.process_payment(user_instance)
        print(f"EL monto a para a {user_instance.get_name()} es : {'{:.2f}'.format(payment)} USD")


if __name__ == '__main__':
    main()
