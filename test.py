import time
import glob
import os
import shutil
from array import *
from datetime import datetime, timedelta
#C:\Bitnami\wampstack-5.4.26-0\apache2\htdocs\NWPVisual\images\charts
list_Model = ["B"]
list_Domain = ["D0"]
list_Lvl = ["SRFC","0925","0850","0700"]
list_LvlOut = ["10","92","85","70"]
list_Var = ["RAIN"]
list_VarOut = ["RAIN"]
list_fileType = [".gif"]

charts_dir = "D:/Test/images/charts/"
dst = "D:/Test/images/charts/current/"
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


                    
