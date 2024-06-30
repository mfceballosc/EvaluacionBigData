import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

def mapper(data):
    count_map = {}
    for item in data:
        if item in count_map:
            count_map[item] += 1
        else:
            count_map[item] = 1
    return count_map.items()

from collections import defaultdict

def reducer(mapped_items):
    count_reduce = defaultdict(int)
    for item, count in mapped_items:
        count_reduce[item] += count
    return count_reduce.items()

def run_map_reduce(data):
    # Fase de Map
    mapped_items = mapper(data)
    
    # Fase de Reduce
    reduced_items = reducer(mapped_items)
    
    return reduced_items

if __name__ == "__main__":
    credit = []
    for line in sys.stdin:
        line = line.strip()
        credit.append(line)

    credit = run_map_reduce(credit)
    for w, idx in credit:
        print(f"{w}\t{idx}")