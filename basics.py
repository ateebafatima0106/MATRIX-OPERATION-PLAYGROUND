import numpy as np

# should be one data type in an array: 
same = np.array([1,2,3,4]);
print(same)
# with diff data types:
diff1 = np.array([1,2,3,4.5,"hello"]);
print(diff1) #converts all in string

# if it has no string but ints and floats then converts all in floats:
diff2 = np.array([1,2,3,4.5])
print(diff2)

# vector - 1d array:
vec = np.array([1,2,3,4,5])
print(vec)

# matrix- 2d array:
mat = np.array([[1,2],[3,4]])
print(mat)

#               ARRAY GENERATION FUNCTIONS:

# arange function:
r = np.arange(1,11);
print(r) # generates an array 1 to 10. works same as range function

r2 = np.arange(0,11,2);
print(r2) #array of even numbers 

# zeros function - vector:
z = np.zeros(6)
print(z) # gives a vector 6 zeros

# zeros function - matrix:
zz = np.zeros((3,4));
print(zz) # 3 rows and 4 columns of zeros

# ones function - same as zeros function:
o = np.ones((4,2))
print(o)

# length function:
print(len(zz)) # or to find no. of rows

# linspace function - generates a range with linear spacing:
# lets say you want 10 numbers between 0 and 1:
lin = np.linspace(0,1,10);
print(lin)

lin1 = np.linspace(1,5,2)
print(lin1)

lin2 = np.linspace(1,5,3)
print(lin2)

lin3 = np.linspace(1,5,5)
print(lin3)

# random function: (gets installed with numpy)

# normalization - gives numbers between 0 and 1 :
ran = np.random.rand(10)
print(ran) # 10 random nums between 0 and 1

# standarization - gives numbers between -3 and 3:
ran1 = np.random.randn(10)
print(ran1);

# randint():
ran2 = np.random.randint(6)
print(ran2); # between 0 t0 6
# randint(start,stop,how many):
ran3 = np.random.randint(2,20,9)
print(ran3)

#        array attributes - () is not given

att = np.array([[1,2,3],[4,5,6]])
print(att.shape) # gives no. of rows and cols - here : 2,3
print(att.size) #no. of elements
print(att.dtype) #data type

#         array methods

m = np.array([[1,2],[3,4],[5,6]]);
print(m.min()); # returns minimun number
print(m.max());
print(m.sum());

# for sum of rows or colums:
# np.sum(array_name,axis) - axis = 0 (gives sum of columns) - axis = 1 (gives sum of rows)

ss = np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(ss);
print(np.sum(ss,0));
print(np.sum(ss,1));

# mean function:
print(ss.mean());

# standard deviation:
print(ss.std());

# for returning index of max and min element:
print(ss.argmax());
print(ss.argmin());

# reshapping function:
# suppose we have a vector of 30 elements:
v = np.arange(1,31);
print(v);
# and i want to reshape it into a 2d array/matrix. for that 
# first i need to make sure i have no. of elements same as i want
# the no. of rows and columns
# for eg here we have 30 elements so we cannot take 5*5 matrix, 
# we should take 5*6 or anything combo that can fit 30 elements

print(v.reshape(5,6));


# arange().reshape() combined:

hh = np.arange(1,11).reshape(5,2);
print(hh);

