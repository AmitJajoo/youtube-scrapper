from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os

class ScrapComment:

    def ScrapDetails(url):
        option = webdriver.ChromeOptions()
        print("44444444")
        option.add_argument("--headless")
        print("555555555555")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
        driver.set_window_size(1536, 816)
        driver.get(url)
        time.sleep(10)
        prev_h =0 #driver.execute_script("return document.body.scrollHeight")
        while True:
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(20)

            # Calculate new scroll height and compare with last scroll height
            # height = driver.execute_script("return document.body.scrollHeight")
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
            time.sleep(10)
            prev_h += 200
            if prev_h >= height:
                break
        #         print("height "+str(height))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
        print("soup " +str(soup))
        title_text = soup.select_one("#container h1")
        print("title"+title_text.text)
        time.sleep(5)
        like_text = soup.select_one("#top-level-buttons-computed #text")
        print("like text " + str(like_text.text) + "\n")

        youtuber_name = soup.select_one("#text-container a")
        print("youtuber_name " + str(youtuber_name.text) + "\n")

        subscriber = soup.select_one("#owner-sub-count")
        print("subscriber " + str(subscriber.text) + "\n")

        views = soup.select_one("#count span")
        print("views " + str(views.text) + "\n")

        total_comment = soup.select_one("#title span")
        print("total_comment " + total_comment.text)

        comment_div = soup.select("#content #content-text")
        commentor_span = soup.select("#header #header-author #author-text .ytd-comment-renderer")
        comment_list = [x.text for x in comment_div]
        commentor_name = [x.text for x in commentor_span]

        new_lst = list(map(str.strip, commentor_name))

        li = []
        print(len(commentor_name))
        print(len(comment_list))
        if (len(commentor_name) == len(comment_list)):
            for i in range(0, len(comment_list)):
                li.append({
                    "commentor_name": new_lst[i],
                    "comment": comment_list[i]
                })
        print("dictionary " + str(li))
        print("commentor_name" + str(new_lst))
        print("comment " + str(comment_list))
        print("length " + str(len(comment_list)))
        return {"title": title_text.text, "youtuber_name": youtuber_name.text, "like": like_text.text,
                "subscriber": subscriber.text, "views": views.text, "total_comment": total_comment.text,
                "comment_details": li}
    # ScrapComment(urls[3])