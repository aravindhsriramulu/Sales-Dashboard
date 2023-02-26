import pandas as pd
import streamlit as st
import plotly.express as px
from numerize.numerize import numerize

st.set_page_config(page_title = 'Water Bottles Sales Dashboard',
                    layout='wide',
                    initial_sidebar_state='collapsed')

df = pd.read_csv('erpdata.csv')


header_left,header_mid,header_right = st.columns([1,2,1],gap='large')

with header_mid:
    st.title('Bottles Sales Dashboard')


with st.sidebar:
    Client_filter = st.multiselect(label= 'Select the Client',
                                options=df['Client'].unique(),
                                default=df['Client'].unique())
    
    Month_filter = st.multiselect(label='Select the Month',
                            options=df['Month'].unique(),
                            default=df['Month'].unique())

    Brand_filter = st.multiselect(label='Select the Brand',
                            options=df['Brand'].unique(),
                            default=df['Brand'].unique())

df1 = df.query('Client == @Client_filter & Month == @Month_filter & Brand == @Brand_filter')

total_volume = float(df1['Volume'].sum())
total_gross_sales = float(df1['Gross Sales'].sum())
total_discount = float(df1['Discounts'].sum())
total_net_sales = float(df1['Net Sales'].sum()) 
total_cost_of_goods_sold = float(df1['Cost of Goods Sold'].sum())
total_distribution = float(df1['Distribution'].sum())
total_warehousing = float(df1['Warehousing'].sum())


total1,total2,total3,total4,total5,total6,total7 = st.columns(7,gap='large')

with total1:
    st.metric(label='Total Volume', value= numerize(total_volume))
    
with total2:
    st.metric(label='Total Gross Sales', value=numerize(total_gross_sales))

with total3:
    st.metric(label= 'Total Discount',value=numerize(total_discount,2))

with total4:
    st.metric(label='Total Net Sales',value=numerize(total_net_sales))

with total5:
    st.metric(label='Total Cost of Goods Sold',value=numerize(total_cost_of_goods_sold))
    
with total6:
    st.metric(label='Distributions',value=numerize(total_distribution))

with total7:
    st.metric(label='Warehousing',value=numerize(total_warehousing))

Q1,Q2 = st.columns(2)

with Q1:
    df3 = df1.groupby(by = ['Pack']).sum()[['Net Sales','Cost of Goods Sold']].reset_index()
    df3['Gross Profit'] =round(df3['Net Sales'] + df3['Cost of Goods Sold'],3)
    fig_profit_by_volume = px.bar(df3,
                            x='Pack',
                            y='Gross Profit',
                            title='<b>How pack volume impact profit</b>')
    fig_profit_by_volume.update_layout(title = {'x' : 0.5},
                                    plot_bgcolor = "rgba(0,0,0,0)",
                                    xaxis =(dict(showgrid = False)),
                                    yaxis =(dict(showgrid = False)))
    st.plotly_chart(fig_profit_by_volume,use_container_width=True)

with Q2:
    df2 = df1.groupby(by='Client Type').sum()[['Net Sales']].reset_index()
    fig_diff_client_type = px.bar(df2,x='Client Type',y='Net Sales',title='<b>Category wise sales stats</b>')
    fig_diff_client_type.update_layout(title = {'x':0.5}, plot_bgcolor = "rgba(0,0,0,0)")
    st.plotly_chart(fig_diff_client_type,use_container_width=True)
  
Q3,Q4 = st.columns(2)

with Q3:
    df4 = df1.groupby(by='Client Type').sum()[['Volume']].reset_index()
    fig_diff_client_type = px.pie(df4,names='Client Type',values='Volume',title='<b>Client Volume Stats</b>')
    fig_diff_client_type.update_layout(title = {'x':0.5}, plot_bgcolor = "rgba(0,0,0,0)")
    st.plotly_chart(fig_diff_client_type,use_container_width=True)

with Q4:
    df5 = df1.groupby(by='Size').sum()[['Net Sales','Cost of Goods Sold', 'Distribution', 'Warehousing']].reset_index()
    df5['Fully Delivered Margin'] = round(df5['Net Sales'] + df5['Cost of Goods Sold'] + df5['Distribution'] + df5['Warehousing'],2)
    fig_FDM_by_size = px.bar(df5,x='Size',y='Fully Delivered Margin',title='<b>How FDM changes according to size</b>')
    fig_FDM_by_size.update_layout(title = {'x':0.5},xaxis =(dict(showgrid = False)),yaxis =(dict(showgrid = False)), plot_bgcolor = "rgba(0,0,0,0)")
    st.plotly_chart(fig_FDM_by_size,use_container_width=True)


