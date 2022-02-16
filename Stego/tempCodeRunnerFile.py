
          m[k] = A[6]
          m[k + 1] = B[6] 
        k = k + 2

    M = []
    str1 = ""

    for j in range(0, len(m) + 1):
      if j%8 != 0 or j == 0:
        str1 = str1 + str(m[j])