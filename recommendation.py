# import recommendation
# import requests
import pandas as pd
import numpy as np
# from urllib.request import urlopen
# from itertools import zip_longest
# import re #Regex
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# import scipy.sparse as sp


df = pd.read_csv("C:/Users/Dnaaya/Downloads/Recommendation 2.0/Unlock_test_final.csv",encoding='unicode_escape')
# df=df.dropna()
df

c_names= df['c_names']
c_names
Categoery = df['Categoery']
Categoery
Request=df['Request']
Request
df['Categoery'].nunique()
df['Categoery'].value_counts()
#Categoery =df['Categoery'].unique()
Categoery
Sub_Categoery = df['Sub_Categoery']
Sub_Categoery





from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
my_stop_words = text.ENGLISH_STOP_WORDS.union(['360','world','your','and','a','company','want','wide','build','Unlock','Hello,Unlock'
                           ,'development','working','zainab','services','online','work','wish','accelerate','accelerated','accomplish'
                                              ,'achieve','achieving','actively','addition','actualize','solution','issues','help'
                                             ,'best','make','business','egypt','agency','provider','specialized','programs','aziz',
                                              'winning','building','areas','apply','better','based','built','cost','copmany','corporate'
                                              ,'corporates','covering','create','created','high','projects','provides','range'
                                              ,'reach','region','real','small','specific','starting','stride','things','using','way'
                                              ,'new','some','hello','need','choose','serve'
                                              ,'unlock','field','deal','providers','users','comapny','products','digital'
                                              ,'hi'])


df['Request']= df['Request'].fillna(' ')

# Instantiate a TfidfVectorizer object
vectorizer = TfidfVectorizer(stop_words=set(my_stop_words))
# It fits the data and transform it as a vector
X = vectorizer.fit_transform(df.Request)
# Convert the X as transposed matrix
X = X.toarray().T
# Create a DataFrame and set the vocabulary as the index
df = pd.DataFrame(X, index=vectorizer.get_feature_names())
df






# Reverse mapping of indices and Providers
indices = pd.Series(df.index, index=vectorizer.get_feature_names())
indices.head()





import heapq

def results(req):
    req = req.lower()
    print("query:", req)
    print("cosine similarity : ")
    # Convert the query become a vector
    req = [req]
    q_vec = vectorizer.transform(req).toarray().reshape(df.shape[0],)
    sim = {}

  # Calculate the similarity
    for i in range(1,221,2):
        sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
       # print( sim[i])

      # Sort the values 
        sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)

        sim_sorted = heapq.nlargest(1, sim_sorted, key=lambda x:x[1])
  #print(sim_sorted)
  # Print the company_names and their similarity values
    for k, v in sim_sorted:
        if v >= .25:
            print("Similaritas:", v)
            print(Categoery[k])
            print(Sub_Categoery[k])
            print(c_names[k])

            print ()
            return {"Categoery":Categoery[k],
            "Sub_Categoery":Sub_Categoery[k],
            "c_names":c_names[k]}

# Add The Query
#q1 = 'hello,Unlock i want a provider of specialized development programs coaches,training, professionals'
#q1 = 'I want to build a new website to my comapny and we are a legal agency that works in legal issues and be in courts'
#q1 = 'I need a digital transformation company to my website to increase the conversion rate'
#q5 = 'i need agency in digital AI supply chain'
#q1 = 'Hello, i want to buid a new website for my business'
#q1= 'i need a legal company to help me in some issues'
#q1 = 'Hi, i need a mobile app and want to know best company can make it with the lowets budget'
#q1= 'hey, would you help me to best providers to deal with to build a mobile app to my business that alot of users in all over the world'
#q1 =  'I want to build a new website we are a legal agency'
#q1 = 'i want to build a new website as we are are a legal office'
#q1 = 'Hello,Unlock i want a lawyer'
#q1 = 'hello,Unlock I want a social media company that help me in my business to promote my products and website'
#q1 = 'Hi, Unlock i am looking to build a new website to my company that present our products and our services to sell my products online'
#q1= 'i want to buid a website with new branding'
#q1= 'i want a website to my company we are a  digital transformation agency'
#q1 = 'i want a new website and mobile app as we are a social media agency'
#q1 = 'i want a new website for my company as we are a law agency'
#q1 = 'i want to build a mobile appication to our legal agency'
#q1 = 'i want a web development company to buid a new brand for my company'

#q1 = 'I need a Training company developing HR services'
#q1 = 'Hi,Unlock'
#q1= 'i want to sell my products online so i want to make some ads in my page'
q1 = 'i want a company that works in ERP system and sap iam interested in data science Ai and field'
#q1 = 'i want to build a new website for my business' 
#q1= 'i need a comapny to make a logo'
#q1 = 'i want a website for my business'

#q1 = 'I want to make a new logo and buid a new website to my company'
#q1 = 'Hi, Unlock i have a company in e-commerce industry so i want to build a new website'
# Call the function
results(q1)
