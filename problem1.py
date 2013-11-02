#!/usr/bin/python
#generate compressed sparse row matrix and then convert to LIL
import sys
from scipy.sparse import *
from scipy import *
import numpy as np

def main():
    a = np.array([[11, 0, 0, 0, 0, 0, 14], [0, 0, 0, 0, 23, 0, 0], [0, 0, 0, 0, 33, 34, 0], [0, 15, 0, 0, 43, 44, 0], [0, 0, 0, 0, 0, 54, 0], [0, 0, 62, 0, 0, 0, 0], [0, 0, 72, 0, 0, 0, 0]]);
    count_nz = 0            #keep track of how many nonzero elements we've encountered
    aa = []
    ja = []
    ia = []
    for y in range (0, 7):  #iterate through rows
        first_nz_in_row = 1 #bool to see if current element is first nonzero in row
        for x in range (0, 7):
            if a[y][x] != 0:
                aa.append(a[y][x])
                ja.append(x)
                count_nz+=1
                if first_nz_in_row == 1:
                    ia.append(count_nz)
                    first_nz_in_row = 0
    ia.append(count_nz+1)
    ja = [i+1 for i in ja]
    print "aa: " + str(aa)
    print "ja: " + str(ja)
    print "ia: " + str(ia)

    ja = [i-1 for i in ja]
    ia = [i-1 for i in ia]
    my_csr = csr_matrix((aa, ja, ia), shape=(7,7), dtype=int32)
    my_lil = my_csr.tolil()
    print "lil data: " + str(my_lil.data)
    print "lil row indices: " + str(my_lil.rows)

if __name__ == '__main__':
	 main()
