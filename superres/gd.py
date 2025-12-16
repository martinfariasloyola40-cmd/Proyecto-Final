import numpy as np

class GradientDescentSR:
    def __init__(self,A,reg,lam,tau,niter):
        self.A=A; self.reg=reg
        self.lam=lam; self.tau=tau; self.niter=niter

    def cost(self,x,b):
        Ax=self.A.apply(x)
        return 0.5*np.sum((Ax-b)**2)

    def run(self,x,b):
        costs=[]
        for k in range(self.niter):
            grad_data=self.A.adjoint(self.A.apply(x)-b)
            grad_reg=self.reg.grad(x)
            x = x - self.tau*(grad_data+self.lam*grad_reg)
            costs.append(self.cost(x,b))
        return x,costs
