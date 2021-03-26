from Queue import *
from Servers import *
from policies import *
# this class wraps the main component of the system
class System(object):
  def __init__(self,env,numServers,arrivalTime,policy):
    self.env = env
    self.queue = Queue(arrivalTime)
    self.servers = Servers(numServers)
    self.policy = getPolicy(policy)

  def Simulation(self):
    self.env.process(self.queue.generateCustomer(self.env))
    scheduler =  self.policy
    while True :
      # check if there are customers in queue and server available 
      if len(self.queue.customers) and len(self.servers.availableServers):
        # get customer based on policy
        customer = scheduler(self.queue)
        # send customer to server
        self.env.process(self.servers.ServeCustomer(self.env, customer, self.queue))
        
      yield self.env.timeout(0.1)