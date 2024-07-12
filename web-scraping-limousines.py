from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("chromedriver")
driver = webdriver.Chrome(service=service)

def scroll_down(driver):
    # Scroll down in intervals and wait for new content to load
    initial_scroll_height = 3.3
    subsequent_scroll_height = 2.8
    scroll_pause_time = 2
    screen_height = driver.execute_script("return window.screen.height;")
    
    # Initial scroll
    driver.execute_script("window.scrollBy(0, {});".format(screen_height * initial_scroll_height))
    time.sleep(scroll_pause_time)
    
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    
    while True:
        # Subsequent scrolls
        driver.execute_script("window.scrollBy(0, {});".format(screen_height * subsequent_scroll_height))
        time.sleep(scroll_pause_time)
        
        # Calculate new scroll height and compare with the current height
        new_scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if new_scroll_height == scroll_height:
            # Try to click the load more button if available
            try:
                load_more_button = driver.find_element(By.ID, "btnToLoadMorePost")
                load_more_button.click()
                time.sleep(scroll_pause_time)
                new_scroll_height = driver.execute_script("return document.body.scrollHeight;")
            except Exception as e:
                print("No load more button found or error clicking the button:", e)
                break
        scroll_height = new_scroll_height

try:
    driver.get("https://www.limousineworldwide.directory/search_results")

    # Scroll down to load all elements
    scroll_down(driver)

    # Wait for the elements to be loaded
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "member-search-full-name"))
    )

    # Find the elements
    limousine_elements = driver.find_elements(By.CLASS_NAME, "member-search-full-name")

    # Extract and print the names
    limousine_names = [element.text for element in limousine_elements]
    for name in limousine_names:
        print(name)

finally:
    driver.quit()
