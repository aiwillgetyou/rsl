import pandas as pd

#data is a dataframe
data = pd.read_csv('userReviews all three parts.csv', sep=';')
#data glimpse
print(data.head())
print(data[:3])
print(data.movieName.iloc[1])
#create list with column names
column_names = ['movieName','Metascore_w','Author','AuthorHref','Date','Summary'
                ,'InteractionsYesCount','InteractionsTotalCount','InteractionsThumbUp'
                ,'InteractionsThumbDown']
#create table and append list of column names
subset = pd.DataFrame(columns=column_names)
#loop through movie review and append output to subset dataframe called subset
for movie in range(100):
    # if the nth movie in the range between 0 to 99 contains is equal to beach-rats then continue
    if data.movieName.iloc[movie] == '100':
        print(movie)
        #store in row from the dataset the nth movie+1 (+1 because computers count from 0 onwards and not from 1)
        # row = data[movie:movie + 1]
        # append the movie in row to the subset dataframe
        #subset = subset.append(row)
        

