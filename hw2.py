from textblob import TextBlob
import random

movies = [
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "imdb": 9.0,
        "overview": "Batman fights crime and faces the Joker."
    },
    {
        "title": "Toy Story",
        "genre": "Animation",
        "imdb": 8.3,
        "overview": "Toys come alive when humans are not around."
    },
    {
        "title": "Titanic",
        "genre": "Romance",
        "imdb": 7.9,
        "overview": "A love story aboard a doomed ship."
    },
    {
        "title": "The Hangover",
        "genre": "Comedy",
        "imdb": 7.7,
        "overview": "Friends wake up after a wild night in Las Vegas."
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "imdb": 8.4,
        "overview": "Heroes unite to save the universe."
    }
]

moods = {
    "happy": ["Comedy", "Animation"],
    "excited": ["Action"],
    "romantic": ["Romance"]
}

def sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def show_movie(movie):
    print("\nTitle:", movie["title"])
    print("Genre:", movie["genre"])
    print("IMDb Rating:", movie["imdb"])
    print("Overview:", movie["overview"])
    print("Sentiment:", sentiment(movie["overview"]))

def random_recommendation():
    movie = random.choice(movies)
    show_movie(movie)

def genre_recommendation(genre):
    results = [m for m in movies if m["genre"].lower() == genre.lower()]

    if results:
        show_movie(random.choice(results))
    else:
        print("No movies found.")

def mood_recommendation(mood):
    if mood.lower() not in moods:
        print("Mood not available.")
        return

    genres = moods[mood.lower()]
    results = [m for m in movies if m["genre"] in genres]

    if results:
        show_movie(random.choice(results))
    else:
        print("No movies found.")

while True:
    print("\n=== AI Movie Recommendation System ===")
    print("1. Random Recommendation")
    print("2. Recommend by Genre")
    print("3. Recommend by Mood")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        random_recommendation()

    elif choice == "2":
        genre = input("Enter genre: ")
        genre_recommendation(genre)

    elif choice == "3":
        mood = input("Enter mood (happy/excited/romantic): ")
        mood_recommendation(mood)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")