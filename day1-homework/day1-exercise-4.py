#!/usr/bin/env python3

#count number of alignments that match perfectly to the genome

#!/usr/bin/env python3

#count number of alignments

#count number of alignments

import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
#count = 0

for i, line in enumerate(f,1):
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[5] =="*":
        continue
    elif i>10:
        break
    else:
        print(fields[2])
            
            
          