import pandas as pd
import time
from pattern.en import sentiment as sen
import psycopg2 
start_time = time.time()

data = pd.read_csv('authorRecommend.csv', sep=';')

#create 2 new columns for positivity and objectivity
data = data.assign(positivity= '', objectivity= '')

# loop through the recommended movies by author authors with a higher metascore
for i in range(len(data)):
    # for every row, calculate positivity and objectivity of the summary
    senx = sen(data.Summary.iloc[i])
    # store positivity which is senx[0] in positivity column
    data.positivity.iloc[i] = senx[0]
    # store positivity which is senx[1] in positivity column
    data.objectivity.iloc[i] = senx[1]

print("finalRecommend file updated with positivty and objectivity values based on summary of the movie given")
# clean data a little bit
data.sort_values(['diff'], ascending=False)
data.drop_duplicates(subset = 'movieName', keep = 'first', inplace=True)
data.to_csv("finalRecommend.csv", sep= ";", index = False)


# connect database on localmachine
conn = psycopg2.connect('dbname=test')
cur = conn.cursor()
print('connection made with psql database')

#create table
cur.execute('''CREATE TABLE if not exists authorRecommend (
movieName text,
Metascore_w text,
diff text,
Author text,
Summary text,
positivity text,
objectivity text);''')
#commit query
conn.commit()
print('New table created database test with table called authorRecommend')

cur.execute("copy authorRecommend FROM '/home/pi/rsl/finalRecommend.csv' delimiter ';' csv header;")
conn.commit()
print('finalRecommend file pushed to new table succesfully')

print("End script") 
print("--- %s seconds ---" % (time.time() - start_time))