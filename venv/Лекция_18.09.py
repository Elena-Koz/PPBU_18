# Множества
n = 10
m = 100

# print('First variable: "', n,  '" Second variable ', m ,
#       '"m/n = ', m//n, sep='')

# print('First variable- "%d", Second variable - "%d", m/n=%d' , (n,m, m/n))
# print('First variable- "{}", Second variable - "{}", m/n="{}"'.format(n,m, m/n))
# nn = f'First variable- "{n}", Second variable - "{m}", m/n="{m//n: 2f}"'
# print(nn)

ls = [22, 22, 22, 33, 44]
st = set(ls)
print(st)
st.clear()
st= {22, 33, 44}
print(st)

st.add(100)
print(st)

for i in st:
    print(i)
st.update({2,3})
print(st)

n = st.pop()
print(n)
print(st)

# st.remove(3)
# st.discard(2)
# print(n)
# print(st)

st1 = {3, 4, 33}
st2 = {3, 4, 44}
res = st1.union(st2)
print(res)

res = st1| st2
print(res)

