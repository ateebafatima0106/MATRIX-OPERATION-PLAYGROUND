import numpy as np;
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

# addition:
print(arr1+arr2);
# subtraction:
print(arr1-arr2);
print(arr2-arr1);
# exponential:
print(arr2**arr1);
# division:
print(arr2/arr1);
print(arr2//arr1);
# multiplication:
print(arr1*arr2); # but this is not accurate matrix multiplication
m = np.dot(arr1,arr2);
print(m);

