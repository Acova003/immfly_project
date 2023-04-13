import requests
from django.test import TestCase
from media_app.models import Movie, TVShow, Season, Episode


class APITestCase(TestCase):
    # Import the os module to get the MOVIEDB_API_KEY environment variable
    import os
    MOVIEDB_API_KEY = os.environ.get('MOVIEDB_API_KEY', '')

    def setUp(self):
        self.movie_url = 'https://api.themoviedb.org/3/movie/popular'
        self.tvshow_url = 'https://api.themoviedb.org/3/tv/popular'
        self.season_url = 'https://api.themoviedb.org/3/tv/85271/season/1'
        self.episode_url = 'https://api.themoviedb.org/3/tv/85271/season/1/episode/1'
        self.api_key = self.MOVIEDB_API_KEY
    def test_movie_api(self):
        params = {'api_key': self.api_key, 'language': 'en-US', 'page': 1}
        response = requests.get(self.movie_url, params=params)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data['results']), 0)
        self.assertIn('title', data['results'][0])
        self.assertIn('release_date', data['results'][0])
        self.assertIn('overview', data['results'][0])
        self.assertIn('poster_path', data['results'][0])
        self.assertIn('vote_average', data['results'][0])

    def test_tvshow_api(self):
        params = {'api_key': self.api_key, 'language': 'en-US', 'page': 1}
        response = requests.get(self.tvshow_url, params=params)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data['results']), 0)
        self.assertIn('title', data['results'][0])
        self.assertIn('original_language', data['results'][0])
        self.assertIn('overview', data['results'][0])
        self.assertIn('poster_path', data['results'][0])
        self.assertIn('vote_average', data['results'][0])
        self.assertIn('num_seasons', data['results'][0])

    def test_season_api(self):
        params = {'api_key': self.api_key, 'language': 'en-US'}
        response = requests.get(self.season_url, params=params)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data['episodes']), 0)
        self.assertIn('season_number', data['episodes'][0])

    def test_episode_api(self):
        params = {'api_key': self.api_key, 'language': 'en-US'}
        response = requests.get(self.episode_url, params=params)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('name', data)
        self.assertIn('overview', data)
        self.assertIn('air_date', data)
        self.assertIn('vote_average', data)
