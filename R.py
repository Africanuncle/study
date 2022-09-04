# from unittest import result
from textwrap import indent
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np
from sklearn.utils import column_or_1d
from sympy import get_indices


# def get_indices(lst, el):
# 	return np.argwhere(np.array(lst) == el).flatten().tolist() 
def get_indices(lst, el):
    return [ index for index, item in enumerate(lst) if item == el] 
# 绘图参数设置
matplotlib.rcParams.update({
                            # Use the Computer modern font
                            'mathtext.fontset': 'cm',
                            })
plt.rcParams["font.family"] = "FangSong"  # 支持中文显示
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['axes.titlesize'] = 8  # 标题字体大小
plt.rcParams['axes.labelsize'] = 20  # 坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 20  # x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 20  # y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 6

# 图例字符大小
legend_font = {
    'family': 'Times New Roman',  # 字体
    'style': 'normal',
    'size': 15,  # 字号
    'weight': "normal",  # 是否加粗，不加粗
    }

index_HRS = []
index_LRS = []
index_R = []

filepath = 'D:\\数据处理\\i-v\\7-7\\\\NO2\\3-2\\处理 10 2.csv'
data1 = pd.read_csv(filepath,header=None)
data = np.array(data1)
data=np.flip(data,axis=0)
y = data[:,1]
# cc=28
cc = int(len(y)/404)
# cc = 100
check = 0.21
print('cc_len = '+str(cc))
# cc_range = [1:5]  # range(11)
cc_range =range(cc)
x = data[:,0]
z = data[:,2]

fig = plt.figure(figsize=(17, 7))  # 创建图
plt.subplot(1,2,1)

plt.xlabel("电压V(v)   "+str(cc_range[0])+"到"+str(cc_range[-1])+"圈")  # X轴标签
vline_indx = [cc_range[0],cc_range[-1]]
plt.ylabel("电流I(A)")  # Y轴标签
# ax.set
# plt.plot(x,y)

for i in cc_range:
    plt.semilogy(x[i*404:(i+1)*404], y[i*404:(i+1)*404],label=i+1)
# plt.legend(loc='lower right',frameon = False,prop=legend_font) # ,ncol = 2

# print(y[0*404:(0+1)*202])
# plt.show()

# fig1 = plt.figure(figsize=(10, 7))  # 创建图  
plt.subplot(1,2,2)
R_index = get_indices(x,check)
for i in R_index:
    index_R.append(z[i])
index_HRS=index_R[1::2]
index_LRS=index_R[::2]
plt.xlabel("圈数circle(c)")  # X轴标签
plt.ylabel("电阻R(ohm)")  # Y轴标签
resultx = [x for x in range(len(index_HRS))]
resulty = [x for x in range(len(index_LRS))]
# print(str(len(result))+'   '+str(len(index_HRS)))
plt.semilogy(resultx,index_HRS,resulty,index_LRS)
plt.vlines(vline_indx, min(index_LRS), max(index_HRS), colors='r', linestyles='dashed', label='垂直线')
plt.tight_layout()
plt.show()
plt.savefig('figure\处理 10 2.png', format='png')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中

# fig2 = plt.figure(figsize=(10, 5))  # 创建图
# plt.rcParams["font.family"] = "FangSong"  # 支持中文显示
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.xlabel("电压V(v)")  # X轴标签
# plt.ylabel("电阻R(ohm)")  # Y轴标签
# plt.plot(x,z)
# plt.show()



