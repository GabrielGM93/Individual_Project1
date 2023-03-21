<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **INDIVIDUAL PROJECT Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://raw.githubusercontent.com/GabrielGM93/Individual_Project1/master/assets/Slide1.jpg"  height=300>
</p>

Welcome! On this occasion, you will find my first job placing me in the role of a ***MLOps Engineer***.  

<hr>  

## **Description of the problem (Context and role to develop)**

You started working as **`Data Scientist`** in a start-up that provides aggregation services for streaming platforms. The world is beautiful and you are going to create your first ML model that solves a business problem: a recommendation system that has not been launched yet!

You go to their data and you realize that their maturity is low (ok, it's null :sob:): Untransformed data, there are no automated processes for updating new movies or series, among other things…. making your job impossible :weary:.

You must start from 0, doing a quick job of **`Data Engineer`** and have an **`MVP`** (_Minimum Viable Product_) for the next week!. So you scare away your fears and get to work :muscle:

Here are reflected the relationship of the processes that we are going to develop.

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/blob/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>


**`Transformations`**:

+ Generate **`ID`** field: Each id will consist of the first letter of the platform name, followed by the show_id already present in the datasets (example for Amazon titles = **`as123`**)

+ The null values of the rating field must be replaced by the string “**`G`**” (corresponds to the maturity rating: “general for all audiences”

+ Dates must have the format **`YYYY-mm-dd`**

+ Text fields must be in **lowercase**

+ The field ***duration*** must be converted to two fields: **`duration_int`** and **`duration_type`**. The first will be an integer and the second a string indicating the unit of duration measurement: min (minutes) or season (seasons).

You can access the transformation processes through the "ETL.ipynb" file

<br/>

**`API Development`**: I propose to make the company data available using the ***FastAPI*** framework. The queries are as follows:

+ Movie with longer duration with optional filters of YEAR, PLATFORM AND TYPE OF DURATION. (the function should be called get_max_duration(year, platform, duration_type))

+ Number of movies per platform with a score greater than XX in a given year (the function must be called get_score_count(platform, scored, year))

+ Number of movies per platform with PLATFORM filter. (The function should be called get_count_platform(platform))

+ Actor who repeats himself the most according to platform and year. (The function should be called get_actor(platform, year))

To start this work first I create a local virtual environment, install FastApi and Uvicorn libraries in it, create the main.py file using decorators, once everything is in order, within the virtual environment I create the requirements.txt file through the pip command freeze > requirements.txt, upload the datasets, main.py and requirements.txt to github. Once done from [Render](https://dashboard.render.com/) we deploy the repository, where it already gives us the access link to the functions

You can click the [link](https://proyecto-individual1.onrender.com/docs) to access the developed API,set the platform parameter only using the first letter of it, Amazon = "a", Netflix ="n", Hulu="h", Disney= "d" and the parameters for duration_type are "min" or "season"

<br/>

