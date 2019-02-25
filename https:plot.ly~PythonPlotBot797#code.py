# Get this figure: fig = py.get_figure("https://plot.ly/~PythonPlotBot/797/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~PythonPlotBot/797/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="text-hover-bar", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~PythonPlotBot/797/").get_data()[0]["y"]

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
  "x": ["Product A", "Product B", "Product C"], 
  "y": [20, 14, 23], 
  "marker": {
    "color": "rgb(158,202,225)", 
    "line": {
      "color": "rgb(8,48,107)", 
      "width": 1.5
    }
  }, 
  "opacity": 0.6, 
  "text": ["27% market share", "24% market share", "19% market share"], 
  "type": "bar"
}
data = Data([trace1])
layout = {"title": "January 2013 Sales Report"}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)