# Img-Extractor
Web scraper that allows a user to select whether they want to download all the images from a website or only the selected ones
<h4>
This code uses the <code>requests</code> library to send HTTP requests to the website and the <code>BeautifulSoup</code> library to parse the HTML response.
It finds all the <code>img</code> tags on the page and then prompts the user to choose whether they want to download all the images or only the selected ones.
If the user chooses to download all the images, it loops through the list of images and downloads each one.
If the user only wants to download selected images, it loops through the list of images and prompts the user for each one.
</h4>
