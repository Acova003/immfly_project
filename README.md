# Setting up the project

-   Created a new Django project named `immfly_project`
-   Configured the project settings and installed required packages
-   Created a Django app named `media_app` to handle the media-related models and views
-   Created a database using the command-line tool `manage.py`.


# **Defining the models**

-   Defined the `Channel`, `Movie`, `TVShow`, `Season`, and `Episode` models to represent the media data
-   Created the database tables and relationships by running migrations
## Data Models and Relationships


-   Channel table with columns:
    
    -   `id` (primary key)
    -   `title` (CharField)
    -   `language` (CharField)
    -   `poster_image` (URLField)
    -   `description` (TextField)
    -   `maturity_rating` (CharField)
    -   `language` (CharField)
    - 
-   Movie table with columns:
    
    -   `id` (primary key, inherits from Channel)
    -   `duration` (PositiveIntegerField)
    -   `genre` (CharField)
-   TVShow table with columns:
    
    -   `id` (primary key, inherits from Channel)
    -   `num_seasons` (PositiveIntegerField)
    -   `tv_id` (PositiveIntegerField)
-   Season table with columns:
    
    -   `id` (primary key)
    -   `number` (PositiveIntegerField)
    -   `start_date` (DateField)
    -   `end_date` (DateField)
    -   `tvshow_id` (ForeignKey to TVShow)
-   Episode table with columns:
    
    -   `id` (primary key)
    -   `number` (PositiveIntegerField)
    -   `name` (CharField)
    -   `description` (TextField)
    -   `rating` (DecimalField)
    -   `season_id` (ForeignKey to Season)

## API used
To gather data on movies and TV, I used the 
[MovieDB API](https://developers.themoviedb.org/4/getting-started)


# **Implementing management commands**

-   Implemented a custom Django management command that fetches movie, TV show, season, and episode data from the MovieDB API and saves it to the database

# **Future work**
I need to build on my controller layer, create ratings calculations (export to cv) and create the front-end. 

## **Defining url endpoints**
Some endpoints require dynamic values based on the user's choices on the app. Here is an outline of the API endpoints that I would include in my controller: 

No parameters needed:
-   `/`: The choice of movies or TV shows is selected by the user on the homepage. 
-   `/movies/` 
-   `/tvshows/`  

    ----
  Parameters needed
  - `/movies/<movie_id>/`: This URL displays the content page for a specific movie. The `movie_id` parameter represents the ID of the movie of the movie chosen by the user. 
-   `/tvshows/<tvshow_id>/`: The `tvshow_id` parameter is passed in the URL to identify which TV show the user wants to see detailed information about. The value of this parameter comes from the user selecting a TV show (and it's id) from the list of all TV shows. 
    
-   `/tvshows/<tvshow_id>/seasons/`: The `tvshow_id` parameter is passed in the URL to identify which TV show the user wants to see a list of all the seasons for.  
    
-   `/tvshows/<tvshow_id>/seasons/<season_number>/`: The `tvshow_id` and `season_number` The values of these parameters come from the user selecting a season from the list of all the seasons for a specific TV show.  
    
-   `/tvshows/<tvshow_id>/seasons/<season_number>/episodes/`: The `tvshow_id` and `season_number` The values of these parameters come from the user selecting a season from the list of all the seasons for a specific TV show. 
    
-   `/tvshows/<tvshow_id>/seasons/<season_number>/episodes/<episode_number>/`: The `tvshow_id`, `season_number`, and `episode_number`  The values of these parameters come from the user selecting an episode from the list of all the episodes for a specific season of a specific TV show. 

**Hierarchy**
All endpoints are Channels if it doesn't involve a detail page. Content pages are `/movies/<movie_id>/` for movie content and `/tvshows/<tvshow_id>/seasons/<season_number>/episodes/<episode_number>/` for episode content. 


## Calculating  ratings

1. I would create a `calculate_ratings.py file`  to calculate the average rating by :
	- Summing up all the ratings of the episodes
	- Dividing by the total number of episodes
2. Using the built-in csv module, I would create a list of rows to be exported to a CSV file with ratings in descending order. 
3. Finally, I would write each row to my CSV file

This would be handled and exported by a new management command 

## Ideas for groups
Movies and TV shows can be bridged together in tables through a genre. Some content might even have multiple genres. This would establish many-to-many relationships between titles. 

## Testing 

I would implement more tests, especially if going to production. These are some things that I would test: 

- API endpoints
- Rating calculations algorithm
- Exporting the CSV file
- Test the channel/group relationship
- Test the models

# Takeaways

This was my first time using Django and I loved it. Usually I've only built small personal projects with Flask. I feel like it was intuitive and the in-built database was easy to configure. The bulk of my time was spent learning how Django works. Although I only spent a few days coding my app, I believe that I would feel confident using Django fairly quickly. 

There are lots of fun ways that I could improve user experience after my MVP is done (keeping in mind that Immfly entertainment doesn't have user login):

-	It's dinner time and a user paused their movie. Enabling sessions can make it possible for our customers to continue watching a movie at the point where they left off. 

-	It's been a long travel day and our customers find it difficult to find the mental capacity to search through our large catalogue of movies. We could create a short quiz to help suggest entertainment. 
-	We could also create a family friendly catalogue. Parents can rest easy knowing that their young children can find and watch media that's appropriate for them. 

Thank you for the opportunity to work on this take home evaluation. I look forward to speaking more to my experience with this project as well as other valuable skills and experience that I could bring to Immfly. 




