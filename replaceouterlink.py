__author__ = 'David'
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
import urllib
import win32clipboard

from bs4 import BeautifulSoup

def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    try:
        win32clipboard.SetClipboardText(text)
        # win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    except Exception as e:
        print e
    win32clipboard.CloseClipboard()


def changetext(num):
    for i in range(0, num):

        try:
            driver.get(tkPage)
            if i>=1:
                driver.find_element_by_tag_name('body').click()
                driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
                # u'\ue00d'
                time.sleep(5)
            step2 = wait.until(
                EC.element_to_be_clickable((By.ID, 'w0-data-table-grid-row['+str(i)+']-w0')))
            step2.click()

            url=driver.current_url
            # print url
            print 'ID OF PRODUCT:',re.findall(r'\d{12}$',url)

            step3 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'HTML')))
            step3.click()

            try:
                driver.find_element_by_id('v4-22txtEdit_ht')
                driver.switch_to.frame('v4-22txtEdit_ht')
                print 'frame:v4-22txtEdit_ht'
            except NoSuchElementException:
                try:
                    driver.find_element_by_id('v4-20txtEdit_ht')
                    driver.switch_to.frame('v4-20txtEdit_ht')
                    print 'frame:v4-20txtEdit_ht'
                except NoSuchElementException:
                    try:
                        driver.find_element_by_id('v4-46txtEdit_ht')
                        driver.switch_to.frame('v4-46txtEdit_ht')
                        print 'frame:v4-46txtEdit_ht'
                    except NoSuchElementException:
                        try:
                            driver.find_element_by_id('v4-43txtEdit_ht')
                            driver.switch_to.frame('v4-43txtEdit_ht')
                            print 'frame:v4-43txtEdit_ht'
                        except NoSuchElementException:
                            try:
                                driver.find_element_by_id('v4-26txtEdit_ht')
                                driver.switch_to.frame('v4-26txtEdit_ht')
                                print 'frame:v4-26txtEdit_ht'
                            except NoSuchElementException:
                                try:
                                    driver.find_element_by_id('v4-32txtEdit_ht')
                                    driver.switch_to.frame('v4-32txtEdit_ht')
                                    print 'frame:v4-32txtEdit_ht'
                                except NoSuchElementException:
                                    try:
                                        driver.find_element_by_id('v4-29txtEdit_ht')
                                        driver.switch_to.frame('v4-29txtEdit_ht')
                                        print 'frame:v4-29txtEdit_ht'
                                    except NoSuchElementException:
                                        try:
                                            driver.find_element_by_id('v4-23txtEdit_ht')
                                            driver.switch_to.frame('v4-23txtEdit_ht')
                                            print 'frame:v4-23txtEdit_ht'
                                        except NoSuchElementException:
                                            try:
                                                driver.find_element_by_id('v4-28txtEdit_ht')
                                                driver.switch_to.frame('v4-28txtEdit_ht')
                                                print 'frame:v4-28txtEdit_ht'
                                            except NoSuchElementException:

                                                try:
                                                    driver.find_element_by_id('v4-47txtEdit_ht')
                                                    driver.switch_to.frame('v4-47txtEdit_ht')
                                                    print 'frame:v4-47txtEdit_ht'
                                                except NoSuchElementException:

                                                    try:
                                                        driver.find_element_by_id('v4-16txtEdit_ht')
                                                        driver.switch_to.frame('v4-16txtEdit_ht')
                                                        print 'frame:v4-16txtEdit_ht'
                                                    except NoSuchElementException:

                                                        try:
                                                            driver.find_element_by_id('v4-25txtEdit_ht')
                                                            driver.switch_to.frame('v4-25txtEdit_ht')
                                                            print 'frame:v4-25txtEdit_ht'
                                                        except NoSuchElementException:

                                                            try:
                                                                driver.find_element_by_id('v4-5txtEdit_ht')
                                                                driver.switch_to.frame('v4-5txtEdit_ht')
                                                                print 'frame:v4-5txtEdit_ht'
                                                            except NoSuchElementException:
                                                                try:
                                                                    driver.find_element_by_id('v4-35txtEdit_ht')
                                                                    driver.switch_to.frame('v4-35txtEdit_ht')
                                                                    print 'frame:v4-35txtEdit_ht'
                                                                except NoSuchElementException:
                                                                    try:
                                                                        driver.find_element_by_id('v4-19txtEdit_ht')
                                                                        driver.switch_to.frame('v4-19txtEdit_ht')
                                                                        print 'frame:v4-19txtEdit_ht'
                                                                    except NoSuchElementException:

                                                                        try:
                                                                            driver.find_element_by_id('v4-38txtEdit_ht')
                                                                            driver.switch_to.frame('v4-38txtEdit_ht')
                                                                            print 'frame:v4-38txtEdit_ht'
                                                                        except NoSuchElementException:

                                                                            try:
                                                                                driver.find_element_by_id(
                                                                                    'v4-13txtEdit_ht')
                                                                                driver.switch_to.frame(
                                                                                    'v4-13txtEdit_ht')
                                                                                print 'frame:v4-13txtEdit_ht'
                                                                            except NoSuchElementException:

                                                                                try:
                                                                                    driver.find_element_by_id(
                                                                                        'v4-17txtEdit_ht')
                                                                                    driver.switch_to.frame(
                                                                                        'v4-17txtEdit_ht')
                                                                                    print 'frame:v4-17txtEdit_ht'
                                                                                except NoSuchElementException:

                                                                                    driver.find_element_by_id(
                                                                                        'v4-34txtEdit_ht')
                                                                                    driver.switch_to.frame(
                                                                                        'v4-34txtEdit_ht')
                                                                                    print 'frame:v4-34txtEdit_ht'

            content1 = driver.find_element_by_tag_name('body').text

            # Added for store,because it used <a> as anchor, but not supported in html5 2017.9.27
            content = re.sub(r'<(a|\/a).*?>', "", content1)



            soup = BeautifulSoup(content,"lxml")

            links = soup.find_all('a')

            for link in links:
                # print type(link)
                link['target'] = '_blank'

            print 'link target is all _blank'


            try:

                # [link.extract() for link in soup.find_all('a', href=re.compile('xxxxx'))]
                [x.parent.extract() for x in soup.findAll('img', {'src': 'http://www.xxxxxs.com/fpdb/images/Logo_Ny62.jpg'})]
                [x.parent.extract() for x in soup.findAll('img', {'src': 'http://www.xxxxxs.com/images/Risk_Free_logo.gif'})]
                [x.parent.extract() for x in soup.findAll('img', {'src': 'http://www.xxxxxs.com/images/contact_email.jpg'})]

                # [x.parent.extract() for x in soup.findAll('img', {'src': 'http://www.xxxxxs.com/images/contact_email.jpg'})]
            except:
                print 'Category is wrong'
            # modifiedtxt1 = str(soup)
            modifiedtxt = soup.encode_contents(formatter='html')
            #############################################################

            copy(modifiedtxt)
            try:
                driver.find_element_by_tag_name('body').clear()
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, 'v')
            except Exception as e1:
                print 'bad:',e1

