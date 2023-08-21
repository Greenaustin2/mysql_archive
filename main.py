from mysql.connector import connect, Error
import os

create_database = "CREATE DATABASE graphic_balance"
create_table = "CREATE TABLE channels (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), curl VARCHAR(255), download_date DATE)"
create_table_tags = "CREATE TABLE tags (videoId int PRIMARY KEY, FOREIGN KEY(videoId) REFERENCES channels(id), "
insert_sql = "INSERT INTO channels (name, download_date) VALUES (%s, %s)"

#read from database
try:
    with connect(
        host="localhost",
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
        database="graphic_balance"
    ) as connection:
        sql = create_database
        base_path = "/volumes/graphic_balance/complete/"
        directory = os.listdir(base_path)
        for folder in directory:
            # Rule out hidden .DS_Store files
            if folder == ".DS_Store":
                pass
            else:
                channel_directory = os.listdir(base_path + folder + "/channels")
                for channel in channel_directory:
                    # Rule out hidden .DS_Store files
                    if channel == ".DS_Store":
                        pass
                    else:
                        with connection.cursor() as cursor:
                            # channel url from first file name in channel folder
                            channel_file = os.listdir(base_path + folder + "/channels/" + channel)[0]
                            curl = channel_file.split("_")[2]
                            # date reformat to YYYY_MM_DD
                            folder_date = "20" + folder[-2:] + "-" + folder[:2] + "-" + folder.split('_')[1]
                            # execute and save sql script
                            cursor.execute(sql, (channel, folder_date))
                            connection.commit()
except Error as e:
    print(e)







