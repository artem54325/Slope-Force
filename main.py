import time
from Argument_search import Argument_search
from Search_Constant_Test import Search_Constant_Test
import pandas as pd


start_time = time.time()

    # home
way = r"D:\yandex disk\YandexDisk\Python\project_slope (at work)"
    # work
# way = r"E:\yandex disk\YandexDisk\Python\project_slope (at work)"

way_surface = r"\slope_surface 45.txt"
way_parameters = r"\slope_parameters 35.txt"

galocka = 1
type_args = 1


H, alpha, gamma, dx, phi = 100, 45, 2.5, 0.05, 35
C = 4

if galocka==1:
    if type_args == 1:
        slope = Argument_search('manual', [alpha, H, phi, gamma, dx, 'red'])
    else:
        slope = Argument_search('auto', [way, way_surface, way_parameters])
    K = 1.5
    slope.draw_slope(C, K)
else:
    if type_args == 1:
        slope = Argument_search('manual', [alpha, H, phi, gamma, dx, 'red'])
    else:
        slope = Argument_search('auto', [way, way_surface, way_parameters])
    K_accuracy = 100
    slope.search_best_K(C, K_accuracy)  # K=1.518541292749629





# test = Search_Constant_Test(alpha, phi, gamma, H)
# C = test.getC()
# slope = Argument_search('auto', [way, way_surface, way_parameters])




# for phi in range(30,35,5):
H, alpha, gamma = 100, 35, 2.5
# test = Search_Constant_Test(alpha, phi, gamma, H)
# C = test.getC()
lamb = test.getlamba()
# print("Входные данные",alpha,phi, C, gamma*lamb/C)
# slope = Argument_search('auto', [way, way_surface, way_parameters])
slope = Argument_search('manual', [alpha, H, phi, gamma, 0.05, 'red'])
slope.search_best_K(C)

print((time.time() - start_time), 'sec')



#   0   1   2   3   4   5
#   N   x   y   p   F   eta
#   N   x   y   k
