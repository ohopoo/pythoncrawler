import movie
import fresh_tomatoes

#Creating instances of my movie class with a list of my favorite movies.
throne_of_blood = movie.Movie("Throne of Blood",
                              ("http://ia.media-imdb.com/images/M/MV5BMTM1MTk2NDIzOV5B"
                               "Ml5BanBnXkFtZTcwMTA5ODQxMQ@@._V1_SY317_CR5,0,214,317_A"
                               "L_.jpg"),
                              "https://www.youtube.com/watch?v=PoYzsDVyFRU")

#Putthing the movies in a list to pass on to the script that creates our page.
movie_list = [throne_of_blood]


def main():
    #Creates the movies web page.
    fresh_tomatoes.open_movies_page(movie_list)

if __name__ == "__main__":
    main()
