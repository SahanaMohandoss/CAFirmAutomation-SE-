from sentiment_analyzer import SentimentAnalyzer
import warnings

if __name__ == '__main__':
	#warnings.simplefilter(action='ignore', category=FutureWarning)
	test_list=["This is a test example, which is very happy and joyous and I am glad that this works","This is a second test case example that is sad and in fact, sucks."]
	ob=SentimentAnalyzer()
	output=ob.check(test_list)
	vader=ob.vader_scores(test_list)
	#print(nltk.word_tokenize('This is a sentence'))
	for i in range(len(test_list)):
		print(test_list[i],"\t",output[i],"\t",vader[i])
