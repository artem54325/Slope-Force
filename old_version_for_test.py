import scipy.optimize as opt
from sympy import symbols
import matplotlib.pyplot as plt
import math

class Constant:
    @staticmethod
    def eta1Diff(k, f, p):
        return (2*f*f - 2*f*p)*(-f*k + p*p*(f*k - 1) + p*(2*f + 2*k) + 1)/(f*f*k - 2*f*f*p + f*p*p - f + k)**2 + (2*f + 2*k + 2*p*(f*k - 1))/(f*f*k - 2*f*f*p + f*p*p - f + k)

    @staticmethod
    def eta2Diff(k, f, p):
        return 4*p*(p*p + 1)*(f*k + 1)/((f**2 + 1)*(2*f*k*p - f + k + 2*p*p*p - p*p*(3*f + k))) + (p*p + 1)**2*(f*k + 1)*(-2*f*k - 6*p*p + 2*p*(3*f + k))/((f*f + 1)*(2*f*k*p - f + k + 2*p**3 - p**2*(3*f + k))**2)

    @staticmethod
    def eta3Diff(k, f, p):
        return (2*k - 2*p)/(-f + k)

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



class SlopeCalc:
    @staticmethod
    def seq(start, stop, step=1):
        n = int(round((stop - start) / float(step)))
        if n > 1:
            return ([start + step * i for i in range(n + 1)])
        elif n == 1:
            return ([start])
        else:
            return ([])

    @staticmethod
    def appender(list, idx, p, x1, y1, F, eta):
        if p is float and x1 is float and y1 is float and F is float and eta is float:
            accu = 80
            list[idx].append(round(p, accu)), list[idx].append(x1), list[idx].append(round(y1, accu))
            list[idx].append(round(F, accu)), list[idx].append(eta)
        else:
            list[idx].append(p), list[idx].append(x1), list[idx].append(y1)
            list[idx].append(F), list[idx].append(eta)

    @staticmethod
    def prevVariable(blocks, idx):
        prevK, prevX, prevY = blocks[idx - 1][1], blocks[idx - 1][2], blocks[idx - 1][3]
        prevP, prevX1, prevY1 = blocks[idx - 1][4], blocks[idx - 1][5], blocks[idx - 1][6]
        prevF, prevEta = blocks[idx - 1][7], blocks[idx - 1][8]
        return prevK, prevX, prevY, prevP, prevX1, prevY1, prevF, prevEta

    @staticmethod
    def searchKXY(blocks, idx):
        k, x, y = blocks[idx][1], blocks[idx][2], blocks[idx][3]
        return k, x, y

    def saveSlope(self, list, color):
        try:
            if self.saveBlocksList is None: ...
        except AttributeError:
            self.saveBlocksList = []
        try:
            if self.saveColorList is None: ...
        except AttributeError:
            self.saveColorList = []
        self.saveBlocksList.append(list)
        self.saveColorList.append(color)

    def logs(self):
        print('save logs')
        save = self.saveBlocksList
        logs = open("logsSlope0723.txt", "w")
        for idx in range(0, len(save)):
            for id in range(0, len(save[idx]) - 1):
                print('{:=.0f}\t{:=.2f}\t{:=.2f}\t{:=.2f}\t{:= .3f}\t{:=.2f}\t{:= .2f}\t{:= .3f}\t{:=.1f}'.format(
                    save[idx][id][0], save[idx][id][1], save[idx][id][2], save[idx][id][3], save[idx][id][4],
                    save[idx][id][5], save[idx][id][6], save[idx][id][7], save[idx][id][8]), sep=' ', file=logs)
                if id % 30 == 0:
                    print('{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t|||||||'.format(
                        'Num', 'k', 'x', 'y', ' p', 'x1', ' y1', ' F', 'eta'), sep=' ', file=logs)
        logs.close()

    def txtCoords(self):
        print('recording txt')
        save = self.saveBlocksList
        listx, listy, listx1, listy1 = [], [], [], []
        for idx in range(0, len(self.saveBlocksList)):
            listx.append([])
            listy.append([])
            listx1.append([])
            listy1.append([])
            for id in range(0, len(save[idx]) - 1):
                listx[idx].append(save[idx][id][2])
                listy[idx].append(save[idx][id][3])
                listx1[idx].append(save[idx][id][5])
                listy1[idx].append(save[idx][id][6])
        file = open("=pointsSlope0723=.txt", "w")
        for idx in range(0, len(self.saveBlocksList)):
            for id in range(0, len(self.saveBlocksList[idx]) - 1):
                print(listx1[idx][id] - 20, listy1[idx][id], sep=' ', file=file)
        file.close()

    def drawing(self):
        print('drawing slope')
        save = self.saveBlocksList
        colorSlope = '#808080'
        listx, listy, listx1, listy1 = [], [], [], []
        for idx in range(0, len(self.saveBlocksList)):
            listx.append([])
            listy.append([])
            listx1.append([])
            listy1.append([])
            for id in range(0, len(save[idx]) - 1):
                if len(save[idx][id]) == 4:
                    continue
                listx[idx].append(save[idx][id][2])
                listy[idx].append(save[idx][id][3])
                listx1[idx].append(save[idx][id][5])
                listy1[idx].append(save[idx][id][6])
        plt.style.use('ggplot')
        plt.axis([-0 * self.lenght, 1 * self.lenght, -0.2 * self.height, 1.2 * self.height])
        for idx in range(0, len(save)):
            plt.plot(listx[idx], listy[idx], color=colorSlope)
            plt.plot(listx1[idx], listy1[idx], color=self.saveColorList[idx])
        plt.show()

    def createListK(self, listX, listY, dx):
        listK = []
        for idx in range(0, len(listX) - 1):
            if (listY[idx + 1] - listY[idx]) == 0:
                tan = 0
            else:
                tan = (listY[idx + 1] - listY[idx]) / (listX[idx + 1] - listX[idx])
            for x in self.seq(listX[idx], listX[idx + 1] - dx, dx):
                listK.append(tan)
        return listK

    def createListBlocks(self, listX, listK, dx):
        blocks = []
        accu = 8
        for idx in range(0, int(listX[-1] / dx)):
            blocks.append([])
            blocks[idx].append(idx)
            blocks[idx].append(round(listK[idx], accu))
            blocks[idx].append(round(dx * idx, accu))
            if idx != 0:
                blocks[idx].append(round(listK[idx - 1] * dx + blocks[idx - 1][3], accu))
            else:
                blocks[idx].append(0)
        return blocks

    def settingsSlope(self, dx, listCoords, color):
        listX, listY = [], []
        for idx in range(0, len(listCoords)):
            listX.append(listCoords[idx][0])
            listY.append(listCoords[idx][1])
        listK = self.createListK(listX, listY, dx)
        blocks = self.createListBlocks(listX, listK, dx)
        self.alpha = math.degrees(math.atan(max(listK)))
        self.H = blocks[-1][3] - blocks[0][3]
        self.height = max(listY)
        self.lenght = max(listX)
        self.colorname = color
        return blocks

    def calculateP_i(self, mu, eta, k, f, p_i, dx):
        if eta == 1:
            fun = Constant.eta1Diff(k, f, p_i)
        elif eta == 2:
            fun = Constant.eta2Diff(k, f, p_i)
        else:
            fun= Constant.eta3Diff(k, f, p_i)
        p_i = (dx * k - dx * p_i + fun * mu * p_i)/(fun * mu)
        return p_i

    def calculateYi(self, mu, k, f, p_i, prevP, blocks, idx, eta):
        if eta == 1:
            fun = Constant.eta1Diff(k, f, p_i)
        elif eta == 2:
            fun = Constant.eta2Diff(k, f, p_i)
        elif eta == 3:
            fun = Constant.eta3Diff(k, f, p_i)
        yi = mu * fun / (k - p_i) * p_i * (p_i - prevP)
        summYi = yi + blocks[idx - 1][6]
        return yi, summYi

    def calculateFirstP(self, mu, f, k, y, y1):
        firstP = -((f - k) * ((2 * k * mu) / (f - k) - (2 * math.sqrt(
            -f * mu * y1 + f * mu * y + k * k * mu ** 2 + k * mu * y1 - k * mu * y + mu * mu)) / math.sqrt(
            f * f - 2 * f * k + k * k))) / (2 * mu)
        return firstP

    def calculateF(self, eta, dx, gamma, y, y1, p_i, f, C):
        if eta == 1:
            F = dx * (gamma * (y - y1) * (p_i - f) - C * (1 + p_i * p_i)) / (1 + f * p_i)
        elif eta == 2:
            F = dx * (gamma * (y - y1) * (p_i - f) - C * (1 + p_i * p_i)) / (1 + p_i * p_i)
        elif eta == 3:
            F = dx * (gamma * (y - y1) * (p_i - f) - C * (1 + p_i * p_i))
        else:
            F = 0
        return F

    def calculateZeroBlock(self, blocks, idx, x):
        self.appender(blocks, idx, 0, x, 0, 0, 0)
        return

    def calculateBlock(self, eta, blocks, idx, dx, gamma, f, C, mu, counterC, counterLamb):
        k, x, y = self.searchKXY(blocks, idx)
        if eta == 0.5:

            summYi = 0
            yi = 0
            p_i = - math.tan(math.radians(
                math.degrees(math.pi) / 4 - (math.degrees(math.atan(k)) + self.phi) / 2))

        else:
            prevP = blocks[idx - 1][4]
            p_i = self.calculateP_i(mu, eta, k, f, prevP, dx)
            yi, summYi = self.calculateYi(mu, k, f, p_i, prevP, blocks, idx, eta)
            if eta == 3 and blocks[idx - 1][8]==2:
                p_i = self.calculateFirstP(mu, f, k, y, summYi)


        F = self.calculateF(eta, dx, gamma, y, summYi, p_i, f, C)
        print(x, summYi, p_i, F, eta)
        self.appender(blocks, idx, p_i, x, summYi, F, eta)




        counterC += F
        counterLamb += dx * k - yi
        return counterC, counterLamb

    def ClambCalculate(self, Clamb):
        C = (Clamb[0])
        kLamb = (Clamb[1])

        phi, gamma, dx, listCoords, color = self.phi, self.gamma, self.dx, self.listCoords, self.color
        blocks = self.settingsSlope(dx, listCoords, color)
        f = math.tan(math.radians(phi))
        H90 = (2 * C / gamma) * math.tan(math.radians(math.degrees(math.pi) / 4 + phi / 2))
        omega = math.tan(math.radians(math.degrees(math.pi) / 4 + phi / 2))

        p, pi1 = symbols('p pi1')
        mu1, mu2, mu3 = kLamb * (C / gamma), kLamb * (C / gamma), C / gamma
        counterC, counterLamb = 0, 0

        for idx in range(0, len(blocks)):
            k, x, y = blocks[idx][1], blocks[idx][2], blocks[idx][3]
            if idx > 0:
                prevK, prevX, prevY, prevP, prevX1, prevY1, prevF, prevEta = self.prevVariable(blocks, idx)
                y1 = blocks[idx - 1][4] * dx + blocks[idx - 1][6]
            if k == 0 and y == 0:
                eta = 0
            elif y == 0 and k != 0:
                eta = 0.5
            else:
                if prevP < f:
                    eta = 1
                else:

                    p_i = self.calculateP_i(mu2, 2, k, f, prevP, dx)
                    yi, summYi = self.calculateYi(mu2, k, f, p_i, prevP, blocks, idx, 2)
                    F = self.calculateF(2, dx, gamma, y, summYi, p_i, f, C)

                    if prevF < F:
                        eta = 2
                    elif y1 + H90 < y:
                        yi, summYi = self.calculateYi(mu3, k, f, p_i, prevP, blocks, idx, 3)
                        F = self.calculateF(3, dx, gamma, y, summYi, p_i, f, C)
                        firstP = None
                        if prevEta == 2:
                            pass
                            # firstP = self.calculateFirstP(mu3, f, k, y, summYi)
                            # self.firstP = firstP
                        eta = 3
                    else:
                        if prevEta == 3:
                            self.lastP = prevP
                        eta = 4

            if eta == 0:
                self.calculateZeroBlock(blocks, idx, x)
            elif eta == 4:
                self.appender(blocks, idx, 1000, x, y, 1000, 4)
            else:
                if eta == 0.5 or eta == 1:
                    mu = mu1
                elif eta == 2:
                    mu = mu2
                elif eta == 3:
                    mu = mu3

                counterC, counterLamb = self.calculateBlock(eta, blocks, idx, dx, gamma, f, C, mu, counterC, counterLamb)


        counterLamb = counterLamb - H90
        self.blocks = blocks

        self.saveSlope(blocks, 'red')
        self.drawing()
        return counterC , counterLamb

    def ClambCalculateUnerror(self, Clamb):
        C = (Clamb[0])
        kLamb = (Clamb[1])
        try:
            if C>=6.3 or C<=5 or kLamb<=1.6 or kLamb>=1.5:
                phi, gamma, dx, listCoords, color = self.phi, self.gamma, self.dx, self.listCoords, self.color
                blocks = self.settingsSlope(dx, listCoords, color)
                f = math.tan(math.radians(phi))
                H90 = (2 * C / gamma) * math.tan(math.radians(math.degrees(math.pi) / 4 + phi / 2))
                omega = math.tan(math.radians(math.degrees(math.pi) / 4 + phi / 2))

                p, pi1 = symbols('p pi1')
                mu1, mu2, mu3 = kLamb * (C / gamma), kLamb * (C / gamma), C / gamma
                counterC, counterLamb = 0, 0

                for idx in range(0, len(blocks)):
                    k, x, y = blocks[idx][1], blocks[idx][2], blocks[idx][3]
                    if idx > 0:
                        prevK, prevX, prevY, prevP, prevX1, prevY1, prevF, prevEta = self.prevVariable(blocks, idx)
                        y1 = blocks[idx - 1][4] * dx + blocks[idx - 1][6]
                    if k == 0 and y == 0:
                        eta = 0
                    elif y == 0 and k != 0:
                        eta = 0.5
                    else:
                        if prevP < f:
                            eta = 1
                        else:

                            p_i = self.calculateP_i(mu2, 2, k, f, prevP, dx)
                            yi, summYi = self.calculateYi(mu2, k, f, p_i, prevP, blocks, idx, 2)
                            F = self.calculateF(2, dx, gamma, y, summYi, p_i, f, C)

                            if prevF < F:
                                eta = 2
                            elif y1 + H90 < y:
                                yi, summYi = self.calculateYi(mu3, k, f, p_i, prevP, blocks, idx, 3)
                                F = self.calculateF(3, dx, gamma, y, summYi, p_i, f, C)
                                firstP = None
                                if prevEta == 2:
                                    firstP = self.calculateFirstP(mu3, f, k, y, summYi)
                                    self.firstP = firstP
                                eta = 3
                            else:
                                if prevEta == 3:
                                    self.lastP = prevP
                                eta = 4

                    if eta == 0:
                        self.calculateZeroBlock(blocks, idx, x)
                    elif eta == 4:
                        self.appender(blocks, idx, 1000, x, y, 1000, 4)
                    else:
                        if eta == 0.5 or eta == 1:
                            mu = mu1
                        elif eta == 2:
                            mu = mu2
                        elif eta == 3:
                            mu = mu3


                        counterC, counterLamb = self.calculateBlock(eta, blocks, idx, dx, gamma, f, C, mu, counterC, counterLamb)

                counterLamb = counterLamb - H90
                self.blocks = blocks
            else:
                counterC, counterLamb = 1000, 1000
        except:
            counterC, counterLamb = 1000, 1000

        return counterC , counterLamb

    def setCK(self, C, K):
        self.C = C
        self.K = K

    def slopeCalculate(self, phi, gamma, dx, listCoords, color):
        self.phi, self.gamma, self.dx, self.listCoords, self.color = phi, gamma, dx, listCoords, color
        blocks = self.settingsSlope(dx, listCoords, color)

        C, K = 5.240734270891313, 1.518541292749629
        summF, summY = self.ClambCalculate([C, K])
        print(summF, summY)

a = SlopeCalc()
a.slopeCalculate(30,2.5,0.05,[[0,0],[20,0],[57.73503,100],[160,100]], "red")