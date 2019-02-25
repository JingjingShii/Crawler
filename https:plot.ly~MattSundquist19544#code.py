# Get this figure: fig = py.get_figure("https://plot.ly/~MattSundquist/19544/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~MattSundquist/19544/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="mpl-histogram", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~MattSundquist/19544/").get_data()[0]["y"]

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
  "x": [78.3175952985, 98.091227643, 117.864859987, 137.638492332, 157.412124676, 177.185757021, 196.959389365, 216.73302171, 236.506654054, 256.280286399], 
  "y": [0.0, 0.0, 0.0, 33.0, 84.0, 250.0, 304.0, 221.0, 85.0, 23.0], 
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
trace2 = {
  "x": [86.2270482363, 106.000680581, 125.774312925, 145.54794527, 165.321577614, 185.095209959, 204.868842303, 224.642474647, 244.416106992, 264.189739336], 
  "y": [9.0, 51.0, 177.0, 283.0, 264.0, 162.0, 47.0, 6.0, 1.0, 0.0], 
  "marker": {
    "color": "#007F00", 
    "line": {"width": 1.0}
  }, 
  "opacity": 1, 
  "orientation": "v", 
  "type": "bar", 
  "xaxis": "x1", 
  "yaxis": "y1"
}
data = Data([trace1, trace2])
layout = {
  "bargap": 11.8641794067, 
  "hovermode": "closest", 
  "showlegend": False, 
  "xaxis1": {
    "anchor": "y1", 
    "domain": [0.0, 1.0], 
    "mirror": "ticks", 
    "nticks": 6, 
    "range": [50.0, 300.0], 
    "showgrid": False, 
    "showline": True, 
    "side": "bottom", 
    "tickfont": {"size": 12.0}, 
    "ticks": "inside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis1": {
    "anchor": "x1", 
    "domain": [0.0, 1.0], 
    "mirror": "ticks", 
    "nticks": 8, 
    "range": [0.0, 350.0], 
    "showgrid": False, 
    "showline": True, 
    "side": "left", 
    "tickfont": {"size": 12.0}, 
    "ticks": "inside", 
    "type": "linear", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)