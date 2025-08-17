# MATRIX OPERATION PLAYGROUND 

import numpy as np;
import streamlit as st;

st.title("MATRIX OPERATIONS PLAYGROUND!")
print("FIRST MATRIX\n");

rows =3;
columns =3;
matrix_one = np.random.randint(1,31,9).reshape(rows,columns);
matrix_two = np.random.randint(10,21,9).reshape(rows,columns);
det1 = round(np.linalg.det(matrix_one));
det2 = round(np.linalg.det(matrix_two));
trans1 = np.transpose(matrix_one);
trans2 = np.transpose(matrix_two);
#identity matrix:
i = np.eye(3,3);


if st.button("GENERATE RANDOM MATRICES"):
 st.session_state.matrix_one = matrix_one;
 st.session_state.matrix_two = matrix_two;

if 'matrix_one' in st.session_state and 'matrix_two' in st.session_state:
    matrix_one = st.session_state.matrix_one
    matrix_two = st.session_state.matrix_two
    st.write("MATRIX ONE");
    st.write(matrix_one,'\n');

    st.write("MATRIX TWO\n");
    st.write(matrix_two,'\n');

st.subheader("ARITHMETIC OPERATIONS");

if st.button("ADDING THE MATRICES"):
 st.write("ADDING MATRIX ONE AND MATRIX TWO ELEMENT-WISE:\n");
 st.write(matrix_one+matrix_two,'\n');


if st.button("SUBTRACTION"):
 st.write("SUBTRACTING MATRIX ONE FROM MATRIX TWO:\n");
 st.write(matrix_one-matrix_two,'\n');


if st.button("DOT PRODUCT"):
 multiplied = np.dot(matrix_one,matrix_two);

 st.write("DOT PRODUCT OF THE MATRICES:\n",multiplied);

st.subheader("DETERMINANT OF THE MATRICES");

if st.button("CLICK HERE FOR DETERMINANTS"):
 st.write("DETERMINANT OF MATRIX ONE:\n",det1);
 st.write("DETERMINANT OF MATRIX TWO:\n",det2);

st.subheader("ARE BOTH MATRICES SQUARE?");
if st.button("EXPLANATION"):
 st.markdown("""
##  Square Matrix

### **Definition**
A **square matrix** is a matrix that has the **same number of rows and columns**.  

- **Size** = n × n (number of rows = number of columns)  
- Only square matrices can have **determinant, inverse, and eigenvalues**.

### **Key Points**
- Check if the **number of rows equals the number of columns**.  
- Example: 3 × 3 or 4 × 4 → **Square ✅**  
- Example: 2 × 3 → **Not Square ❌**
""")

if st.button("CHECK SQUARE"):
 if(rows == columns):
    st.success("YES!");
 else:
    st.error("NO!\n");

st.subheader("ARE THE MATRICES SINGULAR?");
if st.button("EXPLANATION",key="sing-exp"):
  st.markdown("""
## Singularity of a Matrix

**Definition:** A matrix is **singular** if its determinant is 0 (inverse does not exist).  

**Example:**  
Matrix A = [[2, 4],
[1, 2]] # det(A) = 0 → Singular

""")
if st.button("CHECK SINGULARITY"):
 
 if(det1 != 0 and det2 != 0):
    st.success("NO! THEY ARE NOT SINGULAR. DETERMINANT IS NOT ZERO.THEREFORE, THEIR INVERSE EXISTS.")
 else:
    st.warning("YES!\n");


st.subheader("INVERSE OF THE MATRICES:\n");

if st.button("FIND INVERSE"):
 if(det1 !=0):
    inv1 = np.linalg.inv(matrix_one);
    st.write("INVERSE OF MATRIX ONE:\n",inv1);
 else:
    st.error("MATRIX ONE IS SINGULAR!");

 if(det2 !=0):
    inv2 = np.linalg.inv(matrix_two);
    st.write("INVERSE OF MATRIX TWO:\n",inv2);
 else:
    st.error("MATRIX TWO IS SINGULAR!\n");

st.subheader("\nTRANSPOSE OF THE MATRICES:\n");
if st.button("EXPLANATION",key="trans-exp"):
  st.markdown("""
## Transpose of a Matrix

**Definition:** Swapping rows and columns of a matrix.  

**Example:**  
Matrix A = [[1, 2, 3],
[4, 5, 6]]
Transpose Aᵀ = [[1, 4],
[2, 5],
[3, 6]]

""")
if st.button("TRANSPOSE"):
 st.write("MATRIX ONE TRANSPOSE:\n",trans1);
 st.write("MATRIX TWO TRANSPOSE:\n",trans2);


st.subheader("\n ARE THESE MATRICES ORTHOGONAL?\n");
if st.button("EXPLANATION",key="ortho-exp"):
  st.markdown("""
## Orthogonal Matrices

**Definition:** Two matrices are **orthogonal** if the **transpose of one multiplied by the other gives the identity matrix** (Aᵀ·B = I).  

**Example:**  
Matrix A = [[1, 0],
[0, 1]]

Matrix B = [[1, 0],
[0, 1]] # Aᵀ·B = I → Orthogonal

""")
# if A.transpose of B = identity matrix then they are orthogonal

