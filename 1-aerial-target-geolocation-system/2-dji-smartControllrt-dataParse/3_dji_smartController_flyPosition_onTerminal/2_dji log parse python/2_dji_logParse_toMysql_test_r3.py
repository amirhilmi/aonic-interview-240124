
import time
import mysql.connector
from datetime import datetime

file_path = r"C:\Users\amirh\Downloads\dji log parse python\idea.log"

while True:
    try:
        cnx = mysql.connector.connect(user='root', 
                                      password='abc12345',
                                      host='localhost',
                                      database='flight_data')
        cursor = cnx.cursor()

        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in reversed(lines):
                if "CurrentLocation" in line:
                    current_location = line.strip().split("CurrentLocation")[1]
                    current_time = datetime.now()
                    insert_query = "INSERT INTO table1 (location,datetime) VALUES (%s, %s)"
                    try:
                        cursor.execute(insert_query, (current_location, current_time))
                        cnx.commit()
                        print("Inserted data successfully")
                    except mysql.connector.Error as e:
                        if e.errno == 1062:
                            print("Skipping duplicate entry")
                        else:
                            raise e
                    break
        time.sleep(1)
    except mysql.connector.Error as e:
        print(f'An error occurred: {e}')
    finally:
        cursor.close()
        cnx.close()
