import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.postgresql.org'


def scrapper():
    page = requests.get(url + "/docs/release/")
    soup = BeautifulSoup(page.content, 'html.parser')

    list_item = soup.select("ul.release-notes-list")[0]

    return json.dumps(dictify(list_item))


def dictify(ul):
    result = []
    for li in ul.find_all("li", recursive=False):
        key = next(li.stripped_strings)
        ul = li.find("ul")
        if ul:
            result.append({'release_version': key, 'releases': dictify(ul)})
        else:
            a = li.find('a')
            result.append({'version': key, 'release_notes': url + a['href']})

    return str(result)
    # return root == 'root' ? str(result) : result
