import csv
import json
from tqdm import tqdm


def open_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def open_jsonl_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            json_obj = json.loads(line)
            data.append(json_obj)
    return data


def get_node_num(x):
    i = 0
    while True:
        if i * i < x and (i + 1) * (i + 1) >= x:
            return i
        else:
            i = i + 1
    return 0


def calc_old(truth_file, pre_file):
    truth = open_csv_file(truth_file)
    truth = truth[1:]
    pre = pre_file

    node_num = get_node_num(len(truth))
    old_right = 0
    old_total = 0

    # 原方法的单元格行列准确的准确率
    for i in range(node_num):

        # 序号为i的单元格，需要正确判断的全部关系
        answer_set = []

        turth_temp = []
        temp_id_set = [str(i)]
        flag = True
        for j in range(len(truth)):
            if truth[j][4] == '1':
                turth_temp.append(truth[j])
        while flag:
            flag = False
            for j in range(len(turth_temp)):
                if turth_temp[j][1] in temp_id_set and turth_temp[j][4] == '1':
                    if [turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]] not in answer_set:
                        answer_set.append([turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]])
                        if str(turth_temp[j][2]) not in temp_id_set:
                            temp_id_set.append(str(turth_temp[j][2]))
                        flag = True

        turth_temp = []
        temp_id_set = [str(i)]
        flag = True
        for j in range(len(truth)):
            if truth[j][4] == '2':
                turth_temp.append(truth[j])
        while flag:
            flag = False
            for j in range(len(turth_temp)):
                if turth_temp[j][1] in temp_id_set and turth_temp[j][4] == '2':
                    if [turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]] not in answer_set:
                        answer_set.append([turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]])
                        if str(turth_temp[j][2]) not in temp_id_set:
                            temp_id_set.append(str(turth_temp[j][2]))
                        flag = True

        turth_temp = []
        temp_id_set = [str(i)]
        flag = True
        for j in range(len(truth)):
            if truth[j][4] == '3':
                turth_temp.append(truth[j])
        while flag:
            flag = False
            for j in range(len(turth_temp)):
                if turth_temp[j][1] in temp_id_set and turth_temp[j][4] == '3':
                    if [turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]] not in answer_set:
                        answer_set.append([turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]])
                        if str(turth_temp[j][2]) not in temp_id_set:
                            temp_id_set.append(str(turth_temp[j][2]))
                        flag = True

        turth_temp = []
        temp_id_set = [str(i)]
        flag = True
        for j in range(len(truth)):
            if truth[j][4] == '4':
                turth_temp.append(truth[j])
        while flag:
            flag = False
            for j in range(len(turth_temp)):
                if turth_temp[j][1] in temp_id_set and turth_temp[j][4] == '4':
                    if [turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]] not in answer_set:
                        answer_set.append([turth_temp[j][1], turth_temp[j][2], turth_temp[j][4]])
                        if str(turth_temp[j][2]) not in temp_id_set:
                            temp_id_set.append(str(turth_temp[j][2]))
                        flag = True

        for j in range(len(truth)):
            if truth[j][1] == str(i) and truth[j][4] == '0':
                answer_set.append([truth[j][1], truth[j][2], truth[j][4]])

        label = True
        for j in range(len(pre)):
            if [str(pre[j][0]), str(pre[j][1]), '0'] in answer_set or [str(pre[j][0]), str(pre[j][1]),
                                                                       '1'] in answer_set or [str(pre[j][0]),
                                                                                              str(pre[j][1]),
                                                                                              '2'] in answer_set or [
                str(pre[j][0]), str(pre[j][1]), '3'] in answer_set or [str(pre[j][0]), str(pre[j][1]),
                                                                       '4'] in answer_set:
                if [str(pre[j][0]), str(pre[j][1]), str(pre[j][2])] not in answer_set:
                    label = False
        if label:
            old_right = old_right + 1
            old_total = old_total + 1
        else:
            old_total = old_total + 1

    return old_right / old_total


def calc_new(truth_file, pre_file):
    truth = open_csv_file(truth_file)
    truth = truth[1:]
    pre = pre_file
    node_num = get_node_num(len(truth))
    old_right = 0
    old_total = 0
    # 新方法的单元格行列准确的准确率
    for i in range(node_num):
        answer_set = []
        for j in range(len(truth)):
            if truth[j][1] == str(i):
                answer_set.append([truth[j][1], truth[j][2], truth[j][4]])
        pre_set = []
        for j in range(len(pre)):
            if pre[j][0] == i:
                pre_set.append(pre[j])

        label = True
        for j in range(len(answer_set)):
            for k in range(len(pre_set)):
                if answer_set[j][0] == str(pre_set[k][0]) and answer_set[j][1] == str(pre_set[k][1]) and answer_set[j][
                    2] != str(pre_set[k][2]):
                    label = False
        if label:
            old_right = old_right + 1
            old_total = old_total + 1
        else:
            old_total = old_total + 1

    return old_right / old_total


pre = open_jsonl_file('./rel.jsonl')
acc_sum = 0
num_sum = 0
acc_all = 0
for i in tqdm(range(len(pre))):
    csv_filename = list(pre[i].keys())[0].replace('+', '-') + '_edge.csv'
    acc = calc_new('./graph_edge/' + csv_filename, pre[i][list(pre[i].keys())[0]]['edge_rel'])
    acc_sum = acc_sum + acc
    num_sum = num_sum + 1
    if acc == 1.0:
        acc_all = acc_all + 1
print(acc_sum)
print(num_sum)
print(acc_sum / num_sum)
print(acc_all)

