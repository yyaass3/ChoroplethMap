import plotly.express as px
import pandas as pd

data = pd.read_csv(r"C:\Users\padidar\Downloads\2011_us_ag_exports.csv")
fig = px.choropleth(data, locations='code', locationmode='USA-states', color='total exports', scope='usa')
fig.show()
