# Get this figure: fig = py.get_figure("https://plot.ly/~PythonPlotBot/27/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~PythonPlotBot/27/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="basic-line", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~PythonPlotBot/27/").get_data()[0]["y"]

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
  "x": [1, 2, 3, 4], 
  "y": [10, 15, 13, 17], 
  "type": "scatter", 
  "uid": "9dd707fc-3d68-4e2e-9c66-f1eb0f4ef62c"
}
trace2 = {
  "x": [1, 2, 3, 4], 
  "y": [16, 5, 11, 9], 
  "type": "scatter", 
  "uid": "b5df80d6-db3b-44cf-aecd-3ad0f1d79890"
}
data = Data([trace1, trace2])
fig = Figure(data=data)
plot_url = py.plot(fig)