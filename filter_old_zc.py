import pandas as pd
import timeit

start = timeit.default_timer()
data = pd.read_csv('userReviews all three parts.csv', sep=';')
data = data.drop(columns=['InteractionsYesCount','InteractionsTotalCount','InteractionsThumbUp'
                ,'InteractionsThumbDown','AuthorHref','Date'])
column_names = ['movieName','Metascore_w','Author','Summary', 'Abs_Increase']

subset = data[data['movieName']=='the-lion-king']

result = pd.DataFrame(columns = column_names)

for author in range(subset.shape[0]):
    indexes = data[data['Author'] == subset.Author.iloc[author]]
    indexes = indexes[indexes['Metascore_w']>subset.Metascore_w.iloc[author]].index.values
    for movie in indexes:
        row=data[movie:movie +1]
        row.Abs_Increase = data.Metascore_w.iloc[movie] - subset.Metascore_w.iloc[author]
        result = result.append(row)
        
result.sort_values(['Abs_Increase'], ascending=False)
result.drop_duplicates(subset = 'movieName', keep = 'first', inplace=True)
result.to_csv("RS_Review_KK.csv", sep= ";", index = False)
print(timeit.default_timer() - start)

len(result.index)
