
import copy
import random
import socket
import sys
import time
from time import sleep
import unicodedata
import urllib
from subprocess import call

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

# 검색할 항목 입력
term = "오늘"
# 저장 경로인대 안먹히는듯
destination = "C:\sol"


# 갱신시간을 위해 딜레이를 줌
def randdelay(a, b):
    time.sleep(random.uniform(a, b))


# 유니코드 정규화
def u_to_s(uni):
    return unicodedata.normalize('NFKD', uni).encode('ascii', 'ignore')


class PinterestHelper(object):

    def __init__(self, login_name, pw, download=True):
        self.login_name = login_name
        self.pw = pw
        self.download = download
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome('C:\chromedriver.exe')
        self.browser.get("https://www.pinterest.com")
        self.browser.implicitly_wait(5)

    def login(self):
        btn = self.browser.find_element_by_class_name('RCK.Hsu.USg.Vxj.aZc.Zr3.hA-.GmH.adn.Il7.Jrn.hNT.iyn.BG7.gn8.L4E.kVc')
        btn.click()
        randdelay(2, 4)
        email_elem = self.browser.find_element_by_name('id')
        email_elem.send_keys(self.login_name)
        password_elem = self.browser.find_element_by_name('password')
        password_elem.send_keys(self.pw)
        password_elem.send_keys(Keys.RETURN)
        randdelay(2, 4)

    def runme(self, url, threshold=50):  # threshold = 스크롤바 횟수
        final_results = []
        previmages = []
        tries = 0
        try:
            self.browser.get(url)
            while threshold > 0:
                try:
                    results = []
                    images = self.browser.find_elements_by_tag_name("img")
                    if images == previmages:  # 이미지 중복 체크
                        tries += 1
                    else:
                        tries = 0
                    if tries > 20:
                        return final_results
                    for i in images:
                        src = i.get_property("src")  # src = 이미지 경로.jpg
                        if src:
                            if src.find("/236x/") != -1 or src.find("/474x/") != 1:
                                print(src)
                                src = src.replace("/236x/", "/736x/")
                                src = src.replace("/474x/", "/736x/")
                                results.append(u_to_s(src))

                    previmages = copy.copy(images)
                    final_results = list(set(final_results + results))
                    dummy = self.browser.find_element_by_tag_name('a')
                    dummy.send_keys(Keys.PAGE_DOWN)  # 스크롤바 내림
                    randdelay(0, 1)
                    threshold -= 1
                except StaleElementReferenceException:
                    threshold -= 1
        except (socket.error, socket.timeout):
            pass
        return final_results

    def close(self):
        # 브라우저 닫기
        self.browser.close()


def main():
    # 아이디 입력
    PINTEREST_USERNAME = "phs950501@nate.com"
    # 비밀번호 입력
    PINTEREST_PASSWORD = "bsrdbftlz1"
    # sys.argv는 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리이다.
    # sys.argv[0]는 입력받은 값 중에서 파이썬 프로그램 이름인 .py이므로 필요 없는 값이다.
    # if len(sys.argv) > 1:
    #     trem = sys.argv[1]
    # else:
    #     exit()
    ph = PinterestHelper(PINTEREST_USERNAME, PINTEREST_PASSWORD)  # 초기화 밎 크롬 연결
    sleep(3)
    ph.login()  # 로그인
    sleep(3.2)
    is_url = urllib.parse.urlparse(term)
    # is_url.scheme  = 'https'  , is_url.netloc = www.pinterest.co.kr
    if is_url.scheme and is_url.netloc:
        images = ph.runme(term)
    else:
        images = ph.runme('http://pinterest.com/search/pins/?q=' + urllib.parse.quote(term))
    print(images)
    ph.close()
    type(images[1])

    f = open(term+'_pins.txt' , 'w')
    for i in images:
        f.write('\n'.join([i.decode('UTF-8') for i in images]))
    f.close()

    # with open(term.replace(" ", "") + "_pins.txt", "w") as file:
    #     file.write('\n'.join([i.decode('UTF-8') for i in images]))
    # if len(sys.argv) > 2:
    #     destination = sys.argv[2]
    # else:
    #     destination = "./" + term.replace(" ", "")
    #
    # print(term, destination)
    # # 서브프로세스. shell결과를 파일에 저장
    # call('aria2c -i ./{}_pins.txt -d {} --continue --auto-file-renaming false'.format(term.replace(" ", ""),
    #                                                                                   destination),
    #      shell=True)

if __name__ == '__main__':
    main()
