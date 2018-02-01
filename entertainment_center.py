import media
import fresh_tomatoes


'''
this is where i create each instance of the class Movie and add it to the movies list
'''

movies = []

tank_girl = media.Movie("Tank Girl",
                        "Lori Petty, Ice-T, punk rock, beer, whatever.",
                        "https://www.movieposter.com/posters/archive/main/95/MPW-47507",
                        "https://www.youtube.com/watch?v=YbtrrKpRYqM")

movies.append(tank_girl)

only_lovers = media.Movie("Only Lovers Left Alive",
    					"Vampire art weirdos.",
    					"https://fiu-assets-2-syitaetz61hl2sa.stackpathdns.com/static/use-media-items/17/16872/full-1400x1875/56702dda/Only-Lovers-Print-Ad.jpeg",
    					"https://www.youtube.com/watch?v=ycOKvWrwYFo")

movies.append(only_lovers)

blade_runner = media.Movie("Blade Runner",
    					"Wait... am I a replicant?",
    					"https://www.movieposter.com/posters/archive/main/79/MPW-39919",
    					"https://www.youtube.com/watch?veogpIG53Cis")

movies.append(blade_runner)

labyrinth = media.Movie("Labyrinth",
    					"Magical Bowie nightmareland with Muppets!",
    					"https://www.movieposter.com/posters/archive/main/79/MPW-39960",
    					"https://www.youtube.com/watch?vC7qThslyK-Q")

movies.append(labyrinth)

pacific_rim = media.Movie("Pacific Rim",
    					"Giant robots, giant monsters, Idris Elba.",
    					"https://i.pinimg.com/originals/8a/83/27/8a832775263ac0d97f4bd8d38edd218d.jpg",
    					"https://www.youtube.com/watch?v=K-ZcqwvQbas")

movies.append(pacific_rim)

hackers = media.Movie("Hackers",
    				"HACK THE PLANET!",
    				"https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5MzY1ODg3OF5BMl5BanBnXkFtZTcwMTY4MjkzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    				"https://www.youtube.com/watch?v=c32Vt8IDf5s")

movies.append(hackers)

fresh_tomatoes.open_movies_page(movies)