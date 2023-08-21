from mysql.connector import connect, Error
import os

#read from database
try:
    with connect(
        host="localhost",
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
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







