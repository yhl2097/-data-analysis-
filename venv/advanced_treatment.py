import numpy as np
import pandas as pd
import re

randframe = pd.DataFrame(np.random.randn(1000,3))
a = randframe.describe()
b = randframe.std()
c = randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]
nframe = pd.DataFrame(np.arange(25).reshape(5,5))
new_order = np.random.permutation(5)
new_order1 = [3,4,2]
d = nframe.take(new_order1)
sample = np.random.randint(0,len(nframe),size=3)
text = '16 Bolton Avenue ,Boston'
address,city = [s.strip() for s in text.split(',')]
tokens = address + ',' + city
strings = ['A+','A','A-','B','BB','BBB','C+']
e = ';'.join(strings)
text1 = 'This is     an\t odd \n text!'
f = re.split('\s+',text1)
regex = re.compile('\s+')
g = regex.split(text1)
text2 = 'This is my address: 16 Bolton Avenue, Boston'
h = re.findall('[A,a]\w+',text2)
frame = pd.DataFrame({'color':['white','red','green','red','green'],
                      'object':['pen','pencil','pencil','ashtray','pen'],
                      'price1':[5.56,4.20,1.30,0.56,2.75],
                      'price2':[4.75,4.12,1.60,0.75,3.15]})
result = frame['price1'].groupby(frame['color']).mean()
result1 = frame.groupby(frame['color'])['price1'].mean()
result2 = (frame.groupby(frame['color']).mean())['price1']
ggroup = frame['price1'].groupby([frame['color'],frame['object']])
g = frame[['price1','price2']].groupby(frame['color']).mean()
for name,group in frame.groupby('color'):
    print(name)
    print(group)
means = frame.groupby('color').mean().add_prefix('mean_')
group = frame.groupby('color')
i = group['price1'].quantile(0.6)
def range(series):
    return series.max() - series.min()
j = group['price1'].agg(range)
k = group['price1'].agg(['mean','std',range])
frame1 = pd.DataFrame({'color':['white','red','green','red','green'],
                      'price1':[5.56,4.20,1.30,0.56,2.75],
                      'price2':[4.75,4.12,1.60,0.75,3.15]})
sums = frame.groupby('color').sum().add_prefix('tot_')
m = pd.merge(frame,sums,left_on='color',right_index=True)
n = frame1.groupby('color').transform(np.sum).add_prefix('tot_')
frame2 = pd.DataFrame({'color':['white','black','white','white','black','black'],
                       'status':['up','up','down','down','down','up'],
                       'value1':[12.33,14.55,22.34,27.84,23.40,18.33],
                       'value2':[11.23,31.80,29.99,31.18,18.25,22.44]})
p = frame2.groupby(['color','status']).apply(lambda x: x.max())
q = frame2.groupby(['color','status']).sum()
temp = pd.date_range('1/1/2015',periods=10,freq='H')
timeseries = pd.Series(np.random.rand(10),index=temp)
timetable = pd.DataFrame({'date':temp,'value1':np.random.rand(10),
                          'value2':np.random.rand(10)})
timetable['cat'] = ['up','down','left','left','up','up','down','right',
                        'right','up']
print(timetable)