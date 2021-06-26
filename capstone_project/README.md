# Customer segmentation for marketing campaign optimization


## Problem statement
The main objective of this project takes as a starting point those customers who completed the offer by performing a segmentation that allows discovering patterns of purchasing behavior and thus determine what type of offer is the most optimal according to the different groups of segmented customers. This will help Starbucks to focus its marketing campaigns and increase its economic benefit.

<br>


# Datasets and Inputs

The data is contained in three files:
    
1. **portfolio.json** - containing offer ids and meta data about each offer (duration, type, etc.)
2.	**profile.json** - demographic data for each customer
3.	**transcript.json** - records for transactions, offers received, offers viewed, and offers completed

Here is the schema and explanation of each variable in the files:

a) *portfolio.json*

+ *id* (string) - offer id
+ *offer_type* (string) - type of offer ie BOGO, discount, informational
+ *difficulty* (int) - minimum required spend to complete an offer.
+ *reward* (int) - reward given for completing an offer.
+ *duration* (int) - time for offer to be open, in days.
+ *channels* (list of strings)

<br>

b) *profile.json*
+ *age* (int) - age of the customer
+ *became_member_on* (int) - date when customer created an app account.
+ *gender* (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
+ *id* (str) - customer id
+ *income* (float) - customer's income

<br>

c) *transcript.json*
+ *event* (str) - record description (ie transaction, offer received, offer viewed, etc.)
+ *person* (str) - customer id
+ *time* (int) - time in hours since start of test. The data begins at time t=0
+ *value* - (dict of strings) - either an offer id or transaction amount depending on the record

<br>

However, it is important to specify that the size of the data sets are as follows:
+ Dataset portfolio have 10 rows and 6 columns.
+ Dataset profile have 17000 rows and 5 columns.
+ Dataset transcript have 306534 rows and 4 columns.




## Metrics
Since different unsupervised clustering models will be implemented the metrics to be used are: 

1.	**Elbow method:** used to determine the optimal number of clusters in k-means clusters by plotting the value of the cost function produced by different values of k. 

2.	**Silhouette value:** Measures how similar a point is to its own cluster (cohesion) compared to other clusters (separation).

3.	**Davies Bouldin metric:** Average similarity measure of each cluster to its most similar cluster, where similarity is the ratio of distances within the cluster to distances between clusters. The minimum score is zero, and lower values indicate better clustering.

## Files

The following files attached to this GitHub's repository include the following and for the following reasons:

 - [**Starbucks_Capstone_notebook.ipynb**](./Starbucks_Capstone_notebook.ipynb): This is the Jupyter Notebook in which I performed all my work, including EDA, data preprocessing, and cluster. The results found in this notebook can also be found in the final report.

 - [**helpers.py**](./helpers.py): This file contains functions that are used at different points in the processing and display of data.

 - [**Final report.pdf**](./Final_report.pdf): This PDF document contains all my final results and analyses as performed in the accompanying Jupyter notebook above.

 - [**Proposal Capstone Project.pdf**](./Proposal_Capstone_Project): This document contains the initial project proposal I submitted prior to necessarily beginning this project.

 - [**data**](./data/): This folder contains the three JSON files provided by Starbucks / Udacity as noted above.

 - [**images**](./images/): This directory contains the images used in both the Jupyter Notebook and the final report.

<br>

## Infrastructure
In this project, different resources were used both in cloud and on-premise. The following structure was used to carry out the project.

<p align="center">
<img src="https://i.imgur.com/QCKBFIM.png" alt="Coursera logo" width="70%">
</p>

<br>

La herramienta de visualización para graficar los principales resultados fue Tableau en la versión desktop. Las imagenes con las respectivas interpretaciones se encuentran dentro en el


## Conclusions

1.	If the company's objective is to strengthen BOGO offers, it should focus on the 30-39 age group, since the results show that these are the ones who spend the most on this type of offer, followed by the 20–29-year-olds.
2.	The conversion funnel in each of the clusters for the female gender are the ones with the highest conversion rate in terms of offers sent and offers viewed. This means that women are good customers for the types of offers for the marketing campaign.
3.	The age group where they spend the most on the offers is between 50-59 years old, predominantly female. Even though on some occasions they present less completed offers.

<br>

## Acknowledgements :pray:
Thanks to all the teachers, mentors and colleagues of **Udacity** who have been supportive in this nanodegree. It was undoubtedly a great experience both personally and professionally.


For more information about course on Udacity, visit this [link](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).


<br>


<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Udacity_logo.svg/1280px-Udacity_logo.svg.png" alt="Udacity logo" width="70%">
</p>

<br>

### Follow me on :technologist:
[![alt text][1.1]][1]
[![alt text][2.1]][2]
[![alt text][3.1]][3]
[![alt text][4.1]][4]
[![alt text][5.1]][5]
[![alt text][6.1]][6]


<!-- icons with padding -->

[1.1]: https://i.imgur.com/I3n7R1x.png (portfolio)
[2.1]: https://i.imgur.com/AQlyAgc.png (linkedin)
[3.1]: https://i.imgur.com/LuHf8y7.png (twitter)
[4.1]: https://i.imgur.com/iXstsGR.png (github)
[5.1]: https://i.imgur.com/Zijs86N.png (medium)
[6.1]: https://i.imgur.com/Jucrrsg.png (tableau)

<!-- links to your social media accounts -->

[1]: https://carlosbarros.netlify.app/
[2]: https://www.linkedin.com/in/carlosbarros7/
[3]: https://twitter.com/cbarros27
[4]: https://github.com/cbarros7
[5]: https://medium.com/@cbarros7
[6]: https://public.tableau.com/profile/carlos.barros#!/?newProfile=&activeTab=0