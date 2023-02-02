  
           #Parkinson's Disease Detection
           
A machine learning project for Parkinson's Disease Detection using various classifiers such as Logistic Regression, SVM, Random Forest, XGBoost, and KNN. 
This project uses a dataset from Kaggle with 195 observations and 24 features, including demographic information, such as age and gender, and medical information, such as Parkinson's disease progression score, to determine if a person has Parkinson's disease or not.

         #Getting Started
         
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

         #Prerequisites
The libraries used in this project are:

numpy
pandas
seaborn
matplotlib
scikit-learn
xgboost
opendatasets
You can install these libraries using the following command:

---> pip install numpy pandas seaborn matplotlib scikit-learn xgboost opendatasets
        #Running the code

The code can be run using a Jupyter Notebook or Google Colab. 
The dataset is loaded from Kaggle and processed to clean and analyze the data. 
The data is then split into training and testing sets and scaled using MinMaxScaler. 
The classifiers are trained on the training set and evaluated on the testing set using various metrics such as accuracy, confusion matrix.
