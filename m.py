import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)
OMDB_API_KEY = "bc90a9a5"

@app.route('/')
def home():
    return "Welcome to the NetBear. Use /search?title=<movie_title> to search for movies."

@app.route('/a1fb486106d9e0ec329f1b1fee7a7e86.txt')
def serve_txt():
    return send_file('a1fb486106d9e0ec329f1b1fee7a7e86.txt', mimetype='text/plain')

@app.route('/search')
def search_movie():
    title = request.args.get('title')
    if not title:
        return "Please provide a movie title using the 'title' query parameter."

    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    response = requests.get(url)
    data = response.json()

    if data.get('Response') == 'False':
        return "Movie not found."

    imdb_id = data.get('imdbID')
    if not imdb_id:
        return "Movie not found."

    embed_url = f"https://vidsrc.xyz/embed/movie/{imdb_id}"
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NetBear - Free Forever</title>
        <style>
            body {
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #000;
                color: #fff;
                font-family: Arial, sans-serif;
            }
            iframe {
                width: 80%;
                height: 80%;
                border: none;
            }
        </style>
    </head>
    <body>
        <iframe src="{{ embed_url }}" allowfullscreen></iframe>
    </body>
    </html>
    """
    return render_template_string(html_template, embed_url=embed_url)

if __name__ == '__main__':
    app.run(debug=True)
