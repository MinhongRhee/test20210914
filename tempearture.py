from typing import Text
import requests
from bs4 import BeautifulSoup
from requests.models import Response

def callTemp():
    uri = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98%EB%82%A0%EC%94%A8&tqi=hRtvtwprvh8ssBmFKARssssstQl-338946"
    html = requests.get(uri).content
    soup = BeautifulSoup(html, 'html.parser')
    response = requests.get(uri)

    if(response.status_code == 200):
        target = soup.select_one("#main_pack .todaytemp")
        temp = { 'temp' : target.text }
        print(type(temp))
        print(temp)
        return temp

callTemp()