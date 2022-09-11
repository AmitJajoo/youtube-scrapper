import snowflake.connector

class SnowflakeDatabase:
    def insert_data(youtuber_name, video_title, subscriber, view, likes_video, video_link, firebase_download_link,
                    thumbail, total_comment):
        # Gets the version
        ctx = snowflake.connector.connect(
            user='AMIT',
            password='<password>',
            account='HU39708.ap-southeast-1'
        )
        cs = ctx.cursor()
        try:
            cs.execute("SELECT current_version()")
            cs.execute("CREATE DATABASE if not exists youtube")
            cs.execute("USE DATABASE YOUTUBE")
            cs.execute(
                "CREATE TABLE if not exists details (youtuber_name VARCHAR(255), video_title VARCHAR(255), subscriber VARCHAR(255), view VARCHAR(255), likes_video VARCHAR(255), video_link VARCHAR(255), firebase_download_link VARCHAR(255), thumbail VARCHAR(255),TOTAL_COMMENT VARCHAR(255))")
            sql = "INSERT INTO details (youtuber_name, video_title,subscriber,view,likes_video,video_link,firebase_download_link,thumbail,TOTAL_COMMENT) VALUES (%s, %s,%s, %s,%s, %s,%s, %s, %s)"
            value = (
            youtuber_name, video_title, subscriber, view, likes_video, video_link, firebase_download_link, thumbail,
            total_comment)
            cs.execute(sql, value)
            one_row = cs.fetchone()
            print(one_row[0])
        finally:
            cs.close()