import pandas as pd
import random

# Extended movie dataset
data = {
    'Movie': [
        'The Matrix', 'John Wick', 'Speed', 'The Notebook',
        'Titanic', 'Avengers', 'Iron Man', 'Doctor Strange',
        'Interstellar', 'Inception', 'La La Land', 'Gladiator'
    ],
    'Genre': [
        'Action', 'Action', 'Action', 'Romance',
        'Romance', 'Action', 'Action', 'Action',
        'Sci-Fi', 'Sci-Fi', 'Romance', 'Action'
    ],
    'Year': [
        1999, 2014, 1994, 2004,
        1997, 2012, 2008, 2016,
        2014, 2010, 2016, 2000
    ],
    'Rating': [
        8.7, 7.4, 7.2, 7.8,
        7.9, 8.0, 7.9, 7.5,
        8.6, 8.8, 8.0, 8.5
    ]
}

df = pd.DataFrame(data)

# Function to recommend movies
def recommend_movies(search_term):
    search_term = search_term.lower().strip()
    
    # Surprise recommendation
    if search_term == "surprise me":
        movie = df.sample(1).iloc[0]
        print(f"\n🎬 Surprise Movie: {movie['Movie']} ({movie['Year']}) - {movie['Genre']} - Rating: {movie['Rating']}")
        return
    
    # Search by genre or partial movie name
    results = df[df['Genre'].str.lower().str.contains(search_term) | 
                 df['Movie'].str.lower().str.contains(search_term)]
    
    if not results.empty:
        # Sort by rating (highest first)
        results = results.sort_values(by="Rating", ascending=False)
        print(f"\nRecommended movies matching '{search_term}':")
        for _, row in results.iterrows():
            print(f"- {row['Movie']} ({row['Year']}) - {row['Genre']} - Rating: {row['Rating']}")
    else:
        print("\n❌ No matches found. Try another search term.")

# User interaction
print("🎥 Welcome to the Advanced Movie Recommendation System!")
print("You can search by genre, movie name, or type 'surprise me' for a random pick.")
print("Example searches: Action, Romance, Inception, Sci-Fi, Titanic\n")

while True:
    search = input("Enter a search term (or 'exit' to quit): ")
    if search.lower() == "exit":
        print("\nGoodbye! 🎬")
        break
    recommend_movies(search)
