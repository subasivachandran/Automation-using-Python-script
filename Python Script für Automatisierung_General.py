%%General python script for calculating the stress and strain data for a specimen and plotting it and exporting the data into a (.txt) file

from abaqus import * 
from abaqusConstants import * 
import numpy as np
import visualization 
myViewport = session.Viewport(name='Tensile test') 
odbPath = 'Tensiletest.odb'
myOdb = visualization.openOdb(path=odbPath)
myViewport.setValues(displayedObject=myOdb)
step1 = myOdb.steps['Step-1']
region1 = step1.historyRegions['Node ASSEMBLY.2']
stressdata = region1.historyOutputs['RF3'].data
region2 = step1.historyRegions['Node ZUGVERSUCHS-1.10']
displacement1 = region2.historyOutputs['U3'].data
region3 = step1.historyRegions['Node ZUGVERSUCHS-1.14']
displacement2 = region3.historyOutputs['U3'].data
incrementdata=region1.historyOutputs['RF3'].data
increment=np.asarray(incrementdata)
increment[:,0]
stress = np.asarray(stressdata)
stress = stress/40
stress[:,1]
displacement1_temp = np.asarray(displacement1)
displacement2_temp = np.asarray(displacement2)
strain = (displacement2_temp - displacement1_temp)/80
strain[:,1]
myViewport2 = session.Viewport(name='Stress-Strain') 
xyPlot = session.XYPlot('Stress vs Strain')
xyData1 = session.XYData('Strain', strain)
xyData2 = session.XYData('Stress', stress)
c1 = session.Curve(xyData=xyData1)
c2 = session.Curve(xyData=xyData2)
chartName = xyPlot.charts.keys()[0]
chart = xyPlot.charts[chartName]
chart.setValues(curvesToPlot=(c1, c2))
myViewport2.setValues(displayedObject=xyPlot)
xyPlot = session.XYPlot('Stress vs Strain')
xyData1 = session.XYData('Strain', strain)
xyData2 = session.XYData('Stress', stress)
c1 = session.Curve(xyData=xyData1)
c2 = session.Curve(xyData=xyData2)
chartName = xyPlot.charts.keys()[0]
chart = xyPlot.charts[chartName]
chart.setValues(curvesToPlot=(c1, c2))
chart.axes1[0].axisData.setValues(useSystemTitle=False,title='Displacement') 
chart.axes2[0].axisData.setValues(useSystemTitle=False,title='Force') 
myViewport2.setValues(displayedObject=xyPlot)
list=['Increment','Strain','Stress']
listfinal=np.asarray(list)
np.savetxt("Filename", np.column_stack((listfinal)), delimiter="|", newline='\n\n', fmt='%s')
with open('Filename','ab') as f:
	np.savetxt(f, np.column_stack(([increment[:,0],strain[:,1],stress[:,1]])), delimiter="|", newline='\n', fmt='%s')

%%%For upgrading the Job which has been created in previous release of Abaqus
>>> import visualization 
>>> session.upgradeOdb(existingOdbPath='Job-3.odb', upgradedOdbPath='Zugversuch.odb')



