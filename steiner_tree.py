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

with open(sys.argv[2],"r") as result_file:
    line_list = result_file.readlines()
    for l in line_list:
        words = l.split(" ")
        if len(words)>1:
            if(words[0]=="E"):
                sp.print_line([int(words[1]),int(words[2])],[int(words[3]),int(words[4])],'g')


sp.plt.show()
