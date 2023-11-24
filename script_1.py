
# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# %%

driver = webdriver.Chrome()
driver.get("https://techwithtim.net")
print(driver.title)

# %%
driver.quit()
# %%
