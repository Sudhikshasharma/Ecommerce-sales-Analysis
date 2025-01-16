#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd #pandas for data claning and manipulation
import plotly.express as px #plotly.express is a data visualization libraray that makes easy and quick plots
import plotly.graph_objects as go # graph.object has used to make advance and customized graph
import plotly.colors as colors
import plotly.io as pio # io has used to customize templates
pio.templates.default='plotly_white'


# In[19]:


#reading data encoding = alatin-1 has used to proerly read all special characters like -,#

data=pd.read_csv("Sample - Superstore.csv", encoding= 'latin-1')


# In[20]:


data


# In[21]:


#head() is used to read top 5 rows of dataset
data.head()


# In[22]:


data.describe()#for looking descriptive statistics


# In[23]:


data.info()


# # converting date column 

# In[24]:


# converting date column because its datatype is object and date should be in datetime format


# In[25]:


data['Order Date']= pd.to_datetime(data['Order Date'])# here write name of ur dataset then name of col u want to change = pd. function name then name of ur dataset and col of taht dataset


# In[26]:


data.info()


# In[27]:


data['Ship Date']=pd.to_datetime(data['Ship Date'])


# In[28]:


data.info()


# In[29]:


data.head()


# # creating columns

# In[30]:


# we have to create 3 extra columns month,year, order of the week to perform analysis because we don't have these columns to perform analysis and we will create from order date column


# In[31]:


#Order Month: Order date se month extract karte hain.
#Order Year: Order date se year extract hota hai.
#Order Day of Week: Week ka day (0 for Monday, 6 for Sunday) extract kiya gaya hai.

data['Order Month']=data['Order Date'].dt.month     
data['Order Year']=data['Order Date'].dt.year
data['Order Day Of Week']=data['Order Date'].dt.dayofweek


# In[32]:


data.head()


# # Monthly Sales Analysis

# In[33]:


sales_by_month=data.groupby('Order Month')['Sales'].sum().reset_index()


# In[35]:


fig = px.line(sales_by_month,                     
              x='Order Month',
              y='Sales',
              title='Month Sales Analysis')
fig.show()




#Data Grouping:
#data.groupby('Order Month')['Sales'].sum() se har month ki total sales nikalte hain.
#.reset_index() data ko structured format me rakhta hai.
#px.line: Monthly sales trend show karne ke liye line chart banaya gaya hai.
#fig.show(): Graph display karta hai.


# # Sales Analysis by Category

# In[36]:


#groupby('Category'): Category-wise sales nikalte hain.
sales_by_category=data.groupby('Category')['Sales'].sum().reset_index()


# In[37]:


sales_by_category


# In[38]:


fig = px.pie(sales_by_category, 
             values='Sales', 
             names='Category', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category', title_font=dict(size=24))

fig.show()


#groupby('Category'): Category-wise sales nikalte hain.
#Pie Chart:
#px.pie: Sales proportions ko pie chart me show karta hai.
#hole=0.5: Donut-style chart banata hai.
#Pastel Colors: Chart me soft color palette use kiya gaya hai.


# # Sales by sub Category

# In[39]:


sales_by_subcategory=data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[40]:


sales_by_subcategory


# In[41]:


fig=px.bar(sales_by_subcategory, x='Sub-Category',y='Sales',title='Sales Analysis by Sub Category')
fig.show()


# # Monthly Profit Analysis

# In[42]:


profit_by_month=data.groupby('Order Month')['Profit'].sum().reset_index()


# In[43]:


profit_by_month


# In[44]:


fig=px.bar(profit_by_month,
          x='Order Month',
           y='Profit',
          title='Monthly Profit Analysis')


# In[45]:


fig.show()


# In[46]:


#monthly profit analysis using line chart
fig=px.line(profit_by_month,x='Order Month',y='Profit',title='Monthly Profit Analysis')


# In[47]:


fig.show()


# # Profit By Category

# In[48]:


profit_by_category=data.groupby('Category')['Profit'].sum().reset_index()


# In[49]:


profit_by_category


# In[51]:


fig = px.pie(profit_by_category, 
             values='Profit', 
             names='Category', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit Analysis by Category', title_font=dict(size=24))

fig.show()


# # Profit by Sub Category

# In[52]:


profit_by_subcategory=data.groupby('Sub-Category')['Profit'].sum().reset_index()


# In[61]:


profit_by_subcategory


# In[60]:


profit_by_subcategory=data.groupby('Sub-Category')['Profit'].sum().reset_index()
fig = px.bar(profit_by_subcategory, x='Sub-Category', 
             y='Profit', 
             title='Profit Analysis by Sub-Category')
fig.show()


# # Sales and Profit - Customer Segment

# In[56]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Sales'], 
                     name='Sales',
                     marker_color=color_palette[0]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Profit'], 
                     name='Profit',
                     marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title='Customer Segment', yaxis_title='Amount')

fig.show()


# # Sales to Profit Ratio

# In[67]:


sales_profit_by_segment=data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio']=sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment','Sales_to_Profit_Ratio']])




# # Conclusion

# In[ ]:


#You need to calculate the monthly sales of the store and identify which month had the highest sales and which month ahd the lowest sales?
#Highest sales of the month  - November
#Lowest sales of the month - January

#You need to analyze sales based on product categories and determine which category has the lowest sales and which category has the highest sales?
#Technology has the highest sales
#Office items has the lowest sales


#The sales analysis needs to be done based on sub -category?
#Based on sub-category Phone has the highest sales.


#You need to analyze monthly profit from the sales and determine which month had the highest profit?
#December has the highest profit 
#January ahs the lowest profit


#Analyze the profit by Category and Sub -Category?
#Profit by Category- Technology
#Profit by Sub - Category - Copiers


#Analyze the Sales and Profit by Customer segment?
#Consumer has the highest sales
#Corporate
#Home offices


#Analyze the sales to profit ratio?
#Consumer has the highest sales to profit ratio.

