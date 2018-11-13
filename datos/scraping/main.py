from common import config
import argparse
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def _new_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    logging.info(' Beginning scraper for -->  {}'.format(host))

    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()['news_sites'].keys())
    
    parser.add_argument('news_sites',
                        help='The new site that you want to scrappe',
                        type=str,
                        choices=new_sites_choices)
    
    args = parser.parse_args()
    _new_scraper(args.news_sites)