
mxd = arcpy.mapping.MapDocument("CURRENT")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  arcpy.mapping.ExportToPNG(mxd, "Y:/GitHub/pratt-savi-810-2017-10/img/" + str(pageNum) + ".png")
del mxd


mxd = arcpy.mapping.MapDocument("Y:/GitHub/pratt-savi-810-2017-10/data/nybb_map.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  arcpy.mapping.ExportToPNG(mxd, "Y:/GitHub/pratt-savi-810-2017-10/img/" + str(pageNum) + "_arccatalog_ran.png")
del mxd
