import requests
from django.core.management.base import BaseCommand
from media_app.models import Movie, TVShow, Season, Episode

class Command(BaseCommand):
    help = 'Fetch movie and TV show data from DBMovie API and save to database'

    def handle(self, *args, **options):
        # Import the os module to get the MOVIEDB_API_KEY environment variable
        import os
        MOVIEDB_API_KEY = os.environ.get('MOVIEDB_API_KEY', '')

        # Define the base URLs for the API endpoints
        movie_url = 'https://api.themoviedb.org/3/movie/popular?api_key={MOVIEDB_API_KEY}&language=en-US&page=1'
        tvshow_url = 'https://api.themoviedb.org/3/tv/popular?api_key={MOVIEDB_API_KEY}&language=en-US&page=1'
        season_url = 'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}?api_key={MOVIEDB_API_KEY}&language=en-US'
        episode_url = 'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key={MOVIEDB_API_KEY}&language=en-US'

        # Fetch movie data from the API
        movies_response = requests.get(movie_url)
        movies_data = movies_response.json()

        # Create Movie objects from the data and save them to the database
        for movie_data in movies_data:
            movie = Movie(
                title=movie_data['original_title'],
                release_date=movie_data['release_date'],
                overview=movie_data['overview'],
                poster_path=movie_data['poster_path'],
                vote_average=movie_data['vote_average'],
            )
            movie.save()

        # Fetch the TV show data from the API
        tvshows_response = requests.get(tvshow_url)
        tvshows_data = tvshows_response.json()

        # Create TVShow, Season, and Episode objects from the data and save them to the database
        for tvshow_data in tvshows_data:
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


        # Fetch the season data from the API
        seasons_response = requests.get(season_url)
        seasons_data = seasons_response.json()

        for season_data in seasons_data['seasons']:
            season = Season(
                tvshow=tvshow,
                season_number=season_data['season_number'],
            )
            season.save()

        # Fetch episode data from the API
        episodes_response = requests.get(episode_url)
        episodes_data = episodes_response.json()

        for episode_data in episodes_data['episodes']:
            episode = Episode(
                season=season,
                episode_number=episode_data['episode_number'],
                name=episode_data['name'],
                overview=episode_data['overview'],
                air_date=episode_data['air_date'],
                vote_average=episode_data['vote_average'],
            )
            episode.save()

        # Print a message to indicate success
        self.stdout.write(self.style.SUCCESS('Successfully imported movie and TV show data'))

