import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.larepublica.co/'
XPATH_LINK_ARTICLE = '//text-fill[not(@class)]/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]//text-fill/a/text()'
XPAHT_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                # borro comillas dobles si las hay
                title = title.replace('\"', '')
                summary = parsed.xpath(XPAHT_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n\n')

            print('Success :)')

        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)

        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_ARTICLE) # lista de links
            today = datetime.date.today().strftime('%d-%m-%y')

            if not os.path.isdir(today):
                os.mkdir(today)

            for link in links:
                parse_notice(link, today)
        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    parse_home()