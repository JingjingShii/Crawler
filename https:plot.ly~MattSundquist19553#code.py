# Get this figure: fig = py.get_figure("https://plot.ly/~MattSundquist/19553/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~MattSundquist/19553/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="numpy-bins", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~MattSundquist/19553/").get_data()[0]["y"]

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
  "x": [0.5, 1.5, 2.5], 
  "y": [0.0, 2.0, 1.0], 
  "marker": {
    "color": "#0000FF", 
    "line": {"width": 1}
  }, 
  "name": "y", 
  "opacity": 1, 
  "orientation": "v", 
  "type": "bar", 
  "uid": "2051c5", 
  "xaxis": "x", 
  "yaxis": "y"
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "bargap": 0, 
  "height": 522, 
  "hovermode": "closest", 
  "showlegend": False, 
  "width": 762, 
  "xaxis": {
    "anchor": "y", 
    "autorange": True, 
    "domain": [0, 1], 
    "mirror": "ticks", 
    "nticks": 5, 
    "range": [0, 3], 
    "showgrid": False, 
    "showline": True, 
    "side": "bottom", 
    "tickfont": {"size": 12}, 
    "ticks": "inside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis": {
    "anchor": "x", 
    "autorange": True, 
    "domain": [0, 1], 
    "mirror": "ticks", 
    "nticks": 5, 
    "range": [0, 2.10526315789], 
    "showgrid": False, 
    "showline": True, 
    "side": "left", 
    "tickfont": {"size": 12}, 
    "ticks": "inside", 
    "type": "linear", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)