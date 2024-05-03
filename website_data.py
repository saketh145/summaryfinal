import requests 
from bs4 import BeautifulSoup 


def scrape(url):
    URL = url
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
    # Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link. 

    r = requests.get(url=URL, headers=headers) 
    if r.status_code ==200:
        # print(r.content)

        soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib 
        # print(soup.prettify()) 
        # b = soup.find_all('p','ul li')
        # for yy in b:
        #     print(yy.get_text())
        flag = 0;
        enter = """
    """
        str = ""
        body = soup.body.find_all()
        for tag in body:
            if tag.name=='p' or tag.name=='h1' or tag.name=='h2' or tag.name=='h3' :
                str += tag.get_text() 
                str += enter
                if tag.name=='p':
                    flag=1

            elif (tag.name == 'ul' or tag.name=='ol') and flag==1:
                liBody=tag.find_all('li')
                for text in liBody:    
                    str+=text.get_text()
                    str += enter
        # print(str)
        # print(soup.body.get_text())
        return str
    else:
        return ""