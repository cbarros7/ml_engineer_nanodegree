# Deploy a sentiment analysis model

## Objective
[Sentiment Analysis Web App](https://github.com/udacity/sagemaker-deployment/tree/master/Project) is a notebook and collection of Python files to be completed. The result is a deployed RNN performing sentiment analysis on movie reviews complete with publicly accessible API and a simple web page which interacts with the deployed endpoint.

<br>

## Structure

<br>

<p align="center">
<img src="https://i.imgur.com/mqdArQg.jpeg" alt="Structure">
</p>

<br>

The diagram above gives an overview of how the different services will work together. On the far right is the model that was trained earlier developed in **SageMaker**. On the far left is the web application that collects a user's movie review, submits it, and expects ``positive`` or ``negative`` sentiment in return.

It is important to mention that the **Lambda** function was built, so that it can execute a specific event, and the method to execute this function is a new *endpoint* that was created using **API Gateway**. This endpoint will be a URL that will listen for data to be sent to it. Once it gets some data, it will pass that data to the Lambda function and then return whatever the Lambda function returns. In other words, it will act as an interface that allows our web application to communicate with the Lambda function.

<br>

## Demo

In order to prove that the model will work correctly, we took as an example the reviews of the movie **Inception (2010)** with the low and high rating reviews made by the users. Below is a video detailing how the application works:


<br>

<p align="center">
<img src="https://github.com/cbarros7/ml_engineer_nanodegree/blob/main/sagemaker_sentiment_analysis/website/deploydemo.gif" alt="Coursera logo">
</p>


<p align="center">
<img src="https://github.com/cbarros7/ml_engineer_nanodegree/blob/main/sagemaker_sentiment_analysis/website/deploy.gif" alt="Coursera logo">
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