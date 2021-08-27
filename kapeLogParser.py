import os
import pandas as pd

def makeFilePath() :
    path =".\\kape\\C"
    appCache = pd.DataFrame(columns=['path'])
    installLog = pd.DataFrame(columns=['path'])
    infLog = pd.DataFrame(columns=['path'])
    for path, dir, files in os.walk(path) :
        if len(files)!=0 :
            TAG = path.split('\\')[-1]
            if TAG == 'DeviceSearchCache' :
                for filename in files :
                    filepath = path+'\\'+filename
                    appCache.loc[len(appCache)] = filepath
            elif TAG == 'Install' :
                for filename in files :
                    filepath = path+'\\'+filename
                    installLog.loc[len(installLog)] = filepath
            elif TAG == 'INF' :
                for filename in files :
                    filepath = path+'\\'+filename
                    infLog.loc[len(infLog)] = filepath

    appCache.to_csv('.\\parsingResult\\appCache.csv',index=False,header=None)
    installLog.to_csv('.\\parsingResult\\installLog.csv',index=False,header=None)
    infLog.to_csv('.\\parsingResult\\infLog.csv',index=False,header=None)

if __name__ =='__main__' :
    makeFilePath()

