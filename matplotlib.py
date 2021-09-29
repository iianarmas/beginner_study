import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = [0,0.5,1,2,2.4,4]
y = [0,4.2,2,2.3,6,8]

x2 = np.arange(0,4.5,0.5)

fontdict = {'fontname':'Roboto', 'fontsize':20}
fontlabel = {'fontname':'Roboto', 'fontsize':14}
xticks = [0,1,2,3,4]
yticks = [0,2,4,6,8]


###### line chart

# resize
#plt.figure(figsize=(4,2), dpi=150)

plt.plot(x,y, label='label 1', linewidth=1, markersize=12, color='red', linestyle='dashed', marker='.')    # color accepts hexadecimal colors

plt.plot(x2, x2**2, label='2nd')


plt.title('First Graph', fontdict=fontdict)

plt.ylabel('Sample Y Label', fontdict=fontlabel)
plt.xlabel('Sample X Label', fontdict=fontlabel)

plt.xticks(xticks)
#plt.yticks(yticks)

plt.legend()    # legend takes the label in plt.plot as parameter


#plt.savefig('firstgraph.png', dpi=300)

plt.show()


###### bar chart

labels = ['A', 'B', 'C']
values = [1,4,2]
values2 = [2.1,1.5,2.6]



bars = plt.bar(labels, values, width=-0.3, align='edge')
plt.bar(labels, values2, color='#2a6989', width=0.3, align='edge', animated=True)

"""pat = ['/', 'o', '*']
for bar in bars:
    bar.set_hatch(pat.pop(0))"""


plt.show()
