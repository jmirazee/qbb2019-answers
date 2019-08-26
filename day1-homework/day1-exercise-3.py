#!/usr/bin/env python3

#count number of alignments that match perfectly to the genome

#!/usr/bin/env python3

#count number of alignments

import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
count = 0
for line in f:
    line = line.rstrip("\n")
    fields = line.split("\t")
    for field in fields:
        if field == "NH:i:1":
            count +=1
        
print(count)