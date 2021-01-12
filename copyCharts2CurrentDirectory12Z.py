import time
import glob
import os
import shutil
from array import *
from datetime import datetime, timedelta

list_Model = ["D"]
list_Domain = ["D0","D1"]
list_Lvl = ["SRFC","0925","0850","0700"]
list_LvlOut = ["10","92","85","70"]
list_Var = ["U___U___","R______","PVD"]
list_VarOut = ["UV","RH","RA"]
list_fileType = [".gif"]

charts_dir = "./images/charts/"
list_dateString = []
runTime = 12
runTimeString = "12"

modelRunDateObj = datetime.utcnow() - timedelta(days=1)
print (modelRunDateObj)
modelRunDateObj = modelRunDateObj.replace(hour=runTime)
modelRunString = modelRunDateObj.strftime("%m")+modelRunDateObj.strftime("%d")+runTimeString+"00"
modelRunFolderString = modelRunDateObj.strftime("%Y") + modelRunDateObj.strftime("%m")+modelRunDateObj.strftime("%d")+runTimeString

for i in range(0,99,3):
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
				
				