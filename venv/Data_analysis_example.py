import numpy as np
import pandas as pd
import datetime

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser

from sklearn.svm import SVR
from scipy.optimize import fsolve

# 加载数据集
df_ferrara = pd.read_csv('WeatherData/ferrara_270615.csv')
df_milano = pd.read_csv('WeatherData/milano_270615.csv')
df_mantova = pd.read_csv('WeatherData/mantova_270615.csv')
df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
df_torino = pd.read_csv('WeatherData/torino_270615.csv')
df_asti = pd.read_csv('WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('WeatherData/bologna_270615.csv')
df_piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
df_cesena = pd.read_csv('WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('WeatherData/faenza_270615.csv')
print(df_ravenna)


#温度数据分析
#取出要分析的温度和日期数据
y1 = df_ravenna['temp']
x1 = df_ravenna['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']

#把日期数据转化成datetime的格式
day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
day_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

#调用subplot函数，fig是图像对象，ax是坐标轴对象
fig,ax = plt.subplots()

#调整x轴坐标刻度，使其旋转70度，方便查看
plt.xticks(rotation=70)

#设定时间格式为24:00
hours = mdates.DateFormatter('%H:%M')

#设定x轴显示的格式为以上设置的格式
ax.xaxis.set_major_formatter(hours)

#作折线图
ax.plot(day_ravenna,y1,'r',day_faenza,y2,'r',day_cesena,y3,'r')
ax.plot(day_milano,y4,'g',day_asti,y5,'g',day_torino,y6,'g')


#10个城市的最高温和最低温，显示最值点离海远近的关系
#dist：城市距海边距离列表
dist = [df_ravenna['dist'][0],
        df_cesena['dist'][0],
        df_faenza['dist'][0],
        df_ferrara['dist'][0],
        df_bologna['dist'][0],
        df_mantova['dist'][0],
        df_piacenza['dist'][0],
        df_milano['dist'][0],
        df_asti['dist'][0],
        df_torino['dist'][0]
        ]

#temp_max:每个城市最高温度列表
temp_max = [df_ravenna['temp'].max(),
            df_cesena['temp'].max(),
            df_faenza['temp'].max(),
            df_ferrara['temp'].max(),
            df_bologna['temp'].max(),
            df_mantova['temp'].max(),
            df_piacenza['temp'].max(),
            df_milano['temp'].max(),
            df_asti['temp'].max(),
            df_torino['temp'].max()
            ]

#temp_min:每个城市最低温度列表
temp_min = [df_ravenna['temp'].min(),
            df_cesena['temp'].min(),
            df_faenza['temp'].min(),
            df_ferrara['temp'].min(),
            df_bologna['temp'].min(),
            df_mantova['temp'].min(),
            df_piacenza['temp'].min(),
            df_milano['temp'].min(),
            df_asti['temp'].min(),
            df_torino['temp'].min()
            ]

#画出最高温
fig,ax = plt.subplots()
ax.plot(dist,temp_max,'r--o')

#dist1、dist2分别为靠近与远离海的城市集合
dist1 = dist[0:5]
dist2 = dist[5:10]
print(dist1)

#改变列表的结构，从一维（1，N）变为二维（N，1）
dist1 = [[x] for x in dist1]
dist2 = [[x] for x in dist2]

#temp_max1 是dist1中城市的对应最高温度,同理亦然
temp_max1 = temp_max[0:5]
temp_max2 = temp_max[5:10]

#调用SVR函数，使用线性拟合
svr_lin1 = SVR(kernel='linear',C=1e3)
svr_lin2 = SVR(kernel='linear',C=1e3)

#加入数据，进行拟合
svr_lin1.fit(dist1,temp_max1)
svr_lin2.fit(dist2,temp_max2)

#reshape改变列表的结构
xp1 = np.arange(10,100,10).reshape((9,1))
xp2 = np.arange(50,400,50).reshape((7,1))
yp1 = svr_lin1.predict(xp1)
yp2 = svr_lin2.predict(xp2)
print(xp1)

#绘图，限制x轴取值范围
ax.set_xlim(0,400)
ax.plot(xp1,yp1,c='b',label='Strong sea effect')
ax.plot(xp2,yp2,c='g',label='Light sea effect')

#影响转变点即斜率、截距
print(svr_lin1.coef_)
print(svr_lin1.intercept_)
print(svr_lin2.coef_)
print(svr_lin2.intercept_)


#定义第一条拟合曲线
def line1(x):
    a1 = svr_lin1.coef_[0][0]
    b1 = svr_lin1.intercept_[0]
    return a1*x + b1

#定义第二条拟合曲线
def line2(x):
    a2 = svr_lin2.coef_[0][0]
    b2 = svr_lin2.intercept_[0]
    return a2 * x + b2

#定义找到两条直线交点的x的坐标函数
def findIntersection(fun1,fun2,x0):
    return fsolve(lambda x : fun1(x) - fun2(x),x0)

result = findIntersection(line1,line2,0.0)
print('[x,y] = [ %d,%d ]' % (result,line1(result)))

fig,ax = plt.subplots()
x = np.linspace(0,300,31)
ax.plot(x,line1(x),x,line2(x),result,line1(result),'ro')

#最低气温
fig,ax = plt.subplots()
plt.axis((0,400,15,25))
plt.plot(dist,temp_min,'bo')


#风向频率玫瑰图
#绘制极区图
def showRoseWind(values,city_name,max_value):
    N = 8
    # theta = [pi*1/4,pi*2/4,pi*3/4,...,pi*2]
    theta = np.arange(0.,2 * np.pi,2 * np.pi / N )
    radii = np.array(values)
    fig,ax = plt.subplots()

    #绘制极区图的坐标系
    plt.axes([0.025,0.025,0.95,0.95],polar = True)

    #定义每个扇区的RGB值，x越大，颜色越深
    colors = [(1-x/max_value,1-x/max_value,0.75) for x in radii]

    #画出每个扇区
    plt.bar(theta,radii,width=(2*np.pi/N),bottom=0.0,color=colors)

    #设置极区图的标题
    plt.title(city_name,x = 0.2,fontsize=20)

#以ravenna为例，将所有数据分到这几个面元中
hist,bins = np.histogram(df_ravenna['wind_deg'],8,[0,360])
print(hist)
showRoseWind(hist,'Ravenna',max(hist))

#计算风速均值的分布情况
def RoseWind_Speed(df_city):
    degs = np.arange(45,361,45)
    tmp = []
    for deg in degs:
        #获取wind_deg 在指定范围的平均风速
        #风向大于deg-46与风向小于deg的数据
        tmp.append(df_city[(df_city['wind_deg'] > (deg-46)) & (df_city['wind_deg'] < deg)]
                   ['wind_speed'].mean())
        return np.array(tmp)

showRoseWind(RoseWind_Speed(df_ravenna),'Ravenna',max(hist))
plt.savefig('fig.png',bbox_inches='tight')
plt.show()