import plotly
import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv("45basa_alt.csv")

markercolor = data['cY']

figure = go.Scatter3d(x=data['C'], y=data['K'], z=data['cF'],
                      marker=dict(opacity=1,
                                  color=markercolor,
                                  reversescale=True,
                                  colorscale='darkmint',
                                  size=5),
                      line=dict(width=0.02),
                      mode='markers')

layer = go.Layout(scene=dict(xaxis=dict( title="C"),
                             yaxis=dict( title="K"),
                             zaxis=dict( title="cF")))

plotly.offline.plot({"data": [figure],
                     "layout": layer},
                     auto_open=True,
                     filename=("3DPlot.html"))



