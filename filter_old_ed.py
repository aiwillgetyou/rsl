# build a recommender system based on customer reviews
import pandas as pd
# read the csv file in a dataset
ratings = pd.read_csv('userReviews all three parts.csv', sep=';')
# create new dataframe with the given column names
column_names = ['movieName' , 'Metascore_w' , 'Author' , 'AuthorHref' , 'Date' , 'Summary' , 'InteractionsYesCount' , 'InteractionsTotalCount' , 'InteractionsThumbUp' , 'InteractionsThumbDown']
# create subset of reviews on your favorite movie
fav_movie = 'arrival'
# create a new dataframe to find customers who likes the favorite movie
consumers_who_likes_favorite_movie = pd.DataFrame(columns=column_names)
#loop all of the users that watched the same movie you like
for i in range(ratings.movieName.size):
    if ratings.movieName.iloc[i] == fav_movie:
        row = ratings[i:i + 1]
        consumers_who_likes_favorite_movie = consumers_who_likes_favorite_movie.append(row)
print("%d customers like the favorite movies %s" % (len(consumers_who_likes_favorite_movie), fav_movie))
# create a third dataframe to store all the movies that the user rated higher than 6
new_subset = pd.DataFrame(columns=column_names)
# find all the movies that rated by the same user and rated higher than 6
for i in range(ratings.movieName.size):
    if ratings.Author.iloc[i] in consumers_who_likes_favorite_movie.Author.values and ratings.movieName.iloc[i] != fav_movie:
        consumer = consumers_who_likes_favorite_movie.loc[consumers_who_likes_favorite_movie['Author'] == ratings.Author.iloc[i]]
        if ratings.Metascore_w.iloc[i] > consumer.Metascore_w.iloc[0]:
           row = ratings[i:i + 1]
           new_subset = new_subset.append(row)
print("there are %d movies rated by the same consumers who liked %s and with higher rating" % (new_subset.movieName.size, fav_movie))
# export the final dataframe to csv with these movies recommendation
new_subset.to_csv('python-output.csv', index=False)
# print done when finished the all process
print('Done!')