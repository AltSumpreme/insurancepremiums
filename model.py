from sklearn.linear_model import LinearRegression
model = LinearRegression()
#Create inputs and targets
non_smoker_df = medical_df[medical_df.smoker == 'no']
inputs, targets = non_smoker_df[['age', 'bmi']], non_smoker_df['charges']

# train the model
model = LinearRegression().fit(inputs, targets)
targets = non_smoker_df.charges
# Generate the predictions
predictions = model.predict(inputs)

# to compute the loss of the model
loss = rmse(targets, predictions)
print('Loss:', loss)
