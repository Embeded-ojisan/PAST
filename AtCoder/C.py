N = int(input())

s = (N-1)//5

total = (10**17) * ((N-1)//(5**17)) + (10**16) * ((N-1)//(5**16)) + (10**15) * ((N-1)//(5**15)) +   (10**14) * ((N-1)//(5**14)) +  (10**13) * ((N-1)//(5**13)) + (10**12) * ((N-1)//(5**12)) +  (10**11) * ((N-1)//(5**11)) +  (10**10) * ((N-1)//(5**10)) +  (10**9) * ((N-1)//(5**9)) +  (10**8) * ((N-1)//(5**8)) +  (10**7) * ((N-1)//(5**7)) +  (10**6) * ((N-1)//(5**6)) +  (10**5) * ((N-1)//(5**5)) +  (10**4) * ((N-1)//(5**4)) + (10**3) * ((N-1)//(5**3)) + (10**2) * ((N-1)//(5**2)) + (10**1) * ((N-1)//(5**1)) + 2 * (N-1)

print(str(total))
