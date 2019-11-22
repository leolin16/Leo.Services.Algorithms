# Machine Learning

## problmem solving techniques

1. rule-based
2. machine-learning: pick problem -> represent data -> apply an algorithm -> 

## types of ML

1. Classification: sentiment analysis, spam detection, trading strategy
2. Regression: sales forecasting, predicting a value of a stock market
3. Clustering: recommendations
4. Recommendations: Dimensionality reduction

## Traditional ML Models

Build a tree structure to classify instances or fit a line or curve to make predictions

features chosen by domain experts

structured data such as numbers and probabilities

### Regression models

   1. Linear
   2. Lasso
   3. Ridge
   4. SVR

### Classfication models

   1. Naive Bayes
   2. SVMs
   3. Decision trees
   4. Random forests

### Dimensionality Reduction(models)

   1. Manifold learning
   2. factor analysis

### Clustering models

   1. K-means
   2. Hierarchical clustering
   3. DBSCAN
   4. Spectral clustering

## Representation ML Models

Learn significant features from the underlying data

### Deep learning models

such as neural networks

each layer with neurons learn from data a bit

Pixels -> Edges -> Corners -> Object parts

features implicitly chosen by model itself

unstructured data such as images and movies

#### supervised and unsupervised

##### supervised - learn the relation between ...

    got feature vector(x variables) and labels(y variables)
    seek the function f that links the features and labels

###### types of labels

    1. Categorical(classification)
    2. Continuous(regression)

##### unsupervised

    does not have y variables and a labeled corpus
    does have info to correct itself or tweak model parameters to become better
    model the underlying structure to learn more about data
    algorithms self-discover the patterns and structure in the data

    clustering(k-means)/dimensionality reduction(PCA)

## work flow of ML

1. Raw Data
2. Prepare Data
3. Cleaned data
4. Choose an algorithm
5. Training algorithm
6. fit a model
7. model
8. choose a validation method
9. validation method
10. examine fit and update
11. satisfied?
12. 11: no -> update model -> No.7
13. New Data
14. 11: yes -> Use fitted model for predictions - input with No.13
15. Prediction