# #############################################################
#             # update and save
#
            driver.switch_to.default_content()
            step4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#actionbar > input')))
            step4.click()
            # print 'step4 ok'
            time.sleep(10)

            step5 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#confirm_button_wrap > input')))
            step5.click()
            print i,' is Ok'
            with open('picturefolder.txt', 'a') as f:
                f.writelines('Ok')

        ############################################################

        except Exception as e3:

            print 'error in first, i is',i
            print e3
            time.sleep(3)
            continue
            # k = k + 1


loginPage = "https://signin.ebay.com/ws/eBayISAPI.dll?SellItem"

# tkPage = "https://mesg.ebay.com/mesgweb/ViewMessageDetail/0/All/91486739360"
tkPage = "http://www.ebay.com/sh/lst/active/contact-info"
driver = webdriver.Chrome('c:/chromedriver')
driver.get(loginPage)

wait = WebDriverWait(driver, 20)

login = wait.until(EC.element_to_be_clickable((By.ID, 'userid')))
password = wait.until(EC.element_to_be_clickable((By.ID, 'pass')))
# login.send_keys("xxxxx")
login.send_keys("xxxxx")
password.send_keys("xxxxxx")
driver.find_element_by_id('sgnBt').click()
with open('picturefolder.txt', 'w') as f:
    f.writelines('begin modidify:')
changetext(50)
# for i in range(0,50):
#     try:
#
#         changetext(99,i)
#         if i>0 and i<49:
#             i=i+1
#
#         elif i>=50:
#             i=i-1
#     except:
#         changetext(99,i+1)

f.close()
driver.quit()
