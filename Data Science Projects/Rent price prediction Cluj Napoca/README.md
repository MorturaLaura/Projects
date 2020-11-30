# Rent price prediction of apartments from Cluj Napoca

As my first Data Science project I wanted to do one that can help me in something that I need to do in the nearest future. In my journey to become a data scientist and my process in getting my first job in the field in Cluj Napoca, when I am able to do so, the first thing I need to do is to find a rent. As a result I thought the proper project would be a 'Rent price prediction' one where you have to write the size of the apartment and select the number of rooms, number of the floor you like your apartment to be, the partitioning of the apartment, if it is in a new building or not and one of the most important things the neighborhood and then obtain the predicted price of the rent based upon these independent variables. 

As a result the first step was to obtain the data for processing and building my machine learning model. Therefore I needed to scrape the data from a website that has listed apartments for rent in Cluj Napoca and for that I chose the website: [www.imobiliare.ro](https://www.imobiliare.ro/inchirieri-apartamente/cluj-napoca). I did the webscraping using Python, being my first webscrapink project, what helped me was [a youtube tutorial for webscraping](https://www.youtube.com/watch?v=3A36TOm7NC8&t=4963s) provided by the channel [DR PI](https://www.youtube.com/channel/UCtvGCaEzQZX7GwUJi-E3ALQ). 

Being my first project what helped guide me through the process of building the machine learning model and the webb app was the youtube tutorial [Real Estate Price Prediction Project](https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg). 

For the process of building my model I used Python programming language and its specific modules used in Data Science Projects such as Numpy, Matplotlib, Seaborn and Sklearn. For creating the server that uses the saved model to serve http requests I used Python Flask Server. For building the web app I used HTML, CSS and JavaScript that will provide the user the ability to enter the desired square footage of the apartment and select other specific features such as the number of the floor, number of rooms, the partitioning of the apartment, if the apartment-building is new or old and the neighborhood in which the apartment is located. After all these characteristics of the desired apartment are established then the Python Flask Server will be called and it will retrieve the predicted price.

In building the model what really made a difference and improved the score of the Linear Regression Model to 0.85 where the following aspects:

1. Removing the outliers that appear when the price per square footage of an apartment with more number rooms is less than the price per square footage of an apartment with less number of rooms that both are in the same neighborhood.

2. Considering the independent features, number of rooms and the number of the floor as discrete features and aplying feature scaling didn't give me the espected score for my model, but when I considered them categorical features that's when the score of my model grew and I was pleased with my result.

<img src='Rent price prediction of apartments from Cluj Napoca caption.png'>
