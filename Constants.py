from sympy import integrate, nsolve, symbols

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
