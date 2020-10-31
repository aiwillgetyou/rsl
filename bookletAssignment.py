print("""Name: Keremsah K.
Studentnr: 500694326
Study: Digital Driven Business
Level: Master
University: HVA

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