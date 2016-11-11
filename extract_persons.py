
PERSON_TYPE_PATH = './distinct_person_types.txt'

def get_person_types():
    with open(PERSON_TYPE_PATH) as f:
        lines = f.readlines()

    return lines

if __name__ == '__main__':
    print(get_person_types())
