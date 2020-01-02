# Feature Hashing

Sample of Feature Hashing for Machine Learning

### Feature Hashing란?
>In machine learning, feature hashing, also known as the hashing trick (by analogy to the kernel trick), is a fast and space-efficient way of vectorizing features, i.e. turning arbitrary features into indices in a vector or matrix.[1][2] It works by applying a hash function to the features and using their hash values as indices directly, rather than looking the indices up in an associative array. 
[WIKIPEDIA](https://en.wikipedia.org/wiki/Feature_hashing)


## Why is it necessary? (Necessity)

Feature are required when machine learning is in operation. 

Since the **lengths of the features are different**, it is necessary to process them.

## 예시

```python
from sklearn.feature_extraction import FeatureHasher

h = FeatureHasher(n_features=n, input_type="string")
f = h.transform(data)
```
