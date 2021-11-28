from collections import Counter
import requests
from bs4 import BeautifulSoup


def count_words(paragraph):
    """
    Counts the 3 words, 4 words and 5 words count in a given paragraph
    Args:
        paragraph (str) : Paragraph of type str

    Returns:
        tuple : counts of words : 3 words, 4 words and 5 words
    """
    wc = Counter(len(word) for word in paragraph.split())
    return wc[3], wc[4], wc[5]


def search_wikipedia(wikipedia_url):
    """
    Searches wikipedia for all paragraphs and counts words average
    Args:
        wikipedia_url (str) : Valid wikipedia URL startswith "https://en.wikipedia.org/wiki/"
    Returns:
        str : Average words count
    """
    if not wikipedia_url.startswith('https://en.wikipedia.org/wiki/'):
        return 'Requested URL is not wikipedia URL! ' \
               'Please provide valid wikipedia URL (Ex: https://en.wikipedia.org/wiki/Earth)'
    paragraphs = []
    response = requests.get(wikipedia_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    body_content_div = soup.find('div', attrs={'id': 'bodyContent'})
    paragraphs_div = body_content_div.find_all('p')
    for paragraph in paragraphs_div:
        word_3, word_4, word_5 = count_words(paragraph.text)
        paragraphs.append({3: word_3, 4: word_4, 5: word_5})
    avg_word_3 = sum(p[3] for p in paragraphs) // len(paragraphs)
    avg_word_4 = sum(p[4] for p in paragraphs) // len(paragraphs)
    avg_word_5 = sum(p[5] for p in paragraphs) // len(paragraphs)

    return f'Output : 3-letter words: {avg_word_3}/paragraph. ' \
           f'4-letter words: {avg_word_4}/paragraph.' \
           f'5-letter words: {avg_word_5}/paragraph.'


if __name__ == '__main__':
    query = input('Enter wikipedia page? ')
    print(search_wikipedia(query))
