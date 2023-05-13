"""
    calculadora para calcular el salario de un empleado basado en blockes
"""
import logging
from util.utils import get_data_from_archive, clean_data,get_name,get_days_worked, format_input, get_time, set_time, get_price_per_day

def get_worked_hours(payload, shift = {'start':9, 'end': 18}):
    """
        shift is a dicctionary that represend the start and end of a shedule working time
        payload is a input for the day worked following this format 'MO03:00-17:00'
    """
    start = shift['start']
    end = shift['end']
    if payload is None:
        raise ValueError('Invalid Input Exception')
    timeframe = format_input(payload)
    tStart = get_time(timeframe[0])
    tEnd = get_time(timeframe[1])

    if start > tStart.hour:
        tStart = set_time(start)

    if tEnd.hour > end :
        tEnd = set_time(end)

    deltaTime = tEnd - tStart
    hours = deltaTime.total_seconds() / 3600
    if hours <= 0:
        return 0

    return hours

def get_payout(payload):
    """
        calculate the payout USD besed on the schedule send
    """
    if payload is None:
        raise IOError("payload send is not a valid one")

    total_payout = 0
    midnight_hours = 0
    day_hours = 0
    night_hours = 0
    morning_shift = {
        'start': 9,
        'end': 18,
        'price': {
            "LV": 15,
            "SD": 20
        }
    }
    midnight_shift = {
        'start': 0,
        'end': 9,
        'price': {
            "LV": 25,
            "SD": 30
        }

    }
    night_shift = {
        'start': 18,
        'end': 24,
        'price': {
            "LV": 20,
            "SD": 25
        }
    }

    day_hours = get_worked_hours(payload, morning_shift)
    night_hours = get_worked_hours(payload, night_shift)
    midnight_hours = get_worked_hours(payload, midnight_shift)
    payment_block_day = get_price_per_day(payload,morning_shift)
    payment_block_night = get_price_per_day(payload, night_shift)
    payment_block_midnight = get_price_per_day(payload, midnight_shift)
    total_payout = (day_hours * payment_block_day) + (night_hours * payment_block_night) + (midnight_hours * payment_block_midnight)
    # timeframe = format_input(payload)
    # total_hours_worked = day_hours + night_hours + midnight_hours
    # print(f"""total hours worked are in the shift from {timeframe[0]} to {timeframe[1]} total hours worked {total_hours_worked} :\n
    #             mornight {day_hours} hours priced at {payment_block_day} equals to {day_hours * payment_block_day} USD\n
    #             night {night_hours} hours priced at {payment_block_night} equals to {night_hours * payment_block_night} USD\n
    #             midnight {midnight_hours} hours priced at {payment_block_midnight} equals to {midnight_hours * payment_block_midnight} USD\n
    #         """)
    return total_payout

def main():
    """
        application entry point
    """

    data = get_data_from_archive()
    cleaned = clean_data(data)
    for user in cleaned:
        user_name = get_name(user)
        days_worked = get_days_worked(user)
        total_payment = 0
        for p in days_worked:
            total_payment += get_payout(p)
        print( f"EL monto a para a {user_name} es :{total_payment} USD")

if __name__ == '__main__':
    main()
