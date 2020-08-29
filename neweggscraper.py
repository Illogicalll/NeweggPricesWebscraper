# Importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import time

# Defining Variables for later use (allowing user to choose if they want to see the results of the webscraping just in the spreadsheet or in the terminal too)
incorrectInput = True
terminalOutput = False


# Setting up the spreadsheet output
filename = "products.csv"
f = open(filename, "w")
headers = "Name, Price\n"
f.write(headers)

# Inputting URL, downloading page and then opening the HTML
url = 'https://www.newegg.com/global/uk-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1582767'
while incorrectInput == True:
    userChoice = input("Would you like to use your own Newegg link (Y/N)")
    if userChoice == "Y":
        url = input("Please enter your chosen Newegg link: ")
        incorrectInput = False
    elif userChoice == "N":
        print("Choice confirmed, proceeding with default link")
        incorrectInput = False
    else:
        print("------------Please input either Y or N------------\n")
incorrectInput = True
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

for i in range(3):
    time.sleep(0.3)
    print(".", end = "")
print("\n")

# Allowing user to choose whether they want terminal output or not
while incorrectInput == True:
    userChoice2 = input("Would you like the results of the webscraping to be printed in the terminal (Y) or just the spreadsheet (N): ")
    if userChoice2 == "Y":
        terminalOutput = True
        incorrectInput = False
    elif userChoice2 == "N":
        terminalOutput = False
        incorrectInput = False
    else:
        print("-----------------------------------------Please input either Y or N-----------------------------------------\n")

for i in range(3):
    time.sleep(0.3)
    print(".", end = "")
print("\n")

# HTML parsing
page_soup = bs(page_html, "html.parser")

# The webscraping loop itself, which finds out the name and price of the product and then either outputs it to a spreadsheet, or the terminal and a spreadsheet
containers = page_soup.findAll("div", {"class":"item-container"})
container = containers[0]
if terminalOutput == True:
    for i in range (len(containers)):
        container = containers[i]
        pricecontainer = (container.find("li", {"price-current"}))
        print(container.img["title"])
        print("£"+(str(pricecontainer.strong)).lstrip("<strong>").rstrip("</strong>")+(str(pricecontainer.sup)).lstrip("<sup>").rstrip("</sup>"))
        f.write(str(container.img["title"]).replace(",", " ") + "," + "£"+ str((str(pricecontainer.strong)).lstrip("<strong>").rstrip("</strong>")+(str(pricecontainer.sup)).lstrip("<sup>").rstrip("</sup>")).replace(",", ".") + "\n")
        print("\n")
        i += 1
else:
    for i in range (len(containers)):
        container = containers[i]
        pricecontainer = (container.find("li", {"price-current"}))
        f.write(str(container.img["title"]).replace(",", " ") + "," + "£"+ str((str(pricecontainer.strong)).lstrip("<strong>").rstrip("</strong>")+(str(pricecontainer.sup)).lstrip("<sup>").rstrip("</sup>")).replace(",", ".") + "\n")
        i += 1
container = containers[0]

# Closing the spreadsheet so that it can be viewed by the user
f.close()

# Confirmation message notifying the user that the webscraping has been completed
print("Done.")

