# Chiller Performance Model

Welcome to the Chiller Performance Model project! This project aims to predict the power consumption of a chiller system based on various parameters using machine learning models. By accurately predicting power consumption, we can estimate potential power savings, which will be advertised to customers.

## Table of Contents

- [Chiller Performance Model](#chiller-performance-model)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Project Steps](#project-steps)

## Introduction

Chiller systems are crucial for cooling in various industrial and commercial applications. Predicting their power consumption accurately can lead to significant energy savings. This project involves building and comparing multiple machine learning models to find the most accurate predictor of chiller power consumption based on parameters such as temperature, cooling load, pressure, and pump speed.

## Project Steps

1. **Data Collection:** Gather data from various sensors and sources.
2. **Data Cleaning:** Deep cleansing of temperature data to ensure accuracy.
3. **Data Aggregation:** Hourly aggregation of data to address performance lag issues.
4. **Feature Engineering:** Create relevant features for the models.
5. **Model Training:** Train multiple models using XGBoost and Random Forest algorithms.
6. **Model Comparison:** Compare the performance of 13 different models.
7. **Final Model Selection:** Choose the best-performing model for power consumption prediction.
8. **Power Saving Estimation:** Use the final model to estimate potential power savings.

