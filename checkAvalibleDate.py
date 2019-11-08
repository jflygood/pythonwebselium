# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from sendmail import sendemail
from datetime import datetime

class Lihantestcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_lihantestcase(self):
        print "==============================Begin==========================================="
        flag=False
        content=""
        driver = self.driver
        driver.get("https://ieltsregistration.org/ielts-candidate/candidateonline/home.html")
        el = driver.find_element_by_id('moduleName')
        for option in el.find_elements_by_tag_name('option'):
            if 'General Training' in option.text :
                option.click()  # select() in earlier versions of webdriver
                print "----",option.is_selected()
                break

        print "Select module name"
        time.sleep(1)

        driver.find_element_by_id("countryId").click()
        Select(driver.find_element_by_id("countryId")).select_by_visible_text("United States Of America")
        driver.find_element_by_xpath("//option[@value='USA']").click()
        print "Select country name"
        time.sleep(1)
        driver.find_element_by_id("locationName").click()
        Select(driver.find_element_by_id("locationName")).select_by_visible_text("Austin, Texas")
        driver.find_element_by_xpath("//option[@value='Austin,  Texas']").click()
        print "Select city name"
        time.sleep(1)
        driver.find_element_by_name("Search").click()
        # ele=driver.find_element_by_xpath("//div[@id='main']/div[1]/div[2]/form[1]/fieldset[1]/table[1]/tbody[1]/tr[1]/td[1]")
        ele = driver.find_element_by_xpath("//div[@id='main']/div[1]/div[2]/form[1]/fieldset[1]/table[1]/tbody[1]")
        for tr in ele.find_elements_by_tag_name('tr'):
            tdtext = tr.find_element_by_xpath("./td[1]").text
            print tdtext
            # if '28/07/2018' in tdtext :
            #     flag=True
            #     content=tdtext
            #     break
            if '12/05/2018' in tdtext:
                flag = True
                content = tdtext
                break
            if '02/06/2018' in tdtext:
                flag = True
                content = tdtext
                break
        print '------'
        print "Content=",content
        print "flag=",flag
        print str(datetime.now())
        if flag:
            mailto = "lihan@xxx.com"
            sub = "Notification send from ling to remind"
            content = "Hi, Ling \n Please go to check the web, it already has what you need"
            # sendmail = sendemail(mailto, sub, content)
            # sendmail.send_mail()
            print content



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
