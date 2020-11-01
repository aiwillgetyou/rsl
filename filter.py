import pandas as pd
import time
start_time = time.time()

#data is a dataframe
data = pd.read_csv('userReviews all three parts.csv', sep=';')
data = data.drop(columns=['InteractionsYesCount','InteractionsTotalCount','InteractionsThumbUp'
                ,'InteractionsThumbDown','AuthorHref','Date'])
#create list with column names
column_names = ['movieName','Metascore_w','Author','Summary']
#create dataframe and append list of column names
authorReview = pd.DataFrame(columns=column_names)
authorRecommend = pd.DataFrame(columns=column_names)

#subset of authors for my favorite movie
authorReview = data[data['movieName']=='arrival']

#export authors favorite movies
authorReview.to_csv(r'/home/pi/rsl/authorReview.csv', sep = ';', index = False)
#iterate through the range of the number of authors of my favorite movies
for i in range(len(authorReview)):
    #subset of the index values of all the occurences of the authors of my favorite movie in the dataset
    indexes=data[data['Author']==authorReview.Author.iloc[i]].index.values
    for j in indexes:
        # reviewscore must be higher then my favorite movie by the authors
        if authorReview.Metascore_w.iloc[i] < data.Metascore_w.iloc[j]:
            row = data[j:j + 1]
            authorRecommend = authorRecommend.append(row)
            
authorRecommend = authorRecommend.reset_index()
authorRecommend['diff'] = ""
for i in range(len(authorReview)):
    for j in range(len(authorRecommend)):
        if authorReview.Author.iloc[i] == authorRecommend.Author.iloc[j]:
            authorRecommend.at[j,'diff'] = authorRecommend.Metascore_w.iloc[j] - authorReview.Metascore_w.iloc[i]    

authorRecommend = authorRecommend[['movieName','Metascore_w','diff','Author','Summary']]

#review by authors from my favorite movie of other movies 
authorRecommend.to_csv(r'/home/pi/rsl/authorRecommend.csv', sep = ';', index = False)
print("--- %s seconds ---" % (time.time() - start_time))
# 142 seconds
