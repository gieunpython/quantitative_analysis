#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 
# <h1 align=center><font size = 5>Assignment: Notebook for Peer Assignment</font></h1>
# 

# # Introduction
# 
# Using this Python notebook you will:
# 
# 1.  Understand three Chicago datasets
# 2.  Load the three datasets into three tables in a Db2 database
# 3.  Execute SQL queries to answer assignment questions
# 

# ## Understand the datasets
# 
# To complete the assignment problems in this notebook you will be using three datasets that are available on the city of Chicago's Data Portal:
# 
# 1.  <a href="https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01">Socioeconomic Indicators in Chicago</a>
# 2.  <a href="https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01">Chicago Public Schools</a>
# 3.  <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01">Chicago Crime Data</a>
# 
# ### 1. Socioeconomic Indicators in Chicago
# 
# This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.
# 
# A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:
# [https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)
# 
# ### 2. Chicago Public Schools
# 
# This dataset shows all school level performance data used to create CPS School Report Cards for the 2011-2012 school year. This dataset is provided by the city of Chicago's Data Portal.
# 
# A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:
# [https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)
# 
# ### 3. Chicago Crime Data
# 
# This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.
# 
# A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:
# [https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)
# 

# ### Download the datasets
# 
# This assignment requires you to have these three tables populated with a subset of the whole datasets.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the links below to download and save the datasets (.CSV files):
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01" target="_blank">Chicago Census Data</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01" target="_blank">Chicago Public Schools</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01" target="_blank">Chicago Crime Data</a>
# 
# **NOTE:** Ensure you have downloaded the datasets using the links above instead of directly from the Chicago Data Portal. The versions linked here are subsets of the original datasets and have some of the column names modified to be more database friendly which will make it easier to complete this assignment.
# 

# ### Store the datasets in database tables
# 
# To analyze the data using SQL, it first needs to be loaded into SQLite DB.
# We will create three tables in as under:
# 
# 1.  **CENSUS_DATA**
# 2.  **CHICAGO_PUBLIC_SCHOOLS**
# 3.  **CHICAGO_CRIME_DATA**
# 
# Let us now load the ipython-sql  extension and establish a connection with the database
# 
# *   Here you will be loading the csv files into the pandas Dataframe and then loading the data into the above mentioned sqlite tables.
# 
# *   Next you will be connecting to the sqlite database  **FinalDB**.
# 
# Refer to the previous lab for hints .
# 
# <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing_SQLite.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01">Hands-on Lab: Analyzing a real World Data Set</a>
# 

# In[1]:


get_ipython().system('pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3')
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
get_ipython().system('pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24')
get_ipython().system('pip install ipython-sql')


# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[3]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://gfz96399:1hD3tuhyRbziYIxD@8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30120/BLUDB?security=SSL')


# In[4]:


import pandas, csv


# 
# ## Problems
# 
# Now write and execute SQL queries to solve assignment problems
# 
# ### Problem 1
# 
# ##### Find the total number of crimes recorded in the CRIME table.
# 

# In[11]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(ID) FROM CHICAGO_CRIME_DATA;')


# ### Problem 2
# 
# ##### List community areas with per capita income less than 11000.
# 

# In[12]:


get_ipython().run_line_magic('sql', 'SELECT COMMUNITY_AREA_NAME FROM CHICAGO_CONCENSUS_DATA WHERE PER_CAPITA_INCOME < 11000;')


# ### Problem 3
# 
# ##### List all case numbers for crimes  involving minors?(children are not considered minors for the purposes of crime analysis)
# 

# In[14]:


get_ipython().run_line_magic('sql', "SELECT CASE_NUMBER FROM CHICAGO_CRIME_DATA WHERE '%MINOR%' IN (PRIMARY_TYPE, DESCRIPTION)")


# ### Problem 4
# 
# ##### List all kidnapping crimes involving a child?
# 

# In[28]:


get_ipython().run_line_magic('sql', 'SELECT CASE_NUMBER FROM CHICAGO_CRIME_DATA WHERE IUCR IN (1792, 1790)')


# ### Problem 5
# 
# ##### What kinds of crimes were recorded at schools?
# 

# In[40]:


get_ipython().run_line_magic('sql', 'SELECT PRIMARY_TYPE FROM CHICAGO_CRIME_DATA INNER JOIN CHICAGO_PUBLIC_SCHOOLS ON CHICAGO_CRIME_DATA.LOCATION = CHICAGO_PUBLIC_SCHOOLS.LOCATION')


# ### Problem 6
# 
# ##### List the average safety score for each type of school.
# 

# In[41]:


get_ipython().run_line_magic('sql', 'SELECT AVG(SAFETY_SCORE) AS AVERAGE_SAFETY_SCORE FROM CHICAGO_PUBLIC_SCHOOLS')


# ### Problem 7
# 
# ##### List 5 community areas with highest % of households below poverty line
# 

# In[53]:


get_ipython().run_line_magic('sql', 'SELECT PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CHICAGO_CONCENSUS_DATA ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5')


# ### Problem 8
# 
# ##### Which community area is most crime prone?
# 

# In[62]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(ID) AS NUM_OF_CRIME, COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(ID) DESC LIMIT 1')


# Double-click **here** for a hint
# 
# <!--
# Query for the 'community area number' that is most crime prone.
# -->
# 

# ### Problem 9
# 
# ##### Use a sub-query to find the name of the community area with highest hardship index
# 

# In[75]:


get_ipython().run_line_magic('sql', 'SELECT COMMUNITY_AREA_NAME FROM CHICAGO_CONCENSUS_DATA WHERE HARDSHIP_INDEX = (SELECT MAX(HARDSHIP_INDEX) FROM CHICAGO_CONCENSUS_DATA)')


# ### Problem 10
# 
# ##### Use a sub-query to determine the Community Area Name with most number of crimes?
# 

# In[88]:


get_ipython().run_line_magic('sql', 'SELECT COMMUNITY_AREA_NAME FROM CHICAGO_CONCENSUS_DATA WHERE COMMUNITY_AREA_NUMBER = (SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(ID) DESC LIMIT 1)')


# Copyright © 2020 This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 

# ## Author(s)
# 
# <h4> Hima Vasudevan </h4>
# <h4> Rav Ahuja </h4>
# <h4> Ramesh Sannreddy </h4>
# 
# ## Contribtuor(s)
# 
# <h4> Malika Singla </h4>
# 
# ## Change log
# 
# | Date       | Version | Changed by        | Change Description                             |
# | ---------- | ------- | ----------------- | ---------------------------------------------- |
# | 2022-03-04 | 2.5     | Lakshmi Holla     | Changed markdown.                              |
# | 2021-05-19 | 2.4     | Lakshmi Holla     | Updated the question                           |
# | 2021-04-30 | 2.3     | Malika Singla     | Updated the libraries                          |
# | 2021-01-15 | 2.2     | Rav Ahuja         | Removed problem 11 and fixed changelog         |
# | 2020-11-25 | 2.1     | Ramesh Sannareddy | Updated the problem statements, and datasets   |
# | 2020-09-05 | 2.0     | Malika Singla     | Moved lab to course repo in GitLab             |
# | 2018-07-18 | 1.0     | Rav Ahuja         | Several updates including loading instructions |
# | 2018-05-04 | 0.1     | Hima Vasudevan    | Created initial version                        |
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 

# In[85]:





# In[ ]:




