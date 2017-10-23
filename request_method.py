# -------------------------------------------------------------------------------
# Name:        FACEBOOK TEST
# Purpose:
#
# Author:      Julius
#
# Created:     16.06.2015
# Copyright:   (c) Julius 2015
# Licence:     <APACHE>
# -------------------------------------------------------------------------------

# IMPORTS
import requests
from bs4 import BeautifulSoup
from login import INFO

# CONSTRAINTS
EMAIL = INFO["login"]
PASSW = INFO["pass"]
LOGIN_URL = "https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&amp;refid=8"
FACEBOOK_URL = "https://m.facebook.com/"

# VARS
s = None


# MAIN CLASS
class Facebook():
    def __init__(self):
        self.s = requests.session()
        self.login()

    def login(self):
        # GET DEFAULT VALUES FROM PAGE
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        r = self.s.get(FACEBOOK_URL, headers=headers)
        soup = BeautifulSoup(r.text)
        print(r.text)
        # GET DEFAULT VALUES
        tmp = soup.find(attrs={"name": "lsd"})
        lsd = tmp.get("value")
        # tmp = soup.find(attrs={"name": "charset_test"})
        # csettest = tmp.get("value")
        # tmp = soup.find(attrs={"name": "version"})
        # version = tmp.get("value")
        # tmp = soup.find(attrs={"name": "ajax"})
        #
        # ajax = tmp.get("value")
        # tmp = soup.find(attrs={"name": "width"})
        # width = tmp.get("value")
        # tmp = soup.find(attrs={"name": "pxr"})
        # pxr = tmp.get("value")
        # tmp = soup.find(attrs={"name": "gps"})
        # gps = tmp.get("value")
        # tmp = soup.find(attrs={"name": "dimensions"})
        # dimensions = tmp.get("value")
        tmp = soup.find(attrs={"name": "m_ts"})
        m_ts = tmp.get("value")
        tmp = soup.find(attrs={"name": "li"})
        li = tmp.get("value")

        # data = {
        #     'lsd': lsd,
        #     'm_ts': m_ts,
        #     'li': li,
        # }
        data = dict(lsd=lsd, m_ts=m_ts, li=li)
        data['email'] = EMAIL
        data['pass'] = PASSW
        data['login'] = 'Log In'

        r = self.s.post(LOGIN_URL, data=data, headers=headers)
        # print(r.cookies,"\n", r.headers)
        # https://m.facebook.com/login/save-device/cancel/?flow=interstitial_nux&nux_source=regular_login
        # r = self.s.get("https://m.facebook.com/login/save-device/cancel/?flow=interstitial_nux&nux_source=regular_login")
        check_device = BeautifulSoup(r.text, "html.parser").select("form[action='/login/device-based/update-nonce/']")
        if len(check_device) > 0:
            r = self.s.get(
                "https://m.facebook.com/login/save-device/cancel/?flow=interstitial_nux&nux_source=regular_login",
                headers=headers)
        print(r.text)


fb = Facebook()
