print("Первое задание")
a= int(input("Введите целое число: "))
b= float(input("Введите дробное число: "))
answer= round(b/a, 3)
left= (b//a)
exp= b**a
print ("Answer: " + str(answer))
print("Remain: " + str(left))
print("Exponentiation: " + str(exp))

print("Второе задание")
n= int(input("Введите количество школьников: "))
k= int(input("Введите количество яблок: "))
rest= divmod(k,n)
print("По ровну яблок достанется " + str(rest[0]) + " ученикам, и останется " + str(rest[1]) + " яблок(а)")

print("Третье задание")
num= int(input("Введите трехзначное число: "))
print(num// 100 + (num//10 - num//100*10) + (num - num//10*10))

print("Четвертое задание")
l= int(input("first: "))
m= int(input("second: "))
print(l+m, "|", l-m, "|", l*m, "|", l/m, "|", l//m, "|", l%m, "|", l**m)

print("Пятое задание")
w= int(input("first: "))
e= int(input("second: "))
print((w+4*e) * (w-3*e) +(w**2))

print("Шестой задание")
km= int(input("km: "))
minutes= int(input("minutes: "))
meter= km/1000
seconds=minutes/60
print(round(meter/seconds, 2), "m/s")

print("Седьмое задание")
inp= int(input("число: "))
if inp%2==0:
    print("0")
else:
    print("1")
