import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (khtml, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-language': 'en-US,en;q=0.9'

}
def get_page_content(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None

def extract_article(content):
    soup = BeautifulSoup(content, 'html.parser')
    articles = []

    for article in soup.find_all('div', class_="search-item"):
        title_dev = article.find('div', class_="search-txt")

        title = "no title found"
        link = "no link found"
        date = "no date found"
        description = "no description founs"

        if title_duv:
            title_tag = title_div.find('a')
            if title_tag:
                title = title_Tag.get_text(strip=True)
                link = title_tag['href']

                meta_ul = title_div.find('ul', class_='story-meta')
                if meta_ul:
                    date_li = meta_ul.find_all('li')[0]
                    if date_li:
                        date = date_li.get_text(strip=True)

                        description_tag = article.find(;p)
                        if description_tag:
                            description = description_tag.get_text(strip=True)

                        articles.append({
                            'Title': title,
                            'Link': link,
                            'date': date,
                            'description': description

                        })

                        return articles
                    def scrape_multiple_pages(base_url, num_pages):
                        all_articles = []
                        for page in range(1 ,num_pages + 1):
                            url = f"{base_url}/page/{page}"
                            print(f"scraping {url}...")
                            page_content = get_page_content(url)
                            if page_content:
                                articles = extract_article((page_content))
                                all_articles.extend(articles)
                            else:
                                print(f"Failed to retrieve content from {url}")

                            return all_articles
                        base_url = 'http://www.technewsworld.com/section/technology'
                        num_pages = 5
                        all_articles = scrape_multiple_pages(base_url, num_pages)
                        df = pd.DataFrame(all_articles)
                        df.to_csv('technewsworld_articles.csv', index=False)

                        print("Articles have been saved to technewsworld_articles.csv")