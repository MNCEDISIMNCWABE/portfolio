import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Mncedisi's Webpage", page_icon=":white_flower:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img_loop = Image.open("images/loop.png")
img_tal = Image.open("images/tal2.png")
img_mcg = Image.open("images/mcg3.jpg")
stockp = Image.open("images/original.png")
prope = Image.open("images/prop.png")
mult = Image.open("images/mult.png")
out = Image.open("images/outlier.png")
viz = Image.open("images/viz.jpg")
ht = Image.open("images/ht.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, I am Mncedisi Mncwabe :wave:")
    st.title("A Data Scientist From South Africa")
    st.write(
        """I've been working for over 3 years on Data Science and Analytics projects. 
           I'm passionate about learning new concepts to continuously build on my previous knowledge.
           My professional interests are using my toolbox of programming, machine learning, statistics and probability to solve challenging problems.
           These problems can be theoretical or practical in nature.
           """
    )
    st.write("[LinkedIn Profile >](https://www.linkedin.com/in/mncedisi-mncwabe-a1b087171/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((12,5))
    with left_column:
        st.header("Skillset Summary")
        st.write(
            """
            | Tool                                                    | Estimated Hours Of Usage                               |
            | --------------------------------------------------------|------------------------------------------------------- |
            | SQL (MS SQL Server, MySQL, Google BigQuery, PostgreSQL) | 3500                                                   |
            | Data Visualization (dashboards)                         | 2000                                                   |
            | Data Studio, Power BI, Tableau                          | 2000                                                   |
            | Python (incl. pandas, numpy, scipy, sklearn, datetime)  | 1800                                                   |
            | Google Sheets, Microsoft Excel                          | 1500                                                   |
            | Supervised Learning                                     | 1200                                                   |
            | Clustering algorithms (K-means, DBSCAN, hierarchical)   | 1000                                                   |
            | Constrained Clustering (constrained K-means)            | 800                                                    |
            | Prophet, ARIMA, SARIMA models (time series prediction)  | 800                                                    |
            | R (R-Studio, R-GUI)                                     | 600                                                    |
            | Theory of Experimental Design (hypothesis testing etc.) | 350                                                    | 
            | SAS                                                     | 200                                                    | 
            | Recommender Engines (incl. Collaborative Filtering)     | 105                                                    | 
            | Streamlit                                               | 100                                                    | 
            | Linear Optimisation                                     | 85                                                     | 
            | TensorFlow, Keras                                       | 80                                                     | 
            | Natural Language Processing                             | 75                                                     |
            | Uplift Modelling                                        | 40                                                     | 
            | Exponential Smoothing Models (time series prediction)   | 35                                                     | 
            | Web Scraping (Python BeautifulSoup & Selenium)          | 30                                                     |
            | Git                                                     | 15                                                     |
            | ...list TBC                                             | 0                                                      |
 
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")
        
# ---- EXPERIENCE ----
with st.container():
    st.write("---")
    st.header("Experience")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_loop)
    with text_column:
        st.subheader("Snr Data Scientist")
        st.write(
            """
            Sep 2022 - present
            
            **Tools & Skills:**
            Google Analytics · Looker Studio (Data Studio) · Google Cloud Platform (GCP) · Data Science · Machine Learning · Route Planning ·
            Data Analysis · Python · Statistics · Data Visualization · SQL · Google BigQuery · Time Series Forecasting 
            """
        )
        #st.markdown("[Watch Video...](link-here)") 
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_tal)
    with text_column:
        st.subheader("Data Scientist")
        st.write(
            """
            Aug 2021 - Aug 2022
            
            **Tools & Skills:**
            Python · R · Machine Learning · Predictive & Prescriptive Analytics · Time Series Forecasting · Data Analysis · Data Visualization · MySQL · 
            PostgreSQL · Google Cloud Platform (GCP) · Google Big Query · Looker Studio (Data Studio) · MS Excel · QlikView/QlikSense ·
            MS Power BI · Google Slides · Google Sheets
            """
        )
        #st.markdown("[Watch Video...](link-here)")  
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mcg)
    with text_column:
        st.subheader("Data Analyst | Specialist Customer Quality")
        st.write(
            """
           Feb 2020 - Jul 2021
           
            **Tools & Skills:**
            Python · Machine Learning · MS SQL Server · PostgreSQL · MS Power BI · MS Excel · Data Analysis · 
            Data Visualization · MS Power Automate · Speech Analytics · Nexidia Analytics
            """
        )
        #st.markdown("[Watch Video...](link-here)")   
  

     
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Exploring Machine Learning & Data Analytics")
    st.write("##")
    st.write(
            """
            These are some of the projects or frameworks I've explored during my spare time outside of my professional working environment and hours.
            """
        )
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(stockp)
    with text_column:
        st.subheader("Closing Stock Price Predictions App")
        st.write(
            """
            The app allows users to easily type a company's ticker symbol, as listed on Yahoo Finance, and the date range 
            then the app will run that through the model to predict the closing stock price for the selected date(s). 
            The model is trained and tested on the historical stock price data from Yahoo Finance.
            """
        )
        st.markdown("[Deployed Web App Link...](https://sp-preds-predictions-mod-app-aqcjue.streamlit.app/)")         

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(prope)
    with text_column:
        st.subheader("Customer Purchase Propensity Modelling")
        st.write(
            """
            Propensity Modelling is a method of generating a probability score on how customers do a particular action. 
            In this exercise I explore a combination of Propensity Analysis with RFM scores (Recency, Frequency, Monetary) 
            to predict the probability score of a customer to purchase a product after a campaign was done.

            """
        )
        st.markdown("[Propensity Modelling...](https://github.com/MNCEDISIMNCWABE/exploring-ml-and-analytics/tree/main/Propensity%20Modelling)")        
 
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(mult)
    with text_column:
        st.subheader("Multiple Time Series Forecasting")
        st.write(
            """
            Using Light Gradient-Boosting to forecast the sales of multiple store products.

            """
        )
        st.markdown("[Multiple Time Series...](https://github.com/MNCEDISIMNCWABE/exploring-ml-and-analytics/tree/main/Multiple%20Time%20Series%20Forecasting)")     
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(out)
    with text_column:
        st.subheader("Comparison Of Outlier Detection Models ")
        st.write(
            """
            Using PyOD to compare the detection of outliers by several models such as Histogram-based Outlier Score, K Nearest Neighbors,
            Isolation Forest and Feature Bagging.
            """
        )
        st.markdown("[Outlier Detection...](https://github.com/MNCEDISIMNCWABE/exploring-ml-and-analytics/tree/main/Comparing%20Oulier%20Detection%20Algorithms)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(ht)
    with text_column:
        st.subheader("Predict The Likelihood Of Someone Being At Risk For Heart Disease")
        st.write(
            """
           Using Machine Learning to identify people who are at risk for heart disease. This would
           be a good indicator of people that will benefit most from health-allowance.
            """
        )
        st.markdown("[Heart Disease Prediction...](https://github.com/MNCEDISIMNCWABE/exploring-ml-and-analytics/tree/main/Heart%20Disease%20Classification)") 
        
with st.container():
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(viz)
with text_column:
    st.subheader("Data Visualization")
    st.write(
        """
       I worked on a data visualization project which was part of Maven Analytics challenge series.
       The dataset featured 375000+ Kickstarter projects from 2009-2017, including project name, category and more.
       The objective of the project was to generate key insights to enable investors to identify projects with higher likelihood of success.
       Link below contains some more data visualization work.
        """
    )
    st.markdown("[Data Visualization...](https://github.com/MNCEDISIMNCWABE/exploring-ml-and-analytics/tree/main/Data%20Visualization)")       

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Let's Chat...")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/leemncwabe29@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
