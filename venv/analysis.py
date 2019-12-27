import numpy as np
import pandas as pd

frame = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                      'color':['white','red','red','black','green'],
                      'brand':['OMG','ABC','ABC','POD','POD']})
frame1 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'brand':['OMG','POD','ABC','POD']})
a = pd.merge(frame,frame1,on='id')
frame1.columns = ['id1','brand1']
b = frame.join(frame1)
array = np.array([[0,1,2],[3,4,5],[6,7,8]])
array1 = np.arange(9).reshape((3,3))+6
c = np.concatenate([array,array1],axis=0)
d = np.concatenate([array,array1],axis=1)
ser = pd.Series(np.random.rand(4),index=[1,2,3,4])
ser1 = pd.Series(np.random.rand(4),index=[5,6,7,8])
e = pd.concat([ser,ser1],axis=1,keys=[1,2])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3,3),index=[1,2,3],
                      columns=['A','B','C'])
frame3 = pd.DataFrame(np.random.rand(9).reshape(3,3),index=[4,5,6],
                      columns=['A','B','C'])
f = pd.concat([frame2,frame3],axis=1)
ser2 = pd.Series(np.random.rand(5),index=[1,2,3,4,5])
ser3 = pd.Series(np.random.rand(4),index=[2,4,5,6])
g = ser2.combine_first(ser2)
frame4 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white','black','red'],
                      columns=['ball','pen','pencil'])
ser4 = frame4.stack()
longframe = pd.DataFrame({'color':['white','white','white','red','red','red',
                                   'black','black','black'],
                          'item':['ball','pen','mug','ball','pen','mug',
                                  'ball','pen','mug'],
                          'value':np.random.rand(9)})
wideframe = longframe.pivot('color','item')
dframe = pd.DataFrame({'color':['white','white','red','red','white'],
                       'value':[2,1,3,3,2]})
h = dframe.drop_duplicates()
frame5 = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                       'color':['white','rosso','verde','black','yellow'],
                       'price':[5.56,4.20,1.30,0.56,2.75]})
newcolors = {'rosso':'red','verde':'green'}
i = frame5.replace(newcolors)
ser5 = pd.Series([1,3,np.nan,4,6,np.nan,3])
j = ser5.replace(np.nan,0)
frame6 = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                       'color':['white','rosso','verde','black','yellow']})
price = {'ball':5.56,'mug':4.20,'bottle':1.30,'scissors':3.41,'pen':1.30,
         'pencil':0.56,'ashtray':2.75}
frame6['price'] = frame6['item'].map(price)
reindex = {0:'first',1:'second',2:'third',3:'fourth',4:'fifth'}
recolumn = {'item':'object','price':'value'}
frame6.rename(columns={'item':'object'},inplace=True)
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
cat = pd.cut(ages,bins,right=False)
print(pd.value_counts(pd.cut(ages,4)))
print(pd.value_counts(pd.qcut(ages,4)))
