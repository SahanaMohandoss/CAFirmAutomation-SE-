import pandas as pd
import collections
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import math

class regModel:
	def model(self,service,hrs):
		#Read the dataset into a pandas dataframe
		dfs = pd.read_excel("regression_dataset.xlsx", sheet_name="Sheet4")
		#print(dfs.head())
		type_split=collections.OrderedDict()
		#Create sub datasets depending on the type of service.
		for i,j in dfs.groupby(['Type']):
			name=i
			type_split.update({''+name:j.reset_index(drop=True)})
		#print(set(dfs['Type']))
		models=[]
		#Build a regression model for each type of service and store them in models
		for key,value in type_split.items():
			regr = linear_model.LinearRegression()
			arr1=np.array(value['Hours'])
			arr1=np.reshape(arr1, (-1, 1))
			#print(len(arr1))
			regr.fit(arr1,value['Amount'])
			#print(key, regr.coef_)
			models.append(regr)
		ctr=0
		min_amt=0
		'''
		for key,value in type_split.items():
			print(key)
		'''
		#print("\n\n")
		#Find the index corresponding to the type of service passed as argument.
		for key,value in type_split.items():
		#print(key)
			if(service.strip().lower() == key.strip().lower()):
				min_amt=min(value['Amount'])
				break
			else:
				ctr=ctr+1
		#print(ctr)
		#If no such type of service exists, return 0.
		if(ctr==len(type_split)):
			return 0
		#Else, predict the amount from the regression model, by taking the number of hours parameter and return the amount predicted.
		else:
			mod=models[ctr]
			val=mod.predict([[hrs]])[0]
			if(val<0.75*min_amt):
				val=min_amt
			#print(val)
			return val

#Example of how to run the code.
if __name__ == '__main__':
	service="Income Tax"
	hours=4
	ob=regModel()
	amt=round(ob.model(service,hours))
	print("Amount is",amt)

    
