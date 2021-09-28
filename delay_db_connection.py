
# delaying database connection for faster app startup

# ----- main.py -------- #

from typing import Optional
from connection import Connection


class Main:
    def __init__(self):
        self.greet = 'Hello'
    
    # method to delay the initialization of db connection
    def initialize_db(self):
        connect = Connection()
        connect.get_data()

    def greet_person(self):
        print(f'{self.greet} Iian')
        self.initialize_db()


greet = Main()
greet.greet_person()

if __name__ == '__main__':
    Main()
    
# ----- connection.py -------- #

import mysql.connector
import subprocess
import platform

db = None
cursor = None

class Connection:
    def __init__(self):
        param = 'n' if platform.system().lower == 'windows' else '-c'
        self.command = ['ping', param, '1', 'google.com']
        

    # method to check internet connection
    def _connection_check(self):
        if (subprocess.call(self.command) == 0) == True:
            global db, cursor
            db = mysql.connector.connect(
                host='sample.host.com',
                user='iian',
                passwd='password',
                database='faith'
            )
            cursor = db.cursor()
        else:
            return False

    def get_data(self):
        # condition if there is no connection
        if self._connection_check() == False:
            print('Sorry you have no connection')
        else:
            cursor.execute('select * from main_service')

            for i in cursor.fetchall():
                print(i)


if __name__ == '__main__':
    Connection()
