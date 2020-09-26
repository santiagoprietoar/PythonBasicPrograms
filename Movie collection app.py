'''
As a user I'd like to:
a. Add new movies to my collection -> So I can keep track of all my movies.
b. List all the movies of my collection -> So I can see what movies I already have.
c. Find a movie by using the movie title -> So I can locate a specific movie easily when the collection grows.

'''

# Incomplete app!

MENU_PROMPT = "\nEnter '1' to add a movie, '2' to see your movies, '3' to find a movie by title, or '0' to quit: "
movies = []


# Function for Adding movies
def add_movie():
    #Input of the values of the movie
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    #Adding the movie to the list
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    #Showing what the user just added
    print(f"You just added: \n  Title: {title}\n  Director: {director}\n  Year: {year}")

# Function for Listing movies
def listing_movies():
    print("\nMovie list: \n") #Shows the structure the list is gonna print
    for movie in movies:
        print(f"Title: {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")
        print(" ")


# Function for Finding movies
def find_movie():
    movie_wanted = input("What movie are you looking for? ")
    for movie in movies:
        if movie['title'] == movie_wanted:
            print(f"Title: {movie['title']}")
            print(f"Director: {movie['director']}")
            print(f"Year: {movie['year']}")
            print(" ")

# Function for menu
user_options = {
    '1': add_movie,
    '2': listing_movies,
    '3': find_movie,
}

def user_menu():
    selection = input(MENU_PROMPT)
    while selection != '0':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# User menu function at the end to run the program

user_menu()