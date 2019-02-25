# Get this figure: fig = py.get_figure("https://plot.ly/~PlotBot/88/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~PlotBot/88/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="mpl-basic-histogram", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~PlotBot/88/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": [-2.76433596732, -2.16625927713, -1.56818258695, -0.970105896766, -0.372029206582, 0.226047483601, 0.824124173785, 1.42220086397, 2.02027755415, 2.61835424434], 
  "y": [7.0, 30.0, 66.0, 150.0, 213.0, 230.0, 159.0, 103.0, 28.0, 14.0], 
  "marker": {
    "color": "#0000FF", 
    "line": {"width": 1.0}
  }, 
  "opacity": 1, 
  "orientation": "v", 
  "type": "bar", 
  "xaxis": "x1", 
  "yaxis": "y1"
}
data = Data([trace1])
layout = {
  "autosize": False, 
  "bargap": -4.4408920985e-16, 
  "height": 500, 
  "hovermode": "closest", 
  "margin": {
    "r": 50, 
    "t": 90, 
    "b": 65, 
    "l": 65
  }, 
  "showlegend": False, 
  "title": "Gaussian Histogram", 
  "titlefont": {
    "color": "#000000", 
    "size": 14.4
  }, 
  "width": 500, 
  "xaxis1": {
    "anchor": "y1", 
    "domain": [0.0, 1.0], 
    "mirror": "ticks", 
    "nticks": 8, 
    "range": [-4.0, 3.0], 
    "showgrid": False, 
    "showline": True, 
    "side": "bottom", 
    "tickfont": {"size": 12.0}, 
    "ticks": "inside", 
    "title": "Value", 
    "titlefont": {
      "color": "#000000", 
      "size": 12.0
    }, 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis1": {
    "anchor": "x1", 
    "domain": [0.0, 1.0], 
    "mirror": "ticks", 
    "nticks": 6, 
    "range": [0.0, 250.0], 
    "showgrid": False, 
    "showline": True, 
    "side": "left", 
    "tickfont": {"size": 12.0}, 
    "ticks": "inside", 
    "title": "Frequency", 
    "titlefont": {
      "color": "#000000", 
      "size": 12.0
    }, 
    "type": "linear", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)