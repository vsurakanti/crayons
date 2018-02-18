# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
data = pd.read_csv('2010_Census_Populations_by_Zip_Code.csv')
xVec = 'Zip_Code'
yVec = 'Total_Population' 
zVec = 'Test_color'
class plot() : 
  def __init__(self, data = [], rows =1 , cols = 1) :
    self.data = data
    self.xlim = 10
    self.ylim = 10
    self.title = ''
    self.color = mpl.cm.Dark2.colors
#    self.color = ['g', 'r', 'b'] *10
    self.enMinMax = False
    self.figure_size = (12,6)
    self.fig,self.axes = plt.subplots(rows, cols, figsize = self.figure_size, tight_layout=True)
    self.minorgrid = dict(b = True , color='r', linestyle=':', linewidth=0.7, which = 'minor')
    self.majorgrid = dict(b= True, color='b', linestyle='-', linewidth=1, which = 'major')
  def scatter(self, xVec = None , yVec = None , axes = None, hueVec = None, hueColor = [],  **kwargs):

    if hueVec == []:
      xArray =  self.data[xVec].dropna().tolist()
      yArray =  self.data[yVec].dropna().tolist()
      axes.scatter(xArray, yArray, **kwargs)
    else:
      hueArray = self.data[hueVec].dropna().unique()
      if hueColor == []:
         hueColor = self.color[:len(hueArray)+1]
         print hueColor
#      data =  self.data[]
      idx = 0
      for key, filtergroup in self.data.groupby([hueVec]):
        xArray =  filtergroup[xVec].dropna().tolist()
        yArray =  filtergroup[yVec].dropna().tolist()
        if filtergroup[xVec].dropna().dtype == 'object':
          axes.scatter(xArray, yArray, **kwargs) 
        if filtergroup[xVec].dropna().dtype == 'int64':
           axes.scatter(xArray, yArray, color = hueColor[idx], **kwargs)
        idx = idx +1
    self.set_axis_grid(axes)
#    axes.show()
  def hist (self, xVec =None, axes= None , hueVec = None, hueColor = [], **kwargs):  
    if hueVec == []:
      xArray = self.data[xVec].dropna()
      axes.hist(xArray, **kwargs)
      
    else:
      hueArray = self.data[hueVec].dropna().unique()
      if hueColor == []:
         hueColor = self.color[:len(hueArray)]
         print hueColor
         xArray = []
         for key, filtergroup in self.data.groupby([hueVec]):
           xArray.append(filtergroup[xVec].dropna().tolist())
         print len(xArray)
         if filtergroup[xVec].dropna().dtype == 'int64':
              axes.hist(xArray, color = hueColor, **kwargs)
    self.set_axis_grid(axes)
              
  def hist2d (self, xVec =None, yVec = None , axes= None , hueVec = None, hueColor = [], **kwargs):  
    if hueVec == []:
      xArray = self.data[xVec].dropna()
      yArray = self.data[yVec].dropna()
      axes.hist2d(xArray, yArray, **kwargs)
    else:
      hueArray = self.data[hueVec].dropna().unique()
      if hueColor == []:
         hueColor = self.color[:len(hueArray)]
         xArray = []
         yArray = []
         for key, filtergroup in self.data.groupby([hueVec]):
           xArray.append(filtergroup[xVec].dropna().tolist())
           yArray.append(filtergroup[yVec].dropna().tolist())
         print len(yArray)
         if filtergroup[xVec].dropna().dtype == 'int64':
              axes.hist2d(xArray, yArray, **kwargs)  
              
  def set_limits(self,axes, minmax=[None,None], **kwargs) :
      if minmax[0] != None : 
        axes.set_xlim(left = minmax[0][0], right = minmax[0][1])
      if minmax[1] != None : 
        axes.set_ylim(bottom = minmax[1][0], top = minmax[1][1])
  
  def set_axis_grid(self, axes):
      axes.set_axisbelow(True)
      axes.minorticks_on()
      axes.grid(**self.majorgrid)
      axes.grid(**self.minorgrid)
      
      
      
  def filterData (self, filVec = []):
      filterdata = []
      for Vec in filVec :
        zdata = self.data[self.data[Vec].dropNA().unquie()]
        for condn in filVec:
            resVec =  condn.strip('>=')[0].replace(' ','')  
            resValue = condn.strip('>=')[1].replace(' ','')      
            if '>=' in filter and condn.strip('>=')[1] == type(int):
               resValue = condn.strip('>=')[1]  
               data = zdata[zdata[resVec]>=resValue]
            if '=<' in filter and condn.strip('<=')[1] == type(int) :
                resValue = condn.strip('>=')[1]  
                data = zdata[zdata[resVec]<=resValue]
            if '==' in filter and condn.strip('==')[1] == type(int):
                   resArray = list(map(int, resValue.split(',')))
                   data = self.zdata[self.zdata[resVec].isin(resArray)] 
            if '==' in filter and condn.strip('==')[1] == type(str) :
                  resArray = list(map(int, resValue.split(',')))
                  data = zdata[zdata[resVec].isin(resArray)]
            if '!=' in filter and condn.strip('==')[1] == type(str) :
                  resArray = list(map(int, resValue.split(',')))
                  data = zdata[zdata[resVec].isin(resArray)]
      filterdata.merge(data)
      self.data = filterdata
  
    
    
xyplot = plot(data,1,3)
keyword = dict(s = 20)
xyplot.set_limits(xyplot.axes[0],minmax = [[90000,94000],[10000,100000]])
xyplot.scatter(xVec,yVec, xyplot.axes[0], hueVec = zVec , hueColor = [], **keyword)
xyplot.set_limits(xyplot.axes[1],minmax = [[90000,94000], [0,30]])
xyplot.set_limits(xyplot.axes[2],minmax = [[10000,94000], [0,30]])
keyword = dict(bins = 10)
xyplot.hist (xVec, xyplot.axes[1] , hueVec = zVec , hueColor = [], **keyword)
keyword = dict(bins =10)
xyplot.hist(yVec, xyplot.axes[2] , hueVec = zVec , hueColor = [], **keyword)   