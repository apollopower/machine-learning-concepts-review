import numpy
import pandas as pd 

# Filepath to data
file_path = '../data/world_happiness_report.csv'

# Reading Data
data = pd.read_csv(file_path)



# Creating Train-test split

train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

# Decide what fields we want to process
input_param_name_1 = 'Economy..GDP.per.Capita'
input_param_name_2 = 'Freedom'
output_param_name = 'Happiness.Score'

# Split training set input and output
x_train = train_data[[input_param_name_1, input_param_name_2]].values
y_train = train_data[[output_param_name]].values

# Split test set input and output
x_test = test_data[[input_param_name_1, input_param_name_2]].values
y_test = test_data[[output_param_name]].values



# Set up linear regression parameters
num_iterations = 500 # Num of gradient descent iterations
regularization_param = 0 # Helps to fight model overfitting
learning_rate = 0.01 # The size of the gradient descent step
polynomial_degree = 0 # The degree of additional polynomial features
sinusoid_degree = 0 # The degree of sinusoid parameters multipliers of additional features

# Init Linear Regression
