import fresh_tomatoes
import media

# Defining instances of class Movie

sons_of_anarchy = media.Movie("Sons of Anarchy",
                              "American crime drama television series about motorcycle club ",
                              "http://stuffpoint.com/sons-of-anarchy/image/119317-sons-of-anarchy-sons-of-anarchy-poster.jpg",
                              "https://www.youtube.com/v=FXjbllOSUnQ")


avatar = media.Movie("Avatar",
                     "A marine on a allien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


spy_movie = media.Movie("Spy",
                        "A comedy about CIA agents",
                        "https://upload.wikimedia.org/wikipedia/en/5/5d/Spy2015_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=YrY3v1eDmQY")


prison_break = media.Movie("Prison break",
                           "Brother saving brother from the dead row",
                           "https://upload.wikimedia.org/wikipedia/en/4/46/Prison_Break_season_1_dvd.jpg",
                           "https://www.youtube.com/watch?v=3zxSwYyb2Vk")


transformers = media.Movie("Transformers",
                           "Story about alien robots",
                           "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                           "https://www.youtube.com/watch?v=KrUhwet0ngg")


selena = media.Movie("Selena",
                     "Biography of Mexican singer",
                     "http://www.mediacircus.net/selena________3.jpg",
                     "https://www.youtube.com/watch?v=EVMSuZXEz4s")

# Array of the movies
movies = [sons_of_anarchy,avatar,spy_movie,prison_break,transformers,selena]

# Call the function open_movie_page from fresh_tomatoes file
# which takes an array of the movies
fresh_tomatoes.open_movies_page(movies)


