

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

packzero = erpzerothcluster.groupby(['Pack','Client Type'])['Gross Profit'].sum().reset_index()
fig_packzero = px.bar(packzero,
                 x = packzero['Pack'],
                 y = packzero['Gross Profit'],
                 color = packzero['Client Type'], color_discrete_map={"Supermarkets": "red", "Discounters": "green", "Grocery": "blue", "Big-box": "goldenrod"},
                 category_orders={"Client Type": ["Supermarkets", "Discounters", "Grocery", "Big-box"]},
                 barmode='group', title = "<b>How profit looks with respect to packs</b>")

fig_packzero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packzero.update_yaxes(automargin = True, title_standoff = 10)

sizezero = erpzerothcluster.groupby(['Size','Client Type'])['Gross Profit'].sum().reset_index()
fig_sizezero = px.bar(sizezero,
                 x = sizezero['Size'],
                 y = sizezero['Gross Profit'],
                 color = sizezero['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to size</b>")

fig_sizezero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizezero.update_yaxes(automargin = True, title_standoff = 10)

brandzero = erpzerothcluster.groupby(['Brand','Client Type'])['Gross Profit'].sum().reset_index()
fig_brandzero = px.bar(brandzero,
                 x = brandzero['Brand'],
                 y = brandzero['Gross Profit'],
                 color = brandzero['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to Brand</b>")

fig_brandzero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandzero.update_yaxes(automargin = True, title_standoff = 10)

clientzero = erpzerothcluster.groupby(['Client','Client Type'])['Gross Profit'].sum().reset_index()
fig_clientzero = px.bar(clientzero,
                 x = clientzero['Client'],
                 y = clientzero['Gross Profit'],
                 color = clientzero['Client Type'],
                 title = "<b>How profit looks with respect to Client</b>")

fig_clientzero.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientzero.update_yaxes(automargin = True, title_standoff = 10)

# Plotting four charts for erp cluster one

erponecluster = erp[erp['Cluster']==1]
fig_typeone = px.pie(erponecluster, values='Gross Profit', names='Client Type', color='Client Type')

packone = erponecluster.groupby(['Pack','Client Type'])['Gross Profit'].sum().reset_index()
fig_packone = px.bar(packone,
                 x = packone['Pack'],
                 y = packone['Gross Profit'],
                 color = packone['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to packs</b>")

fig_packone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packone.update_yaxes(automargin = True, title_standoff = 10)

sizeone = erponecluster.groupby(['Size','Client Type'])['Gross Profit'].sum().reset_index()
fig_sizeone = px.bar(sizeone,
                 x = sizeone['Size'],
                 y = sizeone['Gross Profit'],
                 color = sizeone['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to size</b>")

fig_sizeone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizeone.update_yaxes(automargin = True, title_standoff = 10)

brandone = erponecluster.groupby(['Brand','Client Type'])['Gross Profit'].sum().reset_index()
fig_brandone = px.bar(brandone,
                 x = brandone['Brand'],
                 y = brandone['Gross Profit'],
                 color = brandone['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to Brand</b>")

fig_brandone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandone.update_yaxes(automargin = True, title_standoff = 10)

clientone = erponecluster.groupby(['Client','Client Type'])['Gross Profit'].sum().reset_index()
fig_clientone = px.bar(clientone,
                 x = clientone['Client'],
                 y = clientone['Gross Profit'],
                 color = clientone['Client Type'],
                 title = "<b>How profit looks with respect to Client</b>")

fig_clientone.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientone.update_yaxes(automargin = True, title_standoff = 10)

# Plotting four charts for erp cluster two

erptwocluster = erp[erp['Cluster']==2]
fig_typetwo = px.pie(erptwocluster, values='Gross Profit', names='Client Type', color='Client Type')

packtwo = erptwocluster.groupby(['Pack','Client Type'])['Gross Profit'].sum().reset_index()
fig_packtwo = px.bar(packtwo,
                 x = packtwo['Pack'],
                 y = packtwo['Gross Profit'],
                 color = packtwo['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to packs</b>")

fig_packtwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packtwo.update_yaxes(automargin = True, title_standoff = 10)

sizetwo = erptwocluster.groupby(['Size','Client Type'])['Gross Profit'].sum().reset_index()
fig_sizetwo = px.bar(sizetwo,
                 x = sizetwo['Size'],
                 y = sizetwo['Gross Profit'],
                 color = sizetwo['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to size</b>")

fig_sizetwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizetwo.update_yaxes(automargin = True, title_standoff = 10)

brandtwo = erptwocluster.groupby(['Brand','Client Type'])['Gross Profit'].sum().reset_index()
fig_brandtwo = px.bar(brandtwo,
                 x = brandtwo['Brand'],
                 y = brandtwo['Gross Profit'],
                 color = brandtwo['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to Brand</b>")

fig_brandtwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandtwo.update_yaxes(automargin = True, title_standoff = 10)

clienttwo = erptwocluster.groupby(['Client','Client Type'])['Gross Profit'].sum().reset_index()
fig_clienttwo = px.bar(clienttwo,
                 x = clienttwo['Client'],
                 y = clienttwo['Gross Profit'],
                 color = clienttwo['Client Type'],
                 title = "<b>How profit looks with respect to Client</b>")

fig_clienttwo.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clienttwo.update_yaxes(automargin = True, title_standoff = 10)


# Plotting four charts for erp cluster three

erpthreecluster = erp[erp['Cluster']==3]
fig_typethree = px.pie(erpthreecluster, values='Gross Profit', names='Client Type', color='Client Type')

packthree = erpthreecluster.groupby(['Pack','Client Type'])['Gross Profit'].sum().reset_index()
fig_packthree = px.bar(packthree,
                 x = packthree['Pack'],
                 y = packthree['Gross Profit'],
                 color = packthree['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to packs</b>")

fig_packthree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packthree.update_yaxes(automargin = True, title_standoff = 10)

sizethree = erpthreecluster.groupby(['Size','Client Type'])['Gross Profit'].sum().reset_index()
fig_sizethree = px.bar(sizethree,
                 x = sizethree['Size'],
                 y = sizethree['Gross Profit'],
                 color = sizethree['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to size</b>")

fig_sizethree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizethree.update_yaxes(automargin = True, title_standoff = 10)

brandthree = erpthreecluster.groupby(['Brand','Client Type'])['Gross Profit'].sum().reset_index()
fig_brandthree = px.bar(brandthree,
                 x = brandthree['Brand'],
                 y = brandthree['Gross Profit'],
                 color = brandthree['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to Brand</b>")

fig_brandthree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandthree.update_yaxes(automargin = True, title_standoff = 10)

clientthree = erpthreecluster.groupby(['Client','Client Type'])['Gross Profit'].sum().reset_index()
fig_clientthree = px.bar(clientthree,
                 x = clientthree['Client'],
                 y = clientthree['Gross Profit'],
                 color = clientthree['Client Type'],
                 title = "<b>How profit looks with respect to Client</b>")

fig_clientthree.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientthree.update_yaxes(automargin = True, title_standoff = 10)

# Plotting four charts for erp cluster four

erpfourcluster = erp[erp['Cluster']==4]
fig_typefour = px.pie(erpfourcluster, values='Gross Profit', names='Client Type', color='Client Type')

packfour = erpfourcluster.groupby(['Pack','Client Type'])['Gross Profit'].sum().reset_index()
fig_packfour = px.bar(packfour,
                 x = packfour['Pack'],
                 y = packfour['Gross Profit'],
                 color = packfour['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to packs</b>")

fig_packfour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Pack</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_packfour.update_yaxes(automargin = True, title_standoff = 10)

sizefour = erpfourcluster.groupby(['Size','Client Type'])['Gross Profit'].sum().reset_index()
fig_sizefour = px.bar(sizefour,
                 x = sizefour['Size'],
                 y = sizefour['Gross Profit'],
                 color = sizefour['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to size</b>")

fig_sizefour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Size</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_sizefour.update_yaxes(automargin = True, title_standoff = 10)

brandfour = erpfourcluster.groupby(['Brand','Client Type'])['Gross Profit'].sum().reset_index()
fig_brandfour = px.bar(brandfour,
                 x = brandfour['Brand'],
                 y = brandfour['Gross Profit'],
                 color = brandfour['Client Type'],
                 barmode='group', title = "<b>How profit looks with respect to Brand</b>")

fig_brandfour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Brand</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_brandfour.update_yaxes(automargin = True, title_standoff = 10)

clientfour = erpfourcluster.groupby(['Client','Client Type'])['Gross Profit'].sum().reset_index()
fig_clientfour = px.bar(clientfour,
                 x = clientfour['Client'],
                 y = clientfour['Gross Profit'],
                 color = clientfour['Client Type'],
                 title = "<b>How profit looks with respect to Client</b>")

fig_clientfour.update_layout(height = 600, width = 1000, template = custom_template, xaxis_title = '<b>Client</b>',
                      yaxis_title = '<b>Gross Profit</b>')

fig_clientfour.update_yaxes(automargin = True, title_standoff = 10)


# Creating the streamlit layout

tab1, tab2, tab3, tab4, tab5 = st.tabs(['**Segment Zero**', '**Segment One**', '**Segment Two**', '**Segment Three**',
                                        '**Segment Four**'])

with tab1:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typezero)
    st.write("Supermarkets leads the chart with highest profit of \$700K while Discounters, Grocery and Big-box have \$350K, \$200k and \$142K")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packzero)
    st.write("4X and 15X achieve a gross profit of over \$200K. Contrastingly, 6X and 20X attain the lowest profit figure of \$60K")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizezero)
    st.write("500ML is the ideal range for sale in this segment. It has recorded a gross profit if above \$400K. Other sizes manage to cross the threshold of \$100K gross profit except for the 750ML size which records the lowest gross profit of \$10K")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandzero)
    st.write("Zumba Orange and Pit Bull are the most profitable brands, with a gross profit of \$500K and \$390K respectively while its subsidiaries does not even cross the \$200K threshold. Evan Vitamin does not even manage to hit \$10K gross profit")

    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clientzero)
    st.write("ShopRite is the most profitable client with a profit mark of \$200K while Publix is the least profitable client with a profit mark of less than \$20K")
    
with tab2:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typeone)
    st.write("Supermarkets is the leader with a gross profit of over \$5.8M while Discounters, Grocery and Big-box have \$2.6M, \$1.8M and \$1M")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packone)
    st.write("All packs have an average gross profit of \$500K while the topmost packs are 12X and 15X with a gross profit of \$2.4M and \$1.4M")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizeone)
    st.write("500ML is the highest profitable category with a gross profit if over \$4M while other sizes like 250ML, 750ML and 600ML cross the \$1.5M threshold. Only 1.25L size range has the least profitable mark threshold of \$1M")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandone)
    st.write("Dundy and its subsidiaries is the only profitable brand with an accumulated gross profit of over \$8M while Crocky, Evan Vitamin, Buratino and its subsidiaries are under the \$500K mark")
    
    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clientone)
    st.write("Super Target, Trader Joe's, ShopRite, WinCo Foods, Walmart - Supermarkets cross the \$1.5M threshold while Sam's Club, Safeway and Walmart Dicounters have their gross profit below \$1M.")

with tab3:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typetwo)
    st.write("Supermarkets have over $2M gross profit while Big-box and discounters have over \$600K")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packtwo)
    st.write("18X and 20X are the least profitable packs with a gross profit of under \$150K while other packs are above \$400K")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizetwo)
    st.write("The most profitable size is 250ML with a gross profit of over \$700k and the least profitable size is 750ML with a gross profit of \$100K")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandtwo)
    st.write("Evan and Dundy One is the most profitable brand with a gross profit of over \$800K")
    
    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clienttwo)
    st.write("Safeway is the least profitable client with a profit range below \$100K")

with tab4:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typethree)
    st.write("Supermarket has a profit share of almost \$8M while Discounters and Big-box of \$4M and \$3M")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packthree)
    st.write("18X and 20X are the least profitable packs with a gross profit range below \$1M while other size are above \$1M")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizethree)
    st.write("2.25L, 1.75L and 500ML have a profit range of over \$2M while 250ML, 750ML and 1.25L have gross profit below \$1.5M")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandthree)
    st.write("Dundy Diet, Dundy Max and Dundy Free have a gross profit over \$3M")
    
    st.header('Client Vs Distribution')
    st.plotly_chart(fig_clientthree)
    st.write("Kmart super center is the leading client with a gross profit of over \$4M")

with tab5:
    st.header('Client Type Distribution')
    st.plotly_chart(fig_typefour)
    st.write("Supermarkets have over \$1.8M profit share while Discounters, Grocery and Big-box has over \$3.6M, \$2.9M and \$1.5M")
    
    st.header('Pack vs Profit Distribution')
    st.plotly_chart(fig_packfour)
    st.write("4X and 6X is the most profitable pack, with an average gross profit margin of above \$2.5M")

    st.header('Size vs Profit Distribution')
    st.plotly_chart(fig_sizefour)
    st.write("2.25L and 1.5L are the most profitable size with \$5M and \$4m respectively")
    
    st.header('Brand vs Profit Distribution')
    st.plotly_chart(fig_brandfour)
    st.write("Dundy and its subsidiaries have a gross profit of over \$10M while Evan Vitamin is the least profitable brand with gross profit below \$50K")
    
    st.header('Client vs Profit Distribution')
    st.plotly_chart(fig_clientfour)
    st.write("Super Target and Trader's Joe continue to dominate the market with a gross profit of over \$2.5M independently")

