import os
import json
import sched, time
import subprocess
import boto3


outerDict={}
jdict ={}

rootIndex = 'target'
data = 'output'
target = ''
blackbox = "http://localhost:9115"
output = ''


client = boto3.client('kinesis')
def sendToKinesis (data): 
    client.put_record(StreamName='blackbox',PartitionKey="partitionKey1",Data=data)
    return


def probeSite(target):
    outerDict[rootIndex] = target
    for line in os.popen("curl -m 5 "+blackbox+"/probe?target="+target+"&module=http_2xx").readlines():
        if not line.startswith('#'):
            line = line.strip()			
            sep = line.split()
            key = sep.pop(0)		
            jdict[key] = sep[0]
    outerDict[data] = jdict
        

probeSite("https://www.amazon.com")
output = json.dumps(outerDict, indent=4)
sendToKinesis(output)
print(output)



    
    




