import ipdb


INSTANCE_TYPES_TRANSITIVE_PATH = './data/instance_types_transitive_en.ttl'
PERSON_TYPE_PATH = './data/distinct_person_types.txt'


def get_person_types():
    types = set()
    with open(PERSON_TYPE_PATH) as f:
        for line in f:
            types.add(line.strip())

    return types


def get_instance_types(type_filter_set=set()):
    instance_type_list = []
    with open(INSTANCE_TYPES_TRANSITIVE_PATH) as f:
        for line in f:
            split_line = line.strip().split(' ')
            instance = split_line[0]
            instance_type = split_line[1]
            if instance_type in type_filter_set:
                instance_type_list.append(
                    (instance, instance_type)
                )

    return instance_type_list


if __name__ == '__main__':
    types_person = get_person_types()
    instance_type_list = get_instance_types(types_person)
    output = [' '.join(entry) for entry in instance_type_list]
    with open('temp.txt', 'w') as f:
        f.writelines(output)
