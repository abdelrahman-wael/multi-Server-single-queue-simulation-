import pandas as pd
import numpy as np, scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display 

def serverStats(availableServers,totalTime=4800 , numServers = 5):
  totalServiceTime =0
  avgBusyTime = 0
  for server in availableServers:
    avgBusyTime += server.TotalServiceTime/totalTime
  return avgBusyTime/numServers


def  customerStat(queue):
  AllCustomers=queue.customerServerd
  arrivalTime=[]
  timeSpent=[]
  numOfSatisfied = 0
  for customer in AllCustomers:
    arrivalTime.append(customer.interarrival_time)
    timeSpent.append(customer.timeSpent)
    if(customer.num_of_services == 1):
      numOfSatisfied +=1
    
  return arrivalTime,timeSpent,numOfSatisfied


def saveSystemStat(dic,system):

  arrivalTime,timeSpent,satisfiedCustomer = customerStat(system.queue)
  dic["numOfCustomer"].append(len(timeSpent))

  dic["totalTimeInSys"].append(sum(timeSpent)/len(timeSpent) )
  dic["maxTimeInSys"].append(max(timeSpent))

  # total num of satisfied customer 
  dic["numOfSatisfied"].append(satisfiedCustomer)
  # queue stats 
  dic["avgQueueLen"].append(sum(system.queue.numCustomer)/len(system.queue.numCustomer))
  dic["maxQueueLen"].append(system.queue.maxLen)

  # average server busy time 
  dic["meanBusyTime"].append(serverStats(system.servers.availableServers))

  # max number of busy server
  dic["maxBusyServer"].append(system.queue.maxNumBusyServer)




def showSystemStats(dic):
  variables=dic.keys()
  dataframe = {"variables":[],"mean":[],"stander deviation":[],"confidence interval 95%":[]}
  for variable in list(variables):
    mean , std, confidenceInterval = variableStats(dic[variable]) 
    dataframe["variables"].append(variable)
    dataframe["mean"].append(mean)
    dataframe["stander deviation"].append(std)
    dataframe["confidence interval 95%"].append(confidenceInterval)
  dataframe=pd.DataFrame(dataframe)
  dataframe=dataframe.set_index("variables")
  pd.set_option('display.max_columns', None)
  display(dataframe)




def variableStats(list_):
  mean=np.mean(list_)
  std = np.std(list_)
  confidenceInterval = st.t.interval(0.95, len(list_)-1, loc=np.mean(list_), scale=st.sem(list_))

  return mean , std , confidenceInterval