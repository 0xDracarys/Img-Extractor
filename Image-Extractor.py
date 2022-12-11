import requests
from bs4 import BeautifulSoup

# Prompt the user to enter the URL of the website they want to scrape
url = input("Enter the URL of the website you want to scrape: ")

# Send a GET request to the website and parse the response using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all the img tags on the page
images = soup.find_all("img")

# Ask the user if they want to download all the images or only the selected ones
download_all = input("Do you want to download all the images? [y/n]: ")

# If the user wants to download all the images, loop through the list of images and download each one
if download_all.lower() == "y":
    for image in images:
        # Get the URL of the image
        img_url = image["src"]

        # Send a GET request to download the image
        img_response = requests.get(img_url)

        # Save the image to a local file
        with open("image.jpg", "wb") as f:
            f.write(img_response.content)

# If the user only wants to download selected images, loop through the list of images and prompt the user for each one
else:
    for image in images:
        # Get the URL of the image
        img_url = image["src"]

        # Prompt the user if they want to download the current image
        download = input(f"Do you want to download {img_url}? [y/n]: ")

        # If the user wants to download the image, download it
        if download.lower() == "y":
            # Send a GET request to download the image
            img_response = requests.get(img_url)

            # Save the image to a local file
            with open("image.jpg", "wb") as f:
                f.write(img_response.content)
