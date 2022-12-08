# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

class Visualization():
    def __init__(self,obs, true, sim, sim2, da, interval, nt_asm, name,xlim):
        self.obs = obs
        self.true = true
        self.sim = sim
        self.sim2 = sim2
        self.da = da
        self.da = da
        self.interval = interval
        self.nt_asm = nt_asm
        self.name = name
        self.xlim = xlim

    def fit(self):
        fig = plt.figure(figsize=(12, 3)) # figureオブジェクト作成
        _xrange = range(len(self.true))

        if(self.obs != None):
            _xrange2 = range(0,self.nt_asm,self.interval)
            _xobs2 = []
            for i in range(0,self.nt_asm,self.interval):
                _xobs2.append(self.obs[i])
            plt.scatter(_xrange2,_xobs2,color='red',label='Obs.')
        plt.plot(_xrange,self.sim2,color='orange',label='Sim2')
        plt.plot(_xrange,self.true,color='green',label='True')
        plt.plot(_xrange,self.sim,color='blue',label='Sim.')
        plt.plot(_xrange,self.da,color='purple',label='DA')
        plt.xlabel("Time Step",size=12)
        plt.ylabel(self.name,size=12)
        plt.xlim(0,self.xlim)
        plt.legend()
        plt.show()
        return self

    def plot_rmse(self):
        _rmse_da= 0.0
        for i in range(len(self.da)):
            _rmse_da = _rmse_da + (self.true[i] - self.da[i])**2
        _rmse_da = np.sqrt(_rmse_da/len(self.da))

        _rmse_sim= 0.0
        for i in range(len(self.sim)):
            _rmse_sim = _rmse_sim + (self.true[i] - self.sim[i])**2
        _rmse_sim = np.sqrt(_rmse_sim/len(self.da))

        _rmse_sim2= 0.0
        for i in range(len(self.sim)):
            _rmse_sim2 = _rmse_sim2 + (self.true[i] - self.sim2[i])**2
        _rmse_sim2 = np.sqrt(_rmse_sim2/len(self.da))

        print ("RMSE of Simulation = ", _rmse_sim)
        print ("RMSE of Simulation2 = ", _rmse_sim2)
        print ("RMSE of DA result = ", _rmse_da)
        print ()
        return self

    def get_rmse(self, start = 0, end = 0):
        if (end == 0):
            end = len(self.da) - start
        true_2 = self.true[start:end]
        da_2 = self.da[start:end]
        sim_2 = self.sim[start:end]
        sim2_2 = self.sim2[start:end]
        _rmse_da= 0.0
        for i in range(len(da_2)):
            _rmse_da = _rmse_da + (true_2[i] - da_2[i])**2
        _rmse_da = np.sqrt(_rmse_da/len(da_2))

        _rmse_sim= 0.0
        for i in range(len(sim_2)):
            _rmse_sim = _rmse_sim + (true_2[i] - sim_2[i])**2
        _rmse_sim = np.sqrt(_rmse_sim/len(da_2))

        _rmse_sim2= 0.0
        for i in range(len(sim_2)):
            _rmse_sim2 = _rmse_sim2 + (true_2[i] - sim2_2[i])**2
        _rmse_sim2 = np.sqrt(_rmse_sim2/len(da_2))

        return (_rmse_da, _rmse_sim, _rmse_sim2)
