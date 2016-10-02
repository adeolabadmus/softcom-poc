from threading import Thread
from xml.etree import cElementTree as parser

import requests


def get_results(query):
    thread_results = []
    nlm = Thread(target=process_nlm, args=('https://wsearch.nlm.nih.gov/ws/query?' +
                                           'db=digitalCollections&term=%s', query, thread_results))
    arx = Thread(target=process_arx, args=('http://export.arxiv.org/api/query?search_query=all' +
                                           '%s&start=0&max_results=10', query, thread_results))
    nlm.start()
    arx.start()

    while True:
        if len(thread_results) == 2:
            break

    rv = {}
    result = [res for gen in thread_results for res in gen]
    rv['result'] = result
    rv['query'] = query
    rv['length'] = len(result)
    return rv


def process_nlm(base_url, query, results):
    response = make_api_call(base_url, query)
    data = parse_nlm(response)
    results.append(data)


def process_arx(base_url, query, results):
    response = make_api_call(base_url, query)
    data = parse_arx(response)
    results.append(data)


def make_api_call(base_url, query):
    response = requests.get(base_url % query).text.encode('utf-8')
    return response


def parse_nlm(markup):
    root = parser.fromstring(markup)
    return ({'title': document[0].text, 'url': document.attrib.get('url')} for document in root[6])


def parse_arx(markup):
    root = parser.fromstring(markup)
    entry_id = '{http://www.w3.org/2005/Atom}entry'
    return ({'title': tag[3].text.replace('\n ', ' '), 'url': tag[0].text} for tag in root if tag.tag == entry_id)
