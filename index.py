# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import base64
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu




st.set_page_config(
        page_icon="Logo4.png",
        page_title="Dashboard Pro",
        layout="wide"
            )



data= pd.read_csv("titanic.csv")


# data=data.dropna()



# Function to convert an image file to base64 encoding
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



# Convert the local images to base64 encoding
background_img1 = get_img_as_base64("back.jpg")  # Replace with your local image path




def Line_Break(width):
        line_code=f"""

            <hr style="border: none; height: 2px;width: {width}%; background: linear-gradient(90deg, rgba(216,82,82,1) 13%, rgba(237,242,6,1) 57%, rgba(226,0,255,1) 93%); margin: 0 auto;" />


                    """
        st.markdown(line_code,unsafe_allow_html=True)

def Line_Break_start(width):
        line_code=f"""

            <hr style="border: none; height: 2px;width: {width}%; background: linear-gradient(90deg, rgba(216,82,82,1) 13%, rgba(237,242,6,1) 57%, rgba(226,0,255,1) 93%);" />


                    """
        st.markdown(line_code,unsafe_allow_html=True)

def heading(heading,color):
        heading_code=f"""

            <{heading} style='text-align: center;color: {color};'>Uplode DataSet</{heading}>


                    """
        st.markdown(heading_code,unsafe_allow_html=True)








# internal css 


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{background_img1}");

       
    background-size: 100%;
    background-position: top left;
    # background-repeat: no-repeat;
    # background-attachment: local;
    # opacity: 0.3;
    # transition: opacity 2s ease-in-out; /* 2 seconds transition */
}}



[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stSidebar"] > div:first-child {{
    background-repeat: no-repeat;
    background-attachment: fixed;
    # background: rgb(18 18 18 / 0%);
    background: #0d425d;
}}

.st-emotion-cache-h4xjwg {{

    display: none;
}}



.st-emotion-cache-1jicfl2 {{
    width: 100%;
    padding: 1rem 1rem 1rem;
    min-width: auto;
    max-width: initial;
}}




h1 {{
    font-family: "Source Sans Pro", sans-serif;
    font-weight: 700;
    color: rgb(250, 250, 250);
    padding: 1.25rem 0px 1rem;
    margin: 0px;
    font-size: 60px;
    line-height: 1.2;
}}


.st-emotion-cache-j5r0tf {{
    width: calc(20% - 1rem);
    flex: 1 1 calc(20% - 1rem);
    padding: 10px;
}}


.st-emotion-cache-j5r0tf {{
    width: calc(20% - 1rem);
    flex: 1 1 calc(20% - 1rem);
    padding: 10px;
    # border-right: 1px solid;
    border:1px solid white;

    background: #ffc10721;
    border-radius: 8px;
 box-shadow: 0 5px 32px rgb(22 131 144 / 70%);

}}

.js-plotly-plot .plotly .user-select-none {{
   border:1px solid white;

   background: #2a391854;
    border-radius: 8px;
 box-shadow: 0 5px 32px rgb(22 131 144 / 70%);
}}


[data-testid="stSidebar"] > div:first-child {{
    background-repeat: no-repeat;
    background-attachment: fixed;
    background: #168390;
}}


</style>
"""

# Apply CSS styling to the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)






        # Define the HTML and CSS for centered metrics
metric_html1 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """



metric_html2 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """

metric_html3 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;margin-top: 10px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """



metric_html4 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """


metric_html5 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """


