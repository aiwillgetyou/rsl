print("""Name: Keremsah K.
Studentnr: 500694326
Study: Digital Driven Business
Level: Master
University: HVA
Professor: Rob Loke

Assignment bookletRaspberryPi: Building a recommender system on a raspberry pi (version 1.0.6)


My favorite movies:
1. Arrival
2. Captain Fantastic
3. 300

Building a recommendationsystem(RS) for movies in PostgresQL.

For this assignment, a recommendationsystem was build on a RaspberryPI via PostgreSQL(PSQL).
A dataset of 5229 movies was scraped in advance from metacritic.com, which then was copied into a PSQL table.
Based on my favorite movies, natural language processing technqiues were used to rank movies based on 
similarities from between either summary OR Title OR Starring for my favorite movies and the rest.


1. Results Arrival with Summary (see topRecommendationsArrivalSummary.csv).
Based on the first movie ´Arrival' 44 unique movies were suggested ranging with ranking between 0.5 till 1.

The top 3 movies next that the recommendation system suggested where: Midnight run, Battleship, The Vow.
After analyzing the contents of these movies, I could not spot any similarities in terms of whether the movies
would be interesting movies for me to watch.

Arrival is a movie about extraterrestrial life that suddenly appears on earth. Battleship movies, has the greatest
similarities wrt the contents of Arrival Movie. However, the movie is rather a sci-fi action movie, while Arrival is more a drama.
Moreover, the remaining movies (Midnight run and the vow, are rather romance and comedy movies.

From the terminal the inital SQL can be called by: psql test -f RecommendationsSummaryArrival.sql

2. Results Captain Fantastic with Starring (see topRecommendationsCaptainFantasticStarring.csv)
Unfortunately 0 results were given by the RS.

From the terminal the inital SQL can be called by: psql test -f RecommendationsStarringCaptainFantastic.sql

3. Results 300 with title (see topRecommendations300Title.csv)
Again, 0 results were given by the RS. Probably due to the name of the movie.

From the terminal the inital SQL can be called by: psql test -f RecommendationsTitle300.sql""")

Print(''' now comes the python part

For this part I used my favorite movie: Arrival

There are two python scripts and and 3 output files
1. python script: filter.py --> output files: authorRecommend.csv, authorReview.csv *dependency userReviews all three parts.csv, but exluded due to its size
I ran the filter.py script on my RPI. The time that the script takes to run is 142 seconds. I assume that this is much quicker if I utilized my laptop's computing power
See filter.py scrip for comments about the interpretation.

The authorReview.csv file output is 248
Meaning 248 authors reviewed my favorite movie(arrival)

the authorRecommend.csv file output is 1732
These are reviews of other movies from all the authors that reviewed my favorite movies.
Also, the reviews have a greater Metascore than was given for the movie arrival.
This difference can also be observed via the 'diff' column


2. python script: sentimentMovie.py --> files: finalRecommend.csv *dependecy authorRecommend.
I ran the sentimentMovie.py on my RPI. The time to the script takes to run is 19.3 seconds.
see sentimentMovie.py scrip for comments about the interpretation.

The finalRecommend.csv file output is 1732 as well.
This is a similar file as authorRecommend.
Additionally, for this script pattern.en package was downloaded and used to calculat positivity level (0 to 1) and objectivity (0 to 1)
Also, connection with postgreSQL database was made via psycopg2 package. The script script creates a table if not exists yet and
copies the finalRecommend file into the database.

If you have any questions regarding this assignment, please feel free to ask me.
''')
