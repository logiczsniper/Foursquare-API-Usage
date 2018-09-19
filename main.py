"""The Foursquare API service

A while ago, I made a Foursquare Python program that used Bs4 and Requests to web scrape the data from their website.
Recently, I have been craving to work with another API. So basically, this will be the last program but in terms of
functionality, on steroids.
"""

from api_requests.category_requests import CategoryRequest
from api_requests.venue_actions_requests import VenueActionRequest
from api_requests.venue_info_requests import VenueInfoRequest


def access_input(acceptable_inputs, user_input):
    """
    This function serves as a general purpose tool to be used with input(). It will check if the user has entered one
    of the valid options in acceptable_inputs.

    :param acceptable_inputs: the acceptable response(s) that a user could give
    :type: list

    :param user_input: the actual user response
    :type: str

    :return: the user input (if the user input is in acceptable_inputs)
    :rtype: str

    :return: False (if the user input is not in acceptable_inputs)
    :rtype: bool
    """

    if user_input in [possible_input.lower() for possible_input in acceptable_inputs]:
        return user_input
    else:
        print("Try again.")
        return False


def handle_input(acceptable_inputs):
    """
    This function is used in conjunction with access_input() in order to repeatedly prompt the user for a valid response
    until a valid response is provided.

    :param acceptable_inputs: the acceptable response(s) that a user could give
    :type: list

    :return: the validated user input
    :rtype: str
    """

    is_valid = False
    while not is_valid:
        is_valid = access_input(acceptable_inputs, input().lower())
    return is_valid


def user_searching_loop(category_id=None):
    """
    This function is used whenever the user is given the option to have another task completed repeatedly until the user
    stops requesting information or quits.

    :param category_id: for certain loops, a specific category id is necessary. Those loops which need it should pass it
    as a parameter here. If no category id is specified, all categories will be searched.
    :type: str

    :return: the name of the venue that has been selected by the user
    :rtype: str
    """

    while True:

        searched_venue_names = list()
        print("Please enter the search keywords.")
        user_search = input().lower()

        for venue_data_dict in new_venue_action_request.search_venues(user_search, category_id=category_id).get(
                'venues'):
            print(venue_data_dict.get('name'))
            searched_venue_names.append(venue_data_dict.get('name'))

        if searched_venue_names == list():
            print("I could not find any venues with the searched keywords.\nIf you want to try again, please enter"
                  " 'ta'. If you want to quit, enter 'q'.")
            user_valid_input_inner = handle_input(['ta', 'q'])

            if user_valid_input_inner == 'q':
                print("Okay! Cya!")
                exit()
            elif user_valid_input_inner == 'ta':
                continue
        else:
            print("\nEnter the name of the venue you would like more information for.")
            user_valid_input_inner = handle_input(searched_venue_names)
            break

    return user_valid_input_inner


def user_selects_venue():
    """
    This is used with user_searching_loop() in order to get a user selected and valid venue.

    :return: the valid selected venue
    :rtype: str
    """

    print("Would you like to search for a venue or look for a venue category? \n" +
          "Enter 'v' for venue or 'vc' for venue category.")
    user_valid_input_inner = handle_input(['v', 'vc'])

    if user_valid_input_inner == 'v':
        output = user_searching_loop()

    else:
        category_names = list()

        for category_data_dict in new_category_request.get_all_categories().get('categories'):
            print(category_data_dict.get('name'))
            category_names.append(category_data_dict.get('name'))

        print("\nEnter the name of the category you would like to search in.")
        user_valid_input_inner = handle_input(category_names)
        print("Perfect!")

        for category_data_dict in new_category_request.get_all_categories().get('categories'):
            if category_data_dict.get('name') == user_valid_input_inner:
                searched_category_id = category_data_dict.get('id')
                break
        else:
            searched_category_id = None

        output = user_searching_loop(searched_category_id)

    return output


def process_response(raw_response, response_type):
    """
    Accept a dictionary full of scattered info and based on the response_type, convert the information into usable
    text.

    :param raw_response: the complete response from the api
    :type: dict

    :param response_type: the type of dictionary raw_response is. If it is one that corresponds to 'hours',
    response_type should be set to 'hours'.
    :type: str

    :return: readable data extracted from the raw_response.
    :rtype: str
    """

    readable_output = str()

    if response_type == 'hours':

        try:
            weekday_times = raw_response.get('hours').get('timeframes')[0].get("open")[0]
            readable_output += f'Monday-Friday: {weekday_times.get("start")} to {weekday_times.get("end")}'
            weekend_times = raw_response.get('hours').get('timeframes')[1].get("open")[0]
            readable_output += f'\nSaturday+Sunday: {weekend_times.get("start")} to {weekend_times.get("end")}'
        except TypeError:
            readable_output += 'I am sorry, but there are no registered open hours for the selected venue!'

    elif response_type == 'events':
        readable_output += f'Number of events: {raw_response.get("events").get("count")}'

    elif response_type == 'links':

        for item in raw_response.get('links').get('items'):
            if item.get('url') is not None:
                readable_output += item.get('url') + '\n'

        if readable_output == str():
            readable_output = 'I am sorry, no links have been connected to your searched venue!'

    elif response_type == 'tips':

        try:
            readable_output += f'Tip: \n{raw_response.get("tips").get("items")[0].get("text")}'
        except IndexError:
            readable_output += 'I am sorry, there are no registered tips for your searched venue.'

    elif response_type == 'menu':
        readable_output += f'Number of menus: {raw_response.get("menu").get("menus").get("count")}'

    return readable_output


def get_venue_info(venue_name, requested_info):
    """
    First, the function converts the venue name into the corresponding venue id. Using this id and requested_info, it
    gets the information requested by the user. With this, it converts the dictionary into a more presentable way and
    prints this to the console.

    :param venue_name: the name of the valid user selected venue
    :type: str

    :param requested_info: one of ['hours', 'events', 'links', 'tips', 'menu'].
    :type: str
    """

    for venue_data_dict in new_venue_action_request.search_venues().get('venues'):
        if venue_data_dict.get('name').lower() == venue_name.lower():
            searched_venue_id = venue_data_dict.get('id')
            break

    else:
        raise Exception("Searched venue id could not be found!")

    user_requested_info = new_venue_info_request.get_venue_item(searched_venue_id, requested_info)
    print(process_response(user_requested_info, requested_info))


def user_gets_info():
    """
    Enter a loop allowing the user to get all information they want.
    """

    print("Great! I can provide you with hours, events, links, tips and a menu for your venue! "
          "Which one would you like?")

    while True:

        user_valid_input = handle_input(['hours', 'events', 'links', 'tips', 'menu'])
        get_venue_info(user_selected_venue, user_valid_input)
        print("\nIf you want more information, please enter 'mi'. If you want to quit, enter 'q'.")
        user_valid_input = handle_input(['mi', 'q'])

        if user_valid_input == 'q':
            print("Okay! Cya!")
            exit()
        elif user_valid_input == 'mi':
            print("Okay! I can provide you with hours, events, links, tips and a menu for your venue! "
                  "Which one would you like?")
            continue


if __name__ == '__main__':
    # Set up request instances.
    new_category_request = CategoryRequest()
    new_venue_action_request = VenueActionRequest()
    new_venue_info_request = VenueInfoRequest()

    # Welcome user.
    print("Welcome to my Foursquare API service! \n\n")

    # User to select a venue.
    user_selected_venue = user_selects_venue()

    # With the selected venue, the user gets information.
    user_gets_info()
