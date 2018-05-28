# author：--Vincent--
from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
import json
import os
import time

dcap=dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
)
logger = logging.getLogger(__name__)
logging.getLogger("selenium").setLevel(logging.WARNING) # 将selenium的日志级别设成WARNING，太烦人

myzhipin=[
    ('15077306171','wen8226789'),
]


def getCookie(account,password):
    loginURL='https://login.zhipin.com/'

    try:
        browser = webdriver.PhantomJS(desired_capabilities=dcap)
        browser.set_window_size(1024,900)
        browser.get("https://login.zhipin.com/")
        #logDIV=browser.find_element_by_class_name("sign-form sign-pwd")
        elem_user=browser.find_element_by_css_selector('.sign-pwd .ipt-phone')
        elem_user.send_keys(account)
        elem_pwd=browser.find_element_by_css_selector('.sign-pwd .ipt-pwd')
        elem_pwd.send_keys(password)
        while True:
            browser.save_screenshot("bosszhipin.png")
            code_txt = input("请输入bosszhipin.png下的验证码:")
            code=browser.find_element_by_css_selector(".ipt-code")
            code.clear()
            code.send_keys(code_txt)
            login=browser.find_element_by_css_selector(".btn")
            login.click()
            time.sleep(2)   #有bug，因为跳转速度不定
            title = browser.find_element_by_css_selector('.label-text').text
            if title=='庞先生':
                print("登陆成功")
                break

        try:
            cookie={}
            for elem in browser.get_cookies():
                cookie[elem["name"]] = elem["value"]
            logger.warning("Get Cookie Success!( Account:%s )" % account)
            return json.dumps(cookie)
        except Exception:
            logger.warning("Failed %s!" % account)
            return ""
    except Exception:
        logger.warning("Failed %s!" % account)
        return ""
    finally:
            browser.quit()



def iniCookie(rconn,spiderName):
    for zhipin in myzhipin:
        if rconn.get("%s:Cookies:%s--%s" % (spiderName, zhipin[0], zhipin[1])) is None:  # 'zhipinspider:Cookies:账号--密码'，为None即不存在。
            cookie = getCookie(zhipin[0], zhipin[1])
            if len(cookie) > 0:
                rconn.set("%s:Cookies:%s--%s" % (spiderName, zhipin[0], zhipin[1]), cookie)
    cookieNum = str(rconn.keys()).count("bossspider:Cookies")
    logger.warning("The num of the cookies is %s" % cookieNum)
    if cookieNum == 0:
        logger.warning('Stopping...')
        os.system("pause")

def updateCookie(accountText, rconn, spiderName, cookie):
    """ 更新一个账号的Cookie """
    account = accountText.split("--")[0]
    #pdb.set_trace()
    new_cookie = UpdateCookie(account, cookie)
    if len(new_cookie) > 0:
        logger.warning("The cookie of %s has been updated successfully!" % account)
        rconn.set("%s:Cookies:%s" % (spiderName, accountText), new_cookie)
    else:
        logger.warning("The cookie of %s updated failed! Remove it!" % accountText)
        removeCookie(accountText, rconn, spiderName)


def removeCookie(accountText, rconn, spiderName):
    """ 删除某个账号的Cookie """
    rconn.delete("%s:Cookies:%s" % (spiderName, accountText))
    cookieNum = rconn.keys().count("bossspider:Cookies")
    logger.warning("The num of the cookies left is %s" % cookieNum)
    if cookieNum == 0:
        logger.warning("Stopping...")
        os.system("pause")


def UpdateCookie(account,cookie):
    browser = webdriver.PhantomJS(desired_capabilities=dcap)
    #browser = webdriver.Firefox()
    browser.set_window_size(1920, 1080)
    browser.get('https://www.zhipin.com')
    browser.delete_all_cookies()
    send_cookie = []
    for key,value in cookie.items():
        one = {}
        one = {'domain':'.zhipin.com','name':key,'value':value,'path':'/','expiry':None}
        #pdb.set_trace()
        browser.add_cookie({k: one[k] for k in ('name', 'value', 'domain', 'path', 'expiry')})
        #one = {'domain':'.zhihu.com','name':key,'value':value}
        #send_cookie.append(one)
    #browser.add_cookie(send_cookie)
    browser.get('https://login.zhipin.com/')
    time.sleep(1)
    browser.save_screenshot("update.png")
    code_txt = input("请查看路径下新生成的update.png，然后输入验证码:")
    browser.find_element_by_name("captcha").send_key(code_txt)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    try:
        cookie = {}
        for elem in browser.get_cookies():
            cookie[elem["name"]] = elem["value"]
        logger.warning("Update Cookie Success!( Account:%s )" % account)
        #pdb.set_trace()
        return json.dumps(cookie)
    except Exception:
        logger.warning("Update Failed %s!" % account)
        return ""
    finally:
        try:
            browser.quit()
        except Exception:
            pass



if __name__=='__main__':
    getCookie(myzhipin[0][0],myzhipin[0][1])
