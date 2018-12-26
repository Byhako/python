from common import config
import news_pages_objects as news
import argparse
import datetime
import logging
import csv
import re  # expresiones regulares

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# expresiones regulares
is_well_formed_link = re.compile(r'^https?://.+/.+$')  # http://example.com/hello
is_root_path = re.compile(r'^/.+$')  # /some-text

def _new_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    logger.info(' Beginning scraper for -->  {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)
    articles = []



    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)

        if article:
            logger.info('Article fetched!')
            articles.append(article)
            break

    _save_articles(news_site_uid, articles)




def _fetch_article (news_site_uid, host, link):
    logger.info('Start fetching article at {}'.format(link))

    article = None
    try:
        article = news.ArticlePage(news_site_uid, _build_link(host, link))
    except (HTTPError, MaxRetryError) as err:
        logger.warning('Error while fetching the article', exc_info=False)

    if article and article.body:
        logger.warning('Invalid article. There is not body.')
        return None

    return article


def _build_link(host, link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host, link)
    else:
        return '{host}/{uri}'.format(host=host, uri=link)


def _save_articles(news_sites_uid, articles):
    now = datetime.datetime.now().strftime('%y_%m_%d')
    out_file_name = '{}_{}_articles.csv'.format(news_sites_uid, now)

    csv_headers = list(filter(
        lambda property: not property.startswith('_'),
        dir(articles[0])
    ))

    with open(out_file_name, mode='w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()['news_sites'].keys())
    
    parser.add_argument('news_sites',
                        help='The new site that you want to scrappe',
                        type=str,
                        choices=new_sites_choices)
    
    args = parser.parse_args()
    _new_scraper(args.news_sites)
