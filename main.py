import simpy 
from processes import *
from policies import *
from customer import *
from queue import *
from 

def runSim(env,availableServers,queue,priority = False):
  env.process(generateCustomer(env,queue))
  if priority:
    scheduler = priority_
  else:
    scheduler = FIFO
  while True :
    # check if there are customers in queue and server available 
    if len(queue.customers) and len(availableServers):
      # get customer based on policy
      customer = scheduler(queue)
      # send customer to server
      env.process(ServeCustomer(env, customer,queue,availableServers))
      # ServeCustomer(customer,queue,availableServers )
    yield env.timeout(0.1)
    

if name =="__main__":
  main()
