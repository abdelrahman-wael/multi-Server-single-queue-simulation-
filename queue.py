import numpy as np 
from Customer import Customer

class Queue():
  def __init__(self):
    self.customers=[]
    self.maxLen=0
    self.customerServerd = []
    self.available = 1
    self.maxNumBusyServer = 0
    self.numCustomer = []
  
  def updateMaxLen(self):
    if(len(self.customers)>self.maxLen):
      self.maxLen = len(self.customers)

  def generateCustomer(self,env):
    id =0
    while(self.available):
      arrival_time=np.random.exponential(5)
      yield env.timeout(arrival_time)
      c=Customer()
      c.arrival_timeStamp =  env.now
      c.interarrival_time = arrival_time
      c.id = id
      id+=1
      self.customers.append(c)
      if(len(self.customers)>self.maxLen):
        self.maxLen = len(self.customers)
      self.numCustomer += [len(self.customers)]
      
    return 0
