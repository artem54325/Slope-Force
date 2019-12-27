from Loading_data import Loading_data
from Calculate_Slope import Calculate_Slope
import math
import pandas as pd
import plotly
import plotly.graph_objects as go

class Argument_search:
    """docstring for Calculate_Slope"""
    def __init__(self, type, args):
        if type == 'manual':
            [alpha, H, phi, gamma, dx, color] = args
            slope_surface = [[0, 20, 0, round(math.tan(math.radians(alpha)),8)],[1, 20 + H * (math.tan(math.radians(alpha)))**-1, H, 0],[2, 20 + 0.5 * H + H * (math.tan(math.radians(alpha)))**-1, H, 0]]
            slope_parameters = {'phi': phi, 'gamma': gamma, 'dx': dx, 'color': color}
            self.slope = Calculate_Slope(slope_surface, slope_parameters)
            self.parameters = slope_parameters
        elif type == "auto":
            [way1, way2, way3] = args
            import_txt = Loading_data(way1, way2, way3)
            self.slope = Calculate_Slope(import_txt.get_slope_surface(), import_txt.get_slope_parameters())
            self.parameters = import_txt.get_slope_parameters()

    def best_in_dict(self,dict):
        list_keys = list(dict.keys())
        list_keys.sort()
        return dict[list_keys[0]]

    def draw_slope(self, C, K):
        cY, cF, result_surface = self.slope.caclulate_class_slope(C, K)
        print("Невязка",cY, cF)
        x_line = [x[1] for x in result_surface]
        y1_line = [y[2] for y in result_surface]
        y_line = [y[6] for y in result_surface]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_line, y=y1_line,
                                 mode='lines',
                                 name='Поверхность скольжения'))
        fig.add_trace(go.Scatter(x=x_line, y=y_line,
                                 mode='lines',
                                 name='Поверхность откоса'))
        fig.update_xaxes(showgrid=False, zeroline=False, dtick=5, range=[10,190])
        fig.update_yaxes(showgrid=False, zeroline=False, dtick=5, range=[-10,110])
        # fig.update_xaxes(showgrid=False, zeroline=False, dtick=5, range=[max(x_line)*-0.01, max(x_line)+max(x_line)*0.01])
        # fig.update_yaxes(showgrid=False, zeroline=False, dtick=5, range=[max(y_line)*-0.01, max(y_line)+max(y_line)*0.01])
        fig.show()

    def save_txt_coords(self, name, result_surface):
        x_line = [x[1] for x in result_surface]
        y1_line = [y[2] for y in result_surface]
        file = open('points({}).txt'.format(name), "w")
        for idx in range(0, len(x_line)):
            print(idx, x_line[idx], y1_line[idx], sep=' ', file=file)
        file.close()

    def search_best_K(self, C):
        minK, maxK, razrK = 0.19, 1.83, 100
        best_cYF = {}
        for idx in range(int(minK*razrK),int(maxK*razrK)):

            try:
                K = idx / (razrK)
                cY, cF, result_surface = self.slope.caclulate_slope(C, K)
                if abs(cY<1) and abs(cF)<50:
                    best_cYF[abs(cF)] = [C, K, cY, cF, result_surface]
            except:
                pass
        try:
            best_result = self.best_in_dict(best_cYF)
            print("Лучший найденный К",best_result[1], '({:.3f}{:.3f})'.format(best_result[2],best_result[3]))
            self.draw_slope(best_result[0],best_result[1])
            self.save_txt_coords('phi={},K={},C={}'.format(self.parameters['phi'],best_result[1],round(C,2)), best_result[4])
        except:
            print("Не могу найти решение")

    def create_matrix_CK(self):
        matrix = []

        list_C, list_K, list_cY, list_cF = [], [], [], []
        minC, maxC, razrC = 5.21, 5.22, 100
        minK, maxK, razrK = 0.19, 1.83, 1000
        for i in range(int(minC * razrC), int(maxC * razrC)):
            matrix.append([])
            C = i / razrC
            for x in range(int(minK * razrK), int(maxK * razrK)):
                try:
                    K = x / (razrK)
                    cY, cF, new_K, result_surface = self.slope.caclulate_slope(C, K)
                    matrix[i-int(minC*razrC)].append([C,K,cY,cF, new_K])
                    list_C.append(C), list_K.append(K), list_cY.append(cY), list_cF.append(cF)
                except:
                    pass
                    list_C.append(C), list_K.append(K), list_cY.append("-"), list_cF.append("-")
                    matrix[i-int(minC*razrC)].append([C,K,'cY','cF', 'new_K'])

        file = pd.DataFrame({'C': list_C, 'K': list_K, 'cY': list_cY, 'cF': list_cF})  # собираем фрейм
        file.to_csv('my_csv_export.csv', encoding='utf-8', index=False) #экспортируем в файл
