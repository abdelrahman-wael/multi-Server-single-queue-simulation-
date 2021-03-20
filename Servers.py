import numpy as np

class Server():
  def __init__(self):
    self.TotalServiceTime=0
    self.numCustomer=0

class Servers():
  def __init__(self):
    self.availableServers = [Server() for i in range(5)]
    
  # server customer using one of the servers available
  def ServeCustomer(self,env,customer,queue): 
    server=self.availableServers.pop(0)
    if((5-len(self.availableServers))>queue.maxNumBusyServer):
      queue.maxNumBusyServer = 5-len(self.availableServers)
    serviceTime= customer.calculateServiceTime()
    customer.serviceTime.append(serviceTime)
    server.TotalServiceTime+=serviceTime
    server.numCustomer+=1
    yield env.timeout(serviceTime)
    # release server
    self.availableServers.append(server)
    # check if customer is satisfied
    choices = [0, 1]
    p = 0.2/(1+customer.num_of_services)
    probabilities = [p, 1-p]
    satisfied = np.random.choice(choices, 1, p=probabilities)
    customer.num_of_services += 1
    if not satisfied:
      customer.timeSpent+=serviceTime
      queue.customers.append(customer)
      if(len(queue.customers)>queue.maxLen):
        queue.maxLen = len(queue.customers)
    else:
      customerArrivalTime = customer.arrival_timeStamp
      timeNow = env.now
      customer.timeSpent = timeNow - customerArrivalTime
      queue.customerServerd.append(customer)
    return 0