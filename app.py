from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated movie list
movies = [
    {'id': 1, 'name': 'Inception'},
    {'id': 2, 'name': 'The Dark Knight'},
    {'id': 3, 'name': 'Interstellar'}
]

# Simulated reviews for each movie
reviews = {
    1: [  # Inception reviews
        {'source': 'IMDb', 'rating': 8.8, 'comment': 'Great plot!'},
        {'source': 'Rotten Tomatoes', 'rating': 86, 'comment': 'Brilliant visuals.'}
    ],
    2: [  # The Dark Knight reviews
        {'source': 'IMDb', 'rating': 9.0, 'comment': 'Best superhero movie.'},
        {'source': 'Rotten Tomatoes', 'rating': 94, 'comment': 'Gripping and thrilling.'}
    ],
    3: [  # Interstellar reviews
        {'source': 'IMDb', 'rating': 8.6, 'comment': 'Mind-bending sci-fi!'},
        {'source': 'Rotten Tomatoes', 'rating': 72, 'comment': 'Visually stunning, but confusing at times.'}
    ]
}

# Home page - List of movies
@app.route('/')
def home():
    return render_template('home.html', movies=movies)

# Movie reviews page - Aggregated reviews for a selected movie
@app.route('/movie/<int:movie_id>')
def movie_reviews(movie_id):
    movie = next(movie for movie in movies if movie['id'] == movie_id)
    movie_reviews = reviews.get(movie_id, [])
    return render_template('movie_reviews.html', movie=movie, reviews=movie_reviews)

# Submit a review for a specific movie
@app.route('/movie/<int:movie_id>/submit', methods=['POST'])
def submit_review(movie_id):
    source = request.form['source']
    rating = request.form['rating']
    comment = request.form['comment']
    
    new_review = {'source': source, 'rating': float(rating), 'comment': comment}
    reviews[movie_id].append(new_review)
    
    return redirect(url_for('movie_reviews', movie_id=movie_id))

# Search movies by name
@app.route('/search')
def search_movie():
    query = request.args.get('query')
    result = [movie for movie in movies if query.lower() in movie['name'].lower()]
    return render_template('search_results.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)