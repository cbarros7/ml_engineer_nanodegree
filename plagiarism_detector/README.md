# Plagiarism Detection

## Objective
[Plagiarism Project](https://github.com/udacity/ML_SageMaker_Studies/tree/master/Project_Plagiarism_Detection) Build a model that detects plagiarism among several texts. For this purpose, original texts were defined, and from there *LCS* (Longest Common Subsequence) was calculated to determine if there was similarity between both texts. 

<br>

## Structure
The structure of the project is presented in the following structure composed of 3 fundamental steps: 

### Step 1: Data Exploration
+ Load in the corpus of plagiarism text data.
+ Explore the existing data features and the data distribution.


<br>

### Step 2: Feature Engineering

+ Clean and pre-process the text data.
+ Define features for comparing the similarity of an answer text and a source text, and extract similarity features.
+ Select **"good" features**, by analyzing the correlations between different features.

<br>

### Step 3: Train and Deploy a Model in SageMaker

+ Upload your train/test feature data to S3.
+ Define a binary classification model and a training script.
+ Train a model and deploy it using SageMaker.
+ Evaluate your deployed classifier.

<br>

Below is an image that summarizes the above point:

<br>

<p align="center">
<img src="https://i.imgur.com/6rWAzy9.jpg" alt="Structure">
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