# CO2-emissions-ML-project
LHL capstone project using longitude, latitude, and population data integrated from 3 datasets for the prediction of CO2 emissions for any location.  

Research has shown that global CO2 emissions have risen over time due to incresing human activities ranging from deforestation, to burning of fossil fuels for transportation, electricity, and industry to mention a few. With the common underlying factor here being human activities, we can hypothesize that a relationship exists between a metric to track humans (population) and CO2 emission rates in any (latitude and longitude) location.

## Goal

The primary objective of this project is to develop a predictive ML model to estimate the CO2 emissions rate for any location of interest given its geographical coordinates of latitude, longitude, and population data. 
An effort to generate insights from the data will also be completed and communicated with the aid of visualizations.

## Data

Data under free public licence was obtained from kaggle.com and is available in this repo in the data/raw folder.
CO2 emissions dataset does not contain geographical coordinates which were obtained by mapping the coordinates from latitude and longitude values dataset, while population information was merged from the dataset.

## Results

## Conclusion

It is expected that the model generated will have use cases in academia for research purposes and also in environmental monitoring.

## Challenges and Future Goals

The main challenge encountered during this project was data gathering as CO2 emissions data is not readily available with population data.  

The next steps include periodically updating the dataset and experimenting with more models.  

Currently in progress is the process of taking the cleaning and preprocessing steps from the notebooks and converting them into a python script to create a data pipeline. The model can eventually be dumped and loaded on a cloud platform such as an AWS EC2 instance.