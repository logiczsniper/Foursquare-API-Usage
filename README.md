# Foursquare API Project

#### Introduction
I once stumbled across the website [Foursquare](https://foursquare.com/). I happened to be learning how to webscrape with Requests and BeautifulSoup4, so I made a program that scraped certain information based off of user input. [Here](https://github.com/logiczsniper/Foursquare-webscraping-with-Bs4) it is in all it's glory (it is terribly plain). <br>
<br>
Fast forward to September 14th 2018. I was craving to work with a RESTful API, as I was recently introduced to the world of these APIs. While looking up lists of APIs, I discovered that Foursquare has an API and this project was born. <br>
<br>
This project is a command line program that prompts the user to select a venue, and allows them to request specific information for the venue. This information includes menus, open hours, events and more. Already it has way more functionality than the webscraping project, but it goes a bit further. You can change the area that the venues are located in and also search for venues by category. <br>
<br>
By no means is this a unique service- it is basically a complete downgrade from the website itself. However it was not created to be something new. It was simply made to practice working with a RESTful API, and I had fun doing it.

#### Running
For whatever reason, if you want this to run on your machine, you need Python 3 or greater and the Requests library. In addition, you have to set up a Foursquare app (which is free). Once you do this, you will have access to a client_id and a client_secret key. These should be stored in a file called `client_data.py` in the same directory as `main.py`. Your `client_data.py` should look like this:
```python3
class ClientData:

    CLIENT_ID = '|INSERT YOUR CLIENT_ID HERE|'
    CLIENT_SECRET = '|INSERT YOUR CLIENT_SECRET HERE|'
```
Run `main.py` to start the program!

#### Tools Used
* Pycharm CE
* cmder
* Postman

