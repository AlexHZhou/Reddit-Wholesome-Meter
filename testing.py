import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.reddit.com/r/wholesomememes/comments/dgz1n8/wholesome_hotel_horn/')

continueSpam = True
while continueSpam:
    if response:
        print('Success accessing server!')
        continueSpam = False
    else:
        print('Problem accessing server.', response.status_code)

    response = requests.get('https://www.reddit.com/r/wholesomememes/comments/dgz1n8/wholesome_hotel_horn/')
# print(response.text)
# print(response.json())
# print(response.headers);

soup = BeautifulSoup(response.text, 'html.parser')
soup.prettify()
print(soup.p)