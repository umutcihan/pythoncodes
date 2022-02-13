X=[123,3465,47,689,21,2456,5679,4124,802345,1234,11234,1234,1234,1234,1234,145,245,4,123,1,2,3,4,5,6,3,2,1,3,5,3,2,2,2,23,52,5,2,123,1,23,234,2,421,1,31]
min
def ins(a,X):
    if a==len(X):
        return X
    for i in range(a,len(X)):
        if i==a:
            min=X[i]
            indice=i
        if X[i]<min:
            min=X[i]
            indice=i
    c=X[indice]
    d=X[a]
    X[a]=c
    X[indice]=d
    return ins(a+1,X)
print(ins(0,X))
