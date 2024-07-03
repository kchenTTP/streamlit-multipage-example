import streamlit as st


st.header("This is your secret dashboard")
st.info("You've successfully logged in!")

with st.sidebar:
    st.header("Options")
    with st.container(border=True):
        st.subheader("Date Range")
        st.slider("How old are you?", 0, 130, 25)

    with st.container(border=True):
        st.subheader("Filters")
        instructor_list = st.multiselect("What are your favorite colors",["Green", "Yellow", "Red", "Blue"],["Yellow", "Red"])
        series_bool = st.selectbox(
            "Series Based",
            options=["Standalone", "Series Based Program"],
            index=None,
            placeholder="All",
        )
        online_bool = st.selectbox(
            "In-Person or Online",
            options=["In-Person", "Online"],
            index=None,
            placeholder="All",
        )
        st.button("🚨 Click me if user interface isn't updating! 🚨", type="primary")

