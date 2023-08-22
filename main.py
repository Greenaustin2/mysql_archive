from mysql.connector import connect, Error
import os
from pytube import YouTube


# list of commands
create_database = "CREATE DATABASE graphic_balance"
create_table = "CREATE TABLE channels (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), curl VARCHAR(255), download_date DATE)"
create_tag_table = "CREATE TABLE tags (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255))"
create_assoc_table = "CREATE TABLE channels_tags (channel_id INT, tag_id INT, FOREIGN KEY(channel_id) REFERENCES channels(id), FOREIGN KEY(tag_id) REFERENCES tags(id)"
create_table_tags = "CREATE TABLE tags (videoId int PRIMARY KEY, FOREIGN KEY(videoId) REFERENCES channels(id), "
insert_channels = "INSERT INTO channels (name, curl, download_date) VALUES (%s, %s, %s)"


#write to database from folder structure
try:
    with connect(
        host="localhost",
        user="root",
        password="Gr33nie1",
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
                            # channel url from first file name Youtube ID in channel folder
                            channel_file = os.listdir(base_path + folder + "/channels/" + channel)[0]
                            # Pull video ID from beginning of file name string
                            video_id = channel_file.split("_")[0]
                            # Rule out undefined or missing video_id
                            if len(video_id) != 11:
                                curl = "url undefined"
                            else:
                                # Retrieve respective channel ID number using pytube Youtube object
                                url = "https://www.youtube.com/watch?v=" + video_id
                                x = YouTube(url)
                                curl = x.channel_id
                                # date reformat to YYYY_MM_DD
                                folder_date = "20" + folder[-2:] + "-" + folder[:2] + "-" + folder.split('_')[1]
                                # execute and save sql script
                                cursor.execute(insert_channels, (channel, curl, folder_date))
                                # Save changes to database
                                connection.commit()


except Error as e:
    print(e)







