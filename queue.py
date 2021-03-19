class Queue():
  def __init__(self):
    self.customers=[]
    self.maxLen=0
    self.history = []
    self.available = 1
    self.maxNumBusyServer = 0
    self.numCustomer = []
  
  def updateMaxLen(self):
    if(len(self.customers)>self.maxLen):
      self.maxLen = len(self.customers)
    

class server():
  def __init__(self):
    self.TotalServiceTime=0
    self.numCustomer=0

