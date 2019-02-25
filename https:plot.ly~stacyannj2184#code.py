# Get this figure: fig = py.get_figure("https://plot.ly/~stacyannj/2184/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~stacyannj/2184/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Monthly household estimates, 1995 through Sept. 2015", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~stacyannj/2184/").get_data()[0]["y"]

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
  "x": ["Jan-96", "Feb-96", "Mar-96", "Apr-96", "May-96", "Jun-96", "Jul-96", "Aug-96", "Sep-96", "Oct-96", "Nov-96", "Dec-96", "Jan-97", "Feb-97", "Mar-97", "Apr-97", "May-97", "Jun-97", "Jul-97", "Aug-97", "Sep-97", "Oct-97", "Nov-97", "Dec-97", "Jan-98", "Feb-98", "Mar-98", "Apr-98", "May-98", "Jun-98", "Jul-98", "Aug-98", "Sep-98", "Oct-98", "Nov-98", "Dec-98", "Jan-99", "Feb-99", "Mar-99", "Apr-99", "May-99", "Jun-99", "Jul-99", "Aug-99", "Sep-99", "Oct-99", "Nov-99", "Dec-99", "Jan-00", "Feb-00", "Mar-00", "Apr-00", "May-00", "Jun-00", "Jul-00", "Aug-00", "Sep-00", "Oct-00", "Nov-00", "Dec-00", "Jan-01", "Feb-01", "Mar-01", "Apr-01", "May-01", "Jun-01", "Jul-01", "Aug-01", "Sep-01", "Oct-01", "Nov-01", "Dec-01", "Jan-02", "Feb-02", "Mar-02", "Apr-02", "May-02", "Jun-02", "Jul-02", "Aug-02", "Sep-02", "Oct-02", "Nov-02", "Dec-02", "Jan-03", "Feb-03", "Mar-03", "Apr-03", "May-03", "Jun-03", "Jul-03", "Aug-03", "Sep-03", "Oct-03", "Nov-03", "Dec-03", "Jan-04", "Feb-04", "Mar-04", "Apr-04", "May-04", "Jun-04", "Jul-04", "Aug-04", "Sep-04", "Oct-04", "Nov-04", "Dec-04", "Jan-05", "Feb-05", "Mar-05", "Apr-05", "May-05", "Jun-05", "Jul-05", "Aug-05", "Sep-05", "Oct-05", "Nov-05", "Dec-05", "Jan-06", "Feb-06", "Mar-06", "Apr-06", "May-06", "Jun-06", "Jul-06", "Aug-06", "Sep-06", "Oct-06", "Nov-06", "Dec-06", "Jan-07", "Feb-07", "Mar-07", "Apr-07", "May-07", "Jun-07", "Jul-07", "Aug-07", "Sep-07", "Oct-07", "Nov-07", "Dec-07", "Jan-08", "Feb-08", "Mar-08", "Apr-08", "May-08", "Jun-08", "Jul-08", "Aug-08", "Sep-08", "Oct-08", "Nov-08", "Dec-08", "Jan-09", "Feb-09", "Mar-09", "Apr-09", "May-09", "Jun-09", "Jul-09", "Aug-09", "Sep-09", "Oct-09", "Nov-09", "Dec-09", "Jan-10", "Feb-10", "Mar-10", "Apr-10", "May-10", "Jun-10", "Jul-10", "Aug-10", "Sep-10", "Oct-10", "Nov-10", "Dec-10", "Jan-11", "Feb-11", "Mar-11", "Apr-11", "May-11", "Jun-11", "Jul-11", "Aug-11", "Sep-11", "Oct-11", "Nov-11", "Dec-11", "Jan-12", "Feb-12", "Mar-12", "Apr-12", "May-12", "Jun-12", "Jul-12", "Aug-12", "Sep-12", "Oct-12", "Nov-12", "Dec-12", "Jan-13", "Feb-13", "Mar-13", "Apr-13", "May-13", "Jun-13", "Jul-13", "Aug-13", "Sep-13", "Oct-13", "Nov-13", "Dec-13", "Jan-14", "Feb-14", "Mar-14", "Apr-14", "May-14", "Jun-14", "Jul-14", "Aug-14", "Sep-14", "Oct-14", "Nov-14", "Dec-14", "Jan-15", "Feb-15", "Mar-15", "Apr-15", "May-15", "Jun-15", "Jul-15", "Aug-15", "Sep-15"], 
  "y": ["526000", "765000", "809000", "1083000", "1144000", "1223000", "1243000", "1166000", "1329000", "867000", "893000", "944000", "959000", "1408000", "1320000", "1060000", "933000", "898000", "1096000", "1295000", "1549000", "1512000", "1538000", "1031000", "1501000", "1189000", "1465000", "1644000", "1327000", "1455000", "1147000", "975000", "1055000", "1168000", "1283000", "1783000", "1410000", "1422000", "1291000", "992000", "1438000", "1453000", "1620000", "1820000", "1504000", "1425000", "1287000", "1039000", "821000", "1071000", "606000", "702000", "498000", "242000", "677000", "481000", "822000", "1025000", "1055000", "1540000", "1579000", "1322000", "1599000", "1529000", "1454000", "1424000", "992000", "1119000", "1028000", "1072000", "1305000", "1044000", "-2204000", "-2444000", "-2470000", "-2035000", "-1715000", "-1713000", "-1585000", "-1638000", "-1845000", "-2095000", "-2373000", "-2411000", "1032000", "1047000", "881000", "752000", "415000", "426000", "214000", "342000", "469000", "413000", "514000", "627000", "290000", "574000", "525000", "469000", "701000", "602000", "1065000", "1556000", "1492000", "1761000", "1826000", "1476000", "1973000", "2064000", "1618000", "1621000", "1664000", "2066000", "1951000", "1422000", "1312000", "1125000", "1221000", "1681000", "1626000", "1298000", "1678000", "1793000", "1751000", "1256000", "1174000", "1163000", "1256000", "1384000", "1080000", "667000", "405000", "332000", "508000", "844000", "918000", "911000", "691000", "665000", "652000", "719000", "938000", "1183000", "1117000", "1168000", "1074000", "918000", "609000", "1136000", "1377000", "1448000", "1468000", "1334000", "917000", "675000", "155000", "545000", "932000", "991000", "800000", "882000", "-274000", "-297000", "-242000", "-375000", "5000", "-60000", "607000", "468000", "371000", "20000", "349000", "-82000", "314000", "177000", "876000", "818000", "606000", "798000", "641000", "338000", "-37000", "256000", "274000", "244000", "1657000", "1925000", "1323000", "1617000", "1664000", "1624000", "1933000", "1948000", "1994000", "1673000", "1644000", "1864000", "1179000", "1191000", "1066000", "983000", "886000", "973000", "526000", "547000", "490000", "317000", "781000", "335000", "42000", "79000", "97000", "-110000", "103000", "-205000", "-22000", "14000", "197000", "639000", "274000", "434000", "560000", "249000", "818000", "1435000", "1618000", "2001000", "1585700", "1525200", "1489800", "2330600", "1901000", "2245700", "2095500", "2118200", "1917200"], 
  "connectgaps": False, 
  "fill": "tozeroy", 
  "line": {
    "color": "rgb(0, 51, 102)", 
    "shape": "linear", 
    "width": 1
  }, 
  "marker": {"color": "rgb(0, 51, 102)"}, 
  "mode": "lines", 
  "name": "Col3", 
  "type": "scatter", 
  "uid": "1c333a", 
  "xsrc": "stacyannj:2182:a97151", 
  "ysrc": "stacyannj:2182:7fda7c"
}
data = Data([trace1])
layout = {
  "autosize": False, 
  "height": 400, 
  "margin": {
    "r": 60, 
    "t": 80, 
    "b": 90, 
    "l": 60, 
    "pad": 0
  }, 
  "title": "Household growth, 1995 through Sept. 2015", 
  "titlefont": {
    "family": "Droid Serif, serif", 
    "size": 18
  }, 
  "width": 545, 
  "xaxis": {
    "autorange": True, 
    "dtick": 12, 
    "range": [0, 236], 
    "showgrid": False, 
    "tickangle": -45, 
    "tickfont": {
      "family": "Droid Sans, sans-serif", 
      "size": 11
    }, 
    "tickmode": "linear", 
    "title": "Source: <a href=\"http://www.census.gov/housing/hvs/data/histtables.html\">U.S. Census Bureau</a>", 
    "titlefont": {
      "family": "Droid Sans, sans-serif", 
      "size": 11
    }, 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [-2736700, 2597300], 
    "tickfont": {
      "family": "Droid Sans, sans-serif", 
      "size": 11
    }, 
    "titlefont": {"family": "Droid Sans, sans-serif"}, 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)