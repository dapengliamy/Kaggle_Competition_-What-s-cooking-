Kaggle competition "what's cooking"

https://www.kaggle.com/c/whats-cooking

Machine Learning(Neural network multiclassification, hierarchical clustering) and Natural Language Processing (word2vec) are applied.

-- Multiclass classification (scikit-learn) enhanced by word embeddings (word2vec);

-- Hierarchical clustering of cuisines with Ward linkage

-- Dimensionality reduction using PCA: project all cuisines onto two dimensions


Raw Data from kaggle
```
{
 "id": 24717,
 "cuisine": "indian",
 "ingredients": [
     "tumeric",
     "vegetable stock",
     "tomatoes",
     "garam masala",
     "naan",
     "red lentils",
     "red chili peppers",
     "onions",
     "spinach",
     "sweet potatoes"
 ]
 },
 ```
After data processing(word embeddings), ingredients for each cook is transferrred into a vector of 50 dimensions.


