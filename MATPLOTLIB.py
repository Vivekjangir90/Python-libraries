import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random


"""
days = [1,2,3,4,5]
temp1 = [15.2,52.1,23.5,31.4,32.8]
temp2 = [8,25.2,12,6.9,20.8]

style.use("ggplot")
plt.grid(color = 'k', linestyle = "-", linewidth = 2)
plt.plot(days, temp1, color = 'g', marker = 'o',linestyle='--',linewidth = 2, markersize = 7,label = "temp line1")
plt.plot(days, temp2, color = 'b', marker = 'o',linestyle='--',linewidth = 2, markersize = 7,label = "temp line2")
# plt.plot(days, temp, "go--")
plt.axis([0,6,0,60])
plt.title('temprature',fontsize = 25)
plt.xlabel('day')
plt.ylabel('tempr')
plt.legend(["temp line"],loc = 4)
plt.show()
"""
"""
#histogram plots
std1 = np.random.randint(10,50,(100))
std2 = np.random.randint(10,40,(100))
plt.title("students age histogram")
plt.xlabel("Student age category")
plt.ylabel("Student age number")

bins = [10,20,25,28,30,32,40,50]
plt.hist([std1,std2],bins,rwidth = 0.8,histtype="bar",orientation="vertical",color=["black","b"],label = ["students1","students2"])
# plt.hist(std2,bins,rwidth = 0.8,histtype="bar",orientation="vertical",color="b",label = "students")
style.use("ggplot")
# plt.figure(figsize=(16,9))
plt.legend(loc=1)
plt.show()
"""
"""
#bar chart
classes = ["python","ML","AI","ds","cgm"]
CS1 =[30,10,20,25,10]
CS2 =[40,5,20,20,10]
CS3 =[35,5,30,10,10]
CS4 =[35,6,36,18,27]
plt.bar(classes,CS1)
plt.show()
"""

"""
plt.scatter(x,y)
plt.pie(CS1, labels =classes)

plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)

plt.savefig("chart_name")

"""










