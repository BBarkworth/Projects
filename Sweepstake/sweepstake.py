import random
import csv
import copy
import time

with open('pot4.csv', 'r') as in_file:
    reader = csv.reader(in_file)
    teams = []
    for row in reader:
        teams.append(row[0])

while True:
    user_input = input('Please provide a list of names separated by commas: ')
    if user_input != "":
        break
edited_input = user_input.replace(" ", "")
split_names = edited_input.split(',')
names = []
for i in range(len(split_names)):
    names.append(split_names[i])
complete_list = []

def process(data):
    count = 0
    teams_copy = copy.deepcopy(data)
    names_copy = copy.deepcopy(names)
    for i in range(len(data)):
        choice = random.choice(teams_copy)
        name = random.choice(names_copy)
        teams_copy.remove(choice)
        names_copy.remove(name)
        team_chosen = {name: choice}
        complete_list.append(team_chosen)
        count += 1
        time.sleep(3)
        print(choice, name)
        if count % len(names) == 0:
            names_copy = copy.deepcopy(names)
    return complete_list

process(teams)

with open('pot3.csv', 'r') as in_file:
    reader = csv.reader(in_file)
    teams = []
    for row in reader:
        teams.append(row[0])

process(teams)

with open('pot2.csv', 'r') as in_file:
    reader = csv.reader(in_file)
    teams = []
    for row in reader:
        teams.append(row[0])

process(teams)

with open('topteams.csv', 'r') as in_file:
    reader = csv.reader(in_file)
    teams = []
    for row in reader:
        teams.append(row[0])

final = process(teams)


with open('sweepstake.txt', 'w') as f_output:
    for name in names:
        f_output.write(name + ":")
        f_output.write('\n')
        for row in final:
            for keys, values in row.items():
                if keys == name:
                    f_output.write(values + ", ")
        f_output.write('\n')