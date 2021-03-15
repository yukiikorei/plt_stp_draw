#!/usr/bin/python3.8

import simplePlt as sp
import sys

with open(sys.argv[1],"r") as instance_file:
    line_list = instance_file.readlines()
    for l in line_list:
        words = l.split(" ")
        if len(words)>1:
            if(words[0]=="DD"):
                sp.print_point(int(words[2]),int(words[3]),"r.");
            elif(words[0]=="RR"):
                sp.print_obstale(int(words[1]),int(words[2]),int(words[3]),int(words[4]),"b")

location = []
segments = []
with open(sys.argv[2],"r") as escape_graph_file:
    line_list = escape_graph_file.readlines()
    for l in line_list:
        words = l.split(" ")
        if len(words)>1:
            if(words[0]=="S"):
                segments.append([int(words[1]),int(words[2])])
            elif(words[0]=="N"):
                location.append([int(words[2]),int(words[3])])
                sp.print_point(int(words[2]),int(words[3]),"y.");
            elif(words[0]=="T"):
                location.append([int(words[2]),int(words[3])])

for s in segments:
    sp.print_line(location[s[0]],location[s[1]],"g")

sp.plt.show()
