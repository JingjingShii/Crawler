# Get this figure: fig = py.get_figure("https://plot.ly/~swader/12/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~swader/12/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="PHP Framework Popularity at Work - SitePoint, 2015", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~swader/12/").get_data()[0]["y"]

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
  "x": [1659, 1067, 671, 597, 504, 418, 407, 390, 378, 274, 255, 243, 203, 169, 79, 65, 42, 35, 35, 25, 17, 11, 10], 
  "y": ["Laravel", "Symfony2", "Nette", "CodeIgniter", "Yii 2", "PHPixie", "Yii 1", "Zend Framework 2", "Company Internal Framework", "Zend Framework 1", "CakePHP", "No Framework", "We use a CMS for everything", "Phalcon", "Slim", "Silex", "Simple MVC Framework", "Typo 3", "Kohana", "FuelPHP", "TYPO3 Flow", "Drupal", "Aura"], 
  "name": "Votes", 
  "opacity": 1, 
  "orientation": "h", 
  "showlegend": True, 
  "type": "bar", 
  "uid": "2f399e", 
  "visible": True
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "barmode": "group", 
  "barnorm": "", 
  "height": 742, 
  "margin": {
    "l": 210, 
    "pad": 4
  }, 
  "showlegend": False, 
  "title": "PHP Framework Popularity at Work - SitePoint, 2015", 
  "width": 1151, 
  "xaxis": {
    "autorange": False, 
    "range": [-198.256295918, 1830.67318691], 
    "title": "Votes", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": False, 
    "range": [-3.30157535143, 23.4206122313], 
    "title": "Framework", 
    "type": "category"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)