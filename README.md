<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **INDIVIDUAL PROJECT Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://raw.githubusercontent.com/GabrielGM93/Individual_Project1/master/assets/Slide1.jpg"  height=300>
</p>

Welcome! On this occasion, you will find my first job placing me in the role of a ***MLOps Engineer***.  

<hr>  

## **Context and role to develop**

You've just joined a start-up as a data scientist that provides aggregation services for streaming platforms. You're excited to start working on your first ML model that will solve a key business problem - a recommendation system that hasn't been launched yet!

However, as you start digging into their data, you quickly realize that their data maturity level is low, and there are no automated processes for updating new movies or series, among other things. This makes your job seem impossible, and you realize that you'll have to start from scratch and perform a quick data engineering job to have a Minimum Viable Product (MVP) ready by the end of the week.

Despite feeling overwhelmed, you decide to face your fears and get to work. You know that the key to success lies in developing a well-planned process, so you start mapping out the relationship between the various processes that need to be developed." :muscle:

Here are reflected the relationship of this processes:

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/blob/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>


## **Activities**
**`Transformations`**:

+ Generate **`ID`** field: Each id will consist of the first letter of the platform name, followed by the show_id already present in the datasets (example for Amazon titles = **`as123`**)

+ The null values of the rating field must be replaced by the string “**`G`**” (corresponds to the maturity rating: “general for all audiences”

+ Dates must have the format **`YYYY-mm-dd`**

+ Text fields must be in **lowercase**

+ The field ***duration*** must be converted to two fields: **`duration_int`** and **`duration_type`**. The first will be an integer and the second a string indicating the unit of duration measurement: min (minutes) or season (seasons).

You can access the transformation processes through the file "ETL.ipynb" 

<br/>

**`API Development`**: I propose to make the company data available using the ***FastAPI*** framework. The queries are as follows:

+ Movie with longer duration with optional filters of YEAR, PLATFORM AND TYPE OF DURATION. (the function should be called get_max_duration(year, platform, duration_type))

+ Number of movies per platform with a score greater than XX in a given year (the function must be called get_score_count(platform, scored, year))

+ Number of movies per platform with PLATFORM filter. (The function should be called get_count_platform(platform))

+ Actor who repeats himself the most according to platform and year. (The function should be called get_actor(platform, year))

To start this work, first, I create a local virtual environment and install the FastApi and Uvicorn libraries in it. Then, I create the main.py file using decorators. Once everything is in order, I create the requirements.txt file within the virtual environment using the pip command 'freeze > requirements.txt'. After that, I upload the datasets, main.py, and requirements.txt to GitHub. Finally, I deploy the repository from Render, which provides us with the access link to the functions.

You can click the [link](https://proyecto-individual1.onrender.com/docs) to access the developed API,set the platform parameter only using the first letter of it, Amazon = "a", Netflix ="n", Hulu="h", Disney= "d" and the parameters for duration_type are "min" or "season"

<br/>


**`Exploratory Data Analysis-EDA`**:

Now that the data has been cleaned, it's time to investigate the relationships between variables in the datasets and identify possible outliers or anomalies. These anomalies may not necessarily be errors, but could be valuable insights into the data. Furthermore, it's essential to identify any interesting patterns that could be explored in further analysis.

To help draw conclusions from the data, we have libraries like pandas profiling, sweetviz, autoviz, and other similar tools. These tools can assist visualizing the relationships between the variables and identifying patterns that may not be immediately apparent.

To perform this, we observe unique users, the distribution of ratings, whether there are duplicates or not, and we also see, with the help of the pandas profiling library, where we see variables, interactions, correlations, and missing values.

**`Recommendation system:`**:

Once we have prepared our data and it is ready for the analytics and machine learning department, it's time to train our model. In this case, we will be building a movie recommendation system for users, where given a user ID and a movie, the model will tell us whether to recommend it or not. To carry this out, it's important to make sure we have a full understanding of the data and have conducted proper EDA. Once the model is trained, we can proceed to deploy it, either in the form of a user-friendly graphical interface using Gradio or a similar solution like Streamlit. Having a user interface is a big plus for our project.

To Create a Surprise Dataset,in order to train recommender systems with Surprise, we need to create a Dataset object. A Surprise Dataset object is a dataset that contains the following fields in this order:

1 The user IDs

2 The item IDs (in this case the IDs for each book)

3 The corresponding rating (usually on a scale such as 1–5)

Then we define READER and DATA, separate our data with train_test_split, instantiate the model, in this case, Singular Value Decomposition (SVD), train it, once done we can make predictions, we also verify the RMSE and perform hyperparameter optimization.


In the file EDA_recommendationsystem.ipynb, we can see the detailed procedures for both *`Exploratory Data Analysis-EDA`* and *`Recommendation system`*



<br/>
