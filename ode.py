class MODEL():
    def __init__(self, N,days,seed_Im,seed_Is,beta,theta,cfr,k1,k2,gamma,alpha):
        #parameters
        self.N = float(N) #Population Size
        self.days = int(days) #days to simulate
        self.seed_Im = int(seed_Im) #seed number of mild cases
        self.seed_Is = int(seed_Is)#seed number of servere cases

        # viral parameter
        self.beta = float(beta) #transmission rate, R0
        self.theta = float(theta) #fraction servere cases
        self.cfr = float(cfr) # cfr, overall
        self.phi = self.cfr/self.theta # case fatality risk, servere (All deads occure within severe compartment)

        # timespans as inverse of the mean duration of corresponding period
        self.k1 = 1/int(k1) #incubation period, mild
        self.k2 = 1/int(k2) #incubation period, servere
        self.gamma = 1/int(gamma) #days to recover
        self.alpha = 1/int(alpha) #days to outcome in servere

        #population compartments
        self.S = [0]*self.days
        self.E = [0]*self.days #number of incubating individuals
        self.Im = [0]*self.days  #number of infected individuals, mild
        self.Is = [0]*self.days  #number of infected individuals, servere
        self.R = [0]*self.days  #recovered
        self.D = [0]*self.days  #dead
        self.X = [x+1 for x in range(self.days)] #time intervalls
        self.S[0] = self.N #Number of susceptible individuals = total population
        self.Im[0] = int(seed_Im) #Number of susceptible individuals
        self.Is[0] = int(seed_Is) #Number of susceptible individuals

    #transition rates
    def transition1(self,s,im,is_,N,beta):
        '''transition incubating'''
        return(beta*s*(im+is_))/N

    def transition2m(self,e,k1,theta):
        '''transition mild cases'''
        return k1*e*(1-theta)

    def transition2s(self,e,k2,theta):
        '''transition servere cases'''
        return k2*e*theta

    def transition3rm(self,im,gamma):
        '''transition recovered cases from mild '''
        return gamma*im

    def transition3rs(self,is_,alpha,phi):
        '''transition recovered cases from servere'''
        return alpha*is_*(1-phi)

    def transition3d(self,is_,alpha,phi):
        '''transition dead'''
        return alpha*is_*phi

    #transition
    def runModel(self):
        for t in range(self.days):
            if t == self.days-1:
                break
            else:
                #1: susceptible to incubating
                de = self.transition1(self.S[t],self.Im[t],self.Is[t],self.N,self.beta)
                self.S[t+1] = self.S[t] - de
                self.E[t+1] = self.E[t] + de

                #2: incubating to infectious
                dim = self.transition2m(self.E[t],self.k1,self.theta)
                dis = self.transition2s(self.E[t],self.k2,self.theta)
                self.Im[t+1] = self.Im[t] + dim
                self.Is[t+1] = self.Is[t] + dis
                self.E[t+1] = self.E[t+1] -(dim + dis)

                #infectious to final stage
                #recovered
                drm = self.transition3rm(self.Im[t],self.gamma)
                drs = self.transition3rs(self.Is[t],self.alpha,self.phi)
                self.R[t+1] = self.R[t] + drm + drs

                #dead
                dd = self.transition3d(self.Is[t],self.alpha,self.phi)
                self.D[t+1] = self.D[t] + dd

                #update infectious compartment
                self.Im[t+1] =  self.Im[t+1] - drm
                self.Is[t+1] = self.Is[t+1] - (drs +dd)

        return { "intervalls": self.X,
                 "Dead": self.D,
                 "Recovered": self.R,
                 "infected_mild": self.Im,
                 "infected_severe": self.Is,
                 "incubating": self.E
                }
