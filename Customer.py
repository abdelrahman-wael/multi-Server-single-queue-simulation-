import numpy as np

class Customer():
  def __init__(self):
    self.num_of_services=0
    self.a = 2
    self.b = 2.8
    self.serviceTime = []
    self.timeSpent = 0
    self.arrival_timeStamp = 0
    self.interarrival_time = 0

  def calculateServiceTime(self):
    a=(self.a)/(1+self.num_of_services)
    b= (self.b) / (1+self.num_of_services)
    serviceTime = np.random.uniform(a,b)
    return serviceTime