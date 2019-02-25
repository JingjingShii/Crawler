# Get this figure: fig = py.get_figure("https://plot.ly/~swader/21/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~swader/21/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="PHP Framework Popularity in Personal Projects - SitePoint, 2015", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~swader/21/").get_data()[0]["y"]

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
  "x": [2112, 1005, 703, 620, 482, 420, 346, 306, 293, 231, 229, 176, 158, 142, 79, 65, 53, 27, 22, 20, 16, 14], 
  "y": ["Laravel", "Symfony2", "Nette", "Yii 2", "CodeIgniter", "PHPixie", "Zend Framework 2", "No Framework", "Yii 1", "Phalcon", "CakePHP", "I use a CMS for all my work", "Slim", "Silex", "Zend Framework 1", "Company Internal Framework", "Simple MVC Framework", "FuelPHP", "Kohana", "Typo 3", "TYPO3 Flow", "We use a CMS for everything"], 
  "name": "Votes", 
  "orientation": "h", 
  "type": "bar", 
  "uid": "bf3ef1"
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "height": 702, 
  "margin": {
    "l": 210, 
    "pad": 4
  }, 
  "showlegend": False, 
  "title": "PHP Framework Popularity in Personal Projects - SitePoint, 2015", 
  "width": 1150, 
  "xaxis": {
    "autorange": True, 
    "range": [0, 2223.15789474], 
    "title": "Votes", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-0.5, 21.5], 
    "title": "Framework", 
    "type": "category"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)