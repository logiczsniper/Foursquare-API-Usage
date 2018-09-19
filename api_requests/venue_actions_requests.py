"""The requests here are more unique but still for venues

The requests here are:
get tips for a venue
search venues
"""

from api_requests.base_request import FourSquareRequest


class VenueActionRequest(FourSquareRequest):
    """
    Class that inherits from FourSquareRequest and holds python methods for API requests related to venue actions.
    """

    def __init__(self):
        """ Sets up inheritance """
        super().__init__()

    def search_venues(self, query=None, category_id=None):
        """
        This method searches for venues based on a query AND/OR category id.

        :param query: the term that the venue names will be searched with.
        :type: str

        :param category_id: the id of the category that the events will be searched from.
        :type: str

        :return: a data structure containing venues corresponding with the searched parameters.
        :rtype: dict
        """

        querystring = {**self.base_querystring, **{"near": "New York, NY", "query": query, "categoryId": category_id}}
        response = self.my_get(self.base_url + 'venues/search', querystring)

        return response

    def get_venue_tips(self, venue_id):
        """
        Gets tips about the venue from past visitors.

        :param venue_id: the venue id of the venue to get tips for.
        :type: str

        :return: a data structure containing between 0-10 tips for the specified venue.
        :rtype: dict
        """

        querystring = {**self.base_querystring, **{"sort": "popular", "limit": 10}}
        response = self.my_get(self.venue_url.format(venue_id)+"/tips", querystring)

        return response
