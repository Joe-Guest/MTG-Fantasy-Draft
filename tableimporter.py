import requests
import pandas as pd
from bs4 import BeautifulSoup

class dataTable:

  def getData(self, url):

    #Sets headers to pass to url
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}

    #Submits a request to the url passing previously defined headers
    response = requests.get(url, headers = headers)

    #Parses response into soup
    soup = BeautifulSoup(response.content, 'html5lib')

    #Retrieves table from url and stores it in an array
    table = soup.find_all('table', class_ = 'sortable-table')[0]

    #Creates dataframe from html 
    dataframe = pd.read_html(str(table))[0]

    #, infer_types=False
    #players = dataframe[1]
    #results = dataframe[3]
    #opponents = dataframe[5]

    return dataframe