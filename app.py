from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from video_url import VideoUrl
from scrap_comment import ScrapComment
from mongo import Mongo
from sql_database import SnowflakeDatabase
from youtube_video_download import DownloadVideo
from re import search
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/scrap',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            url = request.form['scrap'].replace(" ", "")
            print(url)
            video_url = VideoUrl.Video_page(url)
            all_video_link_of_channel = video_url['video_url']

            for i in range(0, len(all_video_link_of_channel)):
                if search('watch', all_video_link_of_channel[i]):
                    print("11111111111111111111111")
                    channel_video = "https://www.youtube.com" + all_video_link_of_channel[i]
                    print("22222222222222222222222222222222")
                    dic = ScrapComment.ScrapDetails(channel_video)
                    print("3333333333333333333333333333333")
                    print(dic)
                    firebase_url = DownloadVideo.youtube_video_download(channel_video, dic['youtuber_name'], dic['title'])
                    api_key = "a8ad6e68ae5bee3a3985a1d0b64958fba6fc8"
                    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={firebase_url}"
                    data = requests.get(api_url).json()["url"]
                    if data["status"] == 7:
                        # OK, get shortened URL
                        shortened_url = data["shortLink"]
                        print("Shortened URL:", shortened_url)
                    else:
                        print("[!] Error Shortening URL:", data)
                    Mongo.insertDataMongoDb(dic['comment_details'])
                    SnowflakeDatabase.insert_data(dic['youtuber_name'], dic['title'], dic['subscriber'], dic['views'], dic['like'], channel_video,
                                shortened_url, video_url["thumbail_src"][i], dic['total_comment'])

                    print("\n\n\n" + "*" * 90 + "\n\n\n")
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

if __name__ == "__main__":
    app.run()