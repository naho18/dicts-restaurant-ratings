"""Restaurant rating lister."""


# put your code here
import sys
filename = sys.argv[1]

def restaurant_ratings(filename):

    #reads ratings from file
    raw_restaurant_data = open(filename)

    #create dictionary
    restaurant_scores = {}

   # new_name, new_rating = add_restaurant_rating()
    #restaurant_scores[new_name.title()] = new_rating
    
    #stores restaurant and rating to dictionary

    for line in raw_restaurant_data:
        name, rating = line.strip().split(":")
        restaurant_scores[name] = rating

    #returns ratings in alphabetical order by restaurant
    menus_for_restuarant(restaurant_scores)


def add_restaurant_rating(restaurant_scores):
    """Allows user to add a new restaurant to the list"""

    is_new_add = raw_input("Do you want to add a restaurant?  Yes or No ")

    if is_new_add != "Yes":
        return restaurant_scores
    else:
        new_name = raw_input("What is the restaurant name? ")
        new_rating = raw_input("What is the new rating? ")
        while new_rating not in ["1","2","3","4","5"]:
            new_rating = raw_input("Please enter valid rating 1-5: ")

        restaurant_scores[new_name.title()] = new_rating

        return restaurant_scores


def alpha_restaurants(restaurant_scores):
    """Allows user to view alphabetical restaurant scores"""


    for restaurant, rating in sorted(restaurant_scores.items()):
        print "%s is rated at %s." % (restaurant, rating)


def menus_for_restuarant(restaurant_scores):
    """Allows user to select functions to call"""

    user_choice = "0"
    while user_choice != "3":

        user_choice = raw_input("""
        1. See all the ratings
        2. Add a new restaurant
        3. Quit
        """)

        if user_choice == "1":
            alpha_restaurants(restaurant_scores)
        elif user_choice == "2":
            add_restaurant_rating(restaurant_scores)
        elif user_choice == "3":
            break
        else:
            user_choice = raw_input("Please enter a valid input. ")







restaurant_ratings(filename)
