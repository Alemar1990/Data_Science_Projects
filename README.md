# Data Science Projects

![What_is_Data_Science](What_is_Data_Science.jpg)

These are some projects carried out by me, where I carry out the analysis of the data sets and develop some models.

# Data science
Data science, without going too deep, is nothing more than a set of methodologies to use on available data to obtain meaningful conclusions. 
What makes up a data science?

A data scientist is globally composed of three areas:
- Mathematical and statistical knowledge
- Programming knowledge
- Knowledge and vision of the business

Among others:
- Knowledge of machine learning 
- Passion for data
- Knowledge of handling large volumes of data
- Ability to communicate the knowledge that has been extracted from the data

## What can data do?

Data can describe the current state of an organization or process, such as why energy consumption has increased, why sales are low, and so on.
It can help detect anomalous events, such as fraudulent purchases or non-normal operating conditions.
Data can also diagnose the causes of observed events and behaviors, such as if there was a failure, why it happened.
Data can predict future events, such as forecasting the price of a stock or the composition of a product. 
There is one quote that I would like to show you why data has become so important today, according to Eric Schmidt, who is a senior executive at Google.
5 Exa -> 5e9 -> 5,000,000,000,000 -> 5 billion Gb

To develop the models, we like to be guided by the following Framework:

## Framework
<p align="center">
<img src="https://www.section.io/engineering-education/data-mining-using-crisp-dm-methodology/crisp-dm-framework.png" width="800">
 
## Cross Industry Standard Process for Data Mining (CRISP-DM)
A data mining process model that describes commonly used approaches that data mining experts use to tackle problems... it was the leading methodology used by industry data miners. 

This framework is based on the following steps:

### Business Issue Understanding
This initial phase focuses on understanding the project objectives and requirements from a business perspective, and then converting this knowledge into a data mining problem definition, and a preliminary plan designed to achieve the objectives. A decision model, especially one built using the Decision Model and Notation standard can be used.

For them we must answer the following questions:
- What decisions needs to be made?
- What information is needed to inform those decisions?
- What type of analysis can provide the information needed to inform those decisions?

### Data Understanding
The data understanding phase starts with an initial data collection and proceeds with activities in order to get familiar with the data, to identify data quality problems, to discover first insights into the data, or to detect interesting subsets to form hypotheses for hidden information.

For that we must answer the following questions:
- What data is needed?
- What data is available?
- What are the important characteristics of the data?

### Data Preparation
The data preparation phase covers all activities to construct the final dataset (data that will be fed into the modeling tool(s)) from the initial raw data. Data preparation tasks are likely to be performed multiple times, and not in any prescribed order. Tasks include table, record, and attribute selection as well as transformation and cleaning of data for modeling tools.

Common Steps Used in Data Preparation:
- Gathering: When gathering data - you may need to collect data from multiple sources within your organization.
- Cleansing: The data set you are working with may have issues that you want to resolve prior to your analysis. This can be in the form of incorrect or missing data.
- Formatting: You may need to format the data by changing the way a date field appears, renaming a field, or even rotating the data, similar to using a pivot table.
- Blending: You may want to blend, or combine, your data with other datasets to enrich it with additional variables, similar to using the vlookup function in Excel.
- Sampling: Lastly, you may want to sample the dataset and work with a more manageable number of records.

### Analysis/Modeling
In this phase, various modeling techniques are selected and applied, and their parameters are calibrated to optimal values. Typically, there are several techniques for the same data mining problem type. Some techniques have specific requirements on the form of data. Therefore, stepping back to the data preparation phase is often needed.

Important Steps:
- Determine what methodology to use to solve the problem
- Determine the important factors or variables that will help solve the problem
- Build a model to solve the problem
- Run the model and move to the validation phase

### Validation
At this stage in the project you have built a model (or models) that appears to have high quality, from a data analysis perspective. Before proceeding to final deployment of the model, it is important to more thoroughly evaluate the model, and review the steps executed to construct the model, to be certain it properly achieves the business objectives. A key objective is to determine if there is some important business issue that has not been sufficiently considered. At the end of this phase, a decision on the use of the data mining results should be reached.

Important Steps:
- Observe the key results on the model
- Ensure the results make sense within the content of the business problem
- Determine whether to proceed to the next step or return to a previous phase
- Repeat as many times as necessary

### Presentation/Visualization
Creation of the model is generally not the end of the project. Even if the purpose of the model is to increase knowledge of the data, the knowledge gained will need to be organized and presented in a way that is useful to the customer. Depending on the requirements, the deployment phase can be as simple as generating a report or as complex as implementing a repeatable data scoring (e.g. segment allocation) or data mining process. In many cases it will be the customer, not the data analyst, who will carry out the deployment steps. Even if the analyst deploys the model it is important for the customer to understand up front the actions which will need to be carried out in order to actually make use of the created models.

Key Considerations:
- Determine the best method of presenting insights based on the analysis
- Determine the best method of presenting insights based on the audience
- Make sure the amount of information shared is not overwhelming
- Use the results to tell a story to the audience
- For more complex analyses, you may want to walk the audience through the analytical problem solving process
- Always reference the data sources used
- Make sure your analysis supports the decisions that need to be made