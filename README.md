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

### Example

```
# 1

# Length    5         7        4          9
Input = ['Apple', 'Pumpkin', 'Corn', 'Blueberry']

# Output of equal length
Output = 
 [[ 0.  0.  2.  0.  0.  0. -2.  0.  0.  1.]
  [ 0. -3.  1.  0. -1.  0.  0.  0.  0.  0.]
  [ 0. -1.  0.  1. -1.  1.  0.  0.  0.  0.]
  [ 0. -1.  1.  0.  1.  2.  0.  0.  0.  2.]]
```

```
# 2

# Added 'Apple1' to list of Input
Input = ['Apple', 'Pumpkin', 'Corn', 'Blueberry', 'Apple1']

Output = 
[[ 0.  0.  2.  0.  0.  0. -2.  0.  0.  1.]
 [ 0. -3.  1.  0. -1.  0.  0.  0.  0.  0.]
 [ 0. -1.  0.  1. -1.  1.  0.  0.  0.  0.]
 [ 0. -1.  1.  0.  1.  2.  0.  0.  0.  2.]
 [ 0.  0.  2.  0.  0.  0. -2. -1.  0.  1.]] # The results have changed, but they are similar
```
