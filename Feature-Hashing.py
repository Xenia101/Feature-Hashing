from sklearn.feature_extraction import FeatureHasher
import string
import random

def makestring():
    # make random string 1~10 
    string_pool = string.ascii_lowercase
    result = ""
    for x in range(random.randrange(1,11)):
        result += random.choice(string_pool)
    return result

def setdata(): # set data
    data = []
    for x in range(5):
        data.append(makestring())
    return data

def FeatureHashing(data):
    h = FeatureHasher(n_features=5, input_type="string")
    f = h.transform(data)
    print(f.toarray())
    
if __name__ == "__main__":
    data = setdata()
    FeatureHashing(data)

