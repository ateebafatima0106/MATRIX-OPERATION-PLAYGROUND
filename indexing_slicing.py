import numpy as np;

#          VECTOR INDEXING 
vec1 = np.arange(1,11);
print(vec1);
print(vec1[4]); #5
# print(vec1[10]) # error - out of bound 
print(vec1[-1]); #last element
print(vec1[-3]); #3rd last: 8


#        VECTOR SLICING 
# syntax : array_name(start:stop(excluded):step(by default it is 1))
t = (1,2,3,4,5,6);
vec2 = np.array(t);
print(t);
print(vec2);

print(vec2[:5]); # 1 to 5
print(vec2[1:4]); # 2 to 4
print(vec2[5:0:-1]); # 6 to 2 ( 0 is excluded)
print(vec2[::-1]); # reversed vector 6 to 1



#               MATRIX INDEXING
v = np.arange(1,21);
m = v.reshape(5,4);
print(m);
print(m[0]); #1st row
print(m[4]); #last row
print(m[0,0]); #1st row 1st element
print(m[0,0]+m[1,0]+m[2,0]); # sum of 1st elements of rows 1 2 and 3
print(m[-1]); #last row
print(m[3,-1]) #4th row last element

#               MATRIX SLICING
print(m[0:5]); # all rows
print(m[1:2]); # 2nd row
print(m[::2]); #1st row , 3rd row , 5th row
print(m[::-1]) # reverses the matrix

print(m);

# Q: slice 2 3 6 7 from m matrix:
# how we do it? 
# target the rows - 0 and 1 
# colums - 1 and 2 

print(m[0:2,1:3]); # 2 3 are in row 0 , and 6 7 in row 1 so 0:2 
# , columns of 0 and 1 rows are 1 and 2 so 1:3


# Q: slice 11 12 15 16 19 20:
print(m[2:5,2:4]);

# Q: slice 3rd column from the matrix:
print(m[:,2]);

#                BOOLEAN INDEXING
# lets say we want true where there are even numbers in the array:

arr = np.arange(11,21)
print(arr);

bool_index = arr % 2 == 0;
print(bool_index);

 # for odds
odds = arr % 2 != 0;
print(odds);


