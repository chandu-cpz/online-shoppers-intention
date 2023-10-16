import streamlit as st
from streamlit_option_menu import option_menu
import sklearn
import pickle

@st.cache_resource
def load_model():
    rfc = pickle.load(open("rfc.pkl", "rb"))
    return rfc

# Layout wide
st.set_page_config(layout="wide")

# Hide default header
hide_default_header = """
   <style>
   header {visibility: hidden;}  
   </style>
"""
st.markdown(hide_default_header, unsafe_allow_html=True)


st.markdown("""
<style>
.ea3mdgi4 {
   padding: 0 !important;
   margin: 0 !important;
    margin-left:20px !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([4, 3])

with col2:
    menu = option_menu(None, ["Home", "Predict", "About"],
                       icons=['house', 'graph-up', 'info'],
                       default_index=0, orientation="horizontal")


# Rest of the app
if menu == "Predict":
    with col1:
        header_html = "<div style='padding:5px;font-size:30px;font-weight:boldest; color: white;'>Online Shoppers Intention</div>"
        st.markdown(header_html, unsafe_allow_html=True)
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([2,3,3,3,2])
        with col2:
            BounceRates = st.number_input("Bounce Rates:", min_value=0)
        with col3:
            ExitRates = st.number_input("Exit Rates: ", min_value= 0)
        with col4:
            PageValues = st.number_input("Page Values: ", min_value= 0)
        monthDict = {
            "Jan" : 1, 
            "Feb" : 2,
            "Mar" : 3,
            "April" : 4,
            "May" : 5,
            "June" : 6,
            "Jul" : 7,
            "Aug" : 8,
            "Sep" : 9, 
            "Oct" : 10,
            "Nov" : 11,
            "Dec" :12
        }
        col1, col2, col3, col4, col5 = st.columns([2,3,3,3,2])
        with col2:
            Month = st.selectbox("Month", monthDict.keys())
        with col3:
            SpecialDay = st.checkbox("Special Day")            
        with col4:
            Weekend = st.checkbox("Weekend")
        
        col1, col2, col3, col4 = st.columns([2,4,4,2])
        with col2:
            Administrative	= st.number_input("Administrative: ",min_value= 0)
        with col3:
            Administrative_Duration	= st.number_input("Administrative_Duration: ",min_value= 0)

        col1, col2, col3, col4 = st.columns([2,4,4,2])
        with col2:
             Informational = st.number_input("Informational : ",min_value= 0)
        with col3:
             Informational_Duration = st.number_input("Informational_Duration : ",min_value= 0)

        col1, col2, col3, col4 = st.columns([2,4,4,2])
        with col2:
            ProductRelated = st.number_input("ProductRelated: ", min_value= 0)
        with col3:
            ProductRelated_Duration = st.number_input("ProductRelated_Duration: ", min_value= 0)

        
        col1, col2, col3, col4 = st.columns([2,4,4,2])
        with col2:
            OperatingSystems	= st.number_input("OperatingSystems: ",min_value= 0, max_value=8)
        with col3:
            Browser	= st.number_input("Browser: ",min_value= 0, max_value=13)

        col1, col2, col3, col4 = st.columns([2,4,4,2])
        with col2:
            Region	= st.number_input("Region: ",min_value= 0, max_value=9)
        with col3:
            TrafficType	= st.number_input("TrafficType: ",min_value= 0, max_value=20)

        col1, col2, col3 = st.columns([9,5,5])
        with col2:
            visitorType = st.radio("VisitorType", ["Returning_Visitor","New_Visitor","Other"])
        visitorDict = {
            "Returning_Visitor" : 0,
            "New_Visitor" : 1,
            "Other" : 2
        }
        clicked = False
        col1, col2, col3 = st.columns([9,1,9])
        with col2:
            if st.button("Predict") :
                rfc = load_model()
                prediction = rfc.predict([[Administrative, Administrative_Duration, Informational,
                Informational_Duration, ProductRelated, ProductRelated_Duration,
                BounceRates, ExitRates, PageValues, SpecialDay, monthDict[Month],
                OperatingSystems, Browser, Region, TrafficType, visitorDict[visitorType],
                Weekend]])
                clicked =True
                
        col1, col2, col3 = st.columns([2,9,2])
        with col2:
            if clicked:
                if prediction[0] == 0:
                    st.header("No, User doesn't seem to have intention of buying")
                else:
                    st.header("Yes, User seems to have purchase intentions")


elif menu == "About":
    # Set background
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("https://storage.googleapis.com/kaggle-datasets-images/1541571/2542239/01905c83acea07a60d45e08ec35af3d1/dataset-cover.jpg?t=2021-08-19-20-05-09"); 
        background-size: cover;
        }}  
        </style>
        """,
        unsafe_allow_html=True
    )
    with col1:
        header_html = "<div style='padding:5px;font-size:30px;font-weight:boldest; color: white;'>Online Shoppers Intention</div>"
        st.markdown(header_html, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 3, 1])
    c4, c5, c6 = st.columns([1, 3, 1])

    with c5:
        st.markdown("""
        <div style="height:100vh; display:flex; flex-direction:column; justify-content: center;">
            <h1 style='text-align:center; color:white;'>
                Online shopping is the activity or action of buying products or services over the Internet. It means going online, landing on a seller's website, selectin something, and arranging for its delivery.The buyer either pays for the good or service online with a credit or debit card on upon delivery.The term does not only include buying things online but also searching for them Online. In other words, I may have been engaged in online  shopping but did not buy anything.
            </h1>  
        </div>
        """, unsafe_allow_html=True)
else:
    st.title("Home")
    # Set background
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("https://steemitimages.com/DQmWncBMnJWXbam798YZJ2mMub1UVu842rCv2Z2Y4vsy7dw/Online-Shop-Website-Development-in-Kerala1.jpg"); 
        background-size: cover;
        }}  
        </style>
        """,
        unsafe_allow_html=True
    )
    with col1:
        header_html = "<div style='padding:5px;font-size:30px;font-weight:boldest; color: black;'>Online Shoppers Intention</div>"
        st.markdown(header_html, unsafe_allow_html=True)
