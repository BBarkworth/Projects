import random
import csv
import copy
import time

with open('pot4.csv', 'r') as in_file:
    reader = csv.reader(in_file)
    teams = []
    for row in reader:
        teams.append(row[0])

user_input = input('Please provide a list of names separated by commas: ')
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
        time.sleep(7)
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
print(final)

with open('sweepstake.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output) 
    for row in final:
            csv_output.writerow([row])