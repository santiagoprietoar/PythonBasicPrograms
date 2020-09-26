'''
As a user I'd like to:
a. Add new movies to my collection -> So I can keep track of all my movies.
b. List all the movies of my collection -> So I can see what movies I already have.
c. Find a movie by using the movie title -> So I can locate a specific movie easily when the collection grows.

Implementation tasks:
a. Decide where to store movies in code.
    For now, store them in a python list. Problem, movie list gets deleted when the app ends. Improvement opportunity for later when i learn to manage databases.
b. Decide what data we want to store for each movie.
    We'll create a dictionary for each movie. 
    Concepts: title, director and release year.
c. Show the user a menu and let them pick an option.
    1. Get the user's input
    2. Run the loop and get their input again at the end.
d. Implement each requirement in turn, each as separate function.

e. Stop running the program when they type "q" in the menu.

IDEAS:
Usar el menu simplificado del video de Udem de mlg per car.
'''

# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
title = input("Enter the movie title: ")
director = input("Enter the movie director: ")
year = input("Enter the movie release year: ")

movies.append({
    'title': title,
    'director': director,
    'year': year
})


# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        pass
    elif selection == "l":
        pass
    elif selection == "f":
        pass
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!