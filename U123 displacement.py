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
displacementstepx1 = regionx1.historyOutputs['U1'].data
stepx2 = myOdb.steps['SchubX']
regionx2 = stepx2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx2 = regionx2.historyOutputs['U1'].data
stepx3 = myOdb.steps['SchubY']
regionx3 = stepx3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx3 = regionx3.historyOutputs['U1'].data
stepx4 = myOdb.steps['SchubXY']
regionx4 = stepx4.historyRegions['Node FUEGETEIL-2.8']
displacementstepx4 = regionx4.historyOutputs['U1'].data
stepx5 = myOdb.steps['SchubXundNormal']
regionx5 = stepx5.historyRegions['Node FUEGETEIL-2.8']
displacementstepx5 = regionx5.historyOutputs['U1'].data
stepx6 = myOdb.steps['SchubXYundNormal']
regionx6 = stepx6.historyRegions['Node FUEGETEIL-2.8']
displacementstepx6 = regionx6.historyOutputs['U1'].data
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
displacementfinal1 = np.concatenate((((((displacementx1final,displacementx2final,displacementx3final,displacementx4final,displacementx5final,displacementx6final))))))


stepx1_2 = myOdb.steps['Normalschritt']
regionx1_2 = stepx1_2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx1_2 = regionx1_2.historyOutputs['U2'].data
stepx2_2 = myOdb.steps['SchubX']
regionx2_2 = stepx2_2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx2_2 = regionx2_2.historyOutputs['U2'].data
stepx3_2 = myOdb.steps['SchubY']
regionx3_2 = stepx3_2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx3_2 = regionx3_2.historyOutputs['U2'].data
stepx4_2 = myOdb.steps['SchubXY']
regionx4_2 = stepx4_2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx4_2 = regionx4_2.historyOutputs['U2'].data
stepx5_2 = myOdb.steps['SchubXundNormal']
regionx5_2 = stepx5_2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx5_2 = regionx5_2.historyOutputs['U2'].data
stepx6_2 = myOdb.steps['SchubXYundNormal']
regionx6_2 = stepx6_2.historyRegions['Node FUEGETEIL-2.8']
displacementstepx6_2 = regionx6_2.historyOutputs['U2'].data
displacementx1copy_2 = np.asarray(displacementstepx1_2)
displacementx1final_2 = displacementx1copy_2[:,1]
displacementx2copy_2 = np.asarray(displacementstepx2_2)
displacementx2final_2 = displacementx2copy_2[:,1]
displacementx3copy_2 = np.asarray(displacementstepx3_2)
displacementx3final_2 = displacementx3copy_2[:,1]
displacementx4copy_2 = np.asarray(displacementstepx4_2)
displacementx4final_2 = displacementx4copy_2[:,1]
displacementx5copy_2 = np.asarray(displacementstepx5_2)
displacementx5final_2 = displacementx5copy_2[:,1]
displacementx6copy_2 = np.asarray(displacementstepx6_2)
displacementx6final_2 = displacementx6copy_2[:,1]
displacementfinal2 = np.concatenate((((((displacementx1final_2,displacementx2final_2,displacementx3final_2,displacementx4final_2,displacementx5final_2,displacementx6final_2))))))

stepx1_3 = myOdb.steps['Normalschritt']
regionx1_3 = stepx1_3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx1_3 = regionx1_3.historyOutputs['U3'].data
stepx2_3 = myOdb.steps['SchubX']
regionx2_3 = stepx2_3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx2_3 = regionx2_3.historyOutputs['U3'].data
stepx3_3 = myOdb.steps['SchubY']
regionx3_3 = stepx3_3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx3_3 = regionx3_3.historyOutputs['U3'].data
stepx4_3 = myOdb.steps['SchubXY']
regionx4_3 = stepx4_3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx4_3 = regionx4_3.historyOutputs['U3'].data
stepx5_3 = myOdb.steps['SchubXundNormal']
regionx5_3 = stepx5_3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx5_3 = regionx5_3.historyOutputs['U3'].data
stepx6_3 = myOdb.steps['SchubXYundNormal']
regionx6_3 = stepx6_3.historyRegions['Node FUEGETEIL-2.8']
displacementstepx6_3 = regionx6_3.historyOutputs['U3'].data
displacementx1copy_3 = np.asarray(displacementstepx1_3)
displacementx1final_3 = displacementx1copy_3[:,1]
displacementx2copy_3 = np.asarray(displacementstepx2_3)
displacementx2final_3 = displacementx2copy_3[:,1]
displacementx3copy_3 = np.asarray(displacementstepx3_3)
displacementx3final_3 = displacementx3copy_3[:,1]
displacementx4copy_3 = np.asarray(displacementstepx4_3)
displacementx4final_3 = displacementx4copy_3[:,1]
displacementx5copy_3 = np.asarray(displacementstepx5_3)
displacementx5final_3 = displacementx5copy_3[:,1]
displacementx6copy_3 = np.asarray(displacementstepx6_3)
displacementx6final_3 = displacementx6copy_3[:,1]
displacementfinal3 = np.concatenate((((((displacementx1final_3,displacementx2final_3,displacementx3final_3,displacementx4final_3,displacementx5final_3,displacementx6final_3))))))

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

finaldata=np.column_stack([timefinal,displacementfinal1])
finaldata=np.ascontiguousarray(finaldata)

finaldata2=np.column_stack([timefinal,displacementfinal2])
finaldata2=np.ascontiguousarray(finaldata2)

finaldata3=np.column_stack([timefinal,displacementfinal3])
finaldata3=np.ascontiguousarray(finaldata3)

myViewport2 = session.Viewport(name='Displacement-Time') 
xyPlot = session.XYPlot('Displacement vs Time')
chartName = xyPlot.charts.keys()[0]
xyData1 = session.XYData('U1 displacement', finaldata)
xyData2 = session.XYData('U2 displacement', finaldata2)
xyData3 = session.XYData('U3 displacement', finaldata3)
c1 = session.Curve(xyData=xyData1)
c2 = session.Curve(xyData=xyData2)
c3 = session.Curve(xyData=xyData3)
chartName = xyPlot.charts.keys()[0]
chart = xyPlot.charts[chartName]
chart.setValues(curvesToPlot=(c1, c2, c3))
chart.axes1[0].axisData.setValues(useSystemTitle=False,title='Time') 
chart.axes2[0].axisData.setValues(useSystemTitle=False,title='Displacement') 
myViewport2.setValues(displayedObject=xyPlot)

