from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd

def run():
    the_path = 'test.csv'
    create_file(the_path)
    df = pd.DataFrame(columns=['email', 'link'], index=[0])
    df.to_csv(the_path, mode='w', header=True)

    process = CrawlerProcess(get_project_settings())
    process.crawl('emails', path=the_path, reject=[]) 
    process.start()

    print('Cleaning emails...')
    df = pd.read_csv(the_path, index_col=0)
    df.columns = ['email', 'link']
    df = df.drop_duplicates(subset='email')
    df = df.reset_index(drop=True)
    df.to_csv(the_path, mode='w', header=True)

def create_file(the_path):
    response = False

    with open(the_path, 'wb') as file: 
        file.close()

run()
