import pandas as pd
import time
from pattern.en import sentiment as sen
import psycopg2 
start_time = time.time()

data = pd.read_csv('authorRecommend.csv', sep=';')
 
data = data.assign(positivity= '', objectivity= '')
 
for i in range(len(data)):
     senx = sen(data.Summary.iloc[i])
     data.positivity.iloc[i] = senx[0]
     data.objectivity.iloc[i] = senx[1]
 
data.sort_values(['diff'], ascending=False)
data.drop_duplicates(subset = 'movieName', keep = 'first', inplace=True)
data.to_csv("finalRecommend.csv", sep= ";", index = False)


conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

cur.execute('''CREATE TABLE if not exists authorRecommend (
movieName text,
Metascore_w text,
diff text,
Author text,
Summary text,
positivity text,
objectivity text);''')
conn.commit()

cur.execute("copy authorRecommend FROM '/home/pi/rsl/finalRecommend.csv' delimiter ';' csv header;")
conn.commit()

print("--- %s seconds ---" % (time.time() - start_time))
