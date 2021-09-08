#import modules
import matplotlib.pyplot as plt 

#label data
house_size=[5,10,15,20,25,30]
house_price=[500,1000,1500,2000,2500,3000]

#slope m
sx=house_size[1] - house_size[0]
sy=house_price[1] - house_price[0]
m=sy//sx 
x=int(input("give the size of the house you want : "))

#B
b=0

#Y
y=m*x+b

#Graph
plt.plot(house_size,house_price,"o")
plt.title("house price predicat")
plt.xlabel("house size")
plt.ylabel("house price")
plt.plot(x,y,"o")
plt.show()
print("house price ",y)
