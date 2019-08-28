#!/usr/bin/env python3

"""
Parse and print all records from FASTA file
"""

import sys

class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
        
        
    def next(self):
        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        #If we reach here, ident has been initialized correctly
        
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "": #if line is nothing
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
                
        sequence = "".join(sequences)
        return ident, sequence
            
#create fasta reader and then 


reader = FASTAReader(sys.stdin)

while True: 
    ident, sequence = reader.next()
    if ident is None:
        break
    print (ident, sequence)