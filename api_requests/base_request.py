"""The basic request in the form of a super class

Holds basic information required by each request to the Foursquare API
"""


from requests import get
from client_data import ClientData


class FourSquareRequest:
    """
    This is the base class for all of the FourSquare requests that will be made. It mainly holds common strings and the
    query string (dict) that will be used in almost all requests.
    """

    def __init__(self):
        """ Save special urls and my authentication """
        self.base_url = 'https://api.foursquare.com/v2/'
        self.venue_url = self.base_url + "venues/{}"
        self.base_querystring = {"client_id": ClientData.CLIENT_ID, "client_secret": ClientData.CLIENT_SECRET,
                                 "v": "20180323"}

    @staticmethod
    def my_get(url, querystring):
        """
        A small method that is used in every single request child. With this, only this file needs to import requests
        which is more organised and efficient.

        :param url: the endpoint that the get request will be made to.
        :type: str

        :param querystring: the dictionary of parameters that will be passed into the get request.
        :type: dict

        :return: the response from the api, more specifically, the text attribute with the information.
        :rtype: dict
        """

        return get(url, params=querystring).text
