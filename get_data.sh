# create directory if not exists
mkdir -p data
cd data

# instance types -- transitive
wget http://downloads.dbpedia.org/2016-04/core-i18n/en/instance_types_transitive_en.ttl.bz2
bzip2 -d instance_types_transitive_en.ttl.bz2
# let us filter out distinct 'Person' types
cut -f 3 -d $' ' instance_types_transitive_en.ttl | grep Person | sort -u > distinct_person_types.txt
# TODO remove <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#SocialPerson>
# TODO remove <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#NaturalPerson>

# persondata
wget http://downloads.dbpedia.org/2016-04/core-i18n/en/persondata_en.ttl.bz2
bzip2 -d persondata_en.ttl.bz2
cut -f 1 -d $' ' persondata_en.ttl | sort -u > distinct_persons.txt

# anchor texts
wget http://downloads.dbpedia.org/2016-04/core-i18n/en/anchor_text_en.ttl.bz2
bzip2 -d anchor_text_en.ttl.bz2

# disambiguations
wget http://downloads.dbpedia.org/2016-04/core-i18n/en/disambiguations_en.ttl.bz2
bzip2 -d disambiguations_en.ttl.bz2

# redirects -- transitive
wget http://downloads.dbpedia.org/2016-04/core-i18n/en/transitive_redirects_en.ttl.bz2
bzip2 -d transitive_redirects_en.ttl.bz2