metric_html6 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """

metric_html7 = """
        <div style="text-align: center;background:#13243d;margin-bottom: 40px;border-radius: 8px;border: 1px solid yellow;">
            <p style="font-size: 20px; margin: 0; color : white;">{label}</p>
            <p style="font-size: 32px; margin: 0; font-weight: bold;color : white;">{value}</p>
        </div>
        """







col1,col2= st.columns([1,4])



with col1:
        
        st.image("Logo4.png")
        
        df=data

        # Displaying Metric Cards
        survived_count = df[df['survived'] == 1].shape[0]
        total_passengers = df.shape[0]
        male_count = df[df['sex'] == 'male'].shape[0]
        female_count = df[df['sex'] == 'female'].shape[0]

            # st.dataframe(data)

        rows=data.shape[0]
        Features=data.shape[1]
            
        # Get the data types of each column
        data_types = data.dtypes

        # Convert to a set to get unique data types
        unique_data_types = set(data_types)




        # Get the number of unique data types
        num_unique_data_types = len(unique_data_types)

        
        
        st.markdown(metric_html3.format(label="Total Passengers", value=total_passengers), unsafe_allow_html=True)
        st.markdown(metric_html4.format(label="Male", value=male_count), unsafe_allow_html=True)
        st.markdown(metric_html5.format(label="Female", value=female_count), unsafe_allow_html=True)
        st.markdown(metric_html1.format(label="Survived Passengers", value=survived_count), unsafe_allow_html=True)
        st.markdown(metric_html2.format(label="Total Features", value=Features), unsafe_allow_html=True)
        st.markdown(metric_html2.format(label="Unique DataTypes", value=num_unique_data_types), unsafe_allow_html=True)
        st.markdown(metric_html2.format(label="Maximum DataType", value=num_unique_data_types), unsafe_allow_html=True)

        
       




        


with col2:

    st.title("Dash Board For Titanic DataSet")
    Line_Break(100)
    # st.dataframe(data)

    inner_col1,inner_col2=st.columns(2)

    with inner_col1:
        # Visualization 2: Survival by Gender
        st.subheader("Survival Rate by Gender")
        fig_gender = px.pie(df, names="sex", color="survived", hole=0.3)
                # Remove background color
        fig_gender.update_layout(
            plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot area background
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent outer paper background
        )
        st.plotly_chart(fig_gender)


    with inner_col2:
                # Visualization 2: Survival by Gender
        st.subheader("Count of Passengers by Class")
        # Rename class values for better readability
        df['Class'] = df['pclass'].replace({1: "First Class", 2: "Second Class", 3: "Third Class"})

        # Define colors for each class
        color_map = {
            "First Class": "royalblue",
            "Second Class": "darkorange",
            "Third Class": "green"
        }

        # Plotly bar chart with custom colors
        fig = px.bar(df, x="Class", color="Class", 
                    color_discrete_map=color_map)


        # Remove background color
        fig.update_layout(
            plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot area background
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent outer paper background
        )
        # Show the bar chart
        st.plotly_chart(fig)  
            

    

    inner_col3,inner_col4=st.columns(2)

    with inner_col3:
            
            # Define bright colors for survived (1) and not survived (0)
            color_map = {
                0: "red",       # Not Survived
                1: "limegreen"  # Survived
}

            # Visualization 3: Age Distribution of Survivors
            st.subheader("Age Distribution of Survivors")
            fig_age = px.histogram(df, x="age", color="survived", nbins=20,color_discrete_map=color_map,labels={"survived": "Survived (0 = No, 1 = Yes)"})
            
                    # Remove background color
            fig_age.update_layout(
                plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot area background
                paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent outer paper background
            )
            st.plotly_chart(fig_age)


    with inner_col4:
        # Define bright colors for each class
        color_map = {
            "First Class": "cyan",
            "Second Class": "magenta",
            "Third Class": "limegreen"
        }

        # Visualization 4: Fare Distribution by Class
        st.subheader("Fare Distribution by Class")
        fig_fare = px.box(df, x="Class", y="fare", points="all", color="Class", 
                        color_discrete_map=color_map)

        # Remove background color
        fig_fare.update_layout(
            plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot area background
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent outer paper background
        )

        # Show the box chart
        st.plotly_chart(fig_fare)





big_col1,big_col2=st.columns(2)


with big_col1:
      

    st.subheader("Survival Rate by Class")

    # Rename class values for better readability
    df['Class'] = df['pclass'].replace({1: "First Class", 2: "Second Class", 3: "Third Class"})
    
    # Define colors for each class
    color_map = {
        "First Class": "royalblue",
        "Second Class": "darkorange",
        "Third Class": "green"
    }

    # Create a pie chart for survival rate based on passenger class with custom colors
    fig_class = px.pie(df, names="Class", color="Class", hole=0.3, 
                        
                       color_discrete_map=color_map)
    
    # Remove background color
    fig_class.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot area background
        paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent outer paper background
    )

    # Show the pie chart
    st.plotly_chart(fig_class)

      

with big_col2:


    st.subheader("Survival by Embarked Location")

    # Rename embarked values for better readability
    df['Embarked'] = df['Embarked'].replace({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})

    # Define colors for each embarkation point
    color_map = {
        "Cherbourg": "dodgerblue",
        "Queenstown": "firebrick",
        "Southampton": "forestgreen"
    }

    # Create a bar chart for survival based on embarkation location with custom colors
    fig_embarked = px.bar(df, x="Embarked", color="Embarked", barmode="group", 
                          facet_col="survived", labels={"Embarked": "Embarkation Location", "survived": "Survived (0 = No, 1 = Yes)"}, 
                          color_discrete_map=color_map)
    
    # Remove background color
    fig_embarked.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot area background
        paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent outer paper background
    )
    
    # Show the bar chart
    st.plotly_chart(fig_embarked)



               

# Footer section using HTML and CSS
footer = """
    <style>
    .footer {
    left: 0;
    bottom: 0;
    width: 100%;
    # background-color: #04a5ee;
    text-align: center;
    padding: 10px;
    BORDER-RADIUS: 10PX;
    font-size: 14px;
    # BORDER: 1PX SOLID WHITE;
    color: #fcfcfc;
    MARGIN-TOP: 20PX;
    }

    


    </style>
    <div class="footer">
        <p>Developed by Salman Malik | © 2024 All Rights Reserved</p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
   