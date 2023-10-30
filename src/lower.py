#!/bin/python

import sys

tf=open(sys.argv[1]+".lower","w")
with open(sys.argv[1],"r") as f:
  for line in f:
    line=line.strip()
    line=line.lower()
    tf.write(line+"\n")

