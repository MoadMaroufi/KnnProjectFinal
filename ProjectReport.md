# Report: 

Moaad MAAROUFI was reponsble for modeling and traning while Ahmed Ghaleb was responsible for investigating the curse of dimensionality, conducting experiments, and interpreting the results. ChatGpt was used to for debugging, for example in cross validation it indicated that we had to add some functions in order to conform with sklearn's conventions. We also used it to gain a deeper understanding of how kdtrees work in depth.



## Modeling
We first started out simple, by constructing a knn model as we saw in the lectures. Basically calculating the distance between the test point and every other point in the dataset using numpy operations. Eventhough most of our operations were vectorized, it took our model more than 3 minutes to predict the bounadry compared to the 13 seconds taken by sklearn's knn model. This is extremely inefficient as there are some points which aren't clearely potential nearest neighbours, we knew we had to segmente the vector space into some buckets abstraction  beforehand in traning time and then just look into those buckets for teh enarest neigbours instead of calclating the distance to every point in the vector space. Scipy Kdtrees(k-dimensional tree) implements this already, by sgementing the space into hyperectangles, by splitting the space according to a particular by takking the median and we do this recursively . Thus when we want to querry for the nearest neughbour of a point we traverse this binary tree until we reach a leaf node and then we backtrace.what we saw in the lectures. Basically calculating the distance between the test point and every other point in the dataset using numpy operations. Eventhough most of our operations were vectorized, it took our model more than 3 minutes to detect the bounadry compare to 13 seconds taken by sklearn's knn model. This is extremely inefficient as there are some points which aren't clearly potential nearest neighbours, we knew we had to segmente the vector space into some "buckets"   beforehand in traning  and then just look into those buckets for the enarest neigbours instead of calclating the distance to every point in the vector space. Scipy Kdtrees(k-dimensional tree) implements this already, by sgementing the space into hyperectangles,  splitting the space according to a particular axis by takking the median value  recursively . Thus when we want to querry for the nearest neighbor of a point we traverse this binary tree until we reach a leaf node and then we backtrace.

## Training and validation

In knn generally traning is simply storing the traning data, so we fed the traning data to the kdtree.

To predict we querry the kdtree for the indeces of the closest k points and then we perform a majority voting. We tried using stat.mode and we had a similar time to that of the sklearn knn model for predicting the boundary, but we experiemented with an idea of turning all the 0 labels in our data to -1 and then summing up the labels and if the sum is positive then its class one and vice versa. This turned out to be extremely efficient with less overhead as everything is vetcorized and we use very basic operations (sum) instead of couting occurences. This approach yielded a model which takes 1 second to predict the boundary for this specific dataset which is 13 times better than the sklearns model. We do this for binary classification. When the model is confronted with multiclass classifcation we use stat.mode to do the majority voting.

To tune the hyperparameter k we used cross valadation, eventhough we still haven't seen it in the class. Bascially splitting the traning data into k folds(in our case 5) and then taking turns to train the model on k-1 of these folds and testing on the k'th fold so that eventually we get an unbiased average score while avoiding data leakage. 

We also tested our model on anther dataset (breast cancer binary classifcation with tabular data) and we had comparable reulsts with the sklearn's model.


## The curse of dimentionnality :

The knn algorithm is based on the notion of proximity which itself determined by distance. When working with higher dimentions  distance metrics  becomes less meaningful as points are clustered near the frontier. Consequently, if  the distance between training points and the test point  will be  very similar. Thus the class with the greater number of points in the dataset will always prevail in the majority voting. We can see this in the expeiiments that we conducted as we tried to put the nearest neigbours in a hypercube with a lenght lesser than 1 but we can't because with teh formular we derived we can see in the graph that as d grows l gets closer to one.




