"""The Foursquare API service

A while ago, I made a Foursquare Python program that used Bs4 and Requests to web scrape the data from their website.
Recently, I have been craving to work with another API. So basically, this will be the last program but in terms of
functionality, on steroids.
"""

from api_requests.category_requests import CategoryRequest
from api_requests.venue_actions_requests import VenueActionRequest
from api_requests.venue_info_requests import VenueInfoRequest


def access_input(acceptable_inputs, user_input):
    if user_input in [possible_input.lower() for possible_input in acceptable_inputs]:
        return user_input
    else:
        print("Try again.")
        return False


def handle_input(acceptable_inputs):
    is_valid = False
    while not is_valid:
        is_valid = access_input(acceptable_inputs, input().lower())
    return is_valid


def user_searching_loop(category_id=None):
    while True:
        # Save searched venue names
        searched_venue_names = list()

        # User instructions.
        print("Please enter the search keywords.")

        # Get user search.
        user_search = input().lower()

        # The user wants to search through the venues.
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
    global user_valid_input, program_end
    # Ask Q1.
    print("Would you like to search for a venue or look for a venue category? \n" +
          "Enter 'v' for venue or 'vc' for venue category.")
    # Get answer to Q1.
    user_valid_input = handle_input(['v', 'vc'])
    # Carry out response to users request.
    if user_valid_input == 'v':

        output = user_searching_loop()

        if type(output) == bool:
            program_end = output
        elif type(output) == str:
            user_valid_input = output

    elif user_valid_input == 'vc':

        # Save category names
        category_names = list()

        # The user wants to search through venue categories.
        for category_data_dict in new_category_request.get_all_categories().get('categories'):
            print(category_data_dict.get('name'))
            category_names.append(category_data_dict.get('name'))

        # User instructions.
        print("\nEnter the name of the category you would like to search in.")
        user_valid_input = handle_input(category_names)

        print("Perfect!")
        for category_data_dict in new_category_request.get_all_categories().get('categories'):
            if category_data_dict.get('name') == user_valid_input:
                searched_category_id = category_data_dict.get('id')
                break
        else:
            searched_category_id = None

        output = user_searching_loop(searched_category_id)

        if type(output) == bool:
            program_end = output
        elif type(output) == str:
            user_valid_input = output


if __name__ == '__main__':

    # Define user quit variable
    program_end = False

    # Set up category requests.
    new_category_request = CategoryRequest()

    # Set up venue action requests.
    new_venue_action_request = VenueActionRequest()

    # Set up venue info request.
    new_venue_info_request = VenueInfoRequest()

    # Welcome user.
    print("Welcome to my Foursquare API service! \n\n")

    # All the steps for the user to select a venue.
    user_selects_venue()

    print("Great! I can provide you with details, hours, events, links, tips and menus for your venue! "
          "Which one would you like?")
    user_selected_venue = user_valid_input
    user_valid_input = handle_input(['details', 'hours', 'events', 'links', 'tips', 'menus'])
