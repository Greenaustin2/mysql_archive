# from getpass import getpass
from mysql.connector import connect, Error
import os
# CREATE / SHOW DATABASE / TABLE
# CREATE TABLE students (name VARCHAR(255), age INTEGER(10))

# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1 = ("Rachel", 22)

#cursor.execute(sqlFormula, student1)
# connection.commit()


# sqlFormula = "CREATE TABLE channels (name VARCHAR(255), download_date DATE)"

# sqlFormula = "INSERT INTO channels (name, download_date) VALUES (%s)"


# def create_folder(channel_name, folder_name):
#     directory = os.listdir("/volumes/graphic_balance/complete")
#     for folder in directory:
#         if folder == ".DS_Store":
#             pass
#         else:
#             channel_directory = os.listdir("/volumes/graphic_balance/complete/" + folder + "/channels")
#             for channel in channel_directory:
#                 if channel == ".DS_Store":
#                     pass
#                 else:
#                     print(channel)



#
# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Rachel", 22),
#             ("Bob", 12),
#             ("Maria", 23),
#             ("Dragonaut", 25),
#             ("Calypso", 27),
#             ]





# try:
#     with connect(
#         host="localhost",
#         user="root",
#         password="Gr33nie1",
#         database='graphic_balance'
#     ) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(sqlFormula, students)
#             connection.commit()
# except Error as e:
#     print(e)
#
#
#











#creating a cursor object
# cursor = connection.cursor()


#create a database
# try:
#     with connect(
#         host="localhost",
#         user="root",
#         password="Gr33nie1"
#     ) as connection:
#         create_db_query = "CREATE DATABASE graphic_balance"
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
# except Error as e:
#     print(e)






#read from database
try:
    with connect(
        host="localhost",
        user="root",
        password="Gr33nie1",
        database="channels"
    ) as connection:
        insert_sql = "INSERT INTO channel_list (name, download_date) VALUES (%s, %s)"
        directory = os.listdir("/volumes/graphic_balance/complete")
        for folder in directory:
            if folder == ".DS_Store":
                pass
            else:
                channel_directory = os.listdir("/volumes/graphic_balance/complete/" + folder + "/channels")
                for channel in channel_directory:
                    if channel == ".DS_Store":
                        pass
                    else:
                        with connection.cursor() as cursor:
                            folder_date = "20" + folder[-2:] + "-" + folder[:2] + "-" + folder.split('_')[1]
                            cursor.execute(insert_sql, (channel, folder_date))
                            connection.commit()

except Error as e:
    print(e)







