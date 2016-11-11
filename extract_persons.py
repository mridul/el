
PERSON_TYPE_PATH = './data/distinct_person_types.txt'

def get_person_types():
    lines = []
    with open(PERSON_TYPE_PATH) as f:
        for line in f:
            lines.append(line.strip())

    return lines

if __name__ == '__main__':
    types_person = get_person_types()
