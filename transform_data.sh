reverse_index_anchor_texts() {
    awk -F $"\t" '{print $2 "\t" $1}' $1 | sort > $2
}
