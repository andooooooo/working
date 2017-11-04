import sys
import re
from sklearn.ensemble import RandomForestClassifier
from scipy.sparse import lil_matrix

p20 = re.compile('[0-9]*testvec')
def get_size_of_data_file(file_path):
    column_number = 0
    line_number = 0
    file = open(file_path,'r')
    for line in file :
        line = line.rstrip()
        line_array = line.split(" ")
        label = line_array.pop(0)
        for x in line_array :
            pair = x.split(":")
            f_idx = int(pair[0])
            if column_number < f_idx :
                column_number = f_idx
        line_number += 1
    file.close()
    return line_number, column_number

"""
def count_lines(file_path):
    x = commands.getoutput("wc -l "+file_path)
    xx = x.split(" ")
    return int(xx[0])
"""
### main routin

training_label = []
training_data = []
test_label = []
test_data = []		
args = sys.argv
file_train = args[1]
file_test = args[2]

(training_data_number,max_feature_number) = get_size_of_data_file(file_train)


training_data = lil_matrix((training_data_number,max_feature_number))


file = open(file_train,'r')
row = 0
for line in file :
    line = line.rstrip()
    line_array = line.split(" ")
    label = line_array.pop(0)
    for x in line_array :
        pair = x.split(":")
        f_idx = int(pair[0])
        training_data[row,f_idx-1] = int(pair[1])
    training_label.append(label)
    row += 1


h = open(file_test)
lines = h.readlines()
p=0
for i in lines:
    p+=1
test_data_number = p


test_data = lil_matrix((test_data_number,max_feature_number))


file = open(file_test,'r')
row = 0
for line in file :
    line = line.rstrip()
    line_array = line.split(" ")
    label = line_array.pop(0)
    for x in line_array :
        pair = x.split(":")
        f_idx = int(pair[0])
        test_data[row,f_idx-1] = int(pair[1])
    test_label.append(label)
    row += 1


model = RandomForestClassifier()
model.fit(training_data, training_label)


output = model.predict(test_data)


num=re.sub(p20,"",file_test)
num=num.rstrip(".txt")
core=0
for i in output :
    if i==num:
        core+=1
print(core/(test_data_number-1))
