from selenium import webdriver
from datetime import datetime

# URL = "https://www.google.com/maps/@49.8372773,24.0014289,17z/data=!5m1!1e1"
URL = "https://www.google.com/maps/@49.8373341,24.0601454,16.18z/data=!5m1!1e1"

def make_screenshot():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(executable_path='./chromedriver',
                              chrome_options=options)
    driver.get(URL)

    driver.save_screenshot(f"S-{datetime.now().strftime('%Y-%m-%dT%H-%M')}.png")

    driver.close()


if __name__ == "__main__":
    make_screenshot()
