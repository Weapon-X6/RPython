import re

def get_date(datum):
    """
    valid formats: YYYY-MM-DD, DD-MM-YYYY, MM-DD-YYYY
    """
    year = ''
    month = ''
    day = ''
    r = re.search('(\d{4})-(\d{2})-(\d{2})', datum)
    print(r)
    if r is None:
        r = re.search('(\d{2})-(\d{2})-(\d{4})', datum)
        year = r.group(3)
        if int(r.group(1)) > 12:
            month = r.group(2)
            day = r.group(1)
        else:
            month = r.group(1)
            day = r.group(2)
    else:
        year = r.group(1)
        month = r.group(2)
        day = r.group(3)
    print(r.groups())
    with open()

    print(f"{day}.{month}.{year}")



get_date("2020-11-24")
get_date("24-05-2023")
get_date("10-01-2023")

#get_date("2020-NOV-24")