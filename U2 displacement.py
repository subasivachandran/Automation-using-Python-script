from abaqus import * 
from abaqusConstants import * 
import numpy as np
import visualization
myViewport = session.Viewport(name='displacement') 
odbPath = 'displacement.odb'
myOdb = visualization.openOdb(path='displacement.odb')
myViewport.setValues(displayedObject=myOdb)
stepx1 = myOdb.steps['Normalschritt']
regionx1 = stepx1.historyRegions['Node FUEGETEIL-2.8']
displacementstepx1 = regionx1.historyOutputs['U2'].data
stepx2 = myOdb.steps['SchubX']
regionx2 = stepx2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx2 = regionx2.historyOutputs['U2'].data
stepx3 = myOdb.steps['SchubY']
regionx3 = stepx3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx3 = regionx3.historyOutputs['U2'].data
stepx4 = myOdb.steps['SchubXY']
regionx4 = stepx4.historyRegions['Node FUEGETEIL-2.8']
displacementstepx4 = regionx4.historyOutputs['U2'].data
stepx5 = myOdb.steps['SchubXundNormal']
regionx5 = stepx5.historyRegions['Node FUEGETEIL-2.8']
displacementstepx5 = regionx5.historyOutputs['U2'].data
stepx6 = myOdb.steps['SchubXYundNormal']
regionx6 = stepx6.historyRegions['Node FUEGETEIL-2.8']
displacementstepx6 = regionx6.historyOutputs['U2'].data
displacementx1copy = np.asarray(displacementstepx1)
displacementx1final = displacementx1copy[:,1]
displacementx2copy = np.asarray(displacementstepx2)
displacementx2final = displacementx2copy[:,1]
displacementx3copy = np.asarray(displacementstepx3)
displacementx3final = displacementx3copy[:,1]
displacementx4copy = np.asarray(displacementstepx4)
displacementx4final = displacementx4copy[:,1]
displacementx5copy = np.asarray(displacementstepx5)
displacementx5final = displacementx5copy[:,1]
displacementx6copy = np.asarray(displacementstepx6)
displacementx6final = displacementx6copy[:,1]
displacementfinal = np.concatenate((((((displacementx1final,displacementx2final,displacementx3final,displacementx4final,displacementx5final,displacementx6final))))))

framex1=[]
allFrames = myOdb.steps['Normalschritt'].frames
for j in range(len(allFrames)):
	framestepx1=myOdb.steps['Normalschritt'].frames[j].frameValue
	framex1.append(framestepx1)

framex2=[]
allFrames = myOdb.steps['SchubX'].frames
for j in range(len(allFrames)):
	framestepx2=(myOdb.steps['SchubX'].frames[j].frameValue)
	framestepx2=framestepx2+1
	framex2.append(framestepx2)

framex3=[]
allFrames = myOdb.steps['SchubY'].frames
for j in range(len(allFrames)):
	framestepx3=(myOdb.steps['SchubY'].frames[j].frameValue)
	framestepx3=framestepx3+2
	framex3.append(framestepx3)

framex4=[]
allFrames = myOdb.steps['SchubXY'].frames
for j in range(len(allFrames)):
	framestepx4=(myOdb.steps['SchubXY'].frames[j].frameValue)
	framestepx4=framestepx4+3
	framex4.append(framestepx4)

framex5=[]
allFrames = myOdb.steps['SchubXundNormal'].frames
for j in range(len(allFrames)):
	framestepx5=(myOdb.steps['SchubXundNormal'].frames[j].frameValue)
	framestepx5=framestepx5+4
	framex5.append(framestepx5)

framex6=[]
allFrames = myOdb.steps['SchubXYundNormal'].frames
for j in range(len(allFrames)):
	framestepx6=(myOdb.steps['SchubXYundNormal'].frames[j].frameValue)
	framestepx6=framestepx6+5
	framex6.append(framestepx6)

timefinal = np.concatenate([framex1,framex2,framex3,framex4,framex5,framex6])

finaldata=np.column_stack([timefinal,displacementfinal])
finaldata=np.ascontiguousarray(finaldata)

myViewport2 = session.Viewport(name='Displacement-Time') 
xyPlot = session.XYPlot('Displacement vs Time')
chartName = xyPlot.charts.keys()[0]
xyData = session.XYData('U2 displacement', finaldata)
c = session.Curve(xyData=xyData)
chart = xyPlot.charts[chartName]
chart.setValues(curvesToPlot=(c))
chart.axes1[0].axisData.setValues(useSystemTitle=False,title='Time') 
chart.axes2[0].axisData.setValues(useSystemTitle=False,title='Displacement')
myViewport2.setValues(displayedObject=xyPlot)