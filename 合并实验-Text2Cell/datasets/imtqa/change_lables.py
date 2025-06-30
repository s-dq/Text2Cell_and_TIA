import jsonlines
import os
import csv

with jsonlines.open('combine.jsonl') as reader:
    combine = list(reader)
files=os.listdir("./graph_edge")
for i in range(len(files)):
    #读取csv文件
    csv_reader = csv.reader(open("./graph_edge/"+files[i]))
    data=[]
    for row in csv_reader:
        data.append(row)
    for j  in range(len(combine)):
        if combine[j]['table_id']==files[i].split('_')[0]:
            for k in range(len(data)-1):
                if int(data[k+1][1]) in combine[j]['combine'] and int(data[k+1][2]) in combine[j]['combine']:
                    data[k+1][4]=1
    with open("./graph_edge/"+files[i], 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)





