import undetected_chromedriver as uc

if __name__ == "__main__":
    print("Testing undetected-chromedriver...")
    driver = uc.Chrome()
    driver.get("https://automationexercise.com/login")
    print(f"Page Title: {driver.title}")
    driver.quit()
    print("Verification complete!")