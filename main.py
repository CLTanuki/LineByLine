__author__ = 'cltanuki'
import sys
import codecs
import re
from os import listdir
from os.path import isfile, join, split

if hasattr(sys, 'frozen'):
    basis = sys.executable
else:
    basis = sys.argv[0]

base_folder = split(basis)[0]

print(base_folder)

type_path = join(base_folder, "types")
print(type_path)
input_path = join(base_folder, "input")
print(input_path)
result_path = join(base_folder, "result")

type_files = [f for f in listdir(type_path) if isfile(join(type_path, f))]
print(type_files)
input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]
print(input_files)

type_dict = {}
input_dict = {}
counter_dict = {}

for file in type_files:
    type_dict[file] = codecs.open(file, 'r').readlines()
    counter_dict[file] = 0

for file in input_files:
    data = codecs.open(file, 'r', encoding='utf-8').read()
    input_dict[file] = re.sub("[^\w]", " ",  data).split()

for i in input_dict:
    word_list = input_dict.get(i)
    for word in word_list:
        for a in type_dict:
            counter_dict[i] = {}
            word_data = counter_dict[a]
            type_list = type_dict.get(a)
            print(type_list)
            if word in type_list:
                word_data[word] = 0 if word_data[word] is None else word_data[word]
                word_data[word] += 1

for i in counter_dict:
    f = open(join(type_path, i))

print(counter_dict)