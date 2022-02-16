from PIL import Image, ImageFilter
import numpy as np
import cv2 as cv
from numpy.core.fromnumeric import repeat
import os

#REVERSE STEGO

def revStego(img_):
  #TEXT
  choice = int(input("enter 1 or 2:"))
  if choice == 1:
    img = cv.cvtColor(img_, cv.COLOR_BGR2GRAY)
    r, c = img.shape
    k = 0
    N = img[0, 0]
    m = np.zeros(N*8, dtype=int)

    for i in range(0, r):
      for j in range(0, c):
        if i == 0 and j == 0:
          continue
        P = img[i, j]
        if k < N*8:
          A = format(P, '08b')
          B = format(P + 1, '08b')
          m[k] = A[6]
          m[k + 1] = B[6] 
        k = k + 2

    M = []
    str1 = ""

    for j in range(0, len(m) + 1):
      if j%8 != 0 or j == 0:
        str1 = str1 + str(m[j])
      else:
        M.append(str1)
        str1 = ""
    ascii_string = "".join([chr(int(binary, 2)) for binary in M])
    print(ascii_string)

  #IMAGE
  else:
    img = cv.cvtColor(img_, cv.COLOR_BGR2GRAY)
    print(img)
    r, c = img.shape
    k = 0
    p = int(input("enter rows"))
    q = int(input("enter columns"))
    N = p*q
    m = np.zeros(N*8, dtype=int)

    for i in range(0, r):
      for j in range(0, c):
        # if i == 0 and j == 0:
        #   continue
        P = img[i, j]
        if k < N*8:
          A = format(P, '08b')
          B = format(P + 1, '08b')
          m[k] = A[6]
          m[k + 1] = B[6] 
        k = k + 2
    # print(m)
    M = []
    str1 = ""
    for j in range(0, len(m) + 1):
      if j%8 != 0 or j == 0:
        str1 = str1 + str(m[j])
      else:
        if j == 8:
          M.append(str1)
        else:
          M.append(str(m[j - 8]) + str1)
        str1 = ""
    # M.append(m[0])
    print(len(M))
    print(M)
    
    img_arr = np.reshape(M, (p, q))
    img_final = np.zeros((p, q), dtype = int)
    # print(img_final)
    for i in range(0, p):
      for j in range(0, q):
        img_final[i, j] = int(img_arr[i, j], 2)
    print(img_final)
    path = 'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\'
    cv.imwrite(path+'output.png', img_final)
    # save = np.asarray(img_arr)
    # img_final = Image.fromarray(save)
    # img_final.save(path+'output.png')
    # ascii_string = "".join([chr(int(binary, 2)) for binary in M])
    # print(ascii_string)
    # save.show

# def stego7Bit(I_, message):
choice = int(input("enter 1 or 2:"))
if choice == 1:
  message = input("Enter the string to be encoded: ")
  N = len(message)*8
  binaryString = ''.join(format(ord(i), '08b') for i in message)
  I_ = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\in\\wheel.png')
  I = cv.cvtColor(I_, cv.COLOR_BGR2GRAY)
  r, c = I.shape
  X = np.zeros((r, c), dtype = np.uint8)
  K = 0
  a = 0
  for l in range(0, r):
    for m in range(0, c):
      if l == 0 and m == 0:
        X[l, m] = len(message)
        continue
      A = format(I[l, m], '08b')
      B = format(I[l, m] + 1, '08b')
      if K < (N - 1):
        M1 = int(binaryString[a])
        M2 = int(binaryString[a + 1])
        if (int(A[6]) == 0 and int(B[6]) == 0):
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m]
          elif (M1 == 0 and M2 == 1):
            X[l, m] = I[l, m] + 1
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m] - 1
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m] + 2
        
        elif int(A[6]) == 0 and int(B[6]) == 1:
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m] - 1
          elif M1 == 0 and M2 == 1:
            X[l, m] = I[l, m]
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m] + 2
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m] + 1
        
        elif (int(A[6]) == 1 and int(B[6]) == 0):
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m] + 1
          elif (M1 == 0 and M2 == 1):
            X[l, m] = I[l, m] + 2
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m]
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m] - 1
        
        elif (int(A[6]) == 1 and int(B[6]) == 1):
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m] + 2
          elif (M1 == 0 and M2 == 1):
            X[l, m] = I[l, m] - 1
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m] + 1
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m]
      
      else:
        X[l, m] = I[l, m]
      K = K + 2
      a = a + 2

  gray = cv.cvtColor(X, cv.COLOR_GRAY2RGB)
  path = 'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\'
  saved = cv.imwrite(path+'lenastego5.png', gray)
  forRev = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\lenastego5.png')
  revStego(forRev)

else:
  img_ = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\in\\dog.png')
  img = cv.cvtColor(img_, cv.COLOR_BGR2GRAY)
  print(img)
  p, q = img.shape
  # print(img)
  print(p, q)
  binaryString = ""
  for i in range(0, p):
    for j in range(0, q):
      binaryString = binaryString + format(img[i, j], '08b')
  N = len(binaryString)
  # print(binaryString)
  print(N)

  I_ = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\in\\rose.jpg')
  I = cv.cvtColor(I_, cv.COLOR_BGR2GRAY)
  print(I)
  r, c = I.shape
  print(r, c)
  X = np.zeros((r, c), dtype = np.uint8)
  K = 0
  a = 0
  for l in range(0, r):
    for m in range(0, c):
      # if l == 0 and m == 0:
      #   X[l, m] = len(message)
      #   continue
      A = format(I[l, m], '08b')
      B = format(I[l, m] + 1, '08b')
      if K < (N - 1):
        M1 = int(binaryString[a])
        M2 = int(binaryString[a + 1])
        if (int(A[6]) == 0 and int(B[6]) == 0):
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m]
          elif (M1 == 0 and M2 == 1):
            X[l, m] = I[l, m] + 1
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m] - 1
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m] + 2
        
        elif int(A[6]) == 0 and int(B[6]) == 1:
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m] - 1
          elif M1 == 0 and M2 == 1:
            X[l, m] = I[l, m]
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m] + 2
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m] + 1
        
        elif (int(A[6]) == 1 and int(B[6]) == 0):
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m] + 1
          elif (M1 == 0 and M2 == 1):
            X[l, m] = I[l, m] + 2
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m]
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m] - 1
        
        elif (int(A[6]) == 1 and int(B[6]) == 1):
          if (M1 == 0 and M2 == 0):
            X[l, m] = I[l, m] + 2
          elif (M1 == 0 and M2 == 1):
            X[l, m] = I[l, m] - 1
          elif(M1 == 1 and M2 == 0):
            X[l, m] = I[l, m] + 1
          elif(M1 == 1 and M2 == 1):
            X[l, m] = I[l, m]
      
      else:
        X[l, m] = I[l, m]
      K = K + 2
      a = a + 2

  gray = cv.cvtColor(X, cv.COLOR_GRAY2RGB)
  path = 'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\'
  saved = cv.imwrite(path+'stegoOutput.png', gray)
  forRev = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\stegoOutput.png')
  revStego(forRev)






# I_ = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\in\\wheel.png')
# I = cv.cvtColor(I_, cv.COLOR_BGR2GRAY)
# r, c = I.shape
# X = np.zeros((r, c), dtype = np.uint8)
# K = 0
# a = 0
# for l in range(0, r):
#   for m in range(0, c):
#     if l == 0 and m == 0:
#       X[l, m] = len(message)
#       continue
#     A = format(I[l, m], '08b')
#     B = format(I[l, m] + 1, '08b')
#     if K < (N - 1):
#       M1 = int(binaryString[a])
#       M2 = int(binaryString[a + 1])
#       if (int(A[6]) == 0 and int(B[6]) == 0):
#         if (M1 == 0 and M2 == 0):
#           X[l, m] = I[l, m]
#         elif (M1 == 0 and M2 == 1):
#           X[l, m] = I[l, m] + 1
#         elif(M1 == 1 and M2 == 0):
#           X[l, m] = I[l, m] - 1
#         elif(M1 == 1 and M2 == 1):
#           X[l, m] = I[l, m] + 2
      
#       elif int(A[6]) == 0 and int(B[6]) == 1:
#         if (M1 == 0 and M2 == 0):
#           X[l, m] = I[l, m] - 1
#         elif M1 == 0 and M2 == 1:
#           X[l, m] = I[l, m]
#         elif(M1 == 1 and M2 == 0):
#           X[l, m] = I[l, m] + 2
#         elif(M1 == 1 and M2 == 1):
#           X[l, m] = I[l, m] + 1
      
#       elif (int(A[6]) == 1 and int(B[6]) == 0):
#         if (M1 == 0 and M2 == 0):
#           X[l, m] = I[l, m] + 1
#         elif (M1 == 0 and M2 == 1):
#           X[l, m] = I[l, m] + 2
#         elif(M1 == 1 and M2 == 0):
#           X[l, m] = I[l, m]
#         elif(M1 == 1 and M2 == 1):
#           X[l, m] = I[l, m] - 1
      
#       elif (int(A[6]) == 1 and int(B[6]) == 1):
#         if (M1 == 0 and M2 == 0):
#           X[l, m] = I[l, m] + 2
#         elif (M1 == 0 and M2 == 1):
#           X[l, m] = I[l, m] - 1
#         elif(M1 == 1 and M2 == 0):
#           X[l, m] = I[l, m] + 1
#         elif(M1 == 1 and M2 == 1):
#           X[l, m] = I[l, m]
    
#     else:
#       X[l, m] = I[l, m]
#     K = K + 2
#     a = a + 2

# gray = cv.cvtColor(X, cv.COLOR_GRAY2RGB)
# path = 'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\'
# saved = cv.imwrite(path+'lenastego5.png', gray)
# forRev = cv.imread(r'C:\\Users\\HP\\Desktop\\ISAA\\J\\assets\\out\\lenastego5.png')
# revStego(forRev)

