import pandas as pd


data = pd.read_csv('userReviews all three parts.csv', sep=';')


column_names = ['movieName','Metascore_w','Author','AuthorHref','Date','Summary'
                ,'InteractionsYesCount','InteractionsTotalCount','InteractionsThumbUp'
                ,'InteractionsThumbDown']

subset = pd.DataFrame(columns=column_names)

for movie in range(100):
  if data.movieName.iloc[movie] == '8':
    print(movie)


