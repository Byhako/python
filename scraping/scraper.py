import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'
XPATH_LINK_ARTICLE = '//h2[@class="headline"]/a/@href'
XPATH_TITLE = '//h1[@class="headline"/a/text()]'
XPAHT_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="articleWrapper  "]/p[not[@class]]/text()'


def parse_home():
    try:
        response = requests.get(HOME_URL)

        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_ARTICLE) # lista de links
            print(f'Links:\n{links}')
        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()