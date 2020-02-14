# Epidemic-Model---Ordinary-Differential-Equation
An ordinary differential equation model for simulating a viral epidemic. The model is based on the "Event 201 - a global pandemic excersise" and simualtes an outbreak in a coherent community.

The	model	contains	six	compartments	representing	different	stages	of	
infection:
1) Susceptible -> incubating -> Infected mild or infected severe -> recovered or dead

 further reading: 
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2870608/
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4399521/#ref10
  http://www.centerforhealthsecurity.org/event201/event201-resources/event201-model-desc.pdf

# start parameters
  N = Population Size
  days = days to simulate
  seed_Im = seed number of mild cases
  seed_Is = seed number of servere cases
# viral parameter
 beta = transmission
 theta = float(theta) #fraction servere cases
 cfr = cfr # Case Fatality Risk
 phi = cfr/theta # case fatality risk, servere (All deads occure within severe compartment)

# mean timespans per state
  k1 = incubation period, mild
  k2 = incubation period, servere
  gamma = days to recover
  alpha = days to outcome in servere
