import math
import numpy
import networkx as nx
%matplotlib inline
import matplotlib.pyplot as plt

order = int(raw_input("enter order of graph: "))
def fibonacci(n):
    tmp = [0,1]
    for i in range(n):
        tmp.append(tmp[-1]+tmp[-2])
    return tmp[1:-1]
	
	
def fibonacci_code_generator(n,a):
    tmp = ""
    m=0
    if (n == 0):
        return "0"
    for i in range(1,a[-1]):
        if (n == a[i]):
            m = i
            tmp = "1" + (m-1)*"0"
            return tmp
        if (n < a[i]):
            while(m != 0):
                tmp = tmp + str(int(n/a[m]))
                n = n%a[m]
                m = m-1
            return tmp
        m = i
        
        

def fibonacci_num_length_corrector(a):
    length = len(a[-1])
    for i in range(len(a)):
        if(length > len(a[i])):
            a[i] = ((length-len(a[i]))*"0") + a[i]
    return a



def adjacency_matrix_generator(a):
    length_a = len(a)
    length_b = len(a[0])
    count = 0
    FM = numpy.zeros((length_a,length_a),dtype= int)
    for i in range(length_a -1):
        for j in range(i+1 , length_a):
            for k in range(length_b):
                if(a[i][k] != a[j][k]):
                    count+=1
            if(count == 1):
                FM[i][j] = FM[j][i] = 1
            count = 0
    return FM


fib_codes = []
fib_numbers = fibonacci(order)
FG = nx.Graph()
for i in range(fib_numbers[-1]):
    fib_codes.append(fibonacci_code_generator(i,fib_numbers))
    FG.add_node(i)
fib_codes = fibonacci_num_length_corrector(fib_codes)
FM = adjacency_matrix_generator(fib_codes)
for i in range(1,len(FM)):
    for j in range(i):
        if (FM[i][j] == 1):
            FG.add_edge(i,j)
print FM
nx.draw_networkx(FG,node_color='green',node_size=700)
