import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    credit = []
    for line in sys.stdin:
        line = line.strip()
        words = line.split(',')
        if len(words) > 3:
            # credit.append(words[2])
            print(words[2])