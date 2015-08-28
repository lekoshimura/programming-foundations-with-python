import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on a alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

et = media.Movie(
    "E.T.",
    "After a gentle alien becomes stranded on Earth, the being is discovered and befriended by a young boy named Elliot",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcRGJHE2d9ETIgpONE3pUTXMcUoBMkahlppFmicaL8FG8ovE37x4",
    "https://www.youtube.com/watch?v=qYAETtIIClk"
    )

school_of_rock = media.Movie(
    "School of Rock",
    "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work",
    "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc"    
    )

movies = [toy_story, avatar, et, school_of_rock];
# fresh_tomatoes.open_movies_page(movies)
# print toy_story.VALID_RATINGS
print media.Movie.__doc__

