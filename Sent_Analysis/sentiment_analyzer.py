import nltk
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import re
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
#from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from keras.optimizers import SGD
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from keras import regularizers
from keras.layers import Dropout



class SentimentAnalyzer:
	def tokenize(self,txt):
		#Tokenizing the text into sentences.
		stopwords=nltk.corpus.stopwords.words('english')
		sent=sent_tokenize(txt)
		#Tokenizing into words
		from nltk.tokenize import RegexpTokenizer
		tokenizer = RegexpTokenizer(r'\w+')
		text1=tokenizer.tokenize(txt)
   		#print(len(words))
		#Removing stopwords
		text1=[str.lower(word) for word in text1]
		filtered_words = [word for word in text1 if word not in nltk.corpus.stopwords.words('english') and not word.isdigit()]
		stemmer=nltk.stem.porter.PorterStemmer()
		singles = [stemmer.stem(word) for word in filtered_words]
		return singles

	def preprocess(self):
		#print(self.tokenize("This is a sentence that has several interpretations and is subject to the user's perspective"))
		df=pd.read_csv('dataset.csv')
		l1=[]
		ctr=0
		ctr1=0
		ctr2=0
		for i in df['stars']:
		    #global ctr,ctr1,ctr2
		    if i==4 or i==5:
		        l1.append(1)
		        ctr+=1
		    if i==1 or i==2:
		        l1.append(0)
		        ctr1+=1
		    if i==3:
		        l1.append(-1)
		        ctr2+=1
		print(ctr,ctr1,ctr2)
		#Appending the list to the dataframe
		df['Bin_Review']=l1
		#Creating a dataframe with only those binary reviews with values 0 and 1 (removing all the original 3 stars reviews)
		df1=df[['text','Bin_Review']]
		df2=pd.DataFrame()
		list1=df1['text']
		list2=df1['Bin_Review']
		list3=[]
		list4=[]
		for i in range(len(list1)):
		    if list2[i]!=-1:
		        list3.append(list1[i])
		        list4.append(list2[i])
		df2['text']=list3
		df2['Bin_Review']=list4
		#Counting the number of reviews which are rated 0, 1 and -1
		ctr=0
		ctr1=0
		ctr2=0
		for i in df2['Bin_Review']:
		    #global ctr,ctr1
		    if i==0:
		        ctr+=1
		    if i==1:
		        ctr1+=1
		    if i!=0 and i!=1:
		        ctr2+=1
		print(ctr,ctr1,ctr2)
		#Creating a subset of the dataset with equal number of reviews rated 0 and 1.
		ctr3=0
		list1=df2['text']
		list2=df2['Bin_Review']
		list3=[]
		list4=[]
		i=0
		while ctr3<ctr:
		    #global i
		    if(list2[i]==1):
		        list3.append(list1[i])
		        list4.append(list2[i])
		        ctr3+=1
		    i+=1
		list5=[]
		list6=[]
		for i in range(len(list1)):
		    if list2[i]==0:
		        list5.append(list1[i])
		        list6.append(list2[i])

		list7=list3+list5
		list8=list4+list6
		df3=pd.DataFrame()
		#df3 contains this new dataset with equal number of 0 and 1 reviews.
		df3['text']=list7
		df3['Bin_Review']=list8
		print(df3[1:10])
		df3 = df3.sample(frac=1).reset_index(drop=True)
		ctr=0
		ctr1=0
		for i in df3['Bin_Review']:
			#global ctr,ctr1
			if i==0:
			    ctr+=1
			if i==1:
				ctr1+=1
		print(ctr,ctr1)
		toks=[]
		#list stores the tokens of each review
		'''
		for i in range(len(df3)):
			if(i%200==0):
				print(i)
			toks.append(self.tokenize(df3.iloc[i]['text']))
		print(toks[0:2])
		df3['tokens']=toks
		'''
		print(df3.head())
		'''
		tfidf=TfidfVectorizer(tokenizer=self.tokenize)
		tfs=tfidf.fit_transform(df3['text'])
		with open("x_result.pkl", 'wb') as handle:
			pickle.dump(tfidf, handle)
		return tfidf
		'''
		vectorizer = CountVectorizer(decode_error="replace")
		vec_train = vectorizer.fit_transform(df3['text'])
		transformer = TfidfTransformer()
		tfidf = transformer.fit_transform(vec_train)
		df5=pd.DataFrame(tfidf.toarray())
		print(df5.shape)
		#Save vectorizer.vocabulary_
		pickle.dump(vectorizer.vocabulary_,open("feature.pkl","wb"))
		print("Dumped!")
		X_train,X_test,y_train,y_test=train_test_split(df5,df3['Bin_Review'],test_size=0.25)
		print(X_train.shape,y_train.shape)
		print(X_test.shape,y_test.shape)
		clf=svm.SVC(kernel='linear')
		clf.fit(X_train,y_train)
		pred=clf.predict(X_test)
		print(metrics.accuracy_score(y_test, pred))
		#Printing the mean and sd of the accuracy using kfold=10
		accuracies = cross_val_score(estimator = clf, X = X_train, y = y_train, cv = 10)
		mn=accuracies.mean()
		sd=accuracies.std()
		
		print (" \n SVM :-  ") 
		print ("\n mean Accuracy: ")
		print (mn)
		
		print ("\n Standard Deviation:")
		print (sd)
		
		print ("\n Confusion Matrix : ")
		# Making the Confusion Matrix
		cm = confusion_matrix(y_test, pred)
		print(cm)
		#Printing the classification report.
		print ("\n Classification Report : ")
		from sklearn.metrics import classification_report
		print (classification_report(y_test, pred) )

		fpr, tpr, threshold = roc_curve(y_test, pred)
		#Printing the area under the ROC curve.
		roc_auc=roc_auc_score(y_test, pred)
		#Displaying the ROC curve
		print (roc_auc)
		plt.title('Receiver Operating Characteristic')
		plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
		plt.legend(loc = 'lower right')
		plt.plot([0, 1], [0, 1],'r--')
		plt.xlim([0, 1])
		plt.ylim([0, 1])
		plt.ylabel('True Positive Rate')
		plt.xlabel('False Positive Rate')
		plt.show()
		#Creating an ANN model
		model = Sequential()
		model.add(Dense(18143, input_dim=18143, kernel_initializer='normal', activation='relu'))
		model.add(Dropout(0.2))
		model.add(Dense(30, kernel_initializer='normal', activation='relu'))
		model.add(Dropout(0.2))
		model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
		#model.add(Dense(1, kernel_initializer='normal', activation='softmax'))
		# Compile model
		epochs = 50
		learning_rate = 0.01
		decay_rate = learning_rate / epochs
		sgd = SGD(lr=learning_rate, momentum=0.8, decay=0, nesterov=False)
		model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
		
		# Fit the model. We manually provide the train and test partition
		history=model.fit(df5,df3['Bin_Review'],validation_split=0.25,epochs=50, batch_size=32, verbose=2)
		print(history.history.keys())
		plt.plot(history.history['acc'])
		plt.plot(history.history['val_acc'])
		plt.title('model accuracy')
		plt.ylabel('accuracy')
		plt.xlabel('epoch')
		plt.legend(['train', 'test'], loc='upper left')
		plt.show()
		
		plt.plot(history.history['loss'])
		plt.plot(history.history['val_loss'])
		plt.title('model loss')
		plt.ylabel('loss')
		plt.xlabel('epoch')
		plt.legend(['train', 'test'], loc='upper left')
		plt.show()

		pkl_filename = "svm_model.pkl"  
		with open(pkl_filename, 'wb') as file:  
			pickle.dump(clf, file)

	def check(self,test_list):
		#tfidf=self.preprocess()
		#unseen_tfidf = tfidf.transform("This is a sample unseen description, which is very happy that this works")
		transformer = TfidfTransformer()
		#loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("Sent_Analysis/feature.pkl", "rb")))
		loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl", "rb")))
		#print("About to test")
		tfidf = transformer.fit_transform(loaded_vec.fit_transform(np.array(test_list)))
		df_tfidf=pd.DataFrame(tfidf.toarray())
		#print(df_tfidf.shape)
		#print("Completed")
		#print(tfidf)
		#with open("Sent_Analysis/svm_model.pkl", 'rb') as file:
		with open("svm_model.pkl", 'rb') as file:  
			pickle_model = pickle.load(file)
		Ypredict = pickle_model.predict(df_tfidf)
		#print(Ypredict)
		final_return_list=[]
		for i in Ypredict:
			if(i==1):
				final_return_list.append("Positive")
			else:
				final_return_list.append("Negative")
		return(final_return_list)  

	def vader_scores(self,test_list):
		analyser = SentimentIntensityAnalyzer()
		scores=[]
		for i in test_list:
			snt = analyser.polarity_scores(i)
			scores.append("{}".format(str(snt)))
		return scores



if __name__ == '__main__':
	test_list=["This is a test example, which is very happy and joyous and I am glad that this works","This is a second test case example that is sad and in fact, sucks."]
	ob=SentimentAnalyzer()
	output=ob.check(test_list)
	vader=ob.vader_scores(test_list)
	#print(nltk.word_tokenize('This is a sentence'))
	for i in range(len(test_list)):
		print(test_list[i],"\t",output[i],"\t",vader[i])
	#df=pd.read_csv('dataset.csv')
	#print(df.head())

