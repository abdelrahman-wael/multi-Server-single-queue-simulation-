def priority_(queue):
  queue.customers = sorted(queue.customers, key=lambda customer: customer.num_of_services, reverse=True)
  return queue.customers.pop(0)
  
 def FIFO(queue):
  return queue.customers.pop(0)
