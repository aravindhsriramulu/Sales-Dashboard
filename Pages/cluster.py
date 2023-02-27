

# Importing the libraries 

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Setting page configurations

st.set_page_config(layout = 'wide')

st.markdown("<h1 style = 'text-align: center;'> Clustering Sales Dataset </h1>", unsafe_allow_html = True)

st.subheader('The sales dataset has been clustered with kmeans into five segments. Lets explore these five segments to how packs, size, brand and client have a substantial impact on the gross profit')

# Reading the dataset

erp = pd.read_csv('combinederp.csv')

# Creating a custom template for plotly

custom_template = {'layout':
                   go.Layout(
                       font = {'family': 'Helvetica',
                               'size': 14,
                               'color': '#1f1f1f'},
                       
                       title = {'font': {'family': 'Helvetica',
                                         'size': 20,
                                          'color': '#1f1f1f'}},
                       
                       legend = {'font': {'family': 'Helvetica',
                                          'size': 14,
                                          'color': '#1f1f1f'}},
                       
                       plot_bgcolor = '#f2f2f2',
                       paper_bgcolor = '#ffffff'
                   )}

# Plotting four charts for erp cluster zero

erpzerothcluster = erp[erp['Cluster']==0]
fig_typezero = px.pie(erpzerothcluster, values='Gross Profit', names='Client Type', color='Client Type')

fig_packzero = px.bar(erpzerothcluster,
                 x = erpzerothcluster['Pack'],
                 y = erpzerothcluster['Gross Profit'],
                 color = erpzerothcluster['Client Type'],
                 title = "<b>How profit looks with respect to packs</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_packzero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packzero.update_yaxes(automargin = True, title_standoff = 10)

fig_sizezero = px.bar(erpzerothcluster,
                 x = erpzerothcluster['Size'],
                 y = erpzerothcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to size</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_sizezero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizezero.update_yaxes(automargin = True, title_standoff = 10)

fig_brandzero = px.bar(erpzerothcluster,
                 x = erpzerothcluster['Brand'],
                 y = erpzerothcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Brand</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_brandzero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandzero.update_yaxes(automargin = True, title_standoff = 10)

fig_clientzero = px.bar(erpzerothcluster,
                 x = erpzerothcluster['Client'],
                 y = erpzerothcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Client</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_clientzero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientzero.update_yaxes(automargin = True, title_standoff = 10)

# Plotting four charts for erp cluster one

erponecluster = erp[erp['Cluster']==1]
fig_typeone = px.pie(erponecluster, values='Gross Profit', names='Client Type', color='Client Type')

fig_packone = px.bar(erponecluster,
                 x = erponecluster['Pack'],
                 y = erponecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to packs</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_packone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packone.update_yaxes(automargin = True, title_standoff = 10)

fig_sizeone = px.bar(erponecluster,
                 x = erponecluster['Size'],
                 y = erponecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to size</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_sizeone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizeone.update_yaxes(automargin = True, title_standoff = 10)

fig_brandone = px.bar(erponecluster,
                 x = erponecluster['Brand'],
                 y = erponecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Brand</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_brandone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandone.update_yaxes(automargin = True, title_standoff = 10)

fig_clientone = px.bar(erponecluster,
                 x = erponecluster['Client'],
                 y = erponecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Client</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_clientone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientone.update_yaxes(automargin = True, title_standoff = 10)

# Plotting four charts for erp cluster two

erptwocluster = erp[erp['Cluster']==2]
fig_typetwo = px.pie(erptwocluster, values='Gross Profit', names='Client Type', color='Client Type')

fig_packtwo = px.bar(erptwocluster,
                 x = erptwocluster['Pack'],
                 y = erptwocluster['Gross Profit'],
                 title = "<b>How profit looks with respect to packs</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_packtwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packtwo.update_yaxes(automargin = True, title_standoff = 10)

fig_sizetwo = px.bar(erptwocluster,
                 x = erptwocluster['Size'],
                 y = erptwocluster['Gross Profit'],
                 title = "<b>How profit looks with respect to size</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_sizetwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizetwo.update_yaxes(automargin = True, title_standoff = 10)

fig_brandtwo = px.bar(erptwocluster,
                 x = erptwocluster['Brand'],
                 y = erptwocluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Brand</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_brandtwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandtwo.update_yaxes(automargin = True, title_standoff = 10)

fig_clienttwo = px.bar(erptwocluster,
                 x = erptwocluster['Client'],
                 y = erptwocluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Client</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_clienttwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clienttwo.update_yaxes(automargin = True, title_standoff = 10)


# Plotting four charts for erp cluster three

erpthreecluster = erp[erp['Cluster']==3]
fig_typethree = px.pie(erpthreecluster, values='Gross Profit', names='Client Type', color='Client Type')

fig_packthree = px.bar(erpthreecluster,
                 x = erpthreecluster['Pack'],
                 y = erpthreecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to packs</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_packthree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packthree.update_yaxes(automargin = True, title_standoff = 10)

fig_sizethree = px.bar(erpthreecluster,
                 x = erpthreecluster['Size'],
                 y = erpthreecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to size</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_sizethree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizethree.update_yaxes(automargin = True, title_standoff = 10)

fig_brandthree = px.bar(erpthreecluster,
                 x = erpthreecluster['Brand'],
                 y = erpthreecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Brand</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_brandthree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandthree.update_yaxes(automargin = True, title_standoff = 10)

fig_clientthree = px.bar(erpthreecluster,
                 x = erpthreecluster['Client'],
                 y = erpthreecluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Client</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_clientthree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientthree.update_yaxes(automargin = True, title_standoff = 10)

# Plotting four charts for erp cluster four

erpfourcluster = erp[erp['Cluster']==4]
fig_typefour = px.pie(erpfourcluster, values='Gross Profit', names='Client Type', color='Client Type')

fig_packfour = px.bar(erpfourcluster,
                 x = erpfourcluster['Pack'],
                 y = erpfourcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to packs</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_packfour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packfour.update_yaxes(automargin = True, title_standoff = 10)

fig_sizefour = px.bar(erpfourcluster,
                 x = erpfourcluster['Size'],
                 y = erpfourcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to size</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_sizefour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizefour.update_yaxes(automargin = True, title_standoff = 10)

fig_brandfour = px.bar(erpfourcluster,
                 x = erpfourcluster['Brand'],
                 y = erpfourcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Brand</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_brandfour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandfour.update_yaxes(automargin = True, title_standoff = 10)

fig_clientfour = px.bar(erpfourcluster,
                 x = erpfourcluster['Client'],
                 y = erpfourcluster['Gross Profit'],
                 title = "<b>How profit looks with respect to Client</b>",
                 color_discrete_sequence = ['#636EFA'])

fig_clientfour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientfour.update_yaxes(automargin = True, title_standoff = 10)


# Creating the streamlit layout

tab1, tab2, tab3, tab4, tab5 = st.tabs(['**Segment Zero**', '**Segment One**', '**Segment Two**', '**Segment Three**',
                                        '**Segment Four**'])

with tab1:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typezero)
    st.text("Supermarkets leads the chart with highest profit of $700K while Discounters, Grocery and Big-box have $350K, $200k and $142K")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packzero)
    st.text("4X and 15X achieve a gross profit of over $200K. Contrastingly, 6X and 20X attain the lowest profit figure of $60K")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizezero)
    st.text("500ML is the ideal range for sale in this segment. It has recorded a gross profit if above $400K. Other sizes manage to cross the threshold of $100K gross profit except for the 750ML size which records the lowest gross profit of $10K")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandzero)
    st.text("Zumba Orange and Pit Bull are the most profitable brands, with a gross profit of $500K and $390K respectively while its subsidiaries does not even cross the $200K threshold. Evan Vitamin does not even manage to hit $10K gross profit")

    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clientzero)
    st.text("ShopRite is the most profitable client with a profit mark of $200K while Publix is the least profitable client with a profit mark of less than $20K")
    
with tab2:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typeone)
    st.text("Supermarkets is the leader with a gross profit of over $5.8M while Discounters, Grocery and Big-box have $2.6M, $1.8M and $1M")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packone)
    st.text("All packs have an average gross profit of $500K while the topmost packs are 12X and 15X with a gross profit of $2.4M and $1.4M")

    st.header('Size vs Profit Distribution')
    st.text("500ML is the highest profitable category with a gross profit if over $4M while other sizes like 250ML, 750ML and 600ML cross the $1.5M threshold. Only 1.25L size range has the least profitable mark threshold of $1M")
    st.plotly_chart(fig_sizeone)
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandone)
    st.text("Dundy and its subsidiaries is the only profitable brand with an accumulated gross profit of over $8M while Crocky, Evan Vitamin, Buratino and its subsidiaries are under the $500K mark")
    
    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clientone)
    st.text("Super Target, Trader Joe's, ShopRite, WinCo Foods, Walmart - Supermarkets cross the $1.5M threshold while Sam's Club, Safeway and Walmart Dicounters have their gross profit below $1M.")

with tab3:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typetwo)
    st.text("Supermarkets have over $2M gross profit while Big-box and discounters have over $600K")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packtwo)
    st.text("18X and 20X are the least profitable packs with a gross profit of under $150K while other packs are above $400K")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizetwo)
    st.text("The most profitable size is 250ML with a gross profit of over $700k and the least profitable size is 750ML with a gross profit of $100K")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandtwo)
    st.text("Evan and Dundy One is the most profitable brand with a gross profit of over $800K")
    
    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clienttwo)
    st.text("Safeway is the least profitable client with a profit range below $100K")

with tab4:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typethree)
    st.text("Supermarket has a profit share of almost $8M while Discounters and Big-box of $4M and $3M")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packthree)
    st.text("18X and 20X are the least profitable packs with a gross profit range below $1M while other size are above $1M")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizethree)
    st.text("2.25L, 1.75L and 500ML have a profit range of over $2M while 250ML, 750ML and 1.25L have gross profit below $1.5M")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandthree)
    st.text("Dundy Diet, Dundy Max and Dundy Free have a gross profit over $3M")
    
    st.header('Client Vs Distribution')
    st.plotly_chart(fig_clientthree)
    st.text("Kmart super center is the leading client with a gross profit of over $4M")

with tab5:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typefour)
    st.text("Supermarkets have over $1.8M profit share while Discounters, Grocery and Big-box has over $3.6M, $2.9M and $1.5M")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packfour)
    st.text("4X and 6X is the most profitable pack, with an average gross profit margin of above $2.5M")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizefour)
    st.text("2.25L and 1.5L are the most profitable size with $5M and $4m respectively")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandfour)
    st.text("Dundy and its subsidiaries have a gross profit of over $10M while Evan Vitamin is the least profitable brand with gross profit below $50K")
    
    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clientfour)
    st.text("Super Target and Trader's Joe continue to dominate the market with a gross profit of over $2.5M independently")

