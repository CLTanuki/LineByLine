__author__ = 'cltanuki'
import sys
import codecs
import re
from os import listdir
from os.path import isfile, join, split
from dicttoxml import dicttoxml

if hasattr(sys, 'frozen'):
    basis = sys.executable
else:
    basis = sys.argv[0]

base_folder = split(basis)[0]

type_path = join(base_folder, "types")
input_path = join(base_folder, "input")
result_path = join(base_folder, "result")

type_files = [f for f in listdir(type_path) if isfile(join(type_path, f))]
input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

type_dict = {}
input_dict = {}
counter_dict = {}

for file in type_files:
    type_dict[file] = [x.rstrip() for x in codecs.open(join(type_path, file), 'r').readlines()]

for file in input_files:
    data = codecs.open(join(input_path, file), 'r', encoding='cp1251').read()
    input_dict[file] = re.sub("[^\w]", " ",  data).split()
    counter_dict[file] = 0

for i in input_dict:
    word_list = input_dict.get(i)
    cat_data = {}
    for k, v in type_dict.items():
        word_data = {}
        type_list = v
        for word in word_list:
            if word in type_list:
                word_data[word] = word_data.get(word, 0) + 1
        cat_data[k] = word_data
    counter_dict[i] = cat_data

print(counter_dict)

for k, v in counter_dict.items():
    result = open(join(result_path, k + '.xml'), 'w')
    result.write(dicttoxml(v))
    result.close()