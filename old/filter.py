import pandas as pd
import time
start_time = time.time()


#data is a dataframe
data = pd.read_csv('userReviews all three parts.csv', sep=';')
#data glimpse
#print(data.head())
#print(data[:3])
#print(data.movieName.iloc[1])
#create list with column names
column_names = ['movieName','Metascore_w','Author','AuthorHref','Date','Summary'
                ,'InteractionsYesCount','InteractionsTotalCount','InteractionsThumbUp'
                ,'InteractionsThumbDown']
#create table and append list of column names
subset = pd.DataFrame(columns=column_names)
#loop through movie review and append output to subset dataframe called subset
for movie in range(200):
    # if the nth movie in the range between 0 to 99 contains is equal to beach-rats then continue
    if data.movieName.iloc[movie] == 'baby-driver':
        #store in row from the dataset the nth movie+1 (+1 because computers count from 0 onwards and not from 1)
        row = data[movie:movie + 1]
        #print(row)
        # append the movie in row to the subset dataframe
        subset = subset.append(row)  

subset.to_csv(r'/home/pi/rsl/subsetPython.csv', index = False)
recommendation = pd.DataFrame(columns=column_names)
for i in range(len(subset)):
    for j in range(len(data)):
        if subset.Author.iloc[i] == data.Author.iloc[j] and subset.Metascore_w.iloc[i] < data.Metascore_w.iloc[j]:
            row = data[j:j + 1]
            recommendation = recommendation.append(row)
            
print(recommendation.head())
            
recommendation.to_csv(r'/home/pi/rsl/recommendationPython.csv', index = False)

recommendation["diff"] = ""
recommendation["diff"] = pd.to_numeric(recommendation["diff"])

for i in range(len(subset)):
    for j in range(len(recommendation)):
        if subset.Author.iloc[i] == recommendation.Author.iloc[j]:
            recommendation["diff"] = recommendation.Metascore_w.iloc[j] - subset.Metascore_w.iloc[i]
        
recommendation.to_csv(r'/home/pi/rsl/recommendationDifferencePython.csv', index = False)

print("--- %s seconds ---" % (time.time() - start_time))