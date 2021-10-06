from abaqus import * 
from abaqusConstants import * 
import numpy as np
import visualization
import xyPlot
myViewport = session.Viewport(name='displacement') 
odbPath = 'displacement.odb'
myOdb = visualization.openOdb(path='displacement.odb')
myViewport.setValues(displayedObject=myOdb)

stressstepx1 = myOdb.steps['Normalschritt']
stressregionx1 = stressstepx1.historyRegions['Element KLEBSCHICHT-1.1 Int Point 1']
stressx1 = stressregionx1.historyOutputs['S23'].data
stressstepx2 = myOdb.steps['SchubX']
stressregionx2 = stressstepx2.historyRegions['Element KLEBSCHICHT-1.1 Int Point 1']
stressx2 = stressregionx2.historyOutputs['S23'].data
stressstepx3 = myOdb.steps['SchubY']
stressregionx3 = stressstepx3.historyRegions['Element KLEBSCHICHT-1.1 Int Point 1']
stressx3 = stressregionx3.historyOutputs['S23'].data
stressstepx4 = myOdb.steps['SchubXY']
stressregionx4 = stressstepx4.historyRegions['Element KLEBSCHICHT-1.1 Int Point 1']
stressx4 = stressregionx4.historyOutputs['S23'].data
stressstepx5 = myOdb.steps['SchubXundNormal']
stressregionx5 = stressstepx5.historyRegions['Element KLEBSCHICHT-1.1 Int Point 1']
stressx5 = stressregionx5.historyOutputs['S23'].data
stressstepx6 = myOdb.steps['SchubXYundNormal']
stressregionx6 = stressstepx6.historyRegions['Element KLEBSCHICHT-1.1 Int Point 1']
stressx6 = stressregionx6.historyOutputs['S23'].data
stressfinal = np.concatenate((((((stressx1,stressx2,stressx3,stressx4,stressx5,stressx6))))))

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

finaldata1=np.column_stack([timefinal,displacementfinal])
finaldata1=np.ascontiguousarray(finaldata1)

stressfinal=stressfinal[:,1]
finaldata2=np.column_stack([timefinal,stressfinal])
finaldata2=np.ascontiguousarray(finaldata2)

finaldata3=np.column_stack([displacementfinal,stressfinal])
finaldata3=np.ascontiguousarray(finaldata3)


list=['Steptime','Displacement','Stress']
listfinal=np.asarray(list)
np.savetxt("SDU2.txt", np.column_stack((listfinal)), delimiter="|", newline='\n\n', fmt='%s')
with open('SDU2.txt','ab') as f:
	np.savetxt(f, np.column_stack(([timefinal,displacementfinal,stressfinal])), delimiter="|", newline='\n', fmt='%0.3f|%0.3f|%0.3f')