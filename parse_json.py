import json
import pdb



f = open("sysbench_output.txt")
#opening bracket
j = "{"

for line in f:
  if "Number" in line:
     x = line.split(":")
     j += '"Threads %s": { "SQL Statistics": { "queries": {' %(x[1].strip())

  elif any(item in line for item in ['read:', 'write:', 'other:','transactions:','queries:','total time:','min:','avg:','max','95th percentile:''reconnects:','events (avg/stddev):']): 
     x = line.split(":")
     j += '"%s": "%s",' %(x[0].strip(),x[1].strip())

  elif any(item in line for item in ['total:','execution time (avg/stddev):']):
     x = line.split(":")
     j += '"%s": "%s" }},' %(x[0].strip(),x[1].strip()) 

  elif any(item in line for item in ['General statistics:','Latency (ms):','Threads fairness:']): 
     j += '"%s": {' %(line.strip())

  elif any(item in line for item in ['total number of events:','sum:']):
     x = line.split(":")
     j += '"%s": "%s" },' %(x[0].strip(), x[1].strip())

j = j[:-1]
j += "}"
print j
