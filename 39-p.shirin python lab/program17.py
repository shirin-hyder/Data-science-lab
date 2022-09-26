from matplotlib import pyplot
import pandas
df = pandas.read_csv("iris.csv")
fig,ax = pyplot.subplots(1,1)
df["sepal.length"].plot(kind="hist", edgecolor="black",bins=49)
ax.set_title("Histogram")
ax.set_xticks([4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0])
ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
ax.set_xlabel("sepal Length")
pyplot.show()
