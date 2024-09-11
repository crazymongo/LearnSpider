import json

from selenium import webdriver


def get_cookies(
        url="https://passport.weibo.com/sso/signin?entry=miniblog&source=miniblog&disp=popup&url=https%3A%2F%2Fweibo.com%2Fnewlogin%3Ftabtype%3Dlist%26gid%3D1028039999%26openLoginLayer%3D0%26url%3Dhttps%253A%252F%252Fweibo.com%252F"):
    browser = webdriver.Chrome()
    browser.get(url)
    print("please login in!")
    waiting = True
    while waiting:
        ok = input('after login success, pleas press enter to continue')
        if ok:
            waiting = False

    print(browser.get_cookies())
    with open('cookies.txt', 'w') as f:
        f.write(json.dumps(browser.get_cookies()))
        f.close()
    print("cookies saved!")
    browser.quit()


if __name__ == '__main__':
    get_cookies()
