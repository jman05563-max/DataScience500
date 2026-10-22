# Data Science 500 Assignment
## Book Market Analytics – Books to Scrape

### Project Overview

This project investigates book pricing patterns using data collected from the Books to Scrape website.

A total of 1,000 books were collected using Python and BeautifulSoup. The dataset was cleaned, analysed and used to develop a Linear Regression model for predicting book prices.

### Project Objectives

- Collect book information using web scraping.
- Clean and prepare the collected dataset.
- Analyse book prices, ratings and genres.
- Create statistical visualisations.
- Develop a Linear Regression model.
- Evaluate the model's predictive performance.

### Technologies Used

- Python
- BeautifulSoup
- Requests
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- PyCharm

### Dataset

The dataset contains 1,000 books and includes the following information:

- Book titles
- Prices in GBP
- Star ratings
- Stock availability
- Stock quantities
- Book genres
- Product URLs

**Data Source:** https://books.toscrape.com/

### Data Visualisation

Five graphs were created:

1. Distribution of Book Prices
2. Distribution of Star Ratings
3. Average Book Price by Genre
4. Book Prices Across Star Ratings
5. Actual vs Predicted Book Prices

### Predictive Modelling

A Linear Regression model was developed using book ratings, genres, stock quantities and title lengths.

The dataset was divided into 80% training data and 20% testing data.

### Model Results

| Evaluation Metric | Result |
|---|---|
| Mean Absolute Error (MAE) | £12.91 |
| Mean Squared Error (MSE) | 225.26 |
| Root Mean Squared Error (RMSE) | £15.01 |
| R-squared (R²) | -0.0724 |

The negative R² score indicates that the model performed worse than a mean-price prediction baseline on the testing dataset.

### How to Run the Project

1. Download or clone this GitHub repository.
2. Install the required Python libraries:

   `pip install requests beautifulsoup4 pandas numpy matplotlib seaborn scikit-learn notebook`

3. Open `Book_Market_Analytics.ipynb` in Jupyter Notebook.
4. Run the notebook cells in order to reproduce the data collection, cleaning, visualisation and modelling workflow.

### Conclusion

This project demonstrates an end-to-end data science workflow involving web scraping, data preparation, exploratory data analysis and predictive modelling.

Although the Linear Regression model showed limited predictive accuracy, the project demonstrates how data science techniques can be applied to structured catalogue information.

### GitHub Repository Link

**Public GitHub Repository:**

https://github.com/jman05563-max/DataScience500.git

### Academic Information

**Institution:** Richfield Graduate Institute of Technology

**Module:** Data Science 500

**Project:** Book Market Analytics – Books to Scrape
