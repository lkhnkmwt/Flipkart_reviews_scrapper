from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def page1(searchstring):
            flipkart_url="https://www.flipkart.com/search?q="+searchstring
            flipkartPage=urlopen(flipkart_url)
            flipkart_html=bs(flipkartPage.read(),"html.parser")
            # bigboxes=flipkart_html.find_all("div",{"class":"_1AtVbE col-12-12"})
            bigboxes = flipkart_html.find_all("div", {"class": "_13oc-S"})
            # del bigboxes[0:2]
            # del bigboxes[5:]
            reviews = []
            sno=1
            for box in bigboxes:
                productlink="https://www.flipkart.com"+ box.div.div.a['href']
                prodRes=urlopen(productlink)
                prod_html=bs(prodRes.read(),"html.parser")
                commentboxes=prod_html.find_all('div',{'class':'_16PBlm'})
                del commentboxes[6:]
                # table=db[searchstring]
                for commentbox in commentboxes:

                    try:
                        # productnametag=box.div.div.a.find_all('div',{'class':'_4rR01T'})
                        productname=prod_html.find_all('h1',{'class':'yhB1nd'})[0].span.text
                        # productname=productnametag[0].text

                    except:
                        productname='No name'


                    try:
                        # pricetag=box.find_all('div',{'class':"_30jeq3 _1_WHN1"})
                        # price=pricetag[0].text
                        price=prod_html.find_all('div',{'class':'_30jeq3 _16Jk6d'})[0].text
                    except:
                        price="price not mentioned"
                    try:
                        name=commentbox.div.div.find_all('p',{'class':'_2sc7ZR _2V5EHH'})[0].text
                    except:
                        name='No name'
                    try:
                        rating= commentbox.div.div.div.div.text
                    except:
                        rating = "no rating"
                    try:
                        commenthead=commentbox.div.div.div.p.text
                    except:
                        commenthead="no comment heading"
                    try:
                        contag =commentbox.div.div.find_all('div',{'class':""})
                        custcomment=contag[0].div.text
                    except:
                        custcomment="no customer comment"
                    mydict={
                        "sno":sno,"product":searchstring,"price":price,"productname":productname, "name":name,"rating":rating,"commenthead":commenthead,"comment":custcomment
                    }
                    # x=table.insert_one(mydict)
                    reviews.append(mydict)
                    sno+=1

            return 'results.html',reviews,searchstring