

# Importing the libraries 

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Setting page configurations

st.set_page_config(layout = 'wide', page_icon = '📙')

st.markdown("<h1 style = 'text-align: center;'> Clustering Sales Dataset </h1>", unsafe_allow_html = True)
st.markdown("<h3 style = 'text-align: center;'> A Web App by <b><a href = 'https://github.com/zilmabezerra'> Aravindh </a></b></h3>", unsafe_allow_html = True)

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
fig_packzero = px.bar(erpzerothcluster,
                 x = erpzerothcluster['Pack'],
                 y = erpzerothcluster['Gross Profit'],
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

tab1, tab2, tab3, tab4, tab5 = st.tabs(['**Cluster Zero**', '**Cluster One**', '**Cluster Two**', '**Cluster Three**',
                                        '**Cluster Four**'])

with tab1:
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_packzero)

    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_sizezero)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_brandzero)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_clientzero)
    
with tab2:
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_packone)

    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_sizeone)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_brandone)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_clientone)

with tab3:
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_packtwo)

    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_sizetwo)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_brandtwo)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_clienttwo)

with tab4:
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_packthree)

    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_sizethree)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_brandthree)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_clientthree)

with tab5:
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_packfour)

    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_sizefour)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_brandfour)
    
    st.header('Age Distribution')
    st.write(f'In this plot, it is possible to observe the presence of outliers. The ages **around and over 100** are most likely erroneous data inputs. These errors may have been made by accident or on purpose. For instance, some users may not want to disclose their personal information.')
    st.plotly_chart(fig_clientfour)
