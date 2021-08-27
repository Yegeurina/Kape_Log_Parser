SELECT 
    'setup_api' AS fromTable,driveName AS title, endtime AS accessTime
FROM
    remakekape.setup_api 
UNION SELECT 
   'installlog' AS fromTable, title AS title, lasttime AS accessTime
FROM
    remakekape.installlog 
UNION SELECT 
    'appcache' AS fromTable,itemnamedisplay AS title, dataaccessed AS accessTime
FROM
    remakekape.appcache;