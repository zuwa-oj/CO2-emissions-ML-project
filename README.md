# CO2-emissions-ML-project
LHL capstone project using longitude, latitude, and population data integrated from 3 datasets for the prediction of CO2 emissions for any location.  

Research has shown that global CO2 emissions have risen over time due to incresing human activities ranging from deforestation, to burning of fossil fuels for transportation, electricity, and industry to mention a few. With the common underlying factor here being human activities, we can hypothesize that a relationship exists between a metric to track humans (population) and CO2 emission rates in any (latitude and longitude) location.

Sometimes data collection in some places may not be possible so a way to estimate emissions could be useful in academia and research.

## Goal

The primary objective of this project was to develop a predictive ML model to estimate the CO2 emissions rate for any location of interest given its geographical coordinates of latitude, longitude, and population data. 
An effort to generate insights from the data will also be completed and communicated with the aid of visualizations.

## Data

Data under free public licence was obtained from kaggle.com and is available in this repo in the data/raw folder.
CO2 emissions dataset does not contain geographical coordinates which were obtained by mapping the coordinates from latitude and longitude values dataset, while population information was merged from the dataset.

To gain insights from the features of the data, I have built some visualizations in Tableau along with a dashboard that can be used for long term monitoring of emissions. The Tableau workbook is located in the output folder of this repository.

## Results

From the visualizations created, it is difficult to infer the relationship between the CO2 emissions and the population data, but machine learning can determine this relationship in order to allow for prediction.

After Exploratory Data Analysis(EDA) using Python, the correlation heatmap showed that Latitude has the highest correlation with the variable of interest that I was looking to estimate, and this correlation was observed to be even higher than that of Population_density.
But when you stop to think about it, it makes some sense because as you move towards the equator you get tropical climate conditions under which most people would prefer to live.

Then I used the features with highest correlation to the emissions and built a baseline Linear Regression model which got an R-squared score of 20%, meaning that the problem I was trying to solve wasn't linear.

So I went on to train an XGBoost model and much improved results with an R-squared score of 98%. This model along with a Decision Tree and Random Forest models (for comparison) can be found in the output folder. And I have also included code to deploy the model, using Flask, on any local machine.

It is expected that the model generated will have use cases in academia for research purposes and also in environmental monitoring.

## Challenges and Future Goals

The main challenge encountered during this project was data gathering as CO2 emissions data is not readily available with population data.  

The next steps include periodically updating the dataset and experimenting with more models.  

Currently in progress is the process of taking the cleaning and preprocessing steps from the notebooks and converting them into a python script to create a data pipeline. The model can eventually be dumped and loaded on a cloud platform such as an AWS EC2 instance.