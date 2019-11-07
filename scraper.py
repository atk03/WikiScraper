from selenium import webdriver

url = ''
url = input("Enter wikipedia url: ")
if not url:
    # url examples
    url = "https://it.wikipedia.org/wiki/Attentato_di_via_Rasella"

driver = webdriver.Firefox()
driver.get(url)
title = driver.find_element_by_id("firstHeading").text
toc = driver.find_element_by_id("toc").text
content = driver.find_elements_by_tag_name('p')

file1 = open("myfile.txt", "w")
L = [title + " \n", toc + " \n"]
file1.writelines(L)
for p in content:
    file1.write(p.text + " \n")
file1.close()