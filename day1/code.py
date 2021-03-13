import sys
from pprint import pprint

with open('input.txt', 'r') as file:
    number_list = [int(line) for line in file]

sum_results = {}

for number in number_list:
    root_number = number
    new_sums = {root_number: {num: root_number + num} for num in number_list}
    sum_results.update(new_sums)

pprint(sum_results)

