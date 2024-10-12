from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

print("Automated IP renewal script by Germanized")

try:
    driver.get("http://192.168.0.1")
    time.sleep(2)

    try:
        password_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]')
        print("Login page detected. Proceeding with login...")

        password_box.send_keys("PUT UR PASSWORD HERE SO SELENIUM CAN SEND THE KEYSTROKES TO THE SITE")
        print("Password entered.")

        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/a')
        login_button.click()
        print("Login button clicked.")
        
        time.sleep(5)

        try:
            error_message = driver.find_element(By.CLASS_NAME, 'content.error-tips-content')
            if "Incorrect password" in error_message.text:
                print("Login failed: Incorrect password.")
        except:
            print("Login successful.")

    except Exception as e:
        print("Already logged in or login page not detected. Proceeding to IP renewal...")

    time.sleep(2)
    navigator_icon = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[5]/a/span[1]')
    navigator_icon.click()
    print("Navigated to advanced settings.")

    time.sleep(2)

    internet_settings_link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li[2]/ul/li[2]/a/span[2]')
    internet_settings_link.click()
    print("Navigated to advanced internet settings.")

    time.sleep(2)

    release_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[8]/div[2]/div[1]/a')
    release_button.click()
    print("Clicked the release button.")

    time.sleep(5)
    renew_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[6]/div[2]/div[1]/a')
    renew_button.click()
    print("Clicked the renew button.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
