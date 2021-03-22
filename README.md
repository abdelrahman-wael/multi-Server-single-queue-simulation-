# multi-Servers Single Queue Simulation
this is a simple simulation to gather various data from the system described and investigate how various variables and scheduling polcies impact system's behavior

# System Desciption

<p align="center">
  <img src="./images/simulationFinalProject .jpg"  >
</p>


As we can see above Customers arrive with interarrival times that are exponentially distributed with a mean of 5 and we have an infinite queue that distributes the customer to one of the 5 servers chosen using round robbin or using a priority queue according to the policy.
Each service follows a uniform distribution as shown in the figure.
There a probability P that a customer who is not satisfied rejoins the queue and waits for him to serve again where variable I determines how many times the customer Is dissatisfied.
