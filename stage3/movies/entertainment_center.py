import media #To create an instance we need to use a class Movie. It's store in media.py
import fresh_tomatoes # To open generated website we need to use frsh_tomatoes.py

# Creating an instance to show info about Toy Story
toy_story = media.Movie("Toy Story",
                        """Woody (Tom Hanks), a good-hearted cowboy doll who
                         belongs to a young boy named Andy (John Morris), sees
                         his position as Andy's favorite toy jeopardized when
                        his parents buy him a Buzz Lightyear (Tim Allen) action
                        figure. Even worse, the arrogant Buzz thinks he's a real
                         spaceman on a mission to return to his home planet.
                        When Andy's family moves to a new house, Woody and Buzz
                         must escape the clutches of maladjusted neighbor Sid
                        Phillips (Erik von Detten) and reunite with their boy.""",
                        "https://clck.ru/ApXoD",
                        "https://youtu.be/vwyZH85NQC4")

# Creating an instance to show info about Avatar
avatar = media.Movie('Avatar',
                    """On the lush alien world of Pandora live the Na'vi, beings
                     who appear primitive but are highly evolved. Because the
                    planet's environment is poisonous, human/Na'vi hybrids,
                    called Avatars, must link to human minds to allow for free
                    movement on Pandora. Jake Sully (Sam Worthington), a
                    paralyzed former Marine, becomes mobile again through one
                    such Avatar and falls in love with a Na'vi woman (Zoe
                    Saldana). As a bond with her grows, he is drawn into a
                    battle for the survival of her world.""",
                    'https://clck.ru/ApXoi',
                    'https://youtu.be/uZNHIU3uHT4')

# Creating an instance to show info about What Men Talk About
man = media.Movie('What men talk about',
                    """What Men Talk About is a 2010 Russian comedy written and
                     directed by Dmitriy Dyachenko, filmed in the genre of road
                    movie based on the Russian play Conversations middle-aged men
                     have about women""",
                    'https://clck.ru/ApXpf',
                    'https://www.youtube.com/watch?v=LUMEiL4KsfY')

# Creating an instance to show info about School Of Rock
school_of_rock = media.Movie('School Of Rock',
                            """Overly enthusiastic guitarist Dewey Finn (Jack
                            Black) gets thrown out of his bar band and finds
                            himself in desperate need of work.""",
                            'https://clck.ru/ApXpq',
                            'https://youtu.be/3PsUJFEBC74')

# Creating an instance to show info about Ratatouile
ratatouile = media.Movie('Ratatouile',
                        """Remy (Patton Oswalt), a resident of Paris, appreciates
                        good food and has quite a sophisticated palate. He would
                        love to become a chef so he can create and enjoy culinary
                        masterpieces to his heart's delight. """,
                        'https://clck.ru/ApXnY',
                        'https://youtu.be/uVeNEbh3A4U')

# Creating an instance to show info about Hunger Games
hunger_games = media.Movie('The Hunger Games',
                            """'The Hunger Games film series consists of four
                            science fiction dystopian adventure films based on
                            "The Hunger Games trilogy of novels, by the American
                            author Suzanne Collins""",
                            'https://clck.ru/ApXqD',
                            'https://youtu.be/LrXIG4oK7Ew')

#creating a list of all instances to go through while site loading
movies = [toy_story, avatar, man, ratatouile, hunger_games, school_of_rock]

#Run program
fresh_tomatoes.open_movies_page(movies)
