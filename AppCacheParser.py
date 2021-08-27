import pandas as pd
import json
from datetime import datetime
import filetime

appCache = '.\\parsingResult\\appCache.csv'
log = pd.DataFrame(columns=['madeID','FileExtension','ProductVersion','Kind','TimeUsed','Background','PackageFullName','Identity','FileName','VoiceCommandExamples','ItemType','DataAccessed','EncodedTargetPath','SmallLogoPath','ItemNameDisplay'])
def Parser(filepath) :
    filepath = filepath.strip('\n')
    with open(filepath,'r',encoding='utf-8') as file :
        data = file.read()
        data = data.strip(']')
        data = data.split("{\"System.FileExtension\":")
        for cache in data:
            line=[]
            if (len(cache)>1) :

                cache = "{\"System.FileExtension\":" + cache
                cache = cache.strip(",")
                cache = json.loads(cache)

                line.append(len(log))
                line.append(cache['System.FileExtension']['Value'])
                line.append(cache['System.Software.ProductVersion']['Value'])
                line.append(cache['System.Kind']['Value'])
                line.append(cache['System.Software.TimesUsed']['Value'])
                line.append(cache['System.Tile.Background']['Value'])
                line.append(cache['System.AppUserModel.PackageFullName']['Value'])
                line.append(cache['System.Identity']['Value'])
                line.append(cache['System.FileName']['Value'])
                line.append(cache['System.ConnectedSearch.VoiceCommandExamples']['Value'])
                line.append(cache['System.ItemType']['Value'])
                
                dt = int(cache['System.DateAccessed']['Value'])
                if dt ==0 : line.append('0')
                else :
                    dt = filetime.to_datetime(dt)
                    dt = datetime.strftime(dt,"%m/%d/%Y %H:%M:%S")
                    line.append(dt)

                line.append(cache['System.Tile.EncodedTargetPath']['Value'])
                line.append(cache['System.Tile.SmallLogoPath']['Value'])
                nameDisplay = cache['System.ItemNameDisplay']['Value']
                nameDisplay = str(nameDisplay).replace(',','/')
                line.append(nameDisplay)
                log.loc[len(log)]=line
        

def readfilePath() :
    with open(appCache,'r') as file:
        list = file.readline()
        while list :
            Parser(list)
            list = file.readline()

if __name__ == '__main__' :
    readfilePath()
    # print(log)
    # print(log.info())
    log.to_csv('.\\parsingResult\\appCache\\AppCache.csv',index=False,header=None)