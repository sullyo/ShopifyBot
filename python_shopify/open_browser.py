from selenium import webdriver
import urllib
from bs4 import BeautifulSoup
import time



def main():
    start_time = time.time()
    options = webdriver.ChromeOptions();
    options.add_argument("user-data-dir=D:\\chromesesh\\exc")
    driver = webdriver.Chrome("C:/Users/sully/Documents/python_shopify/chromedriver.exe",chrome_options=options)
    driver.get("https://www.google.ca")
    shoeSize = input("Fix browser location, log into exclucity and enter shoe size: ")
    price = ["$299.99","$300.00"]
    x = True
    price_index = 0;
    #solve captcha?
    while(x):
        try:
            source = urllib.request.urlopen("https://shop.exclucitylife.com")
            parsed_html = BeautifulSoup(source, "html.parser")
            found_item = parsed_html.find(string=price[price_index])
            parent = found_item.find_parent("figure")
            productID = parent.find('a').get('href')
            productURL = "https://shop.exclucitylife.com" + productID +".xml"
            getxml = urllib.request.urlopen(productURL)
            parsed_xml = BeautifulSoup(getxml, "html.parser")
            found_size = parsed_xml.find("title",string=shoeSize)
            parent_of_found_size = found_size.find_parent()
            shopifyPID = parent_of_found_size.find("id")
            finalURL = "https://shop.exclucitylife.com/cart/" +shopifyPID.string + ":1"
            driver.get(finalURL)
            #print(finalURL)
            print("Adding to Cart")
            x = False
            input("Press Enter to finish...")
        except AttributeError:
            price_index = price_index + 1
            if (price_index == len(price)):
                price_index = 0
            print ("Unable to find item, will continue looking")
            print("--- %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
    #print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
