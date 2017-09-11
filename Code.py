xz=(lambda x,y: ((lambda z,c : (x(z),print(c) if c>0 or c>1 else 0)),print(y) if y>1 or y>-1 else 1))

print(xz((lambda new_func: print("This is awesome"))(87),45))
