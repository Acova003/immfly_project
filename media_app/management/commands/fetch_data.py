import requests
from django.test import TestCase
from django.core.management.base import BaseCommand
from media_app.models import Movie, TVShow, Season, Episode

class Command(BaseCommand):
    help = 'Fetch movie and TV show data from DBMovie API and save to database'

    def handle(self, *args, **options):
        # Import the os module to get the MOVIEDB_API_KEY environment variable
        import os

        # Fetch the movie and TV show data from the API
        # Base url for popular movies and parameters: Api key, language and page
        MOVIEDB_API_KEY = os.environ.get('MOVIEDB_API_KEY', '')
        movie_url = 'https://api.themoviedb.org/3/movie/popular?api_key={MOVIEDB_API_KEY}&language=en-US&page=1'
        movie_response = requests.get(movie_url)
        movie_data = movie_response.json()
        
        # Fetch the movie and TV show data from the API
        # Base url for popular TV shows and parameters: Api key, language and page
        tvshow_url = 'https://api.themoviedb.org/3/tv/popular?api_key={MOVIEDB_API_KEY}&language=en-US&page=1'
        tvshow_response = requests.get(tvshow_url)
        tvshow_data = tvshow_response.json()

        # Create Movie objects from the data and save them to the database
        for movie_data in movie_data:
            movie = Movie(
                title=movie_data['original_title'],
                release_date=movie_data['release_date'],
                overview=movie_data['overview'],
                poster_path=movie_data['poster_path'],
                vote_average=movie_data['vote_average'],
            )
            movie.save()

        # Create TVShow, Season, and Episode objects from the data and save them to the database
        for tvshow_data in tvshow_data:
            tvshow = TVShow(
                tv_id=tvshow_data['id'],
                title=tvshow_data['original_title'],
                language=tvshow_data['original_language'],
                release_date=tvshow_data['release_date'],
                overview=tvshow_data['overview'],
                poster_path=tvshow_data['poster_path'],
                vote_average=tvshow_data['vote_average'],
                num_seasons=tvshow_data['num_seasons'],
            )
            tvshow.save()

            for season_data in tvshow_data['seasons']:
                season = Season(
                    tvshow=tvshow,
                    season_number=season_data['season_number'],
                )
                season.save()

                for episode_data in season_data['episodes']:
                    episode = Episode(
                        season=season,
                        episode_number=episode_data['episode_number'],
                        title=episode_data['title'],
                        overview=episode_data['overview'],
                        air_date=episode_data['air_date'],
                    )
                    episode.save()

        # Print a message to indicate success
        self.stdout.write(self.style.SUCCESS('Successfully imported movie and TV show data'))

