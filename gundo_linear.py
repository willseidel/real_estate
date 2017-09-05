#= Parameters
#- last 90 days
#- single family homes
#- north of grand
#- south of walnut
#- west of center
#= data structure
#entry = [sale_price, #BR, #BA, built sqft, lot sqft, address]
import numpy as np
from sklearn import linear_model

sales = []

sales.append([1175000,2,1,1294,7927,'830 maryland'])
sales.append([1240000,3,1,1038,6660,'646 maryland'])
sales.append([1099000,3,2,1600,6000,'602 lomita'])
sales.append([1412500,6,4,2943,4948,'400 bungalow'])
sales.append([850000,2,2,1120,2692,'815 penn'])
sales.append([1866970,4,3,2845,5253,'619 eucalyptus'])
sales.append([1040684,3,2,672,6714,'218 w oak'])
sales.append([1130000,3,2,1026,4791,'811 concord'])
sales.append([1300000,3,3,1520,7309,'300 w sycamore'])
sales.append([1275000,2,1,1194,7152,'521 concord'])
sales.append([1120000,4,1,1197,8232,'414 w oak'])
sales.append([1400000,3,2,1564,6398,'432 loma vista'])
sales.append([1229000,3,2,1528,4922,'606 w mariposa'])
sales.append([910000,2,1,1236,3963,'631 loma vista'])
sales.append([1100000,2,1,948,8253,'650 w maple'])
sales.append([1268500,4,3,1920,7016,'716 w oak'])
sales.append([1381000,4,3,2919,5044,'734 redwood'])

sales_data = []
for home in sales:
    sales_data.append(home[:-1])

sales_array = np.array(sales_data)
sales_fit = linear_model.LinearRegression()
sales_fit.fit(sales_array[:,1:5],sales_array[:,0])

print sales_fit.coef_

predict_inputs = [3,2,1000,6000]

print sales_fit.predict(predict_inputs)
