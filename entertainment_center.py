import media
import fresh_tomatoes

movies = []
# an empty list to store my movies

tank_girl = media.Movie(
    "Tank Girl",
    "Lori Petty, Ice-T, punk rock, beer, whatever.",
    "https://www.movieposter.com/posters/archive/main/95/MPW-47507",
    "https://www.youtube.com/watch?v=YbtrrKpRYqM")

movies.append(tank_girl)
# adding the tank_girl object to the empty list

only_lovers = media.Movie(
    "Only Lovers Left Alive",
    "Vampire art weirdos.",
    "https://fiu-assets-2-syitaetz61hl2sa.stackpathdns.com/static/use-media-items/17/16872/full-1400x1875/56702dda/Only-Lovers-Print-Ad.jpeg",
    "https://www.youtube.com/watch?v=ycOKvWrwYFo")

movies.append(only_lovers)
# adding the only_lovers object to the empty list

mirrormask = media.Movie(
    "MirrorMask",
    "It's all just a dream... or is it?",
    "http://www.impawards.com/2005/posters/mirrormask_xlg.jpg",
    "https://www.youtube.com/watch?v=swrcKRVgeGI")

movies.append(mirrormask)
# adding the mirrormask object to the empty list

labyrinth = media.Movie(
    "Labyrinth",
    "Magical Bowie nightmareland with Muppets!",
    "https://www.movieposter.com/posters/archive/main/79/MPW-39960",
    "https://www.youtube.com/watch?v=XRcOZZDvMv4")

movies.append(labyrinth)
# adding the labyrinth object to the empty list

pacific_rim = media.Movie(
    "Pacific Rim",
    "Giant robots, giant monsters, Idris Elba.",
    "https://i.pinimg.com/originals/8a/83/27/8a832775263ac0d97f4bd8d38edd218d.jpg",
    "https://www.youtube.com/watch?v=A85EtOalcsM")

movies.append(pacific_rim)
# adding the pacific_rim object to the empty list

hackers = media.Movie(
    "Hackers",
    "HACK THE PLANET!",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5MzY1ODg3OF5BMl5BanBnXkFtZTcwMTY4MjkzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=c32Vt8IDf5s")

movies.append(hackers)
# adding the hackers object to the empty list

fresh_tomatoes.open_movies_page(movies)
# calling the open_movies_page() function from fresh_tomatoes.py
# this opens the webpage in the user's browser
