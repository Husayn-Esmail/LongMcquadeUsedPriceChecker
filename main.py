from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import datetime
import logging
import tqdm
import sys
import summarize


if __name__ == '__main__':
    """
    For now the search query must be exact so that the search only returns a single product.
    """
    logging.basicConfig(level=logging.WARNING)
    n = len(sys.argv)
    filename = ""
    search_query = ""
    if n == 3:        
        if sys.argv[1] == '-f':
            filename = sys.argv[2]  
            products = summarize.find_products(filename)
            print(len(products))
            for item in products:
                print(item)
        else:
            logging.ERROR("Invalid Argument")
            sys.exit()
    elif n == 2:
        search_query = sys.argv[1]
        # the web scraping portion
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        lm = webdriver.Chrome(options=chrome_options)
        lm.get("https://www.long-mcquade.com/")
        actions = ActionChains(lm)

        logging.debug(lm.current_url)

        searchbar = lm.find_element(By.ID, "SearchTxt")
        searchbar.send_keys(search_query)
        searchbar.send_keys(Keys.RETURN)
        
        logging.debug(lm.current_url)

        # how do you know you're getting the right product? 
        product = lm.find_element(By.CLASS_NAME, "products-item")

        if search_query in product.text:
            product.click()

        used = lm.find_element(By.XPATH, '//a[contains(@href, "instore_stock")]')
        used.click()

        # once you're on the product listing
        demo_btn = lm.find_elements(By.CLASS_NAME, "demo-available")
        num_stores = len(demo_btn)
        for store in tqdm.tqdm(range(num_stores), desc="working...", ascii=False, ncols=75):
            demo = demo_btn[store]
            # lm.execute_script("arguments[0].scrollIntoView();", demo)
            lm.execute_script("arguments[0].click();", demo)
            # time.sleep(2) # need to give time for action to complete
            # demo.click()
            # time.sleep(2) # need to give time for click consequence to complete becuase it's same page


        # save the data for external processing.
        page_source = lm.page_source
        now = datetime.datetime.now()
        filename = f"{search_query}_{str(now.date())}.txt"
        f = open(filename, "w")
        f.write(page_source.strip())
        f.close()

        products = summarize.find_products(filename)
        for item in products:
                print(item)
    else:
        print("""Usage:
            python3 main.py [search query]
            python3 main.py -f [filename]""")
