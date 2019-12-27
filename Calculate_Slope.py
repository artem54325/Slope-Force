
import math
from inspect import currentframe
from dataclasses import dataclass

def tt(x):
    callingFrame = currentframe().f_back
    callingEnv = callingFrame.f_builtins.copy()
    callingEnv.update(callingFrame.f_globals)
    callingEnv.update(callingFrame.f_locals)
    possibleRoots = [item[0] for item in callingEnv.items() if item[1] == x]
    if not possibleRoots:
        root = '<unnamed>'
    else:
        if len(possibleRoots) == 1:
            root = str(possibleRoots[0])
        else:
            root = '\n | '
            for possibleRoot in possibleRoots[:-1]:
                root += str(possibleRoot) + ', '
            root += 'or ' + str(possibleRoots[-1])
    print(root + ' = ' + str(x))


@dataclass
class slope_info():
    number: int
    x: float
    y1: float
    p: float
    F: float
    eta: int
    y: float
    k: float
    type: str



class Calculate_Slope:
    """docstring for Calculate_Slope"""
    def __init__(self, slope_surface, slope_parameters):
        self.slope_surface = slope_surface
        self.slope_parameters = slope_parameters

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
    def eta1Diff(k, f, p):
        return (2*f*f - 2*f*p)*(-f*k + p*p*(f*k - 1) + p*(2*f + 2*k) + 1)/(f*f*k - 2*f*f*p + f*p*p - f + k)**2 + (2*f + 2*k + 2*p*(f*k - 1))/(f*f*k - 2*f*f*p + f*p*p - f + k)
    @staticmethod
    def eta2Diff(k, f, p):
        return 4*p*(p*p + 1)*(f*k + 1)/((f**2 + 1)*(2*f*k*p - f + k + 2*p*p*p - p*p*(3*f + k))) + (p*p + 1)**2*(f*k + 1)*(-2*f*k - 6*p*p + 2*p*(3*f + k))/((f*f + 1)*(2*f*k*p - f + k + 2*p**3 - p**2*(3*f + k))**2)
    @staticmethod
    def eta3Diff(k, f, p):
        return (2*k - 2*p)/(-f + k)

    def search_first_point(self, slope_surface, phi):
        first_step = 0
        for id in range(0, len(slope_surface)):
            if slope_surface[id][3] == 0:
                first_step += 1
            else:
                break
        slope_surface_dx = [slope_surface[first_step][0],slope_surface[first_step][1], slope_surface[first_step][2], slope_surface[first_step][3]]
        sliding_surface_dx = [slope_surface[first_step][0],slope_surface[first_step][1], slope_surface[first_step][2], - math.tan(math.radians(math.degrees(math.pi) / 4 - (math.degrees(math.atan(slope_surface[first_step][3])) + phi) / 2)), 0, 0,0,slope_surface[first_step][1], slope_surface[first_step][2]]
        return [slope_surface_dx, sliding_surface_dx] # надо оптимизировать приравнивание

    def get_prev_agruments(self, slope_surface_dx, sliding_surface_dx, idx):
        x_prev, y_prev, k_prev = slope_surface_dx[idx - 1][1], slope_surface_dx[idx - 1][2], slope_surface_dx[idx - 1][3]
        x1_prev, y1_prev, p_prev, F_prev, eta_prev = sliding_surface_dx[idx - 1][1], sliding_surface_dx[idx - 1][2], sliding_surface_dx[idx - 1][3], sliding_surface_dx[idx - 1][4],  sliding_surface_dx[idx - 1][5]
        return x_prev, y_prev, k_prev, x1_prev, y1_prev, p_prev, F_prev, eta_prev

    def create_zone_list(self, list):
        list_out = []
        for idx in range(0, len(list)):
            list_out.append(list[idx][1])
        return list_out

    def calculate_p(self, eta, p, f, k, mu, dx):
        fun = {1: self.eta1Diff(k, f, p), 2: self.eta2Diff(k, f, p), 3: self.eta3Diff(k, f, p), 0: self.eta1Diff(k, f, p)}
        p_new = (dx * k - dx * p + fun[eta] * mu * p) / (fun[eta] * mu)
        return p_new

    def calculate_y1(self, eta, p, f, k, mu, p_prev, y1_prev):
        fun = {1: self.eta1Diff(k, f, p), 2: self.eta2Diff(k, f, p), 3: self.eta3Diff(k, f, p), 0: self.eta1Diff(k, f, p)}
        y_delta = mu * fun[eta] / (k - p) * p * (p - p_prev)
        y1 = y1_prev + y_delta
        return y1

    def calculate_first_p3(self, mu, f, y, y1, k):
        first_p = -((f - k) * ((2 * k * mu) / (f - k) - (2 * math.sqrt(
            -f * mu * y1 + f * mu * y + k * k * mu ** 2 + k * mu * y1 - k * mu * y + mu * mu)) / math.sqrt(
            f * f - 2 * f * k + k * k))) / (2 * mu)
        return first_p

    def calculate_F(self, eta, p, f, y, y1, C, gamma, dx):
        if eta == 1:
            F = dx * (gamma * (y - y1) * (p - f) - C * (1 + p * p)) / (1 + f * p)
        elif eta == 2:
            F = dx * (gamma * (y - y1) * (p - f) - C * (1 + p * p)) / (1 + p * p)
        elif eta == 3:
            F = dx * (gamma * (y - y1) * (p - f) - C * (1 + p * p))
        else:
            F = 0
        return F

    def caclulate_slope(self, C, K):
        rounding = 8
        slope_surface, slope_parameters = self.slope_surface, self.slope_parameters

        # задаем константы
        phi, gamma, dx = self.slope_parameters.get('phi'), slope_parameters.get('gamma'), slope_parameters.get('dx')
        f = math.tan(math.radians(phi))
        omega = math.tan(math.radians(math.degrees(math.pi) / 4 + phi / 2))
        mu = K*C/gamma
        if mu<1:
            n = mu/0
            n.append(phi) #ошибка для выхода из решения

        counter_zone, counter_F, counter_y1, counter_y = 0,0,0,0

        all_surface_list = self.search_first_point(slope_surface,phi)
        sliding_surface_dx, slope_surface_dx = [all_surface_list[1]], [all_surface_list[0]]

        try:
            for idx in range(1,(int((slope_surface[-1][1]-slope_surface[0][1])/dx))*2+2200): # начинается цикл с 2*количество умещающихся dx
                x_prev, y_prev, k_prev, x1_prev, y1_prev, p_prev, F_prev, eta_prev = self.get_prev_agruments(slope_surface_dx,sliding_surface_dx, idx)
                N = slope_surface_dx[counter_zone][0]
                y_real = 0
                # Провека на последнюю зону
                for i in range(0,len(slope_surface)-1):
                    if round(x_prev+dx,rounding) >= slope_surface[i][1] and round(x_prev+dx,rounding) < slope_surface[i+1][1]:
                        k = slope_surface[i][3]
                        dx_real = dx
                        break
                    else:
                        k = slope_surface[-1][3]
                        y_real = slope_surface[-1][2]
                        dx_real = dx
                        N=1

                # предрасчет для определения характеристик y1, y, p, F
                x = round(x_prev + dx_real, rounding)
                y = round(y_prev + dx_real * k, rounding-4)
                if y_real>0:
                    y = y_real
                # проверка условий
                mu_real = mu
                if p_prev < f:
                    eta = 1
                    p = self.calculate_p(1, p_prev, f, k, mu, dx_real)
                    y1 = self.calculate_y1(1, p, f, k, mu, p_prev, y1_**prev)
                    F = self.calculate_F(1, p, f, y, y1, C, gamma, dx_real)
                else:

                    p = self.calculate_p(2, p_prev, f, k, mu, dx_real)
                    y1 = self.calculate_y1(2, p, f, k, mu, p_prev, y1_prev)
                    F = self.calculate_F(2, p, f, y, y1, C, gamma, dx_real)
                    h90 = C/gamma*((1+p*p)/(p-f))
                    if F >= F_prev:
                        eta = 2
                    elif y1 + h90 < y:
                        eta = 3
                        mu_real = C / gamma

                        p = self.calculate_p(3, p_prev, f, k, mu_real, dx_real)
                        y1 = self.calculate_y1(3, p, f, k, mu_real, p_prev, y1_prev)
                        if eta == 3 and eta_prev == 2:
                            p = self.calculate_first_p3(mu_real, f, y, y1, k)
                        F = self.calculate_F(3, p, f, y, y1, C, gamma, dx_real)
                    else:
                        counter_y1 += h90
                        break

                slope_surface_dx.append([N, x, y, k])
                sliding_surface_dx.append([N, x, y1, p, F, eta, y, k])

                counter_F+=F
                counter_y+=y-y_prev
                counter_y1+=y1-y1_prev

                if x>160 and x<180:
                    print("i={} N={} k={:.0f} x={:.2f} y1={:.3f} p={:.3f} F={:.3f} e={} y={}".format(idx, N, k, x, y1, p, F, eta, y))

        except Exception as e:
            # print(e)
            # print('Error:\n', traceback.format_exc())
            pass

        return counter_y-counter_y1, counter_F, sliding_surface_dx

    def caclulate_class_slope(self, C, K):
        rounding = 8
        slope_surface, slope_parameters = self.slope_surface, self.slope_parameters

        # задаем константы
        phi, gamma, dx = self.slope_parameters.get('phi'), slope_parameters.get('gamma'), slope_parameters.get('dx')
        f = math.tan(math.radians(phi))
        omega = math.tan(math.radians(math.degrees(math.pi) / 4 + phi / 2))
        mu = K*C/gamma
        if mu<1:
            n = mu/0
            n.append(phi) #ошибка для выхода из решения

        counter_zone, counter_F, counter_y1, counter_y = 0,0,0,0

        all_surface_list = self.search_first_point(slope_surface,phi)
        sliding_surface_dx, slope_surface_dx = [all_surface_list[1]], [all_surface_list[0]]

        try:
            for idx in range(1,(int((slope_surface[-1][1]-slope_surface[0][1])/dx))*2+2200): # начинается цикл с 2*количество умещающихся dx
                x_prev, y_prev, k_prev, x1_prev, y1_prev, p_prev, F_prev, eta_prev = self.get_prev_agruments(slope_surface_dx,sliding_surface_dx, idx)
                N = slope_surface_dx[counter_zone][0]
                y_real = 0
                # Провека на последнюю зону
                for i in range(0,len(slope_surface)-1):
                    if round(x_prev+dx,rounding) >= slope_surface[i][1] and round(x_prev+dx,rounding) < slope_surface[i+1][1]:
                        k = slope_surface[i][3]
                        dx_real = dx
                        break
                    else:
                        k = slope_surface[-1][3]
                        y_real = slope_surface[-1][2]
                        dx_real = dx
                        N=1

                # предрасчет для определения характеристик y1, y, p, F
                x = round(x_prev + dx_real, rounding)
                y = round(y_prev + dx_real * k, rounding-4)
                if y_real>0:
                    y = y_real
                # проверка условий
                mu_real = mu
                if p_prev < f:
                    eta = 1
                    p = self.calculate_p(1, p_prev, f, k, mu, dx_real)
                    y1 = self.calculate_y1(1, p, f, k, mu, p_prev, y1_prev)
                    F = self.calculate_F(1, p, f, y, y1, C, gamma, dx_real)
                else:

                    p = self.calculate_p(2, p_prev, f, k, mu, dx_real)
                    y1 = self.calculate_y1(2, p, f, k, mu, p_prev, y1_prev)
                    F = self.calculate_F(2, p, f, y, y1, C, gamma, dx_real)
                    h90 = C/gamma*((1+p*p)/(p-f))
                    if F >= F_prev:
                        eta = 2
                    elif y1 + h90 < y:
                        eta = 3
                        mu_real = C / gamma

                        p = self.calculate_p(3, p_prev, f, k, mu_real, dx_real)
                        y1 = self.calculate_y1(3, p, f, k, mu_real, p_prev, y1_prev)
                        if eta == 3 and eta_prev == 2:
                            p = self.calculate_first_p3(mu_real, f, y, y1, k)
                        F = self.calculate_F(3, p, f, y, y1, C, gamma, dx_real)
                    else:
                        counter_y1 += h90
                        break

                slope_surface_dx.append([N, x, y, k])
                sliding_surface_dx.append([N, x, y1, p, F, eta, y, k])

                counter_F+=F
                counter_y+=y-y_prev
                counter_y1+=y1-y1_prev

                if x>160 and x<180:
                    print("i={} N={} k={:.0f} x={:.2f} y1={:.3f} p={:.3f} F={:.3f} e={} y={}".format(idx, N, k, x, y1, p, F, eta, y))

        except Exception as e:
            # print(e)
            # print('Error:\n', traceback.format_exc())
            pass

        return counter_y-counter_y1, counter_F, sliding_surface_dx


        