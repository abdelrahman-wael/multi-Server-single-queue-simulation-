import simpy 
from policies import *
from Customer import *
from Queue import *
from System import *
from SystemStats import *
from tqdm import tqdm
import argparse
    
  
def main():

  
  parser = argparse.ArgumentParser()
  parser.add_argument('--numServers', type=int ,  default=5)
  parser.add_argument('--arrivalTime',type = int , choices = range(2,15) , default = 5)
  parser.add_argument('--iteration',type = int , choices = range(100,10000) , default = 200)
  parser.add_argument('--policy',type = str , choices = ["FIFO","Priority"] , default = "FIFO")
  args = parser.parse_args()
  iteration = args.iteration
  numServers = args.numServers
  arrivalTime = args.arrivalTime
  policy = args.policy
  print("num of Servers in the system =",numServers)
  print("customer mean arrival =",arrivalTime)

  dic = {"numSatisfied" : [],
  "totalTimeInSys" : [],
  "numCustomer" : [],
  "maxTimeInSys" : [],
  "avgQueueLen": [],
  "maxQueueLen" :[],
  "meanBusyTime" :[],
  "maxBusyServer" : []}

  # number of repetition the more the better
  n=iteration

  for i in tqdm(range(n)):

    env = simpy.Environment()
    system = System(env,numServers,arrivalTime,policy)
    env.process(system.Simulation())
    env.run(until=4800)
    
    saveSystemStat(dic,system)


  showSystemStats(dic)



 
if __name__=="__main__":
  main()