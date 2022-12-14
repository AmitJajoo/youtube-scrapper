from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os

class VideoUrl:

    def Video_page(url):
        print("url"+url)

        option = webdriver.ChromeOptions()
        option.add_argument("--headless")

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
        driver.set_window_size(1536, 816)
        driver.get(url)
        time.sleep(5)
        prev_h = 0
        while True:
            height = driver.execute_script("""
                    function getActualHeight() {
                        return Math.max(
                            Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                            Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                            Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );
                    }
                    return getActualHeight();
                """)
            driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 200})")
            # fix the time sleep value according to your network connection
            time.sleep(2)
            prev_h += 200
            if prev_h >= height:
                break
            print("height " + str(height))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
        thumbnail = soup.select("#dismissible img")
        video_url_a_href = soup.select("#dismissible #thumbnail")
        print("thumbnail " + str(thumbnail))
        print("\n\n\nurl " + str(video_url_a_href))
        #     thum_list = [x['src'] for x  in thumbnail]
        thumbail_src = []
        video_url = []
        # if (len(thumbnail) < 20):
        for i in range(0, len(thumbnail)): #need to change
            # for i in range(0, 1):
                #             if thumbnail[i]['src']:
            thumbail_src.append(thumbnail[i]['src'])
            print(video_url_a_href[i]['href'])
            video_url.append(video_url_a_href[i]['href'])
    #     print("thumnail"+str(thum_list))
        return {"video_url":video_url,"thumbail_src":thumbail_src}
