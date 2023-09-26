#for column bmi
fig = px.histogram(medical_df,x='bmi',marginal='box',color_discrete_sequence=['red'],title='distribution of body mass index')
fig.update_layout(bargap=0.1)
fig.show()
# for column charges
fig =px.histogram(medical_df,x='charges',marginal='box',color='region',color_discrete_sequence=['green','gray'])
fig.update_layout(bargap=0.1)
fig.show()
#a cooler graph
fig = px.scatter(medical_df,x='age',y='charges',color='smoker',opacity=0.8,hover_data=['sex'],title="Age vs Charges")
fig.update_traces(marker_size=5)
fig.show()