product_of_one_transOf_two = np.dot(matrix_one,trans2);

if st.button("CLICK HERE TO CHECK"):
 if np.allclose(product_of_one_transOf_two,i):
    st.success("THE MATRICES ARE ORTHOGONAL!");
 else:
    st.error("THEY ARE NOT ORTHOGONAL!\n");

st.subheader("AVERAGE OF THE MATRICES");

if st.button("FOR MATRIX ONE"):
  avg_of_one = round(np.mean(matrix_one));
  st.write("AVERAGE OF MATRIX ONE: ",avg_of_one);
if st.button("FOR MATRIX TWO"):
  avg_of_two = round(np.mean(matrix_two));
  st.write("AVERAGE OF MATRIX TWO: ",avg_of_two);

st.subheader("SUM OF THE MATRIX");

if st.button("SUM OF MATRIX ONE"):
  st.write(np.sum(matrix_one));
if st.button("SUM OF MATRIX TWO"):
  st.write(np.sum(matrix_two));

st.subheader("MINIMUM NUMBER IN THE MATRIX");

if st.button("IN MATRIX ONE"):
  st.write(np.min(matrix_one));
if st.button("IN MATRIX TWO"):
  st.write(np.min(matrix_two));

st.subheader("MAXIMUM NUMBER IN THE MATRIX");

if st.button("IN MATRIX ONE",key="max_btn1"):
  st.write(np.max(matrix_one));
if st.button("IN MATRIX TWO",key="max_btn2"):
  st.write(np.max(matrix_two));


st.subheader("SUM OF ROWS");
if st.button("IN MATRIX ONE",key="rowsum_btn1"):
  st.write(np.sum(matrix_one,1));
if st.button("IN MATRIX TWO",key="rowsum_btn2"):
  st.write(np.sum(matrix_two,1));

st.subheader("SUM OF COLUMNS");
if st.button("IN MATRIX ONE",key="colsum_btn1"):
  st.write(np.sum(matrix_one,0));
if st.button("IN MATRIX TWO",key="colsum_btn2"):
  st.write(np.sum(matrix_two,0));

# trace: sum of diagonal elements 
st.subheader("TRACE OF A MATRIX");
if st.button("EXPLANATION",key="trace-exp"):
  st.markdown("""
## Trace of a Matrix

**Definition:** The **sum of diagonal elements** of a square matrix.  

**Example:**  
Matrix A = [[1, 2],
[3, 4]] # Trace = 1 + 4 = 5

""")
if st.button("TRACE OF MATRIX ONE",key="m1trace_btn1"):
  st.write(np.trace(matrix_one));
if st.button("TRACE OF MATRIX TWO",key="m2trace_btn2"):
  st.write(np.trace(matrix_two));

st.subheader("RANK OF A MATRIX");

if st.button("EXPLANATION",key="rank-exp"):
 st.markdown("""
### **Definition**
The **rank of a matrix** is the number of linearly independent **rows** or **columns** in the matrix.  

- It tells you **how much “information” the matrix has**.  
- Rank is always ≤ `min(number of rows, number of columns)`.

### **Key Points**
- If a matrix has **full rank**, all rows (or columns) are independent.  
- If some rows (or columns) are multiples of others, `rank < total rows/columns`.  
- Rank is useful in **solving linear equations, determinants, and ML concepts like PCA**.

### **Easy Example 1**

Matrix:
A = [[1, 2],
[3, 4]]


- Rows: `[1,2]` and `[3,4]` → not multiples of each other ✅  
- Columns: `[1,3]` and `[2,4]` → not multiples of each other ✅  

**Rank = 2** (full rank)

### **Easy Example 2**

Matrix:
B = [[1, 2],
[2, 4]]


- Second row `[2,4]` = 2 × `[1,2]` ❌  
- Only 1 independent row → **Rank = 1**
""")

if st.button("RANK OF MATRIX ONE",key="rank_btn1"):
  st.write(np.linalg.matrix_rank(matrix_one));
if st.button("RANK OF MATRIX TWO",key="rank_btn2"):
  st.write(np.linalg.matrix_rank(matrix_two));


st.subheader("ARE THESE DIAGONAL MATRICES");
if st.button("EXPLANATION",key="diag-exp"):
  st.markdown("""
## Diagonal Matrix

**Definition:** A matrix is **diagonal** if all non-diagonal elements are 0.  

**Example:**  
Matrix A = [[5, 0, 0],
[0, 3, 0],
[0, 0, 8]] # Diagonal Matrix

""")
if st.button("MATRIX ONE",key="diag_btn1"):
  if np.all(matrix_one == np.diag(np.diag(matrix_one))):
   st.success("MATRIX ONE IS DIAGONAL");
  else:
    st.error("MATRIX ONE IS NOT DIAGONAL")
if st.button("MATRIX TWO",key="diag_btn2"):
  if np.all(matrix_two == np.diag(np.diag(matrix_two))):
   st.success("MATRIX TWO IS DIAGONAL");
  else:
    st.error("MATRIX TWO IS NOT DIAGONAL");

