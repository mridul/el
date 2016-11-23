import ipdb
import string


INSTANCE_TYPES_TRANSITIVE_PATH = './data/instance_types_transitive_en.ttl'
PERSON_TYPE_PATH = './data/distinct_person_types.txt'
ANCHOR_TEXTS_PATH = './data/anchor_text_en.ttl'
OUTPUT_PERSONS_ANCHOR_TEXT = './data/persons_anchor_texts.txt'
OUTPUT_PERSONS_PATH = './data/distinct_persons.txt'
OUTPUT_INSTANCE_TYPE_PATH = './data/filtered_instance_types.txt'
DEBUG_STATUS_EVERY=10**6


def get_person_types():
    types = set()
    with open(PERSON_TYPE_PATH) as f:
        for line in f:
            types.add(line.strip())

    return types



def get_instance_types(type_filter_set=set()):
    instance_type_list = []
    instance_set = set()
    with open(INSTANCE_TYPES_TRANSITIVE_PATH) as f:
        i = 0
        for line in f:
            i+=1
            if i%DEBUG_STATUS_EVERY == 0:
                print('{} lines processed'.format(i))

            split_line = line.strip().split(' ')
            instance = split_line[0]
            instance_type = split_line[2]
            if instance_type in type_filter_set:
                instance_set.add(instance)
                instance_type_list.append(
                    (instance, instance_type)
                )

    return instance_type_list, instance_set



def write_iterable_to_file(iterable_obj, filepath):
    with open(filepath, 'w') as f:
        for item in iterable_obj:
            f.write('{}\n'.format(item))



def clean_anchor_text(anchor_text):
    # filter out really small anchor texts
    ANCHOR_TEXT_LENGTH_THRESHOLD = 2
    if len(anchor_text) < ANCHOR_TEXT_LENGTH_THRESHOLD:
        return None

    anchor_text = anchor_text.lower().strip(string.punctuation)
    anchor_text = anchor_text.replace("'s", "")
    return anchor_text



def write_person_aliases(persons, anchor_text_file, output_file):
    discovered_set = set()
    with open(output_file, 'w') as outfile:
        with open(anchor_text_file) as infile:
            i = 0
            for line in infile:
                i += 1
                if i % DEBUG_STATUS_EVERY == 0:
                    print(i)

                entity_until_index = line.find(' ')
                entity = line[:entity_until_index]

                if entity in persons:
                    rest_of_line = line[entity_until_index+1:]
                    rest_of_line = rest_of_line[rest_of_line.find(' ')+1:]
                    anchor_text = rest_of_line[1:rest_of_line.find('"@')]
                    anchor_text = clean_anchor_text(anchor_text)
                    if anchor_text is not None and (entity, anchor_text) not in discovered_set:
                        outfile.write('{}\t{}\n'.format(entity, anchor_text))
                        discovered_set.add((entity, anchor_text))



if __name__ == '__main__':
    types_person = get_person_types()
    instance_type_list, instance_set = get_instance_types(types_person)
    # instance_type_list_delimited = [' '.join(entry) for entry in instance_type_list]

    # write_iterable_to_file(instance_set, OUTPUT_PERSONS_PATH)
    # write_iterable_to_file(instance_type_list_delimited, OUTPUT_INSTANCE_TYPE_PATH)

    # write_person_aliases(instance_set, ANCHOR_TEXTS_PATH, OUTPUT_PERSONS_ANCHOR_TEXT)
