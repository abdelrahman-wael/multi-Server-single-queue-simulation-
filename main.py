import simpy 
from policies import *
from Customer import *
from Queue import *
from System import *
from systemStats import *
from tqdm import tqdm

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
    
  
def main():
  dic = {"numOfSatisfied" : [],
  "totalTimeInSys" : [],
  "numOfCustomer" : [],
  "maxTimeInSys" : [],
  "avgQueueLen": [],
  "maxQueueLen" :[],
  "meanBusyTime" :[],
  "maxBusyServer" : []}

  # number of repetition the more the better
  n=100

  for i in tqdm(range(n)):

    env = simpy.Environment()
    system = System(env,FIFO)
    env.process(system.Simulation())
    env.run(until=480)
    
    saveSystemStat(dic,system)


  showSystemStats(dic)



 
if __name__=="__main__":
  main()