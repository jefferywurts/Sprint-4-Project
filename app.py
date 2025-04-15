import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('cleaned_dataset.csv')
print(df.head())  # shows the first 5 rows
print(df.columns) # shows column names
st.header("Used vehicle market data")
filtered_df = df[(df['price'] < 80000) & (df['model_year'] > 1990)]
import matplotlib.pyplot as plt
fig = px.box(filtered_df,
             x='transmission',
             y='price',
             color='transmission',
             title='Price Distribution by Transmission Type',
             range_y=(0, 100000))

st.plotly_chart(fig)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(df['odometer'], df['price'], alpha=0.5)
ax.set_xlabel('Odometer (miles)')
ax.set_ylabel('Price ($)')
ax.set_title('Price vs Odometer')
ax.set_ylim(0, 100000)

st.pyplot(fig)

fig = px.scatter(df,
                 x='odometer',
                 y='price',
                 title='Price vs Odometer',
                 labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
                 range_y=[0, 100000],
                 opacity=0.5)

st.plotly_chart(fig)

# Filter the data
filtered_df = df[(df['odometer'] < 250000) & (df['price'] < 50000)]

# Create a density heatmap
fig = px.density_heatmap(filtered_df,
                         x='odometer',
                         y='price',
                         nbinsx=20,
                         nbinsy=20,
                         color_continuous_scale='viridis',
                         labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
                         title='Price vs Odometer (Density Heatmap)')

fig.update_layout(
    xaxis_title='Odometer (miles)',
    yaxis_title='Price ($)',
    xaxis_tickangle=45,
    yaxis_range=[0, 30000],
    xaxis_range=[0, 250000]
)

st.plotly_chart(fig)

df['date_posted'] = pd.to_datetime(df['date_posted'])
df_by_month = df.resample('ME', on='date_posted')['price'].mean().reset_index()

fig = px.line(df_by_month,
              x='date_posted',
              y='price',
              title='Average Price Over Time',
              labels={'date_posted': 'Date', 'price': 'Average Price ($)'})

st.plotly_chart(fig)

fig = px.scatter(df,
                 x='days_listed',
                 y='price',
                 opacity=0.5,
                 title='Price vs Days Listed',
                 labels={'days_listed': 'Days Listed', 'price': 'Price ($)'},
                 range_y=[0, 100000])

st.plotly_chart(fig)

show_plot = st.checkbox('Show scatter plot')
fig = px.scatter(filtered_df,
                 x='days_listed',
                 y='price',
                 color='model_year',
                 color_continuous_scale='Reds',
                 opacity=0.5,
                 title='Price vs Days Listed (Colored by Model Year)',
                 labels={'days_listed': 'Days Listed', 'price': 'Price ($)', 'model_year': 'Model Year'},
                 range_y=[0, 80000])

st.plotly_chart(fig)

