"""The GET requests for venue information

All the requests for venue information are in this file. These are:
get details
get hours   -
get menus   -
get links   - All of these are built
get events  - into get_venue_item()
get similar -
get next    -
"""

import requests
from api_requests.base_request import FourSquareRequest


class VenueInfoRequest(FourSquareRequest):
    """
    Class that inherits from FourSquareRequest and holds python methods for API requests related to getting venue info.
    """

    def __init__(self):
        """ Sets up inheritance """
        super().__init__()

    def get_venue_details(self, venue_id):
        """
        Gets large amount of details for the specified venue.

        :param venue_id: the venue id to get details of.
        :type: str

        :return: a data structure containing all relevant information for the specified venue.
        :rtype: dict
        """

        response = requests.get(self.venue_url.format(venue_id), params=self.base_querystring)

        return response.text

    def get_venue_item(self, venue_id, item):
        """
        Has many functions, depending on the item passed. The item parameter could be one of:
        "hours", "menu", "links", "events", "similar" or "nextvenues".

        :param venue_id: the venue id of the venue to be used.
        :type: str

        :param item: the information required by the user. Possible options specified above.
        :type: str

        if item == "hours":
            :return: a data structure containing the open hours on the open days of the venue.
        elif item == "menu":
            :return: a data structure containing the menu, if there is one, of the venue.
        elif item == "links":
            :return: a data structure containing links supplied by the provider for more information for the venue.
        elif item == "events":
            :return: a data structure containing information on events held at the venue.
        elif item == "similar":
            :return: a data structure containing information on venues similar to the specified venue.
        elif item == "nextvenues":
            :return: a data structure containing information on the next recommended venue to visit.

        :rtype: dict
        """

        response = requests.get(self.venue_url.format(venue_id) + "/" + item, params=self.base_querystring)

        return response.text
