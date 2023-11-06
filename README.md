<h1> SOBRIETY TEST MODEL </h1>
<h2> Midterm project during DataTalksClub Zoomcamp September 2023 </h2>
<h2> Objectives for the Project </h2>
<ol>
  <li> Find a problem and select the best dataset </li>
  <li> Explore data, analyze feature importance and prepare the data </li>
  <li> Train, evaluate models on different thresholds and select the best parameters </li>
  <li> Export the notebook into a script </li>
  <li> Dump model inside a web service </li>
  <li> Deploy the model locally using Docker </li>
</ol>
<h2>  OVERVIEW </h2>

Excessive alcohol consumption can result in increased healthcare costs, including hospitalizations, addiction treatments, and mental health care. Therefore reducing the impact of excessive drinking on healthcare budgets is essential.
Predictive models can assist healthcare organizations in identifying high-risk individuals who are more likely to develop alcohol-related illnesses. Early intervention and alcohol cessation programs can be targeted toward these high-risk patients, reducing the overall healthcare expenditure associated with alcohol-related diseases. Additionally, understanding the prevalence of excessive drinking and the distribution of drinking behavior in different populations is crucial for public health planning. Models can provide insights into the drinking behavior of different population groups.

This kaggle [dataset](https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset) is collected from National Health Insurance Service in Korea. All personal information and sensitive data were excluded.
The purpose of this dataset is to:
<ul>
  <li>Analysis of body signal</li>
  <li>Classification of smoker or drinker</li>
</ul>

<h2> APPROACH </h2>

The aim of this project is to train and deploy a model that can predict the sobriety state of any individual. 
I have developed an alcohol prediction model focusing on the "DRK_YN" target variable while also using "SMK_stat_type_cd" which is the smoking target variable as part of the training features to be used to build the model. The result of the prediction is given in binary 1 or 0, in which case 1 represents "Drunk" or "Drinking" and 0 represents "Sober" or "Not drinking".
- Explore and Prepare data
  - Checked for missing and null values
  - Checked the columns for uniformity
  - Checked the numbers of features
  - Carried out feature importance to know what feature is relevant or not
- Prepare data
  - Changed the target variable from a categorical variable to a numerical variable.
  - Split data into USED NOW & USED LATER due to the size of my dataset
- Train data
  - Used DictVectorizer to encode the categorical data
  - Trained the model with a DecisionTreeClassifier

<h2> HOW TO RUN THIS PROJECT LOCALLY </h2>

- Setup virtual environment.
  - Open your terminal and run
  
   ``` pip install pipenv ```
  - Start up the virtual environment using ``` pip shell ```
  
- Install the following libraries using pipenv
  
  - Run ``` pipenv install scikit-learn==1.0.2 flask numpy==1.25.2 gunicorn requests ```
  
  - To make prediction: run both ``` predict.py ``` & ``` serving_predict.py ```

<h2> HOW TO RUN THIS PROJECT USING DOCKER </h2>

Download the Dockerfile into a directory

Create docker image by running

``` docker build -t image_name PUT_DOCKER_NAME ```

Access the docker terminal and run the service with gunicorn

``` gunicorn --bind 0.0.0.0:9696 predict:sobriety_test ```

Finally run serving_predict.py 

<h2> FINAL RESULT </h2>

If you have followed the steps accordingly, your requests should give results in json format. 
And your response will either be "Sober" or "Drunk", this can further be used in  public health policies, 
resources management, resources allocation, and the development of drinking prevention and cessation programs targeting specific areas in need.




