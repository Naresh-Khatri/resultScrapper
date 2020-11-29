from bs4 import BeautifulSoup
import bs4
import csv
from urllib.request import urlopen, Request

def getToken():
    url = 'https://jntuaresults.ac.in/view-results-56736322.html'

    request = Request(url)
    request.add_header("Cookie", "_ga=GA1.3.1774447704.1597145128; _gid=GA1.3.1722252444.1603729361; PHPSESSID=i7cqrbal15jffpol8ilbic5oj3; _gat_gtag_UA_133494275_1=1")

    uClient = urlopen(request)
    page_html = uClient.read()
    uClient.close()

    page_soup = str(BeautifulSoup(page_html, 'html.parser'))
    start_index = int(page_soup.find('accessToken'))

    access_token = page_soup[start_index +14: start_index+21]
    print('acess token acquired -  ' +  access_token)
    return access_token

for i in range(1,200):

    if len(str(i)) == 1:
        htn = '19fh1a040' + str(i)
    elif len(str(i)) == 3:
        htn = '19fh1a04a' + str(100-i)
    else:
        htn = '19fh1a04' + str(i)

    url = 'https://jntuaresults.ac.in/results/res.php?ht=' + htn + '&id=56736322&accessToken=' + getToken()
    headers = 'Cookie: _ga=GA1.3.1774447704.1597145128; _gid=GA1.3.1722252444.1603729361; PHPSESSID=i7cqrbal15jffpol8ilbic5oj3; _gat_gtag_UA_133494275_1=1'

    request = Request(url)
    request.add_header("Cookie", "_ga=GA1.3.1774447704.1597145128; _gid=GA1.3.1722252444.1603729361; PHPSESSID=i7cqrbal15jffpol8ilbic5oj3; _gat_gtag_UA_133494275_1=1")

    uClient = urlopen(request)
    page_html = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page_html, 'html.parser')

    table = page_soup.find('table')
    if(table):
        rows = table.findAll('tr')

        name_index = str(page_soup).find('Student name')
        table_index = str(page_soup).find('table')
        name = str(page_soup)[name_index + 18:table_index-6]
        print(name)
        f = open('results.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([f'{name} ({htn})'])
        f.close()

        data =[]

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])


            tup = (cols)
            f = open('results.csv', 'a', newline='')
            writer = csv.writer(f)
            writer.writerow(tup)
            f.close()

        data.pop(0)
        data.pop(-1)

        print(data)
