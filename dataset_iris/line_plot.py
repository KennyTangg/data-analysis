import matplotlib.pyplot as plt

# Data for line plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Line Plot Customization
plt.plot(x,y,label="Prime Numbers",color="#ff6347",linestyle="--",linewidth=2,marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title('Line Plot of Prime Numbers')

# Add an annotation for the maximum y-value
max_y = max(y)
plt.annotate(max_y,xy=(5,max_y),xytext=(4,10),arrowprops={"facecolor":'black', 'shrink': 0.02})

# Add grid lines to all plots.
plt.grid(True)
# Include a legend for each plot type.
plt.legend()
# Save the generated plot as a PNG file
plt.savefig('plot.png')
plt.show()
