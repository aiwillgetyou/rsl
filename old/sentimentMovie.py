import pandas as pd
import time
from pattern.en import sentiment as sen
start_time = time.time()


#data is a dataframe
data = pd.read_csv('subsetPython.csv', sep=';')


print(sen(data.Summary.iloc[3]))

print("--- %s seconds ---" % (time.time() - start_time))