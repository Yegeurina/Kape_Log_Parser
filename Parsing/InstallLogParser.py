import pandas as pd

install = '.\\parsingResult\\installLog.csv'

log = pd.DataFrame(columns=['madeID','StartTime','Name','Path','Size','Created','Modified','LastAccessed','FileSize'])
header = ['madeID','StartTime','Name','Path','Size','Created','Modified','LastAccessed','FileSize']
fileCreate = pd.DataFrame(columns=['madeID','path'])
arpCreate = pd.DataFrame(columns=['madeID','path'])
msidetected = pd.DataFrame(columns=[])

def Parser(filepath) :

    filepath = filepath.strip('\n')
    base = []
    base.append(str(len(log)))

    with open(filepath,'r',encoding='utf-16-le') as file :
        reader = file.readline()
        while reader :
            reader=reader.strip('\n')
            parsing = reader.split('=')
            if (parsing[0]=='FileCreate') :
                fileCreate.loc[len(fileCreate)]=[str(len(log)),parsing[1]]
            elif (parsing[0]=='ArpCreate') :
                arpCreate.loc[len(arpCreate)]=[str(len(log)),parsing[1]]
            else :
                for hdr in header :
                    if(parsing[0]==hdr) :
                        base.append(parsing[1])
        
            reader = file.readline()
    log.loc[len(log)] = base
    
def readfilePath() :
    with open(install,'r') as file:
        list = file.readline()
        while list :
            Parser(list)
            list = file.readline()

if __name__ == '__main__' :
    readfilePath()

    log=log.dropna(axis=0)
    fileCreate=fileCreate.dropna(axis=0)
    arpCreate = arpCreate.dropna(axis=0)
    
    # print(log)
    # print(fileCreate)
    # print(arpCreate)

    log['Size']=log['Size'].apply(lambda x : int(x,16))
    log['FileSize'] = log['FileSize'].apply(lambda x : int(x,16))

    fileCreate.to_csv('.\\parsingResult\\install\\Install_fileCreate.csv',index=False,header=None)
    arpCreate.to_csv('.\\parsingResult\\install\\Install_arpCreate.csv',index=False,header=None)
    log.to_csv('.\\parsingResult\\install\\Install_Log.csv',index=False,header=None)

    print(log.info())
    print(fileCreate.info())
    print(arpCreate.info())