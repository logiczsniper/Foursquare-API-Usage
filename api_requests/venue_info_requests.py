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

        response = self.my_get(self.venue_url.format(venue_id), self.base_querystring)

        return response

    def get_venue_item(self, venue_id, item):
        """
        Has many functions, depending on the item passed. The item parameter could be one of:
        "hours", "menu", "links", "events", "similar" or "nextvenues".

        :param venue_id: the venue id of the venue to be used.
        :type: str

        :param item: the information required by the user. Possible options specified above.
        :type: str

        :return: a data structure containing the open hours on the open days of the venue. (item == "hours")
        :rtype: dict

        :return: a data structure containing the menu, if there is one, of the venue. (item == "menu")
        :rtype: dict

        :return: a data structure containing links for more information for the venue. (item == "links")
        :rtype: dict

        :return: a data structure containing information on events held at the venue. (item == "events")
        :rtype: dict

        :return: a data structure containing information on venues similar to the specified venue. (item == "similar")
        :rtype: dict

        :return: a data structure containing information on the next recommended venue to visit. (item == "nextvenues")
        :rtype: dict
        """

        response = self.my_get(self.venue_url.format(venue_id) + "/" + item, self.base_querystring)

        return response
