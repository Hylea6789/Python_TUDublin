#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

# Import libraru for URL
import urllib.request


# input of URL
url = input("enter an url : ")
response = urllib.request.urlopen(url)
page_data = response.read().decode('utf-8')
try:
    # gets the data of the page
    response = urllib.request.urlopen(url)
    page_data = response.read().decode('utf-8')

    # stores the data of the page in a file page.html
    with open("page.html", "w") as page_file:
        page_file.write(page_data)
    print("The data has been saved in page.html")

# if the URL is invalid, an error is raised
except:
    print("Something went wrong!")
