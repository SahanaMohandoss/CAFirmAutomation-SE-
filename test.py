from sentiment_analyzer import SentimentAnalyzer
import warnings

if __name__ == '__main__':
	#warnings.simplefilter(action='ignore', category=FutureWarning)
	test_list=["This is a test example, which is very happy and joyous and I am glad that this works","This is a second test case example that is sad and in fact, sucks."]
	ob=SentimentAnalyzer()
	output_sentences=ob.get_string(test_list)
	for i in range(len(test_list)):
		print(test_list[i])
		print(output_sentences[i])
		print("\n\n\n")
