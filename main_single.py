# -*- coding: utf-8 -*- #

"""
"""

import os
import pickle
import requests
import mechanicalsoup
from bs4 import BeautifulSoup

# fire IFTTT if remaining money is under THRESHOLD
THRESHOLD = 10000

loginpageURL = "https://mp.seikyou.jp/mypage/Static.init.do"

id = ""
password = ""
event_name = ""
ifttt_token = ""



def get_page():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(loginpageURL)
    browser.select_form()
    browser["loginId"] = id
    browser["password"] = password
    resp = browser.submit_selected()
    html = resp.text
    return html


def get_remaining(html):
    soup = BeautifulSoup(html, 'html.parser')
    remaining = soup.find(id="point_zandaka").span.get_text().strip().replace(",", "")
    return remaining


def send_ifttt(remaining):
    url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event_name, ifttt_token)
    print(url)
    params = {"value1": remaining}
    requests.post(url, data=params)


def job():
    remain = get_remaining(get_page())
    if THRESHOLD > int (remain):
        send_ifttt(remain)


if __name__ == '__main__':
    try:
        prog_dir = os.path.dirname(__file__)
        cred_path = os.path.join(prog_dir, "credential.pkl")
        with open(cred_path, "rb") as f:
            cred = pickle.load(f)
            id = cred["id"]
            password = cred["password"]
            event_name = cred["event_name"]
            ifttt_token = cred["ifttt_token"]
            job()
    except Exception as e:
        raise FileNotFoundError("valid credential file not found")
