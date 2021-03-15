import matplotlib.pyplot as plt

def print_v_line(x,y1,y2,mode):
    plt.plot([x,x],[y1,y2],mode)

def print_h_line(y,x1,x2,mode):
    plt.plot([x1,x2],[y,y],mode)

def print_line(begin,end,mode):
    plt.plot([begin[0],end[0]],[begin[1],end[1]],mode)

def print_point(x,y,mode):
    plt.plot([x],[y],mode)

def print_obstale(left,down,right,up,mode):
    plt.plot([left,right],[up,up],mode)
    plt.plot([left,right],[down,down],mode)
    plt.plot([left,left],[down,up],mode)
    plt.plot([right,right],[down,up],mode)
