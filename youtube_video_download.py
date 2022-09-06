import pytube
import pyrebase
import os

class DownloadVideo:
    def youtube_video_download(url, youtuber_name, video_title):
        #     link="https://www.youtube.com/watch?v=HY6aK1cX8Ig"
        config = {
            "apiKey": "AIzaSyAGv07QZ0WNP5xpGVjzOxAn4-a4cytalQ0",
            "authDomain": "connectiontopython-bb25d.firebaseapp.com",
            "projectId": "connectiontopython-bb25d",
            "storageBucket": "connectiontopython-bb25d.appspot.com",
            "service": "serviceAccountKey.json",
            "databaseURL": "",
            "messagingSenderId": "718628549907",
            "appId": "1:718628549907:web:e0f852097b4faa2d8616e6",
            "measurementId": "G-1PR6GHSCFF"
        }

        firebase_storage = pyrebase.initialize_app(config)
        storage = firebase_storage.storage()
        yt = pytube.YouTube(url)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()

        storage.child(youtuber_name + "/" + video_title).put(stream.download())
        url = storage.child(youtuber_name + "/" + video_title).get_url(None)
        v = video_title.replace("|", "")
        v1 = v.replace(",", "")
        v2 = v1.replace("?", "")
        v3 = v2.replace(".", "")
        v4 = v3.replace("#", "")
        v5 = v4.replace(",", "")
        v6 = v5.replace(":","")
        print("Video url after split " + v6)
        os.remove(v6 + ".mp4")
        return url