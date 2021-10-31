# 1 - masala

"""musbat sonlardan tashkil topgan royhat"""

# n = int(input())
# a = []
# for x in range(1,n+1) :
#     b = int(input())
#     if b>0 and b%2!=0 :
#         a.append(b)
# for x in a :
#     print(x,end= " ")

# 2-masala


"""2 ni darajalaridan tashkil topgan massiv"""

# n = int(input())
# a = []
# for x in range(n) :
#     a.append(pow(2,x))
# print(a)

# 3 - masala]

# n = int(input())
# b = int(input())
# d = int(input())
# a = []
# a.append(b)
# for x in range(1,n) :
#     a.append(a[x-1]+d)
# print(a)

# 4 - masala]

# n = int(input())
# b = int(input())
# q = int(input())
# a = []
# a.append(b)
# for x in range(1,n) :
#     a.append(a[x-1]*q)
# print(a)

# 5 - masala

"""fibonachi sonlardan tashkil topgan royhat"""

# n = int(input())
# a = [1,1]
# b1,b2 = 1,1
# for x in range(n) :
#     b = int
#     b = b1+b2
#     b1 = b2
#     b2 = b
#     a.append(b)
# print(a)

# 6 - masala

# n = int(input())
# a = [1,1]
# b1,b2 = int(input()),int(input())
# for x in range(n) :
#     c = int
#     c = b1+b2
#     b1 = b2
#     b2 = c
#     a.append(c)
# print(a)

# 7 - masala

# a = []
# a.extend(range(10))
# a.reverse()
# print(a)

# 8 - masala

# a = []
# n = int(input())
# for x in range(n) :
#     b = int(input())
#     a.append(b)
# i = 0
# for x in range(n) :
#     if a[x]%2==0 :
#         a.reverse()
#         print(a[x],end=",")
#         i+=1
# print('\n',i)

# 9-masala

# a = []
# n = int(input())
# for x in range(n) :
#     b = int(input())
#     a.append(b)
# i = 0
# for x in range(n):
#     if a[x]%2!=0 :
#         print(a[x],end=",")
#         i+=1
# print('\n',i)

# 10 - masala

# a = []
# n = int(input())
# for x in range(n) :
#     b = int(input())
#     a.append(b)
# for x in range(n) :
#     if a[x]%2==0 :
#         a.sort()
#         print(a[x])
# for x in range(n) :
#     if a[x]%2==0 :
#         a.sort(reverse=True)
#         print(a[x])

# 11 - masala

# a = list(range(10))
# a.sort(reverse=True)
# print(a)

# 12 - masala

# n = int(input())
# a = list(range(1,n))
# for x in range(n):
#     if a[x]%2==0 :
#         print(a[x],end=',')

# 13 - masala

# a = list(range(1,10))
# for x in range(10) :
#     if a[x]%2!=0 :
#         a.reverse()
#         print(a[x],end=',')

# 14 - masala

# a = []
# n = int(input())
# for x in range(n) :
#     b = int((input()))
#     a.append(b)
# for x in range(n) :
#     if a[x]%2==0 :
#         print(a[x],end=',')
# for x in range(n) :
#     if a[x]%2!=0 :
#         print(a[x],end=',')

# 15 - masala

# a = []
# n = int(input())
# for x in range(n) :
#     b = int(input())
#     a.append(b)
# for x in range(n) :
#     if x%2!=0 :
#         a.sort(reverse=True)
#         print(a[x],end=',')
# for x in range(n) :
#     if x%2==0 :
#         a.sort(reverse=True)
#         print(a[x],end=',')

# 16 - masala

# a = [1,2,3,4,5,6,7]
# for x in range(len(a)//2 if len(a)%2==0 else len(a)//2+1 ) :
#     if len(a) >=2 :
#         print(a[0],a[-1],end=" ")
#     else:
#         for y in a :
#             print(y,end=' ')
#         break
#     a.pop(0)
#     a.pop(-1)

# 17 - masala

# a= [1,2,3,4,5,6,7,8,9,10]
# for x in range(len(a) if len(a)%4==0 else len(a)//4+1) :
#     if len(a)>=4 :
#         print(a[0],a[1],a[-1],a[-2],end=' ')
#     else:
#         for y in a :
#             print(y,end=' ')
#         break
#     a.pop(0)
#     a.pop(0)
#     a.pop(-1)
#     a.pop(-1)


# 18 - masala

# a = []
# n = int(input())
# for x in range(n) :
#     b = int(input())
#     a.append(b)
# for x in range(n) :
#     if a[x] < a[n-1] :
#         print(a[x])
#         break

# 19 - masala

# a = [1,6,45,68,40,3,19]
# m = 0
# for x in range(len(a)) :
#     if a[0] < a[x] < a[-1] :
#         m = x
# print(m)


# 20 - masala

# a = [7,9,3,1,5,8]
# s = 0
# n,k,l = int(input()),int(input()),int(input())
# for x in range(n) :
#     if x>=k and x<=l :
#         s+=a[x]
# print(s)

# 21 - masala

# a = [7,9,3,1,5,8]
# s = 0
# n,k,l = int(input()),int(input()),int(input())
# for x in range(n) :
#     if x>=k and x<=l :
#         s+=a[x]/(l+1-k)
# print(s)

# 22 - masala

# a = [7, 9, 3, 1, 5, 8]
# k, l = int(input()), int(input())
# print(sum(a) - sum(a[i] for i in  range(k, l+1)))

# 23 - masala

# 1 - usul

# a = [7, 9, 3, 1, 5, 8]
# k, l = int(input()), int(input())
# print(((sum(a) - sum(a[x]) for x in range(k,l+1))))

# 2 - usul

# # a = [7,9,3,1,5,8]
# k,l = int(input()),int(input())
# a = a[:k] + a[l+1:]
# print(sum(a))

# 24 - masala

# a = [3,8,13,18,23,28]
# son = bool
# for x in range(1,len(a)-1) :
#     if a[x+1]==a[x]+a[x-1] :
#         son = True
# if son :
#     print(a[1] - a[0])

# 25 - masala

# a = [32,16,8,4,2,1]
# son = bool
# for i in range(1,len(a)-1) :
#     if a[i+1]/a[i]==a[i]//a[i-1] :
#         son = 1
# if son :
#     print(a[1]/a[0])

# 26 - masala

# a = [12, 9, 18, 3, 6]
# for x in range(len(a)-1):
#     if (a[x] + a[x + 1]) % 2 != 0:
#         print(a[x])
#         break
#     else:
#         print(1)

# 27 - masala

# a = [7,3,1,-9,3]
# son = True
# for i in range(len(a)-1) :
#     if a[i]+a[i] ==0 and a[i+1]+a[i+1]!=0 :
#         print(a[i])

# 28 - masala

# a = [1, 6, 5, 3 ,4, 5]
# print(min(a[x] for x in range(0,len(a),2)))

# 29 - masala

# a = [1, 6, 5, 3, 4, 5]
# print(max(a[x] for x in range(1,len(a),2)))

# 30 - masala

# a = [1, 6, 5, 3, 4, 5]
# m = 0
# for i in range(len(a)-1) :
#     if a[i]>a[i+1] :
#         m+=1
#         print(i,end=' ')
# print('\n',m)

# 31 - masala

# a = [1, 6, 5, 3, 4, 5]
# m = 0
# for i in range(1,len(a)) :
#     if a[i-1]<a[i] :
#         m+=1
#         print(i,end=' ')
# print('\n',m)

# 32 - masala

# a = [1, 6, 5, 3, 4, 5]
# for i in range(1,len(a)-1) :
#     if a[i-1] > a[i] <a[i+1] :
#         print(i)
#         break

# 33 - masala

# a = [1, 6, 5, 3, 4, 5]
# m = 0
# for i in range(1,len(a)-1) :
#     if a[i-1] < a[i] > a[i+1] :
#         m = i
# print(m)

# 34 - masala

# a = [6,1,3,2,4,3]
# for i in range(1,len(a)-1) :
#     if a[i-1] > a[i] and a[i] < a[i+1] :
#         print(a[i])

# 35 - masala

# a = [6, 1, 3, 2, 4, 3]
# b = []
# for i in range(1,len(a)-1) :
#     if a[i-1] <a[i] > a[i+1] :
#         b.append(a[i])
# print(max(b))

# 36 - masala

# a = [3, 4, 2, 1, 5, 3]
# for i in range(1,len(a)-1) :
#     if a[i-1] < a[i] > a[i+1] and a[i-1] > a[i] <a[i+1] :
#         a.pop(i)
# print(max(a))

# 37 - masala

# a = [6, 1, 3, 2, 4, 3]
# m = 0
# for i in range(len(a)-1) :
#     if a[i] < a[i+1] :
#         m+=1
# print(m)

# 38 - masala

# a = [6, 1, 3, 2, 4, 3]
# m = 0
# for i in range(len(a)-1) :
#     if a[i] > a[i+1] :
#         m+=1
# print(m)

# 39 - masala

# a = [6, 1, 3, 2, 4, 3]
# m = 0
# for i in range(len(a)-1) :
#     if a[i] <a[i+1] or a[i] >a[i+1] :
#         m+=1
# print(m)

# 40 - masala

# a = [6, 1, 3, 2, 4, 3]
# r = float(input())
# min1 = a[0]
# for i in range(len(a)) :
#     min = abs(a[i] - r)
#     for j in range(i+1,len(a)) :
#         if min < abs(a[j]- r) :
#             print(a[i])

# 41 - masala

# a = [6, 1, 3, 2, 4, 3]
# max = a[0]+a[1]
# for i in range(len(a)-1) :
#     if max < a[i]+a[i+1] :
#         max = a[i]+a[i+1]
# print(max)

# 43 - masala

# a = []
# n = int(input())
# for i in range(n) :
#     b = int(input())
#     a.append(b)
# a.sort()
# for i in range(1,len(a),2) :
#     print(a[i])

# 44 - masala

# a = [5, 1, 2, 1, 3, 7]
# for i in range(len(a)) :
#     if a.count(a[i]) > 1 :
#         print(i,end=' ')

# 47 - masala

# a = [5, 1, 2, 4, 3, 7]
# m = 0
# for i in range(len(a)) :
#     if a.count(a[i]) > 1 :
#         m+=1
# print(len(a)-m)

# 48 - masala

# a = [3, 1, 2, 2, 2, 1,3]
# max = a.count(a[0])
# for i in range(len(a)) :
#     if max < a.count(a[i]) :
#         max = a.count(a[i])
# print(max)

# 49 - masala

# a = [1, 2, 4, 4, 3, 6]
# b = []
# b.extend(range(1,len(a)+1))
# son = bool
# for i in range(len(a)) :
#     if b[i] != a[i] :
#         print(i)
#         break

# 50 - masala

# a = [1,3,2,5,4]
# m = 0
# for i in range(len(a)-1) :
#     for j in (i+1,len(a)-1):
#         if a[i] > a[j] :
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
#             m+=1
# print(a)
# print(m)

# 51 - masala

# a = [3, 5, 9, 6, 1]
# b = [2, 5, 7, 4, 9]
# for i in range(len(a)) :
#     a[i],b[i]=b[i],a[i]
# print(a)
# print(b)

# 52 - masala

# a = []
# b = []
# n = int(input())
# for i in range(n) :
#     m = int(input())
#     a.append(m)
# for i in range(n):
#     if a[i] < 5 :
#         b.append(2*a[i])
#     else:
#         b.append(a[i]/2)
#     print(b[i],end=' ')

# 53 - masala

# a = [3, 5, 9, 6, 1]
# b = [2, 5, 7, 4, 9]
# c = []
# for i in range(len(a)):
#     c.append(max(a[i],b[i]))
#     print(c[i],end=' ')

# 54 - masala

# a = [8, 5, 9, 6, 1]
# b = []
# for i in range(len(a)) :
#     if a[i]%2==0 :
#         b.append(a[i])
# print(len(b),b)

# 55 - masala

# a = [8, 5, 9, 6, 1]
# b = []
# for i in range(len(a)) :
#     if a[i]%2!=0 :
#         b.append(a[i])
# print(len(b),b)

# 56 - masala

# a = [1, 3, 7, 4, 5, 8, 6, 9, 2]
# b = []
# for i in range(len(a)) :
#     if i%3==0 :
#         b.append(a[i])
# print(b)

#  57 - masala

# a = [2, 4, 8, 7, 3, 9]
# b = []
# for i in range(0,len(a),2) :
#     b.append(a[i])
# for i in range(1,len(a),2) :
#     b.append(a[i])
# print(b)

# 58 - masala

# a = [2, 4, 8, 7, 3, 9]
# b = []
# for x in range(len(a)) :
#     b.append(sum(a[:x+1]))
# print(b)

# 59 - masala

# a = [2, 4, 8, 7, 3, 9]
# b = []
# for x in range(len(a)) :
#     b.append(sum(a[:x+1])/x)
# print(b)

# 60 - masala

# a = [2, 4, 6, 8, 10, 12]
# b = []
# for i in range(len(a)) :
#     b.append(sum(a[i:]))
# print(b)

# 61 - masala

# a = [2, 4, 6, 8, 10, 12]
# b = []
# for i in range(len(a)) :
#     b.append(sum(a[i:])/(n-x))
# print(b)

# 63 - masala

# a = [0, 2, 4, 6, 8]
# b = [1, 3, 5, 7, 9]
# c = []
# c=a+b
# c.sort()
# print(c)

#  64 - masala

# a = [3, 2, 1]
# b = [5, 4, 0]
# c = [9, 8, 6]
# d = []
# d = a+b+c
# d.sort(reverse=True)
# print(d)
