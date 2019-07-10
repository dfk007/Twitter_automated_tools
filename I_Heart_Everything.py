"""
[+]Usage with anacoda: conda install selenium
[+]Required: selenium
"""

from selenium import webdriver
from getpass import getpass
import time

class twitter:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()



    def login_twitter(self):
        driver = self.driver
        driver.get("https://twitter.com/login")

        username_field = driver.find_element_by_class_name("js-username-field")
        password_field = driver.find_element_by_class_name("js-password-field")

        username_field.send_keys(username)
        driver.implicitly_wait(1)

        password_field.send_keys(password)
        driver.implicitly_wait(1)

        driver.find_element_by_class_name("EdgeButtom--medium").click()


    def like_tweet(self, hashtag):
        driver = self.driver
        driver.get("https://twitter.com/search?q=" + hashtag + "&src=tyah")


        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets = driver.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                driver.get("https://twitter.com" + link)
                try:
                    driver.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(5)
                except Exception as ex:
                    time.sleep(10)




if __name__ == "__main__":
    username = input("user name : ")
    password = getpass("password  : ")
    likey = input("What do you want to like? ")

    credentials_object = twitter(username, password)

    credentials_object.login_twitter()
    credentials_object.like_tweet(likey)


