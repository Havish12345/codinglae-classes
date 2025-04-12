import random
import time
def random_date(start_date, end_date):
    print("Random date between",start_date,"and", end_date)
    random_date = random.random()
    date_format = "%d/%m/%Y"
    start_timestamp = time.mktime(time.strptime(start_date, date_format))
    end_timestamp = time.mktime(time.strptime(end_date, date_format))
    randomTime = start_timestamp + random_date * (end_timestamp - start_timestamp)
    randomDate = time.strftime(date_format, time.localtime(randomTime))
    return randomDate
    
print("the random date is", random_date("1/1/1992", "1/1/2023"))
    
