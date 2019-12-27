import pandas as pd
import numpy as np

ser = pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
serd = pd.Series([1,5,6,3],index=[0,3,5,6])
sers = serd.reindex(range(6),method='ffill')
data = {'color':['blue','green','yellow','red','white'],
        'object':['ball','pen','pencil','paper','mug'],
        'price':[1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)
frames = frame.reindex(range(5),method='ffill',columns=['new','color','price',
                                                        'object'])
ser1 = pd.Series(np.arange(4.),index=['red','blue','yellow','white'])
frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                      index=['blue','green','white','yellow'],
                      columns=['mug','pen','ball'])
s1 = pd.Series([3,2,5,1],['yellow','white','green','blue'])
s2 = pd.Series([1,4,7,2,1],['white','yellow','blue','black','brown'])
ser1 = pd.Series(np.arange(4),index=['pen','ball','pencil','paper'])
def f(x):
        return pd.Series([x.min(),x.max()],index=['min','max'])

b = frame1.sort_index(axis=1)
c = frame1.mean()
seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008','2009','2010',
                                   '2011','2012','2013'])
seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010',
                                    '2011','2012','2013'])
a = seq2.cov(seq)
frame3 = pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
serred = pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
e = frame3.corrwith(serred)
mser = pd.Series(np.random.rand(8),
                 index=[['white','white','white','blue','blue','red','red','red'],
                        ['up','down','right','up','down','up','down','left']])
mframe = pd.DataFrame(np.random.randn(16).reshape(4,4),
                      index=[['white','white','red','red'],['up','down','up','down']],
                      columns=[['pen','pen','paper','paper'],[1,2,1,2]])
mframe.columns.names = ['objects','id']
mframe.index.names = ['colors','status']
print(mframe.swaplevel('colors','status'))
print(mframe.sum(level='colors'))






