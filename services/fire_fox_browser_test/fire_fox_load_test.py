__author__ = "Manouchehr Rasouli"
__date__ = "22/Aug/2017"

from selenium import webdriver
import time


# What i done here ?
class FireFoxLoadTest:
    def __init__(self, url, result):
        # 1 - Load a fire fox web driver
        self.driver = webdriver.Firefox()
        self.result = result
        self.url = url

    def do_test(self):
        # 2 - Start to check url on the fire fox browser
        try:
            start = time.time()
            self.driver.get(self.url["url"])
            end = time.time()

            navigation_start = self.driver.execute_script("return window.performance.timing.navigationStart")
            response_start = self.driver.execute_script("return window.performance.timing.responseStart")
            dom_complete = self.driver.execute_script("return window.performance.timing.domComplete")

            back_end_performance = response_start - navigation_start
            front_end_performance = dom_complete - response_start

            self.result["fire_fox_check_time"] = str(end - start)
            self.result["fire_fox_back_end_performance"] = str(back_end_performance / 1000)
            self.result["fire_fox_front_end_performance"] = str(front_end_performance / 1000)
            self.driver.quit()
            return self.result
        except Exception as e:
            pass
