import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
    "A story of a boy and his toy",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline
#toy_story.show_trailer()
movies = [toy_story]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
