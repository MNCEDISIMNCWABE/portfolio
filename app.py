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

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, I am Mncedisi Mncwabe :wave:")
    st.title("A Data Scientist From South Africa")
    st.write(
        """I've been working for over 3 years on Data Science and Analytics projects. 
           I'm passionate about learning new concepts, especially in Data Science or Analytics space to continuously build on my previous knowledge.
           My professional interests are using my toolbox of programming, machine learning, statistics, and probability to solve challenging problems.
           These problems can be theoretical or practical in nature.
           """
    )
    st.write("[LinkedIn Profile >](https://www.linkedin.com/in/mncedisi-mncwabe-a1b087171/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((12,5))
    with left_column:
        st.header("Summary of my skillsets")
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
            | Prophet, ARIMA, SARIMA models (time series prediction)  | 800                                                    |
            | R                                                       | 600                                                    |
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
        st_lottie(lottie_coding, height=300, key="coding")
        
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
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)") 
        
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
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")  
        
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
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")   
  

     
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    st.write(
            """
            These are some of the projects I've worked on. I explored some of them during my spare time.
            """
        )
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
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
        st.image(img_contact_form)
    with text_column:
        st.subheader("Customer Purchase Propensity Modelling")
        st.write(
            """
            Propensity Modelling is a method of generating a probability score on how customers do a particular action. 
            In this exercise I explore a combination of Propensity Analysis with RFM scores (Recency, Frequency, Monetary) 
            to predict the probability score of a customer buying a product after a campaign was done.

            """
        )
        st.markdown("[Propensity Modelling...](https://github.com/MNCEDISIMNCWABE/exploring-ml-and-analytics/tree/main/Propensity%20Modelling)")        
        
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Let's Chat...")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/leemncwabe29@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
