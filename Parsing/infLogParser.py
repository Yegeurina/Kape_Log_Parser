import pandas as pd
import re
from datetime import datetime

inf = '.\\parsingResult\\infLog.csv'
log = pd.DataFrame(columns=['madeID','DriveName','Class GUID','Driver Version', 'Configuration', 'Section end'])
header = ['Class GUID','Driver Version', 'Configuration']

def Parser(filepath) :
    filepath = filepath.strip('\n')
    p = re.compile('\d+\/\d+\/\d+ \d+:\d+:\d+')
    p_n = re.compile('\(\w+\s?\w+\)')
    with open(filepath,'r',encoding='ANSI') as file :
        reader = file.read()
        d = reader.split('>>>  [Device Install')
        for data in d :
            parsingLine = []
            data = ">>>  [Device Install" + data
            
            if('<<<  [Exit status: SUCCESS]' in data) : #and ('USBSTOR'  in data)  :
                data = data.split('\n')
                if('USBSTOR' in data[0]) :
                    parsingLine.append(len(log))
                    for line in data:
                        if 'Section end' in line :
                            dt = p.search(line).group()
                            dt = datetime.strptime(dt,"%Y/%m/%d %H:%M:%S")
                            dt = datetime.strftime(dt,"%m/%d/%Y %H:%M:%S")
                            parsingLine.append(dt)
                            break
                        if ">>>  [Device Install"  in line :
                            dn = p_n.search(line).end()
                            # # print (dn)
                            # position = line.find(dn)
                            parsingLine.append(line[dn+3:-1])
                        for hdr in header :
                            if(hdr in line) and ('utl:' in line) :
                                line = line.replace(","," ")
                                line = line.split(hdr)
                                position = line[1].find('-')
                                parsingLine.append(line[1][position+1:])
                        #print(line)
                    
                    if (len(header)+3 == len(parsingLine)):
                        print(parsingLine)
                        log.loc[len(log)]=parsingLine

                      


def readfilePath() :
    with open(inf,'r') as file:
        list = file.readline()
        while list :
            Parser(list)
            list = file.readline()

if __name__ == '__main__' :
    readfilePath()
    # print(log.info())
    # print(log)
    log.to_csv('.\\parsingResult\\inf\\INF.csv',index=False,header=None)