# Get this figure: fig = py.get_figure("https://plot.ly/~RPlotBot/1145/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~RPlotBot/1145/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="plot from API (59)", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~RPlotBot/1145/").get_data()[0]["y"]

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
  "x": [2.1, 1.36, 1.52, 1.5, 0.9, 0.7, 0.96, 0.5, 0.71, 2, 0.33, 0.5, 0.36, 1.5, 0.9, 1.07, 0.9, 1.01, 2.03, 0.72, 0.41, 0.43, 0.9, 1.01, 0.92, 0.5, 1.04, 0.9, 0.91, 0.67, 2.01, 1.01, 0.9, 0.7, 0.91, 1, 0.7, 1, 0.85, 1.47], 
  "y": [15827, 4158, 7186, 7098, 3105, 2339, 4849, 1332, 2368, 11600, 922, 1280, 810, 4704, 4229, 4496, 3288, 6041, 6002, 2306, 1089, 1107, 2930, 4181, 3033, 701, 5633, 3992, 4107, 1642, 15888, 5950, 3276, 1697, 2854, 3136, 1840, 10752, 2493, 6108], 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }, 
    "opacity": 1, 
    "size": 4, 
    "sizemode": "area", 
    "sizeref": 1, 
    "symbol": "circle"
  }, 
  "mode": "markers", 
  "showlegend": False, 
  "text": ["Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: SI2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS1", "Clarity: VS1", "Clarity: SI2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS2", "Clarity: I1", "Clarity: VS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: SI1", "Clarity: VS2", "Clarity: I1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI2"], 
  "type": "scatter", 
  "uid": "71e1ea", 
  "xaxis": "x", 
  "yaxis": "y2"
}
trace2 = {
  "x": [1.51, 0.4, 0.9, 1.5, 0.51, 1.31, 0.25, 0.9, 1.4, 0.7, 0.32, 1.01, 0.99, 0.4, 0.5, 0.73, 0.72, 1.51, 0.9, 1.48, 1.52, 0.9, 0.3, 0.3, 0.32, 0.8, 0.7, 1.01, 1.51, 0.43, 1.51, 0.42, 2, 0.51, 0.51, 1.5, 0.5, 1.01, 1.08, 1.41, 1.19, 1.51, 0.3, 1.12, 0.78, 0.71, 0.51, 0.59, 1, 0.3, 0.43, 1, 0.53, 0.52, 1, 1.01, 0.7, 0.69, 0.53, 0.31, 0.7, 1.01, 1.5, 0.73, 0.3, 1.1, 1.51, 0.7, 0.71, 0.78, 0.9, 0.73, 1.7, 0.24, 1.72, 1.04, 1, 1.22, 0.35, 0.71, 0.42, 0.9, 0.38, 1.51, 0.31, 0.91, 1.01, 3, 1.21, 0.9, 1.08, 1.27, 0.55, 0.5, 1.6, 0.7, 0.78, 0.72], 
  "y": [10696, 798, 4093, 10256, 1060, 4864, 558, 2974, 11519, 2382, 801, 6407, 4052, 807, 1917, 3471, 3140, 11640, 3992, 15164, 6982, 3470, 684, 638, 603, 2363, 1935, 3897, 9069, 739, 7208, 653, 9193, 1220, 1895, 8316, 1333, 5756, 5927, 7738, 5825, 11560, 421, 3880, 2430, 1816, 1875, 1294, 4312, 684, 976, 6389, 1363, 1605, 5864, 4692, 2150, 1846, 1224, 744, 2699, 4355, 8580, 2821, 515, 4312, 9833, 2633, 2494, 2035, 2822, 1210, 8146, 492, 10084, 4191, 3991, 6713, 721, 2599, 722, 2143, 713, 7476, 408, 2813, 4129, 10863, 5787, 3465, 5821, 5588, 1715, 1966, 12467, 1840, 3163, 2795], 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }, 
    "opacity": 1, 
    "size": 4, 
    "sizemode": "area", 
    "sizeref": 1, 
    "symbol": "circle"
  }, 
  "mode": "markers", 
  "showlegend": False, 
  "text": ["Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: VS1", "Clarity: SI2", "Clarity: VS1", "Clarity: VVS2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: IF", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VVS1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: I1", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: I1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS1", "Clarity: I1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1"], 
  "type": "scatter", 
  "uid": "0695ed", 
  "xaxis": "x2", 
  "yaxis": "y2"
}
trace3 = {
  "x": [1.01, 0.3, 1.56, 1.16, 1.7, 0.4, 1.47, 0.3, 0.37, 0.55, 0.3, 1.09, 1.09, 1.02, 0.56, 0.74, 1.73, 0.26, 0.43, 1, 1.36, 0.33, 0.73, 0.5, 0.74, 0.39, 0.81, 0.75, 0.41, 0.8, 0.9, 0.56, 0.58, 0.61, 1.65, 0.28, 0.52, 0.52, 1.06, 0.33, 0.3, 0.55, 1.52, 1, 0.27, 2.29, 0.41, 0.51, 0.52, 0.77, 0.53, 1.5, 0.23, 0.39, 0.72, 1.02, 0.58, 0.23, 1.02, 0.46, 1.2, 1.17, 0.32, 0.7, 0.51, 0.76, 0.31, 0.3, 0.38, 0.39, 0.53, 0.3, 2.01, 0.41, 0.72, 2.03, 1.63, 0.54, 0.33, 0.71, 1.21, 0.71, 1.02, 0.72, 0.51, 0.7, 0.41, 1.02, 1.5, 1.04, 0.55, 0.31, 0.9, 0.79, 1.13, 0.32, 0.71, 0.58, 1.51, 2.01, 2.1, 0.92, 0.67, 1, 0.54, 0.42, 1.27, 1, 1.01, 1.2, 0.31, 1.01, 0.7, 0.23, 0.32, 0.31, 0.5, 0.52, 0.32, 0.3, 1.2, 0.73, 0.3, 1.02, 0.38, 1.51, 0.4, 0.25, 0.7, 0.27, 1.01, 0.54, 0.33, 1.51, 0.58, 0.7, 0.5, 0.91, 0.31, 0.97, 0.71, 0.74, 0.53, 1.5, 0.7, 0.91, 0.3, 0.6, 0.91, 0.71, 1.09, 0.5, 0.39, 0.39, 1.21, 0.71, 1.5, 0.7, 0.31, 1.2, 0.23, 1.01, 0.3, 1.22, 0.52, 0.92, 0.6, 1.01, 0.71, 1.4, 0.59, 0.59, 1.3, 0.31, 1, 0.41, 0.46, 0.7, 0.33, 0.3, 1.5, 0.4, 0.39, 1, 0.72, 0.58, 0.4, 0.29, 0.5, 0.59, 0.3, 0.57, 1.54, 1.12, 0.31, 0.31, 0.4, 0.31, 1.42, 0.41, 1.71, 0.31, 0.49, 0.4, 0.51, 0.4, 0.23, 0.54, 0.74, 0.9, 1.11, 1.02, 0.5, 0.76, 1, 0.5, 0.6, 1.25], 
  "y": [6630, 565, 15334, 8520, 9586, 925, 8055, 684, 844, 2656, 526, 4849, 5588, 5456, 1746, 1632, 13102, 453, 754, 8008, 9178, 579, 3014, 1237, 2740, 958, 2493, 2840, 683, 3603, 2693, 1755, 1090, 2036, 17425, 458, 1665, 1446, 4465, 1014, 499, 1580, 13001, 4704, 620, 11502, 904, 1574, 1369, 3488, 1132, 7888, 465, 1107, 2337, 6432, 1234, 485, 6047, 904, 9139, 4826, 505, 2042, 2041, 2873, 544, 878, 883, 889, 1825, 709, 9781, 647, 2667, 18630, 9556, 1079, 752, 2913, 7826, 2922, 5430, 3043, 1068, 2389, 755, 7861, 9573, 5353, 1667, 553, 3724, 2633, 5052, 576, 2450, 1408, 9513, 15675, 17837, 3986, 1981, 5557, 1356, 755, 7176, 5082, 6540, 9586, 625, 6956, 2421, 352, 449, 489, 1410, 1389, 480, 694, 5280, 2779, 526, 6632, 633, 13945, 1080, 575, 2429, 620, 5294, 1662, 810, 12224, 1408, 2592, 1122, 3567, 907, 4140, 2346, 2583, 1647, 18552, 2039, 3006, 473, 1777, 3664, 2147, 8650, 1351, 793, 694, 6549, 2400, 7392, 2104, 779, 5226, 485, 13312, 759, 6704, 1232, 4327, 1597, 4154, 3799, 11584, 2068, 1445, 7333, 523, 7507, 827, 1006, 2928, 463, 613, 9895, 1078, 1065, 5766, 2333, 1979, 1075, 664, 1337, 2302, 489, 1072, 14433, 9820, 640, 353, 1111, 808, 9278, 835, 13818, 544, 1400, 655, 1080, 810, 505, 1944, 2042, 4315, 6593, 4594, 1106, 2579, 5940, 1154, 1399, 5362], 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }, 
    "opacity": 1, 
    "size": 4, 
    "sizemode": "area", 
    "sizeref": 1, 
    "symbol": "circle"
  }, 
  "mode": "markers", 
  "showlegend": False, 
  "text": ["Clarity: SI1", "Clarity: VS1", "Clarity: VVS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VVS1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: IF", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: VS1", "Clarity: SI2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VVS1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS1", "Clarity: VVS1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS1", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VVS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: IF", "Clarity: SI1", "Clarity: SI2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: IF", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VVS1", "Clarity: VS1", "Clarity: VVS2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI2", "Clarity: VVS1", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS1", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: IF", "Clarity: VS1", "Clarity: SI1", "Clarity: VVS1", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI2"], 
  "type": "scatter", 
  "uid": "fd8e0a", 
  "xaxis": "x3", 
  "yaxis": "y2"
}
trace4 = {
  "x": [2.06, 0.51, 0.32, 0.53, 1.21, 0.74, 1.06, 0.3, 0.3, 0.72, 2.12, 1.57, 0.41, 1.07, 0.41, 1.14, 1.54, 1.42, 0.43, 0.62, 0.71, 1.73, 0.74, 0.9, 1.13, 0.32, 1.91, 0.36, 1.19, 0.7, 0.9, 1.01, 1.61, 1.09, 1.05, 1.02, 0.51, 0.32, 0.34, 0.91, 0.75, 0.3, 1.01, 1.06, 1.08, 1.53, 0.9, 0.31, 1.23, 1.46, 0.35, 2.68, 0.55, 0.41, 1.21, 1.23, 0.83, 1.03, 0.44, 1.03, 0.72, 1.01, 1, 1.02, 0.63, 0.47, 1.4, 1.03, 0.41, 0.3, 2.19, 2.18, 2.14, 0.31, 2.01, 1.01, 1.05, 1, 1.16, 0.3, 0.4, 1.7, 0.91, 0.38, 1.01, 1.5, 1.21, 0.93, 1.22, 0.42, 2.04, 0.91, 0.71, 1.19, 1.01, 0.54, 0.4, 1.09, 1.51, 0.94, 0.68, 1.1, 1, 0.33, 1.94, 0.41, 0.34, 0.52, 0.3, 0.52, 1.06, 1.6, 1.58, 0.7, 0.4, 1, 1.75, 2.01, 0.3, 0.37, 0.7, 0.71, 1.02, 1.12, 1, 0.58, 0.33, 0.32, 1, 0.92, 1.1, 1.51, 0.7, 0.53, 0.51, 1.2, 0.4, 0.36, 0.32, 0.7, 1.58, 0.42, 0.51, 0.7, 1.06, 0.27, 0.9, 0.47, 0.3, 0.43, 1.21, 1.06, 1.02, 1.76, 1.51, 2.02, 0.32, 1, 0.55, 1.54, 2.01, 1.01, 0.89, 0.31, 0.4, 0.39, 0.59, 1.07, 1.07, 0.62, 1.51, 1.54, 1.05, 1.62, 1.14, 0.7, 0.7, 0.35, 1, 0.7, 0.43, 0.3, 0.94, 1.02, 0.31, 1.3, 1.06, 0.3, 1.5, 0.8, 1, 0.9, 1.04, 1.1, 0.5, 0.9, 1.09, 0.31, 0.37, 0.55, 2.04, 0.59, 1.89, 2.03, 0.25, 0.9, 0.7, 0.37, 1.04, 1.7, 0.35, 2.01, 0.5, 1.09, 0.3, 1.22, 0.71, 1.02, 0.42, 0.9, 0.3, 0.4, 0.51, 0.81, 1.11, 0.7, 0.32, 2.05, 0.55, 0.54, 0.3, 0.34, 1.08, 0.44, 0.5, 1.51, 1, 0.57, 0.54, 0.7, 0.33, 1.35, 0.3, 1.21, 0.32, 2.18, 0.51], 
  "y": [13912, 1443, 702, 1132, 6031, 2201, 4654, 776, 878, 2405, 12140, 8001, 1079, 6471, 1079, 4980, 12308, 8102, 739, 1415, 2443, 9494, 2999, 3841, 5338, 756, 13367, 932, 4078, 2167, 4232, 4525, 14833, 4456, 7056, 6220, 1036, 540, 477, 3911, 2415, 608, 8416, 7541, 5078, 12851, 3084, 734, 5841, 6387, 706, 8419, 1668, 827, 9541, 8810, 2311, 5087, 1028, 6479, 2364, 6843, 4170, 7351, 1996, 1143, 5723, 4974, 1107, 905, 15801, 12631, 16390, 816, 17014, 4578, 5433, 8602, 4958, 506, 855, 13256, 2564, 700, 6425, 9055, 8877, 4229, 5773, 992, 9905, 4816, 2443, 6363, 5988, 1662, 855, 4395, 17936, 4817, 2326, 3388, 6468, 723, 18735, 1241, 803, 2012, 844, 1694, 8003, 9017, 7592, 2633, 772, 5322, 12529, 15908, 844, 746, 2777, 2623, 4958, 3942, 5058, 1636, 780, 471, 6989, 2730, 4916, 9301, 1982, 1015, 1781, 5699, 900, 537, 1080, 2354, 13995, 810, 2203, 2369, 4372, 603, 4321, 867, 620, 1209, 10245, 6838, 4061, 13867, 6851, 15987, 936, 8154, 1832, 9926, 13199, 4022, 2815, 872, 1035, 1010, 2578, 6471, 4278, 1579, 7553, 11815, 7244, 14447, 5925, 2777, 1890, 956, 3780, 2999, 830, 911, 5980, 6169, 523, 7621, 5549, 684, 6048, 3312, 5197, 3175, 4316, 4354, 1715, 2927, 4303, 571, 1041, 1698, 9727, 1912, 10055, 12492, 740, 4579, 2513, 1010, 3861, 10662, 647, 14948, 1610, 5640, 1013, 5671, 2169, 5346, 963, 4435, 552, 855, 1443, 3084, 5395, 3199, 720, 15109, 1580, 1013, 641, 596, 4740, 990, 1624, 6342, 6048, 1728, 1340, 2020, 631, 9471, 675, 6566, 624, 17841, 1546], 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }, 
    "opacity": 1, 
    "size": 4, 
    "sizemode": "area", 
    "sizeref": 1, 
    "symbol": "circle"
  }, 
  "mode": "markers", 
  "showlegend": False, 
  "text": ["Clarity: SI2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS1", "Clarity: SI2", "Clarity: SI2", "Clarity: VVS2", "Clarity: I1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS1", "Clarity: SI2", "Clarity: VVS2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS1", "Clarity: VS1", "Clarity: SI2", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS1", "Clarity: SI1", "Clarity: I1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: I1", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: SI1", "Clarity: VS2", "Clarity: VVS1", "Clarity: VVS1", "Clarity: VS1", "Clarity: SI1", "Clarity: SI2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: IF", "Clarity: VS1", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: SI2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: I1", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS1", "Clarity: VVS1", "Clarity: VVS2", "Clarity: SI2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: SI1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: SI2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2"], 
  "type": "scatter", 
  "uid": "eb65c9", 
  "xaxis": "x", 
  "yaxis": "y"
}
trace5 = {
  "x": [0.9, 0.3, 1.08, 0.3, 0.51, 1.24, 0.58, 0.91, 1.21, 0.31, 0.53, 0.31, 1.01, 0.42, 0.52, 0.35, 1.51, 0.55, 0.35, 0.59, 0.47, 0.54, 2.37, 0.61, 0.23, 1, 1, 1.01, 0.26, 1.2, 0.28, 0.35, 0.34, 2.01, 0.31, 1.28, 1.63, 0.51, 1.16, 0.33, 0.72, 0.31, 0.32, 0.41, 0.97, 0.59, 0.72, 0.79, 0.32, 0.55, 0.5, 0.31, 1.02, 0.3, 0.54, 1.05, 0.51, 0.42, 1, 2.02, 0.3, 1.72, 0.78, 0.35, 1.57, 0.7, 2.05, 0.78, 0.3, 0.71, 0.26, 0.54, 0.76, 0.54, 0.5, 0.75, 0.39, 0.31, 0.92, 0.58, 1.2, 0.34, 0.3, 0.85, 0.63, 0.7, 1.21, 0.77, 0.31, 0.54, 0.62, 1.01, 0.59, 1.53, 0.29, 0.3, 0.41, 0.74, 1.2, 0.33, 0.42, 0.32, 0.76, 1, 1.23, 0.54, 0.51, 0.31, 0.43, 1.25, 1.19, 0.6, 0.41, 0.43, 0.3, 1.04, 0.3, 1.1, 1.17, 0.38, 0.32, 1.09, 1, 0.33, 1.13, 1.01, 0.47, 0.31, 0.52, 0.71, 0.32, 1.38, 0.7, 0.43, 0.71, 1.02, 0.31, 0.44, 0.31, 0.72, 0.33, 0.5, 0.72, 1.01, 0.3, 0.41, 1.53, 0.36, 2.5, 0.3, 1.06, 0.39, 1.01, 1.01, 0.37, 0.33, 0.41, 1.55, 1.24, 1.2, 0.51, 0.25, 1.2, 0.36, 1.51, 0.71, 1.5, 0.33, 0.41, 0.45, 0.31, 1.03, 1.18, 0.39, 0.28, 1.13, 0.3, 0.5, 0.72, 0.39, 0.37, 0.33, 0.55, 2.02, 0.87, 0.51, 1.07, 0.53, 0.31, 1.2, 0.4, 1.03, 0.41, 0.4, 0.54, 0.51, 1.1, 1.12, 0.23, 0.51, 0.71, 0.78, 0.77, 0.71, 0.72, 1.2, 1.09, 1.28, 0.91, 1.24, 0.34, 0.32, 0.71, 1.51, 1.25, 0.31, 0.35, 0.32, 0.32, 0.7, 0.31, 0.43, 0.31, 0.77, 1.51, 0.59, 0.5, 0.41, 0.56, 0.58, 0.51, 0.54, 0.73, 0.32, 1.43, 1.3, 0.5, 2.1, 0.32, 0.42, 0.32, 1.21, 0.54, 1.09, 0.42, 1.07, 0.42, 0.36, 0.51, 0.53, 1.07, 1.03, 0.4, 0.34, 0.9, 0.67, 0.27, 1.26, 0.59, 1.51, 0.71, 1.11, 1.5, 1.1, 0.51, 1.01, 0.31, 1.12, 1.01, 0.53, 0.83, 1.01, 0.3, 0.72, 0.37, 0.56, 1.2, 0.55, 0.25, 1.1, 0.56, 1.01, 0.31, 0.55, 1.43, 1.23, 0.82, 0.41, 0.3, 0.41, 0.35, 0.38, 0.53, 1.21, 1.01, 0.54, 0.4, 1.21, 0.75, 0.52, 0.7, 0.3, 1.04, 0.8, 0.61, 0.59, 0.31, 1.61, 0.42, 0.42, 0.53, 0.42, 0.3, 1.21, 0.3, 0.3, 0.54, 2.61, 1.27, 1.51, 0.36, 0.41, 0.32, 1.23, 1.53, 1.12, 0.58, 0.55, 0.7, 0.58, 0.71, 0.79, 0.8, 0.34, 2.24, 0.41, 0.43, 1.25, 0.52, 1.01, 0.4, 0.36, 0.34, 0.41, 0.26, 0.56, 0.28, 2.48, 0.71, 0.52, 0.72, 1.2, 0.42, 0.31, 0.53, 0.7, 0.55, 1.58, 0.4, 0.52, 0.36, 0.3, 0.31, 0.24, 1.21, 0.57, 2.72, 1.5, 0.35, 0.32, 0.31, 0.31, 1.04, 0.55, 0.55, 0.68, 0.79, 0.53, 0.85, 0.31, 0.57, 0.55, 0.5, 0.28, 1.24, 0.53, 0.36, 0.34, 0.3, 1.05, 0.64, 1.42, 0.32, 0.51, 0.33, 0.52, 0.71], 
  "y": [5656, 709, 4544, 838, 1875, 6076, 1196, 4919, 8001, 975, 1020, 687, 4559, 1235, 1872, 706, 7693, 2374, 984, 1916, 1261, 1607, 16059, 1270, 530, 4956, 6612, 7179, 599, 5964, 598, 788, 596, 13498, 942, 12841, 12155, 983, 7113, 743, 2458, 907, 834, 1243, 3729, 2125, 2591, 3107, 602, 2030, 2025, 652, 3142, 1000, 1637, 5361, 2093, 1656, 9294, 14182, 764, 7802, 2386, 707, 16570, 2872, 14111, 3159, 844, 3674, 580, 1065, 3170, 1452, 1306, 2903, 988, 734, 3697, 1742, 10454, 765, 886, 4089, 1641, 2657, 4880, 4039, 789, 1304, 2062, 6855, 1834, 10698, 607, 789, 899, 3537, 8442, 992, 908, 1018, 3363, 6048, 8509, 1662, 1678, 816, 1318, 6944, 3665, 2358, 1107, 935, 1069, 4543, 936, 7453, 8648, 721, 943, 4465, 4172, 854, 7147, 6499, 1163, 707, 1689, 2326, 816, 15968, 2499, 783, 2308, 8303, 791, 1207, 661, 2642, 631, 1286, 2731, 5751, 684, 753, 11525, 587, 14502, 1125, 4541, 857, 4479, 5317, 1041, 946, 1163, 13171, 4916, 5765, 1591, 363, 9317, 878, 7145, 2265, 8770, 723, 647, 1027, 647, 8020, 11415, 1368, 481, 4371, 605, 2145, 2393, 1004, 839, 1114, 2132, 16290, 3090, 1882, 4458, 1690, 871, 7761, 895, 5337, 1079, 918, 1057, 2075, 8796, 8251, 493, 2720, 2637, 3613, 3253, 3281, 2650, 7930, 8422, 7109, 3863, 8299, 1211, 449, 2974, 14844, 11511, 421, 1065, 900, 825, 2353, 942, 1580, 414, 3750, 12100, 1743, 1676, 863, 1819, 1705, 1656, 1368, 2519, 715, 14429, 9060, 1746, 18124, 730, 1087, 466, 10568, 1340, 5496, 938, 7564, 885, 807, 1100, 2158, 6648, 3738, 596, 745, 4101, 2010, 470, 6277, 1782, 9334, 3007, 4969, 8580, 6630, 1909, 4209, 921, 7091, 5274, 1243, 3933, 4796, 776, 3122, 1071, 1963, 11530, 1101, 633, 4897, 2032, 8133, 921, 1980, 10129, 5407, 3306, 876, 475, 613, 522, 963, 1928, 13661, 7179, 2039, 945, 8774, 2821, 1019, 2777, 731, 3588, 3774, 3625, 1789, 942, 15819, 898, 771, 2015, 1179, 499, 12230, 475, 408, 1914, 18756, 5405, 8678, 985, 775, 523, 6557, 12616, 6918, 1965, 1604, 3172, 1811, 3217, 3075, 4043, 495, 17989, 876, 1304, 7423, 1919, 7900, 631, 439, 790, 1276, 447, 1729, 642, 12883, 3136, 1767, 3478, 5766, 773, 489, 1721, 3191, 1890, 17329, 1163, 1919, 560, 873, 625, 559, 6180, 1448, 17801, 14199, 706, 645, 707, 400, 7220, 2242, 2383, 2526, 3167, 1038, 2442, 891, 1728, 1611, 2352, 646, 5714, 1727, 945, 765, 863, 5586, 2587, 18682, 449, 1656, 579, 1651, 2930], 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }, 
    "opacity": 1, 
    "size": 4, 
    "sizemode": "area", 
    "sizeref": 1, 
    "symbol": "circle"
  }, 
  "mode": "markers", 
  "showlegend": False, 
  "text": ["Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI1", "Clarity: VVS1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: IF", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI2", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS1", "Clarity: IF", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VVS1", "Clarity: I1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: IF", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS1", "Clarity: VVS1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: VVS1", "Clarity: VS1", "Clarity: VVS1", "Clarity: VS1", "Clarity: IF", "Clarity: VS2", "Clarity: IF", "Clarity: VVS1", "Clarity: VS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: IF", "Clarity: VS2", "Clarity: I1", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: IF", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VVS2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: SI1", "Clarity: SI2", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: SI2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: IF", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VVS2", "Clarity: VVS2", "Clarity: VVS2", "Clarity: IF", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VVS1", "Clarity: VVS2", "Clarity: IF", "Clarity: VS1", "Clarity: SI2", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: IF", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: VVS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: IF", "Clarity: VS2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: IF", "Clarity: SI1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: VS1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI2", "Clarity: SI1", "Clarity: VVS2", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS2", "Clarity: SI2", "Clarity: IF", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS1", "Clarity: IF", "Clarity: VS1", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS1", "Clarity: SI2", "Clarity: SI1", "Clarity: VS2", "Clarity: SI2", "Clarity: VVS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI1", "Clarity: VS1", "Clarity: SI1", "Clarity: SI1", "Clarity: SI1", "Clarity: VVS2", "Clarity: SI2", "Clarity: IF", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: VS1", "Clarity: VVS1", "Clarity: VVS1", "Clarity: SI1", "Clarity: VVS1", "Clarity: SI1", "Clarity: SI2", "Clarity: VVS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VS1", "Clarity: IF", "Clarity: VS1", "Clarity: VS2", "Clarity: SI1", "Clarity: SI1", "Clarity: VS1", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: SI2", "Clarity: SI2", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: SI2", "Clarity: VS1", "Clarity: IF", "Clarity: SI1", "Clarity: VS2", "Clarity: VVS2", "Clarity: SI2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS1", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: VS1", "Clarity: IF", "Clarity: VVS2", "Clarity: VS2", "Clarity: SI1", "Clarity: IF", "Clarity: VVS2", "Clarity: VVS1", "Clarity: SI1", "Clarity: VS1", "Clarity: SI2", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1", "Clarity: VVS2", "Clarity: VS2", "Clarity: VS2", "Clarity: VVS2", "Clarity: IF", "Clarity: VS1", "Clarity: SI1", "Clarity: VS2", "Clarity: VS2", "Clarity: IF", "Clarity: SI1", "Clarity: SI1", "Clarity: IF", "Clarity: VVS2", "Clarity: SI1", "Clarity: VS2", "Clarity: VVS1", "Clarity: VS2", "Clarity: IF", "Clarity: SI1", "Clarity: VVS2", "Clarity: VVS1", "Clarity: SI2", "Clarity: VS1", "Clarity: VS2", "Clarity: VS2", "Clarity: VS1"], 
  "type": "scatter", 
  "uid": "39a57d", 
  "xaxis": "x2", 
  "yaxis": "y"
}
trace6 = {
  "x": [0.33, 0.352405063291, 0.374810126582, 0.397215189873, 0.419620253165, 0.442025316456, 0.464430379747, 0.486835443038, 0.509240506329, 0.53164556962, 0.554050632911, 0.576455696203, 0.598860759494, 0.621265822785, 0.643670886076, 0.666075949367, 0.688481012658, 0.710886075949, 0.733291139241, 0.755696202532, 0.778101265823, 0.800506329114, 0.822911392405, 0.845316455696, 0.867721518987, 0.890126582278, 0.91253164557, 0.934936708861, 0.957341772152, 0.979746835443, 1.00215189873, 1.02455696203, 1.04696202532, 1.06936708861, 1.0917721519, 1.11417721519, 1.13658227848, 1.15898734177, 1.18139240506, 1.20379746835, 1.22620253165, 1.24860759494, 1.27101265823, 1.29341772152, 1.31582278481, 1.3382278481, 1.36063291139, 1.38303797468, 1.40544303797, 1.42784810127, 1.45025316456, 1.47265822785, 1.49506329114, 1.51746835443, 1.53987341772, 1.56227848101, 1.5846835443, 1.60708860759, 1.62949367089, 1.65189873418, 1.67430379747, 1.69670886076, 1.71911392405, 1.74151898734, 1.76392405063, 1.78632911392, 1.80873417722, 1.83113924051, 1.8535443038, 1.87594936709, 1.89835443038, 1.92075949367, 1.94316455696, 1.96556962025, 1.98797468354, 2.01037974684, 2.03278481013, 2.05518987342, 2.07759493671, 2.1, 2.1, 2.07759493671, 2.05518987342, 2.03278481013, 2.01037974684, 1.98797468354, 1.96556962025, 1.94316455696, 1.92075949367, 1.89835443038, 1.87594936709, 1.8535443038, 1.83113924051, 1.80873417722, 1.78632911392, 1.76392405063, 1.74151898734, 1.71911392405, 1.69670886076, 1.67430379747, 1.65189873418, 1.62949367089, 1.60708860759, 1.5846835443, 1.56227848101, 1.53987341772, 1.51746835443, 1.49506329114, 1.47265822785, 1.45025316456, 1.42784810127, 1.40544303797, 1.38303797468, 1.36063291139, 1.3382278481, 1.31582278481, 1.29341772152, 1.27101265823, 1.24860759494, 1.22620253165, 1.20379746835, 1.18139240506, 1.15898734177, 1.13658227848, 1.11417721519, 1.0917721519, 1.06936708861, 1.04696202532, 1.02455696203, 1.00215189873, 0.979746835443, 0.957341772152, 0.934936708861, 0.91253164557, 0.890126582278, 0.867721518987, 0.845316455696, 0.822911392405, 0.800506329114, 0.778101265823, 0.755696202532, 0.733291139241, 0.710886075949, 0.688481012658, 0.666075949367, 0.643670886076, 0.621265822785, 0.598860759494, 0.576455696203, 0.554050632911, 0.53164556962, 0.509240506329, 0.486835443038, 0.464430379747, 0.442025316456, 0.419620253165, 0.397215189873, 0.374810126582, 0.352405063291, 0.33, 0.33], 
  "y": [3240.25903974, 2936.33459029, 2686.79617669, 2496.29005946, 2367.53453989, 2299.25535175, 2285.72380233, 2319.15588313, 2388.33283162, 2467.90916035, 2549.8358235, 2634.77267272, 2725.35292268, 2824.04986612, 2931.92471523, 3048.15154856, 3170.1837924, 3289.42602932, 3380.9024154, 3464.32520049, 3564.76394892, 3697.61044589, 3862.90509845, 4047.86837974, 4252.56414823, 4497.14888813, 4738.34630259, 5014.88643641, 5324.28956971, 5629.77157211, 5878.45845911, 6066.62467648, 6240.02208852, 6388.77854487, 6505.28478398, 6594.07882261, 6660.31302273, 6709.47333607, 6747.12234879, 6778.63035125, 6808.89625923, 6842.09438202, 6881.50147461, 6929.44772004, 6987.39788784, 7056.12759941, 7135.93905607, 7226.86720023, 7328.84924624, 7441.85252493, 7565.96983638, 7701.49816177, 7849.01939963, 8006.53050108, 8168.1916705, 8334.0696347, 8504.51042607, 8679.91918667, 8860.76988274, 9047.61679746, 9241.10768476, 9441.99818398, 9651.16662643, 9869.62765677, 10098.5421281, 10339.219596, 10593.1087164, 10861.7705174, 11146.8306919, 11449.9105204, 11772.5418091, 12116.0778621, 12481.6170068, 12869.9544835, 13281.571768, 13716.6622549, 14175.1833471, 14656.920891, 15161.5530243, 15688.7048014, 11287.2437023, 11038.1193591, 10786.4596169, 10531.7095776, 10273.3674264, 10011.039057, 9744.50191982, 9473.76945692, 9199.14319144, 8921.23841126, 8640.97349109, 8359.52178253, 8078.23513924, 7798.55488906, 7521.92677245, 7249.73186491, 6983.23886981, 6723.57739015, 6471.72832649, 6228.52637092, 5994.66990219, 5770.73460708, 5557.18828696, 5354.40527246, 5162.67957724, 4982.23639083, 4813.24179303, 4656.54207955, 4531.41666265, 4443.15176773, 4387.09234392, 4358.29842305, 4351.62585583, 4361.80502371, 4383.53619169, 4411.61735278, 4441.11375895, 4467.56408224, 4487.1961428, 4497.1031743, 4495.32498236, 4480.79892689, 4453.18697433, 4412.62246564, 4359.43103763, 4293.86169265, 4215.82984331, 4124.636557, 4022.52872531, 3911.11404895, 3758.2487805, 3542.85909074, 3264.96836553, 2941.05796093, 2615.73806153, 2320.4858437, 2019.70911912, 1747.05921545, 1500.67225225, 1262.18738258, 1026.0636934, 802.111649814, 609.819496091, 466.025845327, 356.022767958, 269.277754745, 198.93904043, 139.875512014, 88.8431901467, 44.0101760353, 3.70449279896, -35.7191994475, -83.3488436572, -153.084283204, -254.897493377, -396.806199961, -584.554287732, -819.281308656, -1098.13435941, -1416.33257743, 3240.25903974], 
  "fill": "tozerox", 
  "fillcolor": "rgba(248,118,109,0.2)", 
  "line": {
    "color": "transparent", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Fair", 
  "showlegend": False, 
  "type": "scatter", 
  "uid": "63b8d7", 
  "xaxis": "x", 
  "yaxis": "y2"
}
trace7 = {
  "x": [0.24, 0.274936708861, 0.309873417722, 0.344810126582, 0.379746835443, 0.414683544304, 0.449620253165, 0.484556962025, 0.519493670886, 0.554430379747, 0.589367088608, 0.624303797468, 0.659240506329, 0.69417721519, 0.729113924051, 0.764050632911, 0.798987341772, 0.833924050633, 0.868860759494, 0.903797468354, 0.938734177215, 0.973670886076, 1.00860759494, 1.0435443038, 1.07848101266, 1.11341772152, 1.14835443038, 1.18329113924, 1.2182278481, 1.25316455696, 1.28810126582, 1.32303797468, 1.35797468354, 1.39291139241, 1.42784810127, 1.46278481013, 1.49772151899, 1.53265822785, 1.56759493671, 1.60253164557, 1.63746835443, 1.67240506329, 1.70734177215, 1.74227848101, 1.77721518987, 1.81215189873, 1.84708860759, 1.88202531646, 1.91696202532, 1.95189873418, 1.98683544304, 2.0217721519, 2.05670886076, 2.09164556962, 2.12658227848, 2.16151898734, 2.1964556962, 2.23139240506, 2.26632911392, 2.30126582278, 2.33620253165, 2.37113924051, 2.40607594937, 2.44101265823, 2.47594936709, 2.51088607595, 2.54582278481, 2.58075949367, 2.61569620253, 2.65063291139, 2.68556962025, 2.72050632911, 2.75544303797, 2.79037974684, 2.8253164557, 2.86025316456, 2.89518987342, 2.93012658228, 2.96506329114, 3, 3, 3, 2.96506329114, 2.93012658228, 2.89518987342, 2.86025316456, 2.8253164557, 2.79037974684, 2.75544303797, 2.72050632911, 2.68556962025, 2.65063291139, 2.61569620253, 2.58075949367, 2.54582278481, 2.51088607595, 2.47594936709, 2.44101265823, 2.40607594937, 2.37113924051, 2.33620253165, 2.30126582278, 2.26632911392, 2.23139240506, 2.1964556962, 2.16151898734, 2.12658227848, 2.09164556962, 2.05670886076, 2.0217721519, 1.98683544304, 1.95189873418, 1.91696202532, 1.88202531646, 1.84708860759, 1.81215189873, 1.77721518987, 1.74227848101, 1.70734177215, 1.67240506329, 1.63746835443, 1.60253164557, 1.56759493671, 1.53265822785, 1.49772151899, 1.46278481013, 1.42784810127, 1.39291139241, 1.35797468354, 1.32303797468, 1.28810126582, 1.25316455696, 1.2182278481, 1.18329113924, 1.14835443038, 1.11341772152, 1.07848101266, 1.0435443038, 1.00860759494, 0.973670886076, 0.938734177215, 0.903797468354, 0.868860759494, 0.833924050633, 0.798987341772, 0.764050632911, 0.729113924051, 0.69417721519, 0.659240506329, 0.624303797468, 0.589367088608, 0.554430379747, 0.519493670886, 0.484556962025, 0.449620253165, 0.414683544304, 0.379746835443, 0.344810126582, 0.309873417722, 0.274936708861, 0.24, 0.24], 
  "y": [1285.46852365, 1226.33799674, 1206.38547144, 1229.57494597, 1296.47636448, 1399.94370416, 1529.91171695, 1678.99726716, 1840.83925832, 1993.04287019, 2140.50079159, 2298.25311278, 2473.56303016, 2664.35039679, 2858.48328228, 3066.79639637, 3289.9623198, 3522.57729467, 3779.20431389, 4068.78948357, 4381.63553287, 4691.28728929, 4969.94705758, 5238.77169171, 5529.12092198, 5846.87838327, 6185.95461782, 6538.92854716, 6902.01429286, 7271.62577281, 7643.91968438, 8014.4165189, 8377.6896397, 8727.27623899, 9055.92753982, 9356.18318132, 9621.14882119, 9863.20922525, 10102.0717673, 10335.6374564, 10562.2012841, 10780.5098415, 10989.6828214, 11189.1297368, 11378.479541, 11557.5266242, 11726.1912082, 11884.4908448, 12032.5199456, 12170.4348918, 12298.4428863, 12416.7931951, 12525.7697916, 12625.6846895, 12716.8714602, 12799.6786109, 12874.4626594, 12941.5808958, 13001.3839594, 13054.2084819, 13100.3701286, 13140.1574077, 13173.8265946, 13201.598045, 13223.6540511, 13240.1382595, 13251.1565379, 13256.7790671, 13257.0433705, 13251.957965, 13241.5063327, 13225.6509511, 13204.3371776, 13177.4968442, 13145.0514744, 13106.9150803, 13062.9965389, 13013.2015642, 12957.4343139, 12895.5986751, 8196.03691646, 8196.03691646, 8452.67241485, 8696.97744378, 8928.86309231, 9148.24072061, 9355.02324487, 9549.12674403, 9730.47243276, 9898.98903651, 10054.6155896, 10197.3046516, 10327.0259023, 10443.7700258, 10547.5527415, 10638.4187748, 10716.4455088, 10781.7460134, 10834.4711374, 10874.8103752, 10902.9912846, 10919.2773434, 10923.964262, 10917.3749078, 10899.8531147, 10871.7567243, 10833.4502289, 10785.2973485, 10727.6537924, 10660.8603343, 10585.2361901, 10501.0725355, 10408.6258386, 10308.1105045, 10199.6901166, 10083.4662888, 9959.46377517, 9827.60999957, 9687.70655437, 9539.38959519, 9382.0758372, 9214.89217552, 9036.59240324, 8845.47871432, 8639.3050221, 8399.59888194, 8118.40704278, 7802.1322704, 7456.61131199, 7087.8924987, 6702.81013079, 6309.23467968, 5915.98374475, 5532.51113146, 5168.52786577, 4833.82181485, 4536.89046657, 4261.50123286, 3994.73761015, 3738.04727761, 3485.00749486, 3222.69581851, 2941.07626598, 2646.87075627, 2365.44458537, 2127.17798881, 1922.30007749, 1723.56162336, 1551.91640974, 1400.69687343, 1255.7153139, 1112.12737394, 972.865590233, 840.357713384, 709.931739798, 573.2970801, 419.908757729, 238.971610597, 25.1424567824, -220.295715907, -492.665865587, 1285.46852365], 
  "fill": "tozerox", 
  "fillcolor": "rgba(163,165,0,0.2)", 
  "line": {
    "color": "transparent", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Good", 
  "showlegend": False, 
  "type": "scatter", 
  "uid": "76b0f9", 
  "xaxis": "x2", 
  "yaxis": "y2"
}
trace8 = {
  "x": [0.23, 0.256075949367, 0.282151898734, 0.308227848101, 0.334303797468, 0.360379746835, 0.386455696203, 0.41253164557, 0.438607594937, 0.464683544304, 0.490759493671, 0.516835443038, 0.542911392405, 0.568987341772, 0.595063291139, 0.621139240506, 0.647215189873, 0.673291139241, 0.699367088608, 0.725443037975, 0.751518987342, 0.777594936709, 0.803670886076, 0.829746835443, 0.85582278481, 0.881898734177, 0.907974683544, 0.934050632911, 0.960126582278, 0.986202531646, 1.01227848101, 1.03835443038, 1.06443037975, 1.09050632911, 1.11658227848, 1.14265822785, 1.16873417722, 1.19481012658, 1.22088607595, 1.24696202532, 1.27303797468, 1.29911392405, 1.32518987342, 1.35126582278, 1.37734177215, 1.40341772152, 1.42949367089, 1.45556962025, 1.48164556962, 1.50772151899, 1.53379746835, 1.55987341772, 1.58594936709, 1.61202531646, 1.63810126582, 1.66417721519, 1.69025316456, 1.71632911392, 1.74240506329, 1.76848101266, 1.79455696203, 1.82063291139, 1.84670886076, 1.87278481013, 1.89886075949, 1.92493670886, 1.95101265823, 1.97708860759, 2.00316455696, 2.02924050633, 2.0553164557, 2.08139240506, 2.10746835443, 2.1335443038, 2.15962025316, 2.18569620253, 2.2117721519, 2.23784810127, 2.26392405063, 2.29, 2.29, 2.26392405063, 2.23784810127, 2.2117721519, 2.18569620253, 2.15962025316, 2.1335443038, 2.10746835443, 2.08139240506, 2.0553164557, 2.02924050633, 2.00316455696, 1.97708860759, 1.95101265823, 1.92493670886, 1.89886075949, 1.87278481013, 1.84670886076, 1.82063291139, 1.79455696203, 1.76848101266, 1.74240506329, 1.71632911392, 1.69025316456, 1.66417721519, 1.63810126582, 1.61202531646, 1.58594936709, 1.55987341772, 1.53379746835, 1.50772151899, 1.48164556962, 1.45556962025, 1.42949367089, 1.40341772152, 1.37734177215, 1.35126582278, 1.32518987342, 1.29911392405, 1.27303797468, 1.24696202532, 1.22088607595, 1.19481012658, 1.16873417722, 1.14265822785, 1.11658227848, 1.09050632911, 1.06443037975, 1.03835443038, 1.01227848101, 0.986202531646, 0.960126582278, 0.934050632911, 0.907974683544, 0.881898734177, 0.85582278481, 0.829746835443, 0.803670886076, 0.777594936709, 0.751518987342, 0.725443037975, 0.699367088608, 0.673291139241, 0.647215189873, 0.621139240506, 0.595063291139, 0.568987341772, 0.542911392405, 0.516835443038, 0.490759493671, 0.464683544304, 0.438607594937, 0.41253164557, 0.386455696203, 0.360379746835, 0.334303797468, 0.308227848101, 0.282151898734, 0.256075949367, 0.23, 0.23], 
  "y": [1076.93892694, 1014.04549223, 978.386654252, 973.788885359, 1001.10539064, 1059.0011351, 1142.64182229, 1244.35360582, 1356.79616937, 1475.8419328, 1599.10609372, 1725.00833577, 1856.04697397, 1996.2458149, 2139.5930168, 2273.33741177, 2406.47610002, 2556.6210732, 2732.40705109, 2933.38249502, 3155.36964926, 3393.52623658, 3645.31435033, 3910.45175957, 4188.66840531, 4478.9086111, 4778.40623797, 5082.11440453, 5382.95097902, 5672.73230583, 5943.40855495, 6208.73636534, 6481.47099545, 6760.92678425, 7046.2944037, 7336.57547654, 7630.55188881, 7926.79468006, 8223.71283943, 8519.63781345, 8812.93805211, 9102.29724601, 9387.21513693, 9667.42112068, 9942.70739771, 10212.9285234, 10477.999123, 10737.890595, 10992.6272648, 11242.2821511, 11486.9722875, 11726.8534159, 11962.1138325, 12192.9672228, 12419.6444637, 12642.3845798, 12861.425277, 13076.9936746, 13289.297967, 13498.5207054, 13704.8142083, 13908.2983216, 14109.0604299, 14307.1573583, 14502.6186364, 14695.4505546, 14885.6404972, 15073.1611493, 15257.9743096, 15440.0341659, 15619.2899842, 15795.6882354, 15969.1742144, 16139.6932323, 16307.1914587, 16471.6164912, 16632.9177139, 16791.0465014, 16945.9563096, 17097.6026872, 13719.8540246, 13738.5187142, 13748.0735961, 13748.5152105, 13739.8380049, 13722.0343455, 13695.0946079, 13659.0073811, 13613.7598264, 13559.3382463, 13495.7289275, 13422.919332, 13340.8997178, 13249.6652639, 13149.2187607, 13039.5738848, 12920.7590119, 12792.8214242, 12655.8316427, 12509.8874839, 12355.1173243, 12191.6820009, 12019.774824, 11839.6193363, 11651.4647238, 11455.5790972, 11252.2411539, 11041.7309102, 10824.3202345, 10600.2638037, 10369.7909056, 10133.0982738, 9890.34393328, 9641.64189425, 9387.05747377, 9126.60306173, 8860.23427499, 8587.84666047, 8309.27341012, 8024.28491131, 7734.41353522, 7442.96222504, 7150.90873239, 6859.16491713, 6568.72018179, 6280.72597925, 5996.54460892, 5717.7581069, 5446.13755849, 5183.57771605, 4921.98498454, 4649.02223028, 4365.46390648, 4072.17364696, 3771.11660943, 3466.29320196, 3163.98457502, 2872.18234163, 2599.66373224, 2355.19380536, 2153.92446374, 1994.64910103, 1856.46437435, 1722.14548749, 1583.55390271, 1441.80250452, 1305.19187333, 1172.19010736, 1045.80276328, 933.794116581, 830.444671052, 735.075531363, 646.783017996, 562.887328266, 475.07987292, 374.92249314, 258.036574517, 123.88721503, -26.0953282062, -189.492632088, 1076.93892694], 
  "fill": "tozerox", 
  "fillcolor": "rgba(0,191,125,0.2)", 
  "line": {
    "color": "transparent", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Very Good", 
  "showlegend": False, 
  "type": "scatter", 
  "uid": "39f795", 
  "xaxis": "x3", 
  "yaxis": "y2"
}
trace9 = {
  "x": [0.25, 0.280759493671, 0.311518987342, 0.342278481013, 0.373037974684, 0.403797468354, 0.434556962025, 0.465316455696, 0.496075949367, 0.526835443038, 0.557594936709, 0.58835443038, 0.619113924051, 0.649873417722, 0.680632911392, 0.711392405063, 0.742151898734, 0.772911392405, 0.803670886076, 0.834430379747, 0.865189873418, 0.895949367089, 0.926708860759, 0.95746835443, 0.988227848101, 1.01898734177, 1.04974683544, 1.08050632911, 1.11126582278, 1.14202531646, 1.17278481013, 1.2035443038, 1.23430379747, 1.26506329114, 1.29582278481, 1.32658227848, 1.35734177215, 1.38810126582, 1.41886075949, 1.44962025316, 1.48037974684, 1.51113924051, 1.54189873418, 1.57265822785, 1.60341772152, 1.63417721519, 1.66493670886, 1.69569620253, 1.7264556962, 1.75721518987, 1.78797468354, 1.81873417722, 1.84949367089, 1.88025316456, 1.91101265823, 1.9417721519, 1.97253164557, 2.00329113924, 2.03405063291, 2.06481012658, 2.09556962025, 2.12632911392, 2.15708860759, 2.18784810127, 2.21860759494, 2.24936708861, 2.28012658228, 2.31088607595, 2.34164556962, 2.37240506329, 2.40316455696, 2.43392405063, 2.4646835443, 2.49544303797, 2.52620253165, 2.55696202532, 2.58772151899, 2.61848101266, 2.64924050633, 2.68, 2.68, 2.64924050633, 2.61848101266, 2.58772151899, 2.55696202532, 2.52620253165, 2.49544303797, 2.4646835443, 2.43392405063, 2.40316455696, 2.37240506329, 2.34164556962, 2.31088607595, 2.28012658228, 2.24936708861, 2.21860759494, 2.18784810127, 2.15708860759, 2.12632911392, 2.09556962025, 2.06481012658, 2.03405063291, 2.00329113924, 1.97253164557, 1.9417721519, 1.91101265823, 1.88025316456, 1.84949367089, 1.81873417722, 1.78797468354, 1.75721518987, 1.7264556962, 1.69569620253, 1.66493670886, 1.63417721519, 1.60341772152, 1.57265822785, 1.54189873418, 1.51113924051, 1.48037974684, 1.44962025316, 1.41886075949, 1.38810126582, 1.35734177215, 1.32658227848, 1.29582278481, 1.26506329114, 1.23430379747, 1.2035443038, 1.17278481013, 1.14202531646, 1.11126582278, 1.08050632911, 1.04974683544, 1.01898734177, 0.988227848101, 0.95746835443, 0.926708860759, 0.895949367089, 0.865189873418, 0.834430379747, 0.803670886076, 0.772911392405, 0.742151898734, 0.711392405063, 0.680632911392, 0.649873417722, 0.619113924051, 0.58835443038, 0.557594936709, 0.526835443038, 0.496075949367, 0.465316455696, 0.434556962025, 0.403797468354, 0.373037974684, 0.342278481013, 0.311518987342, 0.280759493671, 0.25, 0.25], 
  "y": [1267.81356672, 1198.32484945, 1161.34403198, 1158.83451424, 1192.86947809, 1263.67519885, 1367.04415792, 1492.80170311, 1629.48746503, 1775.90109967, 1932.95053007, 2101.69349309, 2282.518006, 2474.98761059, 2678.09845462, 2896.65310973, 3135.64853971, 3395.21627766, 3673.16181582, 3961.59190676, 4245.84967814, 4507.28027748, 4743.43595641, 4983.4446408, 5238.1690194, 5497.91913423, 5752.83430734, 6012.29515821, 6279.0681958, 6553.2248085, 6833.12024814, 7117.86843811, 7407.29193442, 7701.09851326, 7998.79638599, 8299.64035117, 8602.61720887, 8906.47029402, 9209.75356029, 9510.90116543, 9808.30070096, 10100.3646243, 10385.6016989, 10662.6924409, 10930.1054283, 11187.2398559, 11434.1464401, 11670.9370358, 11897.7834089, 12114.9142694, 12322.6096303, 12521.1916024, 12711.0110841, 12892.4305289, 13065.8039749, 13231.4565486, 13389.6662693, 13540.6508419, 13684.5611511, 13821.481704, 13951.4368602, 14074.4008226, 14190.3091962, 14299.0703049, 14400.5751004, 14494.7051229, 14581.3384498, 14660.3538466, 14731.633457, 14795.0643862, 14850.5394914, 14897.9576341, 14937.2235855, 14968.2477245, 14990.9456229, 15005.2375828, 15011.0481643, 15008.3057305, 14996.942022, 14976.8917678, 10840.6207578, 11079.4537647, 11302.4807893, 11509.7455429, 11701.2887483, 11877.1477507, 12037.3560927, 12181.9430583, 12310.9332018, 12424.3458842, 12522.194859, 12604.4879698, 12671.2270561, 12722.4082054, 12758.0225435, 12778.0578182, 12782.501089, 12771.3428786, 12744.5831206, 12702.2391213, 12644.3554679, 12571.0153456, 12482.3520961, 12378.5592088, 12259.8965507, 12126.6908087, 11979.3289846, 11818.2451868, 11643.902436, 11456.7721676, 11257.3142625, 11045.9598135, 10823.0978159, 10589.065962, 10344.1449999, 10088.5557666, 9822.45796086, 9549.04728832, 9273.0100523, 8994.79369196, 8714.64292273, 8432.70615384, 8149.10692863, 7864.01535667, 7577.7213435, 7290.70417586, 7003.68660566, 6717.6593833, 6433.86667198, 6153.75219972, 5878.87447435, 5613.20278826, 5356.40694183, 5103.20048274, 4850.9574058, 4593.30966065, 4319.06575362, 4032.299628, 3756.89665105, 3484.52413913, 3199.56807106, 2903.19506462, 2600.56971772, 2303.62025315, 2029.97363342, 1799.58286186, 1610.94688307, 1445.25384128, 1298.50488747, 1167.27857355, 1048.97792687, 941.675694417, 843.294809336, 749.837446264, 654.956671937, 550.955425757, 432.22630907, 296.983194446, 145.760726283, -15.7416925013, 1267.81356672], 
  "fill": "tozerox", 
  "fillcolor": "rgba(0,176,246,0.2)", 
  "line": {
    "color": "transparent", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Premium", 
  "showlegend": False, 
  "type": "scatter", 
  "uid": "2293e3", 
  "xaxis": "x", 
  "yaxis": "y"
}
trace10 = {
  "x": [0.23, 0.261518987342, 0.293037974684, 0.324556962025, 0.356075949367, 0.387594936709, 0.419113924051, 0.450632911392, 0.482151898734, 0.513670886076, 0.545189873418, 0.576708860759, 0.608227848101, 0.639746835443, 0.671265822785, 0.702784810127, 0.734303797468, 0.76582278481, 0.797341772152, 0.828860759494, 0.860379746835, 0.891898734177, 0.923417721519, 0.954936708861, 0.986455696203, 1.01797468354, 1.04949367089, 1.08101265823, 1.11253164557, 1.14405063291, 1.17556962025, 1.20708860759, 1.23860759494, 1.27012658228, 1.30164556962, 1.33316455696, 1.3646835443, 1.39620253165, 1.42772151899, 1.45924050633, 1.49075949367, 1.52227848101, 1.55379746835, 1.5853164557, 1.61683544304, 1.64835443038, 1.67987341772, 1.71139240506, 1.74291139241, 1.77443037975, 1.80594936709, 1.83746835443, 1.86898734177, 1.90050632911, 1.93202531646, 1.9635443038, 1.99506329114, 2.02658227848, 2.05810126582, 2.08962025316, 2.12113924051, 2.15265822785, 2.18417721519, 2.21569620253, 2.24721518987, 2.27873417722, 2.31025316456, 2.3417721519, 2.37329113924, 2.40481012658, 2.43632911392, 2.46784810127, 2.49936708861, 2.53088607595, 2.56240506329, 2.59392405063, 2.62544303797, 2.65696202532, 2.68848101266, 2.72, 2.72, 2.68848101266, 2.65696202532, 2.62544303797, 2.59392405063, 2.56240506329, 2.53088607595, 2.49936708861, 2.46784810127, 2.43632911392, 2.40481012658, 2.37329113924, 2.3417721519, 2.31025316456, 2.27873417722, 2.24721518987, 2.21569620253, 2.18417721519, 2.15265822785, 2.12113924051, 2.08962025316, 2.05810126582, 2.02658227848, 1.99506329114, 1.9635443038, 1.93202531646, 1.90050632911, 1.86898734177, 1.83746835443, 1.80594936709, 1.77443037975, 1.74291139241, 1.71139240506, 1.67987341772, 1.64835443038, 1.61683544304, 1.5853164557, 1.55379746835, 1.52227848101, 1.49075949367, 1.45924050633, 1.42772151899, 1.39620253165, 1.3646835443, 1.33316455696, 1.30164556962, 1.27012658228, 1.23860759494, 1.20708860759, 1.17556962025, 1.14405063291, 1.11253164557, 1.08101265823, 1.04949367089, 1.01797468354, 0.986455696203, 0.954936708861, 0.923417721519, 0.891898734177, 0.860379746835, 0.828860759494, 0.797341772152, 0.76582278481, 0.734303797468, 0.702784810127, 0.671265822785, 0.639746835443, 0.608227848101, 0.576708860759, 0.545189873418, 0.513670886076, 0.482151898734, 0.450632911392, 0.419113924051, 0.387594936709, 0.356075949367, 0.324556962025, 0.293037974684, 0.261518987342, 0.23, 0.23], 
  "y": [968.14708861, 938.518300805, 941.311646269, 981.762254775, 1061.71670923, 1177.53941873, 1318.48007016, 1474.24010619, 1638.5890915, 1808.91217506, 1986.75141342, 2162.71279631, 2344.36391529, 2547.67388473, 2775.90895377, 3019.44978364, 3266.0504339, 3514.95905634, 3769.72251314, 4033.96614046, 4311.09997743, 4603.37517583, 4911.03821055, 5232.15470067, 5563.34812275, 5901.446997, 6251.66703592, 6614.7103385, 6987.6308943, 7366.92756411, 7748.65124569, 8128.73173306, 8503.98700717, 8873.44282132, 9236.48265523, 9592.56250483, 9941.23436016, 10282.1494168, 10615.0506806, 10939.761149, 11256.1713323, 11564.2279631, 11863.9245541, 12155.293838, 12438.4018468, 12713.3432931, 12980.2379085, 13239.2274198, 13490.4728833, 13734.1521362, 13970.4571706, 14199.5912851, 14421.7659273, 14637.1972094, 14846.1021545, 15048.6948029, 15245.1823706, 15435.7616865, 15620.61614, 15799.9133343, 15973.8035747, 16142.4192389, 16305.8749832, 16464.2686709, 16617.6828555, 16766.1866338, 16909.8376873, 17048.6843583, 17182.7676394, 17312.1229939, 17436.7819602, 17556.7735208, 17672.125238, 17782.8641711, 17889.0175997, 17990.6135798, 18087.6813595, 18180.2516801, 18268.3569854, 18352.0315591, 15605.0724804, 15645.9218557, 15678.069513, 15701.4705546, 15716.0782432, 15721.844139, 15718.7183086, 15706.6496269, 15685.5861923, 15655.4758829, 15616.2670795, 15567.9095835, 15510.3557523, 15443.5618677, 15367.489741, 15282.1085335, 15187.3967454, 15083.3442922, 14969.9545461, 14847.2461893, 14715.2546968, 14574.033265, 14423.6530182, 14264.2023782, 14095.7855531, 13918.5201906, 13732.5343255, 13537.9628169, 13334.9435066, 13123.6133256, 12904.1045403, 12676.5412679, 12441.0363194, 12197.6883508, 11946.5792371, 11687.7715239, 11421.3057615, 11147.1974813, 10865.433534, 10575.9674712, 10278.7136242, 9973.53954454, 9660.25656119, 9338.60849032, 9008.2591566, 8668.78057435, 8319.64555239, 7960.2309054, 7589.86154319, 7211.78003489, 6831.11443822, 6451.1329907, 6075.22503359, 5707.22787118, 5351.53393653, 5011.49720121, 4684.7062607, 4368.19350682, 4059.25280836, 3756.62017667, 3461.21247887, 3175.95125899, 2904.91694843, 2652.40527558, 2424.17759587, 2225.66500632, 2040.95477832, 1855.50273626, 1667.65029243, 1488.34191875, 1321.27605042, 1170.74113709, 1034.53241422, 909.299546556, 789.666201597, 666.172665216, 527.719262777, 371.052799804, 199.358823338, 16.3595908677, 968.14708861], 
  "fill": "tozerox", 
  "fillcolor": "rgba(231,107,243,0.2)", 
  "line": {
    "color": "transparent", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Ideal", 
  "showlegend": False, 
  "type": "scatter", 
  "uid": "133c9d", 
  "xaxis": "x2", 
  "yaxis": "y"
}
trace11 = {
  "x": [0.33, 0.352405063291, 0.374810126582, 0.397215189873, 0.419620253165, 0.442025316456, 0.464430379747, 0.486835443038, 0.509240506329, 0.53164556962, 0.554050632911, 0.576455696203, 0.598860759494, 0.621265822785, 0.643670886076, 0.666075949367, 0.688481012658, 0.710886075949, 0.733291139241, 0.755696202532, 0.778101265823, 0.800506329114, 0.822911392405, 0.845316455696, 0.867721518987, 0.890126582278, 0.91253164557, 0.934936708861, 0.957341772152, 0.979746835443, 1.00215189873, 1.02455696203, 1.04696202532, 1.06936708861, 1.0917721519, 1.11417721519, 1.13658227848, 1.15898734177, 1.18139240506, 1.20379746835, 1.22620253165, 1.24860759494, 1.27101265823, 1.29341772152, 1.31582278481, 1.3382278481, 1.36063291139, 1.38303797468, 1.40544303797, 1.42784810127, 1.45025316456, 1.47265822785, 1.49506329114, 1.51746835443, 1.53987341772, 1.56227848101, 1.5846835443, 1.60708860759, 1.62949367089, 1.65189873418, 1.67430379747, 1.69670886076, 1.71911392405, 1.74151898734, 1.76392405063, 1.78632911392, 1.80873417722, 1.83113924051, 1.8535443038, 1.87594936709, 1.89835443038, 1.92075949367, 1.94316455696, 1.96556962025, 1.98797468354, 2.01037974684, 2.03278481013, 2.05518987342, 2.07759493671, 2.1], 
  "y": [911.963231156, 919.100115441, 933.757434017, 955.867885865, 985.364169967, 1022.17892919, 1066.31975956, 1117.90351974, 1176.30681608, 1235.80682658, 1296.92299977, 1361.80793143, 1432.61421735, 1511.49445327, 1600.60123499, 1702.08715826, 1818.10481886, 1949.62276271, 2091.50703261, 2245.19444694, 2413.47566575, 2599.14134907, 2804.98215695, 3033.78874943, 3286.52499596, 3556.44347483, 3839.70213176, 4139.92740097, 4433.57433023, 4694.0101763, 4894.78625403, 5044.5767009, 5182.32932276, 5302.30419409, 5399.57323832, 5476.75493012, 5536.46774418, 5581.3301552, 5613.96063784, 5636.9776668, 5652.99971676, 5664.64526241, 5674.53277843, 5685.2807395, 5699.50762031, 5719.83189555, 5748.87203989, 5789.24652803, 5843.57383465, 5914.47243443, 6004.56080205, 6116.45741221, 6252.78073959, 6409.88614705, 6575.21403066, 6748.37460597, 6929.45784926, 7118.55373682, 7315.75224491, 7521.14334982, 7734.81702784, 7956.86325523, 8187.37200829, 8426.43326329, 8674.13699651, 8930.57318424, 9195.83180274, 9470.00282831, 9753.17623721, 10045.4420057, 10346.8901102, 10657.6105268, 10977.6932319, 11307.2282017, 11646.3054125, 11995.0148407, 12353.4464624, 12721.690254, 13099.8361917, 13487.9742518], 
  "line": {
    "color": "rgb(248,118,109)", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Fair", 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "2a6468", 
  "xaxis": "x", 
  "yaxis": "y2"
}
trace12 = {
  "x": [0.24, 0.274936708861, 0.309873417722, 0.344810126582, 0.379746835443, 0.414683544304, 0.449620253165, 0.484556962025, 0.519493670886, 0.554430379747, 0.589367088608, 0.624303797468, 0.659240506329, 0.69417721519, 0.729113924051, 0.764050632911, 0.798987341772, 0.833924050633, 0.868860759494, 0.903797468354, 0.938734177215, 0.973670886076, 1.00860759494, 1.0435443038, 1.07848101266, 1.11341772152, 1.14835443038, 1.18329113924, 1.2182278481, 1.25316455696, 1.28810126582, 1.32303797468, 1.35797468354, 1.39291139241, 1.42784810127, 1.46278481013, 1.49772151899, 1.53265822785, 1.56759493671, 1.60253164557, 1.63746835443, 1.67240506329, 1.70734177215, 1.74227848101, 1.77721518987, 1.81215189873, 1.84708860759, 1.88202531646, 1.91696202532, 1.95189873418, 1.98683544304, 2.0217721519, 2.05670886076, 2.09164556962, 2.12658227848, 2.16151898734, 2.1964556962, 2.23139240506, 2.26632911392, 2.30126582278, 2.33620253165, 2.37113924051, 2.40607594937, 2.44101265823, 2.47594936709, 2.51088607595, 2.54582278481, 2.58075949367, 2.61569620253, 2.65063291139, 2.68556962025, 2.72050632911, 2.75544303797, 2.79037974684, 2.8253164557, 2.86025316456, 2.89518987342, 2.93012658228, 2.96506329114, 3], 
  "y": [396.40132903, 503.021140416, 615.763964112, 734.273278285, 858.192561104, 986.620392128, 1119.92172838, 1259.67749027, 1406.85242427, 1552.58512206, 1698.10805274, 1849.4749931, 2012.73971995, 2193.95601007, 2390.39167988, 2596.98719259, 2827.70345259, 3084.72402547, 3360.14028993, 3645.74265104, 3933.32151386, 4214.66728345, 4482.34233386, 4750.13646228, 5033.00569427, 5340.35009906, 5677.24124179, 6035.71983931, 6408.9990188, 6790.43022624, 7173.36490759, 7551.1545088, 7917.15047585, 8264.70425469, 8587.1672913, 8877.89103163, 9130.22692164, 9354.34396978, 9569.33208528, 9775.26481595, 9972.13856067, 10159.9497184, 10338.6946879, 10508.3698682, 10668.9716581, 10820.4964565, 10962.9406624, 11096.3006746, 11220.5728921, 11335.7537136, 11441.8395382, 11538.8267647, 11626.711792, 11705.491019, 11775.1608445, 11835.7176676, 11887.1578871, 11929.4779018, 11962.6741107, 11986.7429127, 12001.6807066, 12007.4838914, 12004.148866, 11991.6720292, 11970.04978, 11939.2785172, 11899.3546397, 11850.2745465, 11792.0346364, 11724.6313083, 11648.0609611, 11562.3199938, 11467.4048052, 11363.3117941, 11250.0373596, 11127.5779005, 10995.9298156, 10855.089504, 10705.0533644, 10545.8177958], 
  "line": {
    "color": "rgb(163,165,0)", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Good", 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "5b18db", 
  "xaxis": "x2", 
  "yaxis": "y2"
}
trace13 = {
  "x": [0.23, 0.256075949367, 0.282151898734, 0.308227848101, 0.334303797468, 0.360379746835, 0.386455696203, 0.41253164557, 0.438607594937, 0.464683544304, 0.490759493671, 0.516835443038, 0.542911392405, 0.568987341772, 0.595063291139, 0.621139240506, 0.647215189873, 0.673291139241, 0.699367088608, 0.725443037975, 0.751518987342, 0.777594936709, 0.803670886076, 0.829746835443, 0.85582278481, 0.881898734177, 0.907974683544, 0.934050632911, 0.960126582278, 0.986202531646, 1.01227848101, 1.03835443038, 1.06443037975, 1.09050632911, 1.11658227848, 1.14265822785, 1.16873417722, 1.19481012658, 1.22088607595, 1.24696202532, 1.27303797468, 1.29911392405, 1.32518987342, 1.35126582278, 1.37734177215, 1.40341772152, 1.42949367089, 1.45556962025, 1.48164556962, 1.50772151899, 1.53379746835, 1.55987341772, 1.58594936709, 1.61202531646, 1.63810126582, 1.66417721519, 1.69025316456, 1.71632911392, 1.74240506329, 1.76848101266, 1.79455696203, 1.82063291139, 1.84670886076, 1.87278481013, 1.89886075949, 1.92493670886, 1.95101265823, 1.97708860759, 2.00316455696, 2.02924050633, 2.0553164557, 2.08139240506, 2.10746835443, 2.1335443038, 2.15962025316, 2.18569620253, 2.2117721519, 2.23784810127, 2.26392405063, 2.29], 
  "y": [443.723147425, 493.975082013, 551.136934641, 615.912729938, 688.01394189, 767.040504012, 852.764575277, 945.568311909, 1045.93585036, 1153.14330193, 1266.45010515, 1385.40554953, 1514.11854066, 1650.71884411, 1790.69776066, 1928.44565724, 2064.31079375, 2206.54272377, 2363.52807606, 2543.65347938, 2755.28172731, 2996.59498441, 3258.74834598, 3537.2181673, 3827.48080364, 4125.01261027, 4425.28994246, 4723.7891555, 5015.98660465, 5297.35864518, 5563.4931355, 5827.43696192, 6099.61455117, 6378.73569659, 6663.51019147, 6952.64782916, 7244.85840297, 7538.85170622, 7833.33753223, 8127.02567433, 8418.61148171, 8705.78532807, 8987.5308987, 9263.82769784, 9534.65522972, 9799.99299858, 10059.8205086, 10314.1172641, 10562.8627693, 10806.0365284, 11043.6180456, 11275.5868252, 11501.9223714, 11722.6041884, 11937.6117804, 12146.9246518, 12350.5223067, 12548.3842493, 12740.489984, 12926.8190148, 13107.3508461, 13282.0649821, 13450.940927, 13613.9581851, 13771.0962606, 13922.3346576, 14067.6528805, 14207.0304335, 14340.4468208, 14467.8815467, 14589.3141153, 14704.7240309, 14814.0907978, 14917.3939201, 15014.6129021, 15105.7272481, 15190.7164622, 15269.5600487, 15342.2375119, 15408.7283559], 
  "line": {
    "color": "rgb(0,191,125)", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Very Good", 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "2cbf43", 
  "xaxis": "x3", 
  "yaxis": "y2"
}
trace14 = {
  "x": [0.25, 0.280759493671, 0.311518987342, 0.342278481013, 0.373037974684, 0.403797468354, 0.434556962025, 0.465316455696, 0.496075949367, 0.526835443038, 0.557594936709, 0.58835443038, 0.619113924051, 0.649873417722, 0.680632911392, 0.711392405063, 0.742151898734, 0.772911392405, 0.803670886076, 0.834430379747, 0.865189873418, 0.895949367089, 0.926708860759, 0.95746835443, 0.988227848101, 1.01898734177, 1.04974683544, 1.08050632911, 1.11126582278, 1.14202531646, 1.17278481013, 1.2035443038, 1.23430379747, 1.26506329114, 1.29582278481, 1.32658227848, 1.35734177215, 1.38810126582, 1.41886075949, 1.44962025316, 1.48037974684, 1.51113924051, 1.54189873418, 1.57265822785, 1.60341772152, 1.63417721519, 1.66493670886, 1.69569620253, 1.7264556962, 1.75721518987, 1.78797468354, 1.81873417722, 1.84949367089, 1.88025316456, 1.91101265823, 1.9417721519, 1.97253164557, 2.00329113924, 2.03405063291, 2.06481012658, 2.09556962025, 2.12632911392, 2.15708860759, 2.18784810127, 2.21860759494, 2.24936708861, 2.28012658228, 2.31088607595, 2.34164556962, 2.37240506329, 2.40316455696, 2.43392405063, 2.4646835443, 2.49544303797, 2.52620253165, 2.55696202532, 2.58772151899, 2.61848101266, 2.64924050633, 2.68], 
  "y": [626.03593711, 672.042787867, 729.163613211, 795.530411654, 871.912451923, 959.315935396, 1058.44080209, 1168.04825622, 1285.58157973, 1412.43951327, 1550.11455181, 1700.09919028, 1863.88592364, 2042.96724683, 2238.84065824, 2463.31337157, 2719.63439643, 2997.89299769, 3288.17844022, 3580.57998891, 3865.18690863, 4132.08846427, 4387.8677922, 4651.25519721, 4915.73934002, 5174.43827002, 5428.01739504, 5684.35105002, 5946.13549203, 6216.04964143, 6493.43622393, 6775.86755504, 7062.47565886, 7352.39255946, 7644.75028092, 7938.68084733, 8233.31628277, 8527.78861132, 8821.22985706, 9112.77204408, 9401.54719646, 9686.68733828, 9967.32449361, 10242.5752009, 10509.3305974, 10765.6924279, 11011.606201, 11247.0174259, 11471.8716112, 11686.1142659, 11889.690899, 12082.5470192, 12264.6281355, 12435.8797567, 12596.2473918, 12745.6765496, 12884.1127391, 13011.501469, 13127.7882484, 13232.918586, 13326.8379908, 13409.4919716, 13480.8260374, 13540.785697, 13589.3164593, 13626.3638332, 13651.8733276, 13665.7904514, 13668.0607134, 13658.6296226, 13637.4426878, 13604.445418, 13559.5833219, 13502.8019086, 13434.0466868, 13353.2631655, 13260.3968536, 13155.3932599, 13038.1978934, 12908.7562628], 
  "line": {
    "color": "rgb(0,176,246)", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Premium", 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "08a56c", 
  "xaxis": "x", 
  "yaxis": "y"
}
trace15 = {
  "x": [0.23, 0.261518987342, 0.293037974684, 0.324556962025, 0.356075949367, 0.387594936709, 0.419113924051, 0.450632911392, 0.482151898734, 0.513670886076, 0.545189873418, 0.576708860759, 0.608227848101, 0.639746835443, 0.671265822785, 0.702784810127, 0.734303797468, 0.76582278481, 0.797341772152, 0.828860759494, 0.860379746835, 0.891898734177, 0.923417721519, 0.954936708861, 0.986455696203, 1.01797468354, 1.04949367089, 1.08101265823, 1.11253164557, 1.14405063291, 1.17556962025, 1.20708860759, 1.23860759494, 1.27012658228, 1.30164556962, 1.33316455696, 1.3646835443, 1.39620253165, 1.42772151899, 1.45924050633, 1.49075949367, 1.52227848101, 1.55379746835, 1.5853164557, 1.61683544304, 1.64835443038, 1.67987341772, 1.71139240506, 1.74291139241, 1.77443037975, 1.80594936709, 1.83746835443, 1.86898734177, 1.90050632911, 1.93202531646, 1.9635443038, 1.99506329114, 2.02658227848, 2.05810126582, 2.08962025316, 2.12113924051, 2.15265822785, 2.18417721519, 2.21569620253, 2.24721518987, 2.27873417722, 2.31025316456, 2.3417721519, 2.37329113924, 2.40481012658, 2.43632911392, 2.46784810127, 2.49936708861, 2.53088607595, 2.56240506329, 2.59392405063, 2.62544303797, 2.65696202532, 2.68848101266, 2.72], 
  "y": [492.253339739, 568.938562071, 656.182223036, 754.740758776, 863.944687223, 983.602810162, 1113.88980836, 1254.3862602, 1404.6651143, 1565.09411274, 1737.54666609, 1915.18154437, 2099.93332577, 2294.31433152, 2500.78698004, 2721.81368975, 2959.22785474, 3209.93800239, 3472.83688607, 3747.58930967, 4033.86007705, 4331.3139921, 4639.61585868, 4958.43048069, 5287.42266198, 5626.49046676, 5979.44745355, 6344.96768605, 6719.3819425, 7099.02100116, 7480.21564029, 7859.29663813, 8232.10895628, 8596.54418685, 8952.63161479, 9300.41083071, 9639.92142524, 9971.20298899, 10294.2951126, 10609.2373866, 10916.0694017, 11214.8307486, 11505.5610177, 11788.2997997, 12063.0866853, 12329.9612651, 12588.9631297, 12840.1318696, 13083.5070756, 13319.1283382, 13547.0352481, 13767.2673959, 13979.8643721, 14184.8657675, 14382.3111725, 14572.240178, 14754.6923744, 14929.7073524, 15097.3247025, 15257.5840156, 15410.524882, 15556.1868925, 15694.6096377, 15825.8327081, 15949.8956945, 16066.8381874, 16176.6997775, 16279.5200553, 16375.3386115, 16464.1950367, 16546.1289215, 16621.1798566, 16689.3874325, 16750.7912399, 16805.4308693, 16853.3459115, 16894.5759571, 16929.1605965, 16957.1394205, 16978.5520198], 
  "line": {
    "color": "rgb(231,107,243)", 
    "dash": "solid", 
    "shape": "linear", 
    "width": 2
  }, 
  "marker": {
    "color": "rgb(67, 67, 67)", 
    "line": {
      "color": "rgb(140, 140, 140)", 
      "width": 0.5
    }
  }, 
  "mode": "lines", 
  "name": "Ideal", 
  "showlegend": True, 
  "type": "scatter", 
  "uid": "8b4bfb", 
  "xaxis": "x2", 
  "yaxis": "y"
}
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15])
layout = {
  "annotations": [
    {
      "x": 0.161666666667, 
      "y": 0.9925, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "Fair", 
      "textangle": 0, 
      "xanchor": "center", 
      "xref": "paper", 
      "yanchor": "top", 
      "yref": "paper"
    }, 
    {
      "x": 0.495, 
      "y": 0.9925, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "Good", 
      "textangle": 0, 
      "xanchor": "center", 
      "xref": "paper", 
      "yanchor": "top", 
      "yref": "paper"
    }, 
    {
      "x": 0.828333333333, 
      "y": 0.9925, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "Very Good", 
      "textangle": 0, 
      "xanchor": "center", 
      "xref": "paper", 
      "yanchor": "top", 
      "yref": "paper"
    }, 
    {
      "x": 0.161666666667, 
      "y": 0.4925, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "Premium", 
      "textangle": 0, 
      "xanchor": "center", 
      "xref": "paper", 
      "yanchor": "top", 
      "yref": "paper"
    }, 
    {
      "x": 0.495, 
      "y": 0.4925, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "Ideal", 
      "textangle": 0, 
      "xanchor": "center", 
      "xref": "paper", 
      "yanchor": "top", 
      "yref": "paper"
    }, 
    {
      "x": 0.5, 
      "y": -0.05, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "carat", 
      "textangle": 0, 
      "xanchor": "auto", 
      "xref": "paper", 
      "yanchor": "top", 
      "yref": "paper"
    }, 
    {
      "x": -0.0401664145234, 
      "y": 0.478494623656, 
      "ax": 0, 
      "ay": 0, 
      "font": {"size": 14}, 
      "showarrow": False, 
      "text": "price", 
      "textangle": -90, 
      "xanchor": "auto", 
      "xref": "paper", 
      "yanchor": "auto", 
      "yref": "paper"
    }
  ], 
  "autosize": True, 
  "height": 761, 
  "legend": {
    "x": 1.05, 
    "y": 0.5, 
    "bgcolor": "rgb(255,255,255)", 
    "bordercolor": "transparent", 
    "font": {"family": ""}, 
    "xanchor": "center", 
    "yanchor": "top"
  }, 
  "margin": {
    "r": 0, 
    "t": 30, 
    "l": 60
  }, 
  "paper_bgcolor": "rgb(255,255,255)", 
  "plot_bgcolor": "rgb(229,229,229)", 
  "showlegend": False, 
  "titlefont": {"family": ""}, 
  "width": 1412, 
  "xaxis": {
    "anchor": "y", 
    "autorange": False, 
    "domain": [0, 0.303333333333], 
    "gridcolor": "rgb(255,255,255)", 
    "range": [0.0915, 3.1385], 
    "showgrid": True, 
    "showline": False, 
    "showticklabels": True, 
    "tickcolor": "rgb(127,127,127)", 
    "ticks": "outside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "xaxis2": {
    "anchor": "y", 
    "autorange": False, 
    "domain": [0.353333333333, 0.656666666667], 
    "gridcolor": "rgb(255,255,255)", 
    "range": [0.0915, 3.1385], 
    "showgrid": True, 
    "showline": False, 
    "showticklabels": True, 
    "tickcolor": "rgb(127,127,127)", 
    "ticks": "outside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "xaxis3": {
    "anchor": "y", 
    "autorange": False, 
    "domain": [0.686666666667, 1], 
    "gridcolor": "rgb(255,255,255)", 
    "range": [0.0915, 3.1385], 
    "showgrid": True, 
    "showline": False, 
    "showticklabels": True, 
    "tickcolor": "rgb(127,127,127)", 
    "ticks": "outside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis": {
    "anchor": "x", 
    "autorange": False, 
    "domain": [0, 0.43], 
    "gridcolor": "rgb(255,255,255)", 
    "range": [-2424.9492063, 19760], 
    "showgrid": True, 
    "showline": False, 
    "showticklabels": True, 
    "tickcolor": "rgb(127,127,127)", 
    "ticks": "outside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis2": {
    "anchor": "x", 
    "autorange": False, 
    "domain": [0.52, 0.95], 
    "gridcolor": "rgb(255,255,255)", 
    "range": [-2424.9492063, 19764.6166289], 
    "showgrid": True, 
    "showline": False, 
    "showticklabels": True, 
    "tickcolor": "rgb(127,127,127)", 
    "ticks": "outside", 
    "type": "linear", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)