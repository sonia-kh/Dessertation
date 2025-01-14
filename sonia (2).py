# -*- coding: utf-8 -*-
"""Sonia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10YMzyljofIe2Y0FQ-ygO7T3efW7vv_N5
"""

# unzipping data file
!unzip /content/archive.zip

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import time
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Loading Data
HRSSAnomalousOptimised = pd.read_csv('/content/HRSS_anomalous_optimized.csv')
HRSSNormalOptimised = pd.read_csv('/content/HRSS_normal_optimized.csv')
HRSSAnomalousStandard = pd.read_csv('/content/HRSS_anomalous_standard.csv')
HRSSNormalStandard = pd.read_csv('/content/HRSS_normal_standard.csv')

# Data Info about HRSSAnomalousOptimised
HRSSAnomalousOptimised.info()

# Head about HRSSAnomalousOptimised
HRSSAnomalousOptimised.head()

# Tail about HRSSAnomalousOptimised
HRSSAnomalousOptimised.tail()

# Describe about HRSSAnomalousOptimised
HRSSAnomalousOptimised.describe()

# Checking Null Values about HRSSAnomalousOptimised
HRSSAnomalousOptimised.isnull().sum()

# Columns about HRSSAnomalousOptimised
HRSSAnomalousOptimised.columns

# Outliers about HRSSAnomalousOptimised
Q1 = HRSSAnomalousOptimised.quantile(0.25)
Q3 = HRSSAnomalousOptimised.quantile(0.75)
IQR = Q3 - Q1
outliers = ((HRSSAnomalousOptimised < (Q1 - 1.5 * IQR)) | (HRSSAnomalousOptimised > (Q3 + 1.5 * IQR))).sum()
print(outliers)

# Data Info about HRSSNormalOptimised
HRSSNormalOptimised.info()

# Head about HRSSNormalOptimised
HRSSNormalOptimised.head()

# Tail about HRSSNormalOptimised
HRSSNormalOptimised.tail()

# Describe about HRSSNormalOptimised
HRSSNormalOptimised.describe()

# Checking Null Values about HRSSNormalOptimised
HRSSNormalOptimised.isnull().sum()

# Columns about HRSSNormalOptimised
HRSSNormalOptimised.columns

# Outliers about HRSSNormalOptimised
Q1 = HRSSNormalOptimised.quantile(0.25)
Q3 = HRSSNormalOptimised.quantile(0.75)
IQR = Q3 - Q1
outliers = ((HRSSNormalOptimised < (Q1 - 1.5 * IQR)) | (HRSSNormalOptimised > (Q3 + 1.5 * IQR))).sum()
print(outliers)

# Data Info about HRSSAnomalousStandard
HRSSAnomalousStandard.info()

# Head about HRSSAnomalousStandard
HRSSAnomalousStandard.head()

# Tail about HRSSAnomalousStandard
HRSSAnomalousStandard.tail()

# Describe about HRSSAnomalousStandard
HRSSAnomalousStandard.describe()

# Checking Null Values about HRSSAnomalousStandard
HRSSAnomalousStandard.isnull().sum()

# Columns about HRSSAnomalousStandard
HRSSAnomalousStandard.columns

# Outliers about HRSSAnomalousStandard
Q1 = HRSSAnomalousStandard.quantile(0.25)
Q3 = HRSSAnomalousStandard.quantile(0.75)
IQR = Q3 - Q1
outliers = ((HRSSAnomalousStandard < (Q1 - 1.5 * IQR)) | (HRSSAnomalousStandard > (Q3 + 1.5 * IQR))).sum()
print(outliers)

# Data Info about HRSSNormalStandard
HRSSNormalStandard.info()

# Head about HRSSNormalStandard
HRSSNormalStandard.head()

# Tail about HRSSNormalStandard
HRSSNormalStandard.tail()

# Describe about HRSSNormalStandard
HRSSNormalStandard.describe()

# Checking Null Values about HRSSNormalStandard
HRSSNormalStandard.isnull().sum()

# Columns about HRSSNormalStandard
HRSSNormalStandard.columns

# Outliers about HRSSNormalStandard
Q1 = HRSSNormalStandard.quantile(0.25)
Q3 = HRSSNormalStandard.quantile(0.75)
IQR = Q3 - Q1
outliers = ((HRSSNormalStandard < (Q1 - 1.5 * IQR)) | (HRSSNormalStandard > (Q3 + 1.5 * IQR))).sum()
print(outliers)

# Removing outliers from dataframes
HRSSAnomalousOptimised = HRSSAnomalousOptimised[~((HRSSAnomalousOptimised < (Q1 - 1.5 * IQR)) | (HRSSAnomalousOptimised > (Q3 + 1.5 * IQR))).any(axis=1)]
HRSSNormalOptimised = HRSSNormalOptimised[~((HRSSNormalOptimised < (Q1 - 1.5 * IQR)) | (HRSSNormalOptimised > (Q3 + 1.5 * IQR))).any(axis=1)]
HRSSAnomalousStandard = HRSSAnomalousStandard[~((HRSSAnomalousStandard < (Q1 - 1.5 * IQR)) | (HRSSAnomalousStandard > (Q3 + 1.5 * IQR))).any(axis=1)]
HRSSNormalStandard = HRSSNormalStandard[~((HRSSNormalStandard < (Q1 - 1.5 * IQR)) | (HRSSNormalStandard > (Q3 + 1.5 * IQR))).any(axis=1)]

"""# Plotting Histograms for each numerical features"""

HRSSAnomalousOptimised.hist(figsize=(15,10))
plt.suptitle('Histograms of HRSS Anomalous Optimized Features', y=0.95)
plt.show()

HRSSNormalOptimised.hist(figsize=(15,10))
plt.suptitle('Histograms of HRSS Normal Optimized Features', y=0.95)
plt.show()

HRSSAnomalousStandard.hist(figsize=(15,10))
plt.suptitle('Histograms of HRSS Anomalous Standard Features', y=0.95)
plt.show()

HRSSNormalStandard.hist(figsize=(15,10))
plt.suptitle('Histograms of HRSS Normal Standard Features', y=0.95)
plt.show()

for column in HRSSAnomalousOptimised.select_dtypes(include=np.number).columns:
  plt.figure()
  sns.boxplot(x=HRSSAnomalousOptimised[column])
  plt.title(f'Boxplot of {column} (HRSS Anomalous Optimized)')
  plt.show()

for column in HRSSNormalOptimised.select_dtypes(include=np.number).columns:
  plt.figure()
  sns.boxplot(x=HRSSNormalOptimised[column])
  plt.title(f'Boxplot of {column} (HRSS Normal Optimized)')
  plt.show()

for column in HRSSAnomalousStandard.select_dtypes(include=np.number).columns:
  plt.figure()
  sns.boxplot(x=HRSSAnomalousStandard[column])
  plt.title(f'Boxplot of {column} (HRSS Anomalous Standard)')
  plt.show()

for column in HRSSNormalStandard.select_dtypes(include=np.number).columns:
  plt.figure()
  sns.boxplot(x=HRSSNormalStandard[column])
  plt.title(f'Boxplot of {column} (HRSS Normal Standard)')
  plt.show()

"""# Correlation Matrix of Dataframes"""

# Correlation heatmaps
plt.figure(figsize=(10, 8))
sns.heatmap(HRSSAnomalousOptimised.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap (HRSS Anomalous Optimized)')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(HRSSNormalOptimised.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap (HRSS Normal Optimized)')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(HRSSAnomalousStandard.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap (HRSS Anomalous Standard)')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(HRSSNormalStandard.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap (HRSS Normal Standard)')
plt.show()

# Data Info about HRSSAnomalousOptimised
HRSSAnomalousOptimised.info()

# Data Info about HRSSNormalOptimised
HRSSNormalOptimised.info()

# Data Info about HRSSAnomalousStandard
HRSSAnomalousStandard.info()

# Data Info about HRSSNormalStandard
HRSSNormalStandard.info()

# Adding a column to dataframes
HRSSAnomalousOptimised['Source'] = 'AnomalousOptimized'
HRSSAnomalousStandard['Source'] = 'AnomalousStandard'
HRSSNormalOptimised['Source'] = 'NormalOptimized'
HRSSNormalStandard['Source'] = 'NormalStandard'

# Combining all dataframes into a single dataframe
CombineData = pd.concat([HRSSAnomalousOptimised,
                         HRSSAnomalousStandard,
                         HRSSNormalOptimised,
                         HRSSNormalStandard],
                        ignore_index=True)

# Printing the shape of the combined dataframe
CombineData.shape

# Printing the head of combined dataframe
CombineData.head()

# Selecting features and target
features = CombineData.drop(columns=['Timestamp', 'Source', 'Labels'])
labels = CombineData['Labels']

# Normalisation of the data
ScalerCombined = StandardScaler()
ScaledCombinedFeatures = ScalerCombined.fit_transform(features)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(ScaledCombinedFeatures, labels, test_size=0.3, random_state=42)

# Training a Random Forest
RandomForestModel = RandomForestClassifier(n_estimators=100, random_state=42)
RandomForestModel.fit(X_train, y_train)

# Making Predictions
yPred = RandomForestModel.predict(X_test)

# Calculating the Performance of the model
RandomForestModelAccuracy = accuracy_score(y_test, yPred)*100
RandomForestModelClassification = classification_report(y_test, yPred)
RandomForestModelConfusionMatrix = confusion_matrix(y_test, yPred)

# Printing the performance of the model
print('Random Forest Accuracy:', RandomForestModelAccuracy, '%')
print('Random Forest Classification Report:\n', RandomForestModelClassification)

# Defining a function to Simulate a real-time data stream
def SimulatingRealTimeStream(model, data, labels, delay=0.1):
    CorrectPredictions = 0
    TotalPredictions = 0
    StartingTime = time.time()

    for i in range(data.shape[0]):
        time.sleep(delay)
        prediction = model.predict(data[i].reshape(1, -1))[0]
        if prediction == labels[i]:
            CorrectPredictions += 1
        TotalPredictions += 1
        print(f"Time: {time.time() - StartingTime:.2f}s, Prediction: {prediction}, True Label: {labels[i]}")

    accuracy = CorrectPredictions / TotalPredictions
    total_time = time.time() - StartingTime
    print(f"\nStreamed {TotalPredictions} data points in {total_time:.2f}s with accuracy: {accuracy:.2%}")

# Converting y_test to numpy array
y_testArray = y_test.to_numpy()

# Simulating the corrected labels
SimulatingRealTimeStream(RandomForestModel, X_test[:50], y_testArray[:50], delay=0.05)

# Plotting Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(RandomForestModelConfusionMatrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix for Random Forest')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()

# Training and Fitting a IsolationForest Model
IsolationForestModel = IsolationForest()
IsolationForestModel.fit(ScaledCombinedFeatures)

# Getting Anamoly Scores
AnomalyScores = IsolationForestModel.decision_function(ScaledCombinedFeatures)

# Visualising anomaly scores
plt.hist(AnomalyScores, bins=50)
plt.xlabel("Anomaly Score")
plt.ylabel("Frequency")
plt.title("Distribution of Anomaly Scores")
plt.show()