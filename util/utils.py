import re
import sys
from datetime import datetime


def get_days_worked(payload :str):
    """
        return a list of days worked
    """
    return payload.rsplit("=")[1].rsplit(',')

def get_name(payload):
    """
        return the name of the user 
    """
    return payload.rsplit('=')[0]

def get_hour_worked_by_day(payload):
    """
        method to tread a payload and separate working hours:
        expected: MO09:00-17:00,TU09:00-17:00,FR09:00-17:00,SA09:00-17:00,SU09:00-17:00
    """
    return payload[2:].rsplit('-')

def check_extension(payload):
    """
        check file extention otherwise raise an exception
    """
    if '.txt' not in payload:
        raise IOError("extencion invalida de archivo, solo soportada .txt")

def get_data_from_archive():
    """
        method created to retreive data from an archive or a path indicated
    """
    file = None
    if len(sys.argv) > 1 and sys.argv[1].find('--path') != -1:
        path = sys.argv[1].rsplit('=')[1]
        check_extension(path)
    else:
        path = input("insert the route of the paymens file ")
        check_extension(path)
    file = open(path, 'rt', encoding='UTF-8')
    try:
        data = file.readlines()
        return data
    finally:
        file.close()

def get_time(payload):
    """
        function to convert a string into a date time
        Input example 21:00
    """
    try:
        return datetime.strptime(str(payload), '%H:%M')
    except ValueError:
        print(f"payload {payload}")

def set_time(payload):
    """
        create a time based on int hour provided
    
    """
    try:
        if type(payload) != int:
            raise ValueError("type provided not supported")
        return datetime.strptime(str(payload), '%H')
    except ValueError:
        print(f"payload set_time {payload}")

def clean_data(payload):
    """
        method created to clean '\\n' from the archive readed
    """
    res = []
    for sub in payload:
        res.append(sub.replace("\n", ""))
    return res

def get_price_per_day(payload, shift):
    """
        method created to recreive price depending on the day schema set up
    """
    day_type = get_day_type(payload)
    return shift['price'][day_type]

def get_day_type(payload):
    """
        method created to retrive the fisrt tow leters of payload and 
        determine the section for the block if its SD or LV schedule
    """
    if payload[:2] == 'SA' or payload[:2] == 'SU':
        return 'SD'
    else:
        return 'LV'

def format_input(payload):
    """
        formater input type must be in this format 'MO03:00-13:00'
    """
    # print(f"formater :{str(payload[2:].rsplit('-'))}")
    start = payload[2:].rsplit('-')[0]
    end = payload[2:].rsplit('-')[1]
    return [start, end]
