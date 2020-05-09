from flask import Flask , request , jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/api',methods=['GET'])
def hello_world():
    l = []
    c={}
    uri = 'https://en.m.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory'
      
    content = requests.get(uri).content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable plainrowheaders sortable'}).tbody
    rows = table.find_all('tr')
    c['country'] = str(request.args['country'])
    
    for i in range(2,len(rows)-2):
            d = {}
            temp = rows[i].find_all('th')
            OverAllCases = rows[i].find_all('td')
            coutryName = temp[1].find('a')
            if c['country'] == coutryName.text:
                #d['Countries'] = coutryName.text
                d['TotalCases'] = OverAllCases[0].text.replace('\n','')
                #d['Deaths'] = OverAllCases[1].text.replace('\n','')
                #d['Recov'] = OverAllCases[2].text.replace('\n','')
                l.append(d)
                return jsonify(d)

                

    return jsonify(d)


if __name__ == '_main_':
    app.run()
