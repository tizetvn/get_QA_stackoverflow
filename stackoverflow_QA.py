#!/usr/bin/env python3
'''
Viết script lấy top N câu hỏi được vote cao nhất của tag LABEL
trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất
Link API: https://api.stackexchange.com/docs
'''

import requests
import sys
import json

api_url = 'https://api.stackexchange.com/2.2/questions?pagesize=' \
          '{}&order=desc&sort=votes&tagged={}&site=stackoverflow'


def get_n_questions(N, tag):
    return json.loads(requests.get(api_url.format(N, tag)).text)['items']


def main():
    N = '20'
    tag = 'python'
    for num, question in enumerate(get_n_questions(N, tag)):
        print('{}. {} - ''Vote link: {}'.format(
            num+1, question['title'], question['link']))


if __name__ == "__main__":
    main()
