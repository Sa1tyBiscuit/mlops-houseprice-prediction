# mlops-houseprice-prediction

Learning Django and MLops :)

Front End:
- utilizes basic HTML and CSS
- User is able to key in a value of the resale flat size which they would like to predict

Back End:
- The result is then stored in a sqllite3 database

ML: 
- resale flat price data was sourced from data.gov.sg
- Utilizes a simple log-linear regression model with a single feature (flat_size) to predict house prices

References: 
1. https://data.gov.sg/dataset/resale-flat-prices
2. https://towardsdatascience.com/creating-a-machine-learning-based-web-application-using-django-5444e0053a09
3. https://datascience.quantecon.org/applications/regression.html
