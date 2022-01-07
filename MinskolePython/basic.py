# Date-5 jan 2022
x = 10.566
print(x)
print(type(x))

print("---------------------------------------------------")


# Function
def calculator(x1, y1):
    print(x1 + y1)
    print(x1 + y1)
    print(x1 - y1)
    print(x1 * y1)
    print(x1 / y1)
    print(x1 % y1)


calculator(20, 46)

print("---------------------------------------------------")

print("Function without parameter without return type")


def add():
    print(7 + 9)


add()

print("Function with parameter without return type")


def sub(s1, s2):
    print(s1 - s2)


sub(21, 11)

print("Function with parameter with return type")


def mul(m1, m2):
    return (m1 * m2)


multiply = mul(23, 12)
print(multiply)

print("Function without parameter with return type")


def div():
    return (56 / 8)


divide = div()
print(divide)

print("---------------------------------------------------")

g = [11, 22, 33, 44, 55]
print(g[0])
j = len(g)
print(j)

for ga in g:
    print((ga))

fruits = ["apple", "mango", "banana"]
print(fruits[0])

# for item in fruits:     Loop-1
#     print(item)

# for i in range(3):       Loop-2
#     print((fruits[i]))

for i in range(len(fruits)):  # Loop-3
    print(fruits[i])

# -----------------------Methods--------------------------
color = ["red", "black", "geeen", "red"]

# Count
a = color.count("red")
print(a)

print("---------------------------------------------------")
# Append-Add element to end of the list
r = color.append("blue")
print(r)
print(color)

print("---------------------------------------------------")

# Pop-Remove last element
m = color.pop()
print(m)  # Return removed element
print(color)

print("---------------------------------------------------")

#Date-6 jan 2022

# Remove-Remove specific element in list
jj = color.remove("red")
print(jj)  # Remove first occerance
print(color)

print("---------------------------------------------------")

# Copy
i=[1,4,7]
k=i.copy()
k[0]="A"
print(i)
print(k)

print("---------------------------------------------------")

# Extend
arrone=["a","g","r"]
arrtwo=["f","u","i"]

arrone.extend(arrtwo)
print(arrone)
print(arrtwo)

print("---------------------------------------------------")

# Index
mixname=["karan","laukik","abhi","prasad","laukik","prati","laukik"]

inx=mixname.index("laukik",mixname.index("laukik")+1)
print(inx)

print("---------------------------------------------------")

# For finding multiple index of repeated words
kk=[]
for i in range(len(mixname)):
    if mixname[i]=="laukik":
        kk.append(i)

print(kk[1])
print(kk)

print("---------------------------------------------------")
city=["Parbhani","mumbai","jaipur","jalna","nagpur"]

# Insert
city.insert(3,"pune")
print(city,"Here pune city is added")

# Remove
city.remove("jalna")
print(city,"Here jalna city is removerd")

# Reverse
city.reverse()
print(city,"Here list of city reversed")

print("---------------------------------------------------")

#Date-7 jan 2022

h="hello"

print(h)
print(h[0])
print(h[len(h)-1])

print("---------------------------------------------------")

fruit="apple"

print("________________Loop-1__________________")
for char in fruit:
    print(char)

print("________________Loop-2__________________")
for i in range(len(fruit)):
    print(fruit[i])

print("---------------------------------------------------")
cityname="pune"

aaa=cityname.upper()
print(aaa)

bbb=cityname.lower()
print(bbb)

kk=cityname.capitalize()
print(kk)

print("---------------------------------------------------")

language="marathi"

for item in language:
    if item=="m":
        print("letter found")
    else:
        print("letter not found")

print("m" in language)

print("---------------------------------------------------")

fruits1="apple mango grapes chiku"
if "mango" in fruits1:
    print("mango found")

if ("mango"in ["mango","grapes","apple","chiku"]):
    print("fruit found !")

print("---------------------------------------------------")
# Count of letter in word
city1="mumbai"

kj=city1.count("m")
print(kj)

print("---------------------------------------------------")
print("10000A".isnumeric())
print("AADD111".isalnum())
print("Aeeee".isalnum())

print("---------------------------------------------------")

# Count of vowels in string
vowels="aaaaaaaebbbbbbbbwwwwwwwwwrrrrrreeeedafskgdshd"

print("________________Method-1__________________")
count=0
for i in vowels:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
print(count)

print("________________Method-2__________________")
count1=0
for i in vowels:
    if i in ["a","e","i","o","u"]:
      count1=count1+1
print(count1)

print("---------------------------------------------------")
print("amol".lstrip())
print(len("amol"))
print(len("amol".rstrip()))
print("karan".strip())

print("---------------------------------------------------")

# Index of letter
flower="lotus"
print(flower.index("o"))

hh="karanJadhav"
for i in range(len(hh)):
    if hh[i]=="J":
     print(i)

print("karan".startswith("kar"))
print("jadhav".endswith("hav"))












