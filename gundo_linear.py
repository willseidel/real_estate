#= Parameters
#- last 90 days
#- single family homes
#- north of grand
#- south of walnut
#- west of main
#= data structure
#entry = [sale_price, #BR, #BA, built sqft, lot sqft, address]
import numpy as np
from sklearn import linear_model
import geopy

sales = []

sales.append([1300000,3,3,1520,7308,'300 w sycamore ave, el segundo CA'])
sales.append([1130000,3,2,1026,5018,'811 concord pl, el segundo CA'])
sales.append([1100000,2,1,948,8253,'650 w maple ave, el segundo CA'])
sales.append([1268500,4,3,1920,7017,'716 w oak ave, el segundo CA'])
sales.append([1255000,5,2,2599,5888,'728 loma vista st, el segundo CA'])
sales.append([1319219,4,1,1197,8233,'414 w oak ave, el segundo CA'])
sales.append([1000000,2,1,672,6715,'218 w oak ave, el segundo CA'])
sales.append([1485000,2,1,2044,4967,'676 w palm ave, el segundo CA'])
sales.append([910000,3,1,1236,3954,'631 loma vista st, el segundo CA'])
sales.append([1229000,3,2,1528,4923,'606 w mariposa ave, el segundo CA'])
sales.append([1275000,2,1,1194,7151,'521 concord st, el segundo CA'])
sales.append([1400000,3,2,1564,6400,'423 loma vista st , el segundo CA'])
sales.append([1603000,4,3,3555,7150,'423 virginia st, el segundo CA'])


sales_data = []
for home in sales:
    sales_data.append(home[:-1])

sales_array = np.array(sales_data)
sales_fit = linear_model.LinearRegression()
sales_fit.fit(sales_array[:,3:5], sales_array[:,0])

print sales_fit.coef_
print sales_fit.intercept_

predict_inputs = [1440,6700]
predict_inputs = np.reshape(predict_inputs, (1,-1))
sales[1][3:5]
print sales_fit.predict(np.reshape(sales[1][3:5], (1,-1)))


#building map
from geopy.geocoders import Nominatim
geolocator = Nominatim()

for entry in sales:
    location = geolocator.geocode(entry[5])
    entry.extend([location.latitude, location.longitude])
    entry.append(sales_fit.predict(np.reshape(entry[3:5], (1,-1)))[0])

import matplotlib.pyplot as plt


for i in range(len(sales)):
    plt.scatter(sales[i][6], sales[i][7], c = sales[i][8]/sales[i][0],cmap = 'gray', vmin = 0.85, vmax = 1.15)
    print sales[i][8]/sales[i][0]


plt.show()
