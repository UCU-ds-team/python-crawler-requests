from selenium import webdriver
import time
# from pyvirtualdisplay import Display
from urllib.parse import urlsplit, parse_qs


class WebGetter:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def login_facebook(self, login=None, password=None):
        """
        Performs the login event to facebook
        """
        if login is None or password is None:
            from login import INFO
            login = INFO["login"]
            password = INFO["password"]
        self.browser.get('https://m.facebook.com')

        login_css = self.browser.find_element_by_id('m_login_email')
        password_css = self.browser.find_element_by_css_selector('input.bl.bm.bo')
        button = self.browser.find_element_by_css_selector('input[name="login"]')

        login_css.send_keys(login)
        password_css.send_keys(password)
        button.click()
        time.sleep(3)
        print("Current_url %s" % self.browser.current_url)
        print("Logged in...")

    def friends_scrapper(self, pg_id):
        url = "https://m.facebook.com/%s/friends" % self.link_editor(pg_id)

        self.browser.get(url)
        time.sleep(1.5)

        while len(self.browser.find_elements_by_css_selector("img._359.img")) == 1:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolled to the bottom...")

        blocks = self.browser.find_elements_by_xpath("//div[@data-testid='friend_list_item']")
        ids_list = list()
        for block in blocks:
            try:
                link = block.find_element_by_css_selector('div.fsl.fwb.fcb a')
                name = link.text
                link = link.get_attribute("href")
            except Exception as e:
                self.add_error(e)
                name = ""
                link = ""
            ids_list.append(name)
            ids_list.append(link)
        return ids_list

    @staticmethod
    def link_editor(link):
        """
        Returns the only id from the url line
        """
        res_id = ""
        return res_id

    def close_browser(self):
        self.browser.quit()


if __name__ == "__main__":
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    inst = WebGetter()
    time_ = time.time()
    inst.login_facebook()
    try:
        # read_perform("./data/interested.txt", "./db_interested/", inst)
        pass
    finally:
        inst.close_browser()
        # display.stop()
    print(time.time() - time_)
