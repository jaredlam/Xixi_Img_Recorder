# coding=utf-8
from dateutil.relativedelta import relativedelta
from datetime import datetime

datetimeFormat = "%Y:%m:%d %H:%M"
datetimeWithSecondFormat = "%Y:%m:%d %H:%M:%S"
birthday = datetime.strptime("2017:03:23 15:45", datetimeFormat)


def get_days(arg):
    take_photo_date = datetime.strptime(str(arg), datetimeWithSecondFormat)

    diff = relativedelta(take_photo_date, birthday)
    diff_years = diff.years
    diff_months = diff.months
    diff_days = diff.days

    result = ""
    if diff_years > 0:
        result += str(diff_years) + "年，"
    if diff_months > 0:
        result += str(diff_months) + "个月~"
    if diff_days > 0:
        result += str(diff_days) + "天"

    return result, take_photo_date.strftime("%Y-%m-%d")
