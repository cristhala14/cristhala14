import streamlit as st
import datetime

# ---- Page Configuration ----
st.set_page_config(page_title="BIOGRAPHY", page_icon="📋", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("BIOGRAPHY")  # large font size

# ---- Personal Info (Left Side) ----
with st.container():
    left_column, right_column = st.columns(2)  # alignment

    with left_column:
        st.subheader("Personal Information")  # medium font size
        
        st.image("2.jpg")
        
        # Name Input
        name = st.text_input("Name", "Cristhal Combestra")
        
        # Age Selection
        age = st.selectbox("age", [str(i) for i in range(18, 101)])  # ages 18-100
        
        # Gender Selection
        gender = st.radio("Gender", ["Female", "Male"])
        

        # ---- Family Background ----
        st.subheader("Family Background")
        
        # Mother's Name
        mother = st.text_input("Mother's Name", "Roselyn B. Combestra")
        mbday = st.date_input("Mother's Birthday", datetime.date(1983, 2, 12))  # Default date
           # Guardian's Name
        guardian = st.text_input("Father's name", "Generoso A. Combestra")
        # Father's Name
        mbday = st.date_input("Father's Birthday", datetime.date(1961, 7, 17))  # Default date
        
        
     

        st.write("---")

        # ---- Educational Attainment ----
        st.subheader("Educational Attainment")
        hs = st.text_area("High School", "JBE-ANHS")
        college = st.text_area("College", "SNSU")
    
    with right_column:
        # ---- Social Media Section ----
        st.subheader("Social Media Accounts")
        fb = st.text_input("Facebook", "Cristhal Baring Combestra")
        instagram = st.text_input("Instagram", "cls_cmbtr")
        twitter = st.text_input("Twitter", "Enter Twitter handle")
        youtube = st.text_input("YouTube", "Enter YouTube channel")

        st.write("---")
        
    
        
# Footer
st.write("[Visit My Facebook Profile](https://www.facebook.com/profile.php?id=100071737216055)")  # Hyperlink example



