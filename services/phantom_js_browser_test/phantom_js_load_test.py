__author__ = "Manouchehr Rasouli"
__date__ = "3/November/2017"

from selenium import webdriver
import time


class PhantomJsTest:
    def __init__(self, url, result):
        self.driver = webdriver.PhantomJS(executable_path='/home/admin1/Uptime/check_point/env/bin/phantomjs')
        self.result = result
        self.url = url

    def do_test(self):
        try:
            start = time.time()
            self.driver.get(self.url["url"])
            end = time.time()

            navigation_start = self.driver.execute_script("return window.performance.timing.navigationStart")
            response_start = self.driver.execute_script("return window.performance.timing.responseStart")
            dom_complete = self.driver.execute_script("return window.performance.timing.domComplete")

            back_end_performance = response_start - navigation_start
            front_end_performance = dom_complete - response_start

            self.driver.get(self.url["url"])

            # Take screen shot for urls that have interrupt capture request.
            if self.url["interrupt"]["error_screen"] == "yes":
                if self.result["status"] == "down":
                    self.result["capture"] = self.driver.get_screenshot_as_base64()
                elif self.url["interrupt"]["speed_interrupt"]["have"] == "yes":
                    if self.result["speed"] > self.url["interrupt"]["speed_interrupt"]["minimum_speed"]:
                        self.result["capture"] = self.driver.get_screenshot_as_base64()

            self.result["chrome_check_time"] = str(end - start)
            self.result["chrome_back_end_performance"] = str(back_end_performance / 1000)
            self.result["chrome_front_end_performance"] = str(front_end_performance / 1000)
            self.driver.quit()
        except Exception as e:
            self.driver.quit()
            self.result['chrome_check_time'] = 'Chrome browser is in truble with your url !'
            self.result["chrome_back_end_performance"] = "-1"
            self.result["chrome_front_end_performance"] = "-1"
        return self.result
