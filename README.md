# Epidemic-Model---Ordinary-Differential-Equation
An ordinary differential equation model for simulating a viral epidemic. The model is based on the "Event 201 - a global pandemic excersise" and simualtes an outbreak in a coherent community.

The	model	contains	six	compartments	representing	different	stages	of	
infection:
1) Susceptible -> incubating -> Infected mild or infected severe -> recovered or dead

# start parameters
  N = Population Size,
  days = days to simulate,
  seed_Im = seed number of mild cases,
  seed_Is = seed number of servere cases

# viral parameter
 beta = transmission,
 theta = fraction servere cases,
 cfr = Case Fatality Risk,
 phi = cfr/theta # case fatality risk of severe cases (All deaths occure within severe compartment)

# time parameters (mean duration of each stage)
  k1 = incubation period of mild cases,
  k2 = incubation period of severe cases, 
  gamma = days to recover for mild cases,
  alpha = days to outcome for servere cases

# further reading: 
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2870608/

  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4399521/#ref10

  http://www.centerforhealthsecurity.org/event201/event201-resources/event201-model-desc.pdf
