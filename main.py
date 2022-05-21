import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings

warnings.filterwarnings("ignore")
model = pickle.load(open("flight price prediction model.joblib","rb")) #loading the created model


st.set_page_config(page_title="Flight Price Prediction Application") #tab title

#prediction function
def predict_status(Airline, Source, Destination, Total_Stops, Additional_Info, Date, Month, Year, Arrival Hour, Arrival Minute, Departure Hour, Departure Minute, Duration Min):
    input_data = np.array([[Airline, Source, Destination, Total_Stops, Additional_Info, Date, Month, Year, Arrival Hour, Arrival Minute, Departure Hour, Departure Minute, Duration Min]])
    #input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("Flight Price Prediction Application")

    #getting the input
    Airline = st.text_input("Enter your Airline")
    Source = st.text_input("Enter your Source")
    Destination = st.text_input("Enter your Destination")
    Total_Stops = st.number_input("Enter your Total Stops")
    Additional_Info = st.text_input("Enter your Additional Info")
    Date = st.text_input("Enter your Date")
    Month = st.text_input("Enter your Month")
    Year = st.text_input("Enter your Year")
    Arrival Hour = st.text_input("Enter your ArrivalHour")
    Arrival Minute = st.text_input("Enter your Arrival Minute")
    Departure Hour = st.text_input("Enter your Departure Hour")
    Departure Minute = st.text_input("Enter your Departure Minute")
    Departure Min = st.text_input("Enter your Departure Min")

    #predict value
    diagnosis = ""

    if st.button("Predict"):
    
        Prie = predict_status(Airline, Source, Destination, Total_Stops,	Additional_Info, Date, Month,	Year,	Arrival Hour,	Arrival Minute,	Departure Hour,	Departure Minute,	Duration Min)
        st.success("You'r Flight Price is: ", Price)

    st.write(" ")    
    st.write("Project by Akshay Narvate")
    
            
if __name__=="__main__":
    main()
