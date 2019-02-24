from selenium import webdriver
import requests
import time
import os

driver = webdriver.Chrome('/usr/local/bin/chromeDriver')
imgLinks = []


#Link of the mainpage(with all the other links)
mainLink = "https://kissmanga.com/Manga/Go-Toubun-no-Hanayome"
imagexPath = '//*[@id="divImage"]/p[%s]/img'
imageName = '%s.JPEG'
counter = 0




directory = input("Inser the directory to download all the images: ")
pdfDirectory = input("Insert the direcoty to move the pdf to: ")
volLink = input("Insert the volume's link: ")
volNumber = input("Insert the volume Number:")

os.system("clear")

print("Are all the informations correct? ")
print("Images's direcotry:",directory)
print("Pdf's direcoty:",pdfDirectory)
print("The volume's link:",volLink)
print("The volume number is:",volNumber)

answer = input("(n/y) ")

if answer == "n":
    quit()
else:
    driver.get(volLink)
    time.sleep(15)

    for i in range(21):
        i+=1
        time.sleep(5)

        try:
            imgLinks.append(driver.find_element_by_xpath(imagexPath%(i)).get_attribute('src'))
        except:
            print("Failed to get the link for the",str(i),"page")
            continue

    print("Gathered all the link, moving to "+directory)
    os.chdir(directory)

    for link in imgLinks:

        if counter < 10:

            response = requests.get(link)

            with open("00%s.JPEG"%(counter),'wb') as image:
                image.write(response.content)

        if counter >= 10:
            response = requests.get(link)

            with open("0%s.JPEG"%(counter),'wb') as image:

                image.write(response.content)


        counter+=1

    os.system("convert *.JPEG Vol.%s.pdf"%(volNumber))