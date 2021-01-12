import time
import glob
import os
import shutil
from array import *
from datetime import datetime, timedelta
#C:\Bitnami\wampstack-5.4.26-0\apache2\htdocs\NWPVisual\images\charts
list_Model = ["B"]
list_Domain = ["D1"]
list_Lvl = ["SRFC","0925","0850","0700"]
list_LvlOut = ["10","92","85","70"]
list_Var = ["R______"]
list_VarOut = ["RH"]
list_fileType = [".gif"]

charts_dir = "./Charts Project/charts/"
list_dateString = []
runTime = 0
runTimeString = "00"

modelRunDateObj = datetime.utcnow()
modelRunDateObj = modelRunDateObj.replace(hour=runTime)
modelRunString = modelRunDateObj.strftime("%m")+modelRunDateObj.strftime("%d")+runTimeString+"00"
modelRunFolderString = modelRunDateObj.strftime("%Y") + modelRunDateObj.strftime("%m")+modelRunDateObj.strftime("%d")+runTimeString

for i in range(0,39,3):
	temp = modelRunString
	temp += modelRunDateObj.strftime("%m") + modelRunDateObj.strftime("%d") + modelRunDateObj.strftime("%H") + "001"
	list_dateString.append(temp)
	modelRunDateObj += timedelta(hours=3)
	print(temp)


for modelName in list_Model:
	for domainName in list_Domain:
		for lvlName in list_Lvl:
			for varName in list_Var:
				for fileType in list_fileType:
					i=0
					for dateString in list_dateString:
						fileName = charts_dir + modelName + "/" + modelRunFolderString + "Z" "/N1" + modelName + dateString + "_" + domainName + "_" + lvlName + "_" + varName + fileType
						print(fileName)
						if i < 10:
							hourString = "0" + str(i)
						else:
							hourString = str(i)
							
						if (os.path.isfile(fileName)):
							shutil.copyfile(fileName,charts_dir + "current/" + "ec" + domainName + list_LvlOut[list_Lvl.index(lvlName)] + list_VarOut[list_Var.index(varName)] + hourString + fileType)
						i += 3
				
				
