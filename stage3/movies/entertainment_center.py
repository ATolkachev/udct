import media
import fresh_tomatoes

# Creating an instance to show info about Toy Story
toy_story = media.Movie("Toy Story",
                        "Storyline here",
                        "https://clck.ru/ApXoD",
                        "https://youtu.be/vwyZH85NQC4")

# Creating an instance to show info about Avatar
avatar = media.Movie('Avatar',
                    'Avatar Storyline here',
                    'https://clck.ru/ApXoi',
                    'https://youtu.be/uZNHIU3uHT4')

# Creating an instance to show info about What Men Talk About
man = media.Movie('What men talk about',
                    '12.8 million USD',
                    'https://clck.ru/ApXpf',
                    'https://www.youtube.com/watch?v=LUMEiL4KsfY')

# Creating an instance to show info about School Of Rock
school_of_rock = media.Movie('School Of Rock',
                            'Overly enthusiastic guitarist Dewey Finn (Jack Black)',
                            'https://clck.ru/ApXpq',
                            'https://youtu.be/3PsUJFEBC74')

# Creating an instance to show info about Ratatouile
ratatouile = media.Movie('Ratatouile',
                        'Remy (Patton Oswalt), a resident of Paris, appreciates good',
                        'https://clck.ru/ApXnY',
                        'https://youtu.be/uVeNEbh3A4U')

# Creating an instance to show info about Hunger Games
hunger_games = media.Movie('The Hunger Games',
                            'In what was once North America, the Capitol of Panem maintains',
                            'https://clck.ru/ApXqD',
                            'https://youtu.be/LrXIG4oK7Ew')

#creating a list of all instances to go through while site loading
movies = [toy_story, avatar, man, ratatouile, hunger_games, school_of_rock]

#Run program
fresh_tomatoes.open_movies_page(movies)
