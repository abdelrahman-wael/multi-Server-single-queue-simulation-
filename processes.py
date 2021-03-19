import numpy as np

# server customer using one of the servers available
def ServeCustomer(env,customer,queue,availableServers):
  
  server=availableServers.pop(0)
  if((5-len(availableServers))>queue.maxNumBusyServer):
    queue.maxNumBusyServer = 5-len(availableServers)
  serviceTime= customer.calculateServiceTime()
  customer.serviceTime.append(serviceTime)
  server.TotalServiceTime+=serviceTime
  server.numCustomer+=1
  yield env.timeout(serviceTime)
  # release server
  availableServers.append(server)
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
    queue.history.append(customer)
  return 0
  
  
  def generateCustomer(env,queue):
  id =0
  while(queue.available):
    arrival_time=np.random.exponential(5)
    yield env.timeout(arrival_time)
    c=Customer()
    c.arrival_timeStamp =  env.now
    c.interarrival_time = arrival_time
    c.id = id
    id+=1
    queue.customers.append(c)
    if(len(queue.customers)>queue.maxLen):
      queue.maxLen = len(queue.customers)
    queue.numCustomer += [len(queue.customers)]
    
  return 0
