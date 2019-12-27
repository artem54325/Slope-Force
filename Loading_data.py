class Loading_data():
    """Загрузка данных из txt"""
    def __init__(self, way, name_surface=r"\slope_surface.txt", name_parameter=r"\slope_parameters.txt"):
        self.way = way
        self.slope_surface = self.upload_txt_file_with_coordinates(name_surface)
        self.slope_parameters = self.upload_txt_file_with_parameters(name_parameter)


    def get_slope_surface(self):
        print('Загружены координаты поверхности откоса ({})'.format(self.slope_surface))
        return self.slope_surface

    def get_slope_parameters(self):
        print('Загружены параметры откоса ({})'.format(self.slope_parameters))
        return self.slope_parameters

    def upload_txt_file_with_coordinates(self, name):
        slope_surface = []
        with open(self.way + name) as surface:
            coordinates_data = surface.readlines()
            for id, line in enumerate(coordinates_data):
                coordinate = line.replace('\n','')
                coordinate = coordinate.split('\t')
                for idx in range(0,len(coordinate)):
                    coordinate[idx] = float(coordinate[idx])
                coordinate = [id]+coordinate
                slope_surface.append(coordinate)
        for idx in range(0,len(slope_surface)):
            if idx<len(slope_surface)-1:
                dx, dy = slope_surface[idx+1][1] - slope_surface[idx][1], slope_surface[idx+1][2] - slope_surface[idx][2]
                if dx  == 0 or dy == 0:
                    k = 0
                else:
                    k = round(dy/dx,8)
            else:
                k = 0
            slope_surface[idx].append(k)
        return slope_surface

    def upload_txt_file_with_parameters(self, name):
        slope_parameters = {}
        with open(self.way + name) as parameters:
            parameters_data = parameters.readlines()
            for line in parameters_data:
                parameter = line.replace(' ','').replace('\n','')
                parameter = parameter.split('=')
                try:
                    parameter[1] = float(parameter[1])
                except:
                    pass
                slope_parameters[parameter[0]]=parameter[1]
        return slope_parameters

        