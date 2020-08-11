import datetime
import pytz

def date():
    utc = datetime.datetime.now(tz=pytz.UTC)
    dt_mtn = utc.astimezone(pytz.timezone("Asia/Calcutta"))
    final_date = dt_mtn.strftime('%d ' '%B ' '%Y ')
    return final_date


def time():
    utc = datetime.datetime.now(tz=pytz.UTC)
    dt_mtn = utc.astimezone(pytz.timezone("Asia/Calcutta")).strftime("%H:%M:%S")
    return dt_mtn

