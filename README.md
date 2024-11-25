import streamlit as st

st.title("Biography")

st.sidebar.header("Personal Information")
name = st.sidebar.text_input("Name:", "Cristhal B.Combestra")
occupation = st.sidebar.text_input("Year:", "Freshmen")
location = st.sidebar.text_input("Location:", "Dinagat Island,San Jose")

st.sidebar.header("About Me")
about_me = st.sidebar.text_area("Write a short paragraph about yourself:", """
I am passionate about the life.
I am currently working on biography.
""")

st.header(f"{name}'s Biography")

col1, col2 = st.columns(2)

with col1:
    st.subheader("09853242540")
    email = st.text_input("Email Address:", "cristhalcombestra@gmail.com")
    linkedin = st.text_input("LinkedIn Profile URL:", "https://www.linkedin.com/in/[https://www.facebook.com/profile.php?id=100071737216055]")
    st.write("Please update with your actual contact information.")


with col2:
    st.subheader("Biography")
    st.write(f"Name: {name}")
    st.write(f"Year: {freshmen}")
    st.write(f"Location: {Dinagat island}")


st.header("About Me")
st.write(about_me)

#Optional Image upload (Comment out if you don't need it)
#uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
#if uploaded_file is not None:
#    st.image(uploaded_file, caption=f"Image of {name}", use_column_width=True)


st.markdown("---") #Horizontal line for visual separation
st.write("This biography is created using Streamlit.")

