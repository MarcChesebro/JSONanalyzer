import sys
import json

def sortFunc(tup):
    key, dic = tup
    return dic['total_coal']

if __name__ == "__main__":

    with open(sys.argv[1]) as json_file:
        json_data = json.load(json_file)

    elves = {}

    for inf in json_data['infractions']:
        if inf['name'] in elves:
            elves[inf['name']]['infractions'] = elves[inf['name']]['infractions'] + 1
            elves[inf['name']]['total_coal'] = elves[inf['name']]['total_coal'] + inf['severity']

        else:
            elves[inf['name']] = {'name' : inf['name'], 'infractions' : 1, 'total_coal' : inf['severity']}

    sorted_data = sorted(elves.items(), key = sortFunc, reverse=True)

    for elf in sorted_data:
        print("Name: {}\t Infractions: {}\t Total Coal: {}".format(elf[0], elf[1]['infractions'], elf[1]['total_coal']))
