mthd = input("Math todo? ")
fn = float(input("First Number: "))
sn = float(input("Second Number: "))

if mthd == ('*'):
    sum = fn * sn
    print("Sum of: ",fn,mthd,sn,"= ", sum)
elif mthd == ('+'):
    sum = fn + sn
    print("Sum of: ",fn,mthd,sn,"= ", sum)
elif mthd == ('-'):
    sum = fn - sn
    print("Sum of: ",fn,mthd,sn,"= ", sum)
elif mthd == ('/'):
    sum = fn / sn
    print("Sum of: ",fn,mthd,sn,"= ", sum)
elif mthd == ('^'):
    sum = fn ** sn
    print("Sum of: ",fn,mthd,sn,"= ", sum)
else:
    print("Not able to complete math. Error: unsupported sign ", mthd)
