import threading
from django.conf import settings
from datetime import datetime

class FirstThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        with open(f'{settings.BASE_DIR}/file.text', '+a') as file:
            date_string = '{0}\n'.format(datetime.now())
            file.write(date_string)