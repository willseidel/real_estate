#= Parameters
#- last 6 months from Feb 21 2018
#- single family homes
#- el segundo, ca
#= data structure
#entry = [sale_price, #BR, #BA, built sqft, lot sqft, address]
import numpy as np
from sklearn import linear_model
import geopy
import math

import pandas as pd
redfin_df = pd.read_csv('redfin_data.csv') #this should point to a csv file generated by redfin's 'Download All' link that is found at the bottom of the table view of search results.
sales = []

number_to_query = 1000
for i in range(len(redfin_df)):
    if i>number_to_query:
        break
    if math.isnan(redfin_df['LOT SIZE'][i]) or math.isnan(redfin_df['PRICE'][i]) or math.isnan(redfin_df['BEDS'][i]) or math.isnan(redfin_df['BATHS'][i]) or math.isnan(redfin_df['SQUARE FEET'][i]):
        print 'skipping this entry because of nan'
    else:
        sales.append([redfin_df['PRICE'][i],redfin_df['BEDS'][i],redfin_df['BATHS'][i],redfin_df['SQUARE FEET'][i],redfin_df['LOT SIZE'][i],redfin_df['ADDRESS'][i] + ', ' + redfin_df['CITY'][i] + ' ' + redfin_df['STATE'][i], redfin_df['LATITUDE'][i], redfin_df['LONGITUDE'][i]])

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
print sales_fit.predict(predict_inputs)


#building sale price/linear cost ratios
max_ratio = 0
min_ratio = 100
ratios = np.array([])
for entry in sales:
    try:
        entry.append(entry[0]/sales_fit.predict(np.reshape(entry[3:5], (1,-1)))[0])
        if entry[8] < min_ratio:
            min_ratio = entry[8]
        if entry[8] > max_ratio:
            max_ratio = entry[8]

        ratios = np.append(ratios, entry[8])

    except:
        print 'could not create sale/value ratio for: ' + entry[5]

print np.mean(ratios)
print np.std(ratios)

import matplotlib.pyplot as plt

for i in range(len(sales)):
    try:
        plt.scatter(sales[i][7], sales[i][6], c = sales[i][8],cmap = 'viridis', vmin = np.mean(ratios) - np.std(ratios), vmax = np.mean(ratios) + np.std(ratios))
    except:
        print 'could not plot data for: ' + sales[i][5]

plt.show()
