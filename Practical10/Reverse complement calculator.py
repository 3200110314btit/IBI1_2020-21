s = input()
z ='ATcgcaTT'
#make a example
Dic ={'A':'T','C':'G','T':'A','G':'C','a':'t','t':'a','c':'g','g':'c'}
X=''
y=''
for i in range(0,len(s),1):
    X = X + Dic[s[i:i+1]]
for i in range(0,len(z),1):
    y = y + Dic[z[i:i+1]]
#make X is the convert complement
def str_reverse(X):
    return X[::-1]
def str_reverse(y):
    return y[::-1]
#use this way to reverse
print (str_reverse(X))
print (y)
print (str_reverse(y))