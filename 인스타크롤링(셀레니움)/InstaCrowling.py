
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

# 검색할 유저 아이디 검색
uesr_id = "gongtho"


# 갱신시간을 위해 딜레이를 줌
def randdelay(a, b):
    time.sleep(random.uniform(a, b))


# 유니코드 정규화
def u_to_s(uni):
    return unicodedata.normalize('NFKD', uni).encode('ascii', 'ignore')


class Insta(object):

    def __init__(self, login_name, pw, download=True):
        #생성자 사용시 사용할 변수 선언
        self.login_name = login_name
        self.pw = pw
        self.download = download
        #크롬 드라이버 파일경로 설정
        self.browser = webdriver.Chrome('C:\chromedriver.exe')
        #인스타 url
        self.browser.get("https://www.instagram.com/")
        self.browser.implicitly_wait(5)

    def login(self):
        #페이스북으로 로그인 버튼 클릭
        #CLASS 같은 경우에는 공백 . 으로 이어주면 됨
        btn = self.browser.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
        #버튼 클릭
        btn.click()
        randdelay(2, 4)
        #아이디 비밀번호 입력란에 값 입력
        email_elem = self.browser.find_element_by_name('email')
        email_elem.send_keys(self.login_name)
        password_elem = self.browser.find_element_by_name('pass')
        password_elem.send_keys(self.pw)
        password_elem.send_keys(Keys.RETURN)
        randdelay(2, 4)




    def runme(self, url, threshold=20):  # threshold = 스크롤바 횟수
        final_results = []
        prevcontent = []
        tries = 0

        try:
            self.browser.get(url)
            # 게시물 하나 클릭
            content_btn = self.browser.find_element_by_class_name('_9AhH0')
            # 버튼 클릭
            content_btn.click()
            randdelay(2, 4)
            while threshold > 0:
                try:
                    results = []
                    content = self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span")
                    real_content = content.text  # real_content : 게시물과 댓글
                    print(real_content)
                    results.append(real_content)
                    final_results = list(set(final_results + results))
                    next = self.browser.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow')
                    next.click()  # 다음 버튼
                    randdelay(0, 1)
                    threshold -= 1
                except :
                    threshold -= 1
        except (socket.error, socket.timeout):
            pass
        return final_results

    def close(self):
        # 브라우저 닫기
        self.browser.close()


def main():
    # 페이스북 아이디 입력
    INSTA_USERNAME = "아이디"
    # 페이스북 비밀번호 입력
    INSTA_PASSWORD = "비밀번호"
    # sys.argv는 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리이다.
    # sys.argv[0]는 입력받은 값 중에서 파이썬 프로그램 이름인 .py이므로 필요 없는 값이다.
    # if len(sys.argv) > 1:
    #     trem = sys.argv[1]
    # else:
    #     exit()
    ph = Insta(INSTA_USERNAME, INSTA_PASSWORD)  # 초기화 밎 크롬 연결
    sleep(3)
    ph.login()  # 로그인
    sleep(3.2)
    is_url = urllib.parse.urlparse(uesr_id)
    # is_url.scheme  = 'https'  , is_url.netloc = www.instagram.com/
    if is_url.scheme and is_url.netloc:
        content = ph.runme(uesr_id)
    else:
        content = ph.runme('https://www.instagram.com/' + urllib.parse.quote(uesr_id))

    print(content)
    ph.close()
    #
    # f = open(uesr_id+'_pins.txt' , 'w')
    # for i in content:
    #     f.write('\n'.join([i.decode('UTF-8') for i in content]))
    # f.close()

    # with open(uesr_id.replace(" ", "") + "_pins.txt", "w") as file:
    #     file.write('\n'.join([i.decode('UTF-8') for i in content]))
    # if len(sys.argv) > 2:
    #     destination = sys.argv[2]
    # else:
    #     destination = "./" + uesr_id.replace(" ", "")
    #
    # print(uesr_id, destination)
    # # 서브프로세스. shell결과를 파일에 저장
    # call('aria2c -i ./{}_pins.txt -d {} --continue --auto-file-renaming false'.format(uesr_id.replace(" ", ""),
    #                                                                                   destination),
    #      shell=True)

if __name__ == '__main__':
    main()
