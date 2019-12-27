import math
from sympy import nsolve, symbols
from scipy.integrate import quad
import scipy.optimize as opt

class Constant:
    @staticmethod
    def getSLessAlpha(s):  # 2.35 search S
        k, f = symbols('k f')
        return (f + k) * s ** 4 + 4 * (1 - k * f) * s ** 3 + 2 \
               * (k * f ** 2 - 3 * f - 2 * k) * s ** 2 + 4 * f * \
               (f + k) * s + f - k - 2 * k * f ** 2


    @staticmethod
    def eta1Diff2(k, f, p):
        return 2 * k * (
                (p * f ** 3 * k - f * p ** 2 - f ** 2 * p + k + f ** 2 * k + p * f * k - p - p ** 2 * f ** 3) / (
                (f * p ** 2 - 2 * f ** 2 * p + k - f + f ** 2 * k) ** 2))


    @staticmethod
    def eta2Diff2(k, f, p):
        return (2 * (1 + f * k) * (1 + p ** 2) * (
                p ** 4 - p ** 3 * k - 3 * p ** 3 * f + 3 * f * k * p ** 2 + 3 * k * p + p * f - 3 * p ** 2 - f * k) / (
                        (1 + f ** 2) * (2 * p ** 3 - p ** 2 * k - 3 * p ** 2 * f + 2 * f * k * p + k - f) ** 2))


    @staticmethod
    def eta1(k, f, p):
        return ((k * f - 1) * p * p + 2 * (k + f) * p + 1 - k * f) / (f * p * p - 2 * f * f * p + k - f + k * f * f)


    @staticmethod
    def eta2(k, f, p):
        return ((1 + k * f) / (1 + f * f)) * (
                ((1 + p * p) * (1 + p * p)) / (2 * p * p * p - (k + 3 * f) * p * p + 2 * k * f * p + k - f))


class Search_Constant_Test:
    def getC(self):
        return self.C[0]

    def gett(self):
        return self.t

    def geth(self):
        return self.h

    def gets(self):
        return self.s

    def getlamba(self):
        return self.lamb

    def geta(self):
        return self.a[0]

    def start(self):
        pass

    def __init__(self, alpha, phi, gamma, H):
        # print(alpha)
        self.const = Constant()
        self.alpha = alpha
        self.phi = phi
        self.gamma = gamma
        self.E = 0
        self.H = H

        self.k = math.tan(math.radians(self.alpha))
        self.f = math.tan(math.radians(self.phi))
        self.s = symbols('s')

        #search and check S
        if(self.alpha<45+self.phi/2):
            self.s = nsolve(self.const.getSLessAlpha(self.s).subs('k',self.k).subs('f', self.f), self.s, 100)
        else:
            self.s = self.f+math.sqrt(1+self.f**2)

        # # Second integrall!
        ffl1 = lambda p: (self.const.eta1Diff2(self.k,self.f,p)/(self.k-p))
        ff1=quad(ffl1, self.f, math.tan(math.radians(self.alpha+self.phi)/2-(math.pi)/4))

        ffl2 = lambda p: (self.const.eta2Diff2(self.k,self.f,p)/(self.k-p))
        ff2 = quad(ffl2, self.s, self.f)

        self.lamb = (self.H/self.k)/((ff1[1] - ff1[0]) + (ff2[1] - ff2[0]))#search lamb

        #search and check h
        self.h=self.lamb*((1+self.f*self.k)/(1+self.f**2))*(((1+self.s**2)**2)/(2*self.s**3-(self.k+3*self.f)*self.s**2+2*self.k*self.f*self.s+self.k-self.f))

        self.C=opt.fsolve(self.func, 1.0)

        # search and check t
        self.t = math.sqrt((((self.h * self.f * self.gamma) / self.C) + 1))

        self.a = ((2*self.C)/(self.gamma*self.f))*quad((lambda p:1), 0, 1)*quad((lambda p:1), math.tan(math.pi/4+math.radians(self.phi)/2), self.t)

    def integrand1(self,p, C):
        return (((self.gamma*self.lamb*(p-self.f)/(1+self.f*p))*self.const.eta1(self.k,self.f, p)-C*(1+p**2)/(1+self.f*p))*self.const.eta1Diff2(self.k,self.f,p)*self.lamb/(self.k-p))

    def integrand2(self, p, C):
        return (((self.lamb*self.gamma*(p-self.f)/(1+p**2))*(self.const.eta2(self.k,self.f,p))-C)*(self.lamb*(self.const.eta2Diff2(self.k,self.f,p))/(self.k-p)))

    def integrand3(self, p, C):
        return (((p**2-1)*(p-self.f)/(self.f)-(1+p**2))*((2*C**2)/(self.gamma*self.f)))

    def func(self, С):
        y1, err1 = quad(self.integrand1, self.f, math.tan(math.radians(self.alpha+self.phi)/2-(math.pi)/4), args=(С,))
        y2, err2 = quad(self.integrand2, self.s, self.f, args=(С,))
        y3, err3 = quad(self.integrand3, math.sqrt((((self.h * self.f * self.gamma) / С) + 1)), self.f+math.sqrt(1+self.f**2) , args=(С,))

        return y1+y2+y3
