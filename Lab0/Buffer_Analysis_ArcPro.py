import arcpy

arcpy.analysis.Buffer("East_Bank", "East_Bank_Buffer_notebook", '30 Meters', 'FULL', 'ROUND', 'NONE','#','PLANAR')

help(arcpy.analysis.Buffer)


