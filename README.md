#  House Price Prediction App
App: https://houseprice-nymtnharq73mmx4fiwzq67.streamlit.app/

###  Overview
This project predicts **house prices** based on multiple housing features such as area, number of bedrooms, bathrooms, stories, location preferences, and furnishing status.  
It uses a **Linear Regression** model trained on a housing dataset and is deployed using **Streamlit** for an interactive web-based prediction interface.

##  Dataset Description — `Housing.csv`

The dataset contains information about residential properties and their attributes.  
Each record represents a house with its selling price and various features influencing it.

| Column Name | Description | Type |
|--------------|-------------|------|
| `price` | Selling price of the house (Target variable) | Numeric |
| `area` | Size of the house in square feet | Numeric |
| `bedrooms` | Number of bedrooms | Numeric |
| `bathrooms` | Number of bathrooms | Numeric |
| `stories` | Number of stories (floors) | Numeric |
| `mainroad` | Whether the house has main road access (`yes`/`no`) | Categorical |
| `guestroom` | Whether the house has a guest room (`yes`/`no`) | Categorical |
| `basement` | Whether the house has a basement (`yes`/`no`) | Categorical |
| `hotwaterheating` | Whether hot water heating is available (`yes`/`no`) | Categorical |
| `airconditioning` | Whether the house has air conditioning (`yes`/`no`) | Categorical |
| `parking` | Number of parking spaces available | Numeric |
| `prefarea` | Whether it’s a preferred area (`yes`/`no`) | Categorical |
| `furnishingstatus` | Type of furnishing (`furnished`, `semi-furnished`, `unfurnished`) | Categorical |

##  Model Workflow

1. **Data Preprocessing**
   - Encodes categorical features using `LabelEncoder`
   - Splits dataset into training (80%) and testing (20%)

2. **Model Training**
   - Uses **Linear Regression** to predict house price
   - Evaluates model using R² score

3. **Model Saving**
   - Saves model as `model.pkl`
   - Saves encoders as `encoders.pkl`

4. **Streamlit Interface**
   - Loads trained model and encoders
   - Takes user input (features)
   - Displays predicted house price instantly
  ## visualization
  <img width="727" height="547" alt="image" src="https://github.com/user-attachments/assets/a0bef15c-85ac-403c-a56a-0f766f3ba603" />

## Key Insights

Area and stories strongly influence the selling price.

Main road access and preferred area houses are priced higher.

Furnished houses typically have better valuation.

Features like air conditioning and parking also add significant value.

##  Conclusion

The Linear Regression model successfully captures the trend between house features and price, achieving a reliable R² score.

This predictive system can assist real estate professionals and buyers to estimate property values before listing or purchasing.

Further improvements can be made by:

Using RandomForest or Gradient Boosting models

Performing feature scaling & polynomial features

Deploying the model as a cloud-based prediction API



