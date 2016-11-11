# create directory if not exists
mkdir -p data
cd data

# instance types -- transitive
wget http://downloads.dbpedia.org/2016-04/core-i18n/en/instance_types_transitive_en.ttl.bz2
bzip2 -d instance_types_transitive_en.ttl.bz2
# let us filter out distinct 'Person' types
cut -f 3 -d $' ' instance_types_transitive_en.ttl | grep Person | sort -u > distinct_person_types.txt
