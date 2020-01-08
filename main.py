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


alpha, phi, gamma, H = 45, 35, 2.5, 100
test = Search_Constant_Test(alpha, phi, gamma, H)
C = test.getC()
print("C = " + str(C))
lamb = test.getlamba()
print(alpha, phi, C, gamma*lamb/C)
slope = Argument_search('manual', [alpha, H, phi, gamma, 0.1, 'red'])
# slope = Argument_search('auto', [way, way_surface, way_parameters])
slope.draw_slope(C, gamma*lamb/C)


# slope = Argument_search('manual', [45, 100, 25, 2.5, 0.05, 'red'])
# slope.draw_slope(13.494222291666834, 1.4769256814848488)

# slope = Argument_search('manual', [45, 100, 35, 2.5, 0.05, 'red'])
# slope.draw_slope(5.240734270891313, 1.518541292749629)

# for phi in range(30,35,5):
#     H, alpha, gamma = 100, 35, 2.5
#     test = Search_Constant_Test(alpha, phi, gamma, H)
#     C = test.getC()
#     lamb = test.getlamba()
#     print("Входные данные",alpha,phi, C, gamma*lamb/C)
#     # slope = Argument_search('auto', [way, way_surface, way_parameters])
#     slope = Argument_search('manual', [alpha, H, phi, gamma, 0.05, 'red'])
#     slope.search_best_K(C) # K=1.518541292749629

print((time.time() - start_time), 'sec')



#   0   1   2   3   4   5
#   N   x   y   p   F   eta
#   N   x   y   k
