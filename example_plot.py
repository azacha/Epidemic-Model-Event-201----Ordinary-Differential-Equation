from ode import MODEL
import matplotlib.pyplot as plt

#parameters
N = 1000000
days = 300
seed_Im = 1
seed_Is = 1
beta = 0.3
theta = 0.5
cfr = 0.22
k1 = 10
k2 = 10
gamma = 10
alpha = 7
model = MODEL(N,days,seed_Im,seed_Is,beta,theta,cfr,k1,k2,gamma,alpha)
output = model.runModel()


fig, ax = plt.subplots()
fig.set_size_inches(12, 8)
plt.plot(output["intervalls"],output["Dead"], color='black', alpha=0.25,linewidth=3,label="Dead")
plt.plot(output["intervalls"],output["Recovered"], color='blue', alpha=0.25,linewidth=3,label="Recovered")
plt.plot(output["intervalls"],output["infected_mild"], color='green', alpha=0.25,linewidth=3,label="Infected mild")
plt.plot(output["intervalls"],output["infected_severe"], color='olive', alpha=0.25,linewidth=3,label="Infected severe")
plt.plot(output["intervalls"],output["infected_mild"], color='red', alpha=0.25,linewidth=3,label="Incubating")
plt.xlabel("ODE-Model: Number of people per stage per day")
plt.xlabel("days")
plt.ylabel("n")
plt.legend()
plt.show()
