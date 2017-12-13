import csv
import statistics

f = open('Demographic_Statistics_By_Zip_Code.csv','r',encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line)

f.close()




