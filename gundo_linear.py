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

sales = []

sales.append([1300000,3,3,1520,7308,'300 w sycamore'])
sales.append([1130000,3,2,1026,5018,'811 concord pl'])
sales.append([1100000,2,1,948,8253,'650 w maple'])
sales.append([1268500,4,3,1920,7017,'716 w oak'])
sales.append([1255000,5,2,2599,5888,'728 loma vista'])
sales.append([1319219,4,1,1197,8233,'414 w oak'])
sales.append([1000000,2,1,672,6715,'218 w oak'])
sales.append([1485000,2,1,2044,4967,'676 w palm'])
sales.append([910000,3,1,1236,3954,'631 loma vista'])
sales.append([1229000,3,2,1528,4923,'606 w mariposa'])
sales.append([1275000,2,1,1194,7151,'521 concord'])
sales.append([1400000,3,2,1564,6400,'423 loma vista'])
sales.append([1603000,4,3,3555,7150,'423 virginia'])



sales_data = []
for home in sales:
    sales_data.append(home[:-1])

sales_array = np.array(sales_data)
sales_fit = linear_model.LinearRegression()
sales_fit.fit(sales_array[:,3:5],sales_array[:,0])

print sales_fit.coef_
print sales_fit.intercept_

predict_inputs = [1000,6000]

print sales_fit.predict(predict_inputs)
