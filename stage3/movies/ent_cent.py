import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Storyline here",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://youtu.be/vwyZH85NQC4")

avatar = media.Movie('Avatar',
                    'Avatar Storyline here',
                    'https://upload.wikimedia.org/wikipedia/mk/c/c3/Avatar1.jpg',
                    'https://youtu.be/uZNHIU3uHT4')

man = media.Movie('What men talk about',
                    '12.8 million USD',
                    'http://ilarge.lisimg.com/image/1055545/740full-what-men-talk-about-poster.jpg',
                    'https://www.youtube.com/watch?v=LUMEiL4KsfY')

school_of_rock = media.Movie('School Of Rock',
                            'Overly enthusiastic guitarist Dewey Finn (Jack Black)',
                            'http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg',
                            'https://youtu.be/3PsUJFEBC74')

ratatouile = media.Movie('Ratatouile',
                        'Remy (Patton Oswalt), a resident of Paris, appreciates good',
                        'http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg',
                        'https://youtu.be/uVeNEbh3A4U')

hunger_games = media.Movie('The Hunger Games',
                            'In what was once North America, the Capitol of Panem maintains',
                            'http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC',
                            'https://youtu.be/LrXIG4oK7Ew')


movies = [toy_story, avatar, man, ratatouile, hunger_games, school_of_rock]
#fresh_tomatoes.open_movies_page(movies)
print media.Movie.__doc__
