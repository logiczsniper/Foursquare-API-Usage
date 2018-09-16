"""Request for a category

The request here is:
get all categories
"""

from api_requests.base_request import FourSquareRequest


class CategoryRequest(FourSquareRequest):
    """
    Class that inherits from FourSquareRequest and holds python methods for API requests related to categories.
    """

    def __init__(self):
        """ Sets up inheritance """
        super().__init__()

    def get_all_categories(self):
        """
        Method that gets a dictionary containing info on all venue categories.

        :return: a huge data structure that contains a key called 'response' which corresponds to a value that contains
        all information on all the venue categories.
        :rtype: dict
        """

        self.base_url += 'venues/categories'
        response = self.my_get(self.base_url, self.base_querystring)

        return response
