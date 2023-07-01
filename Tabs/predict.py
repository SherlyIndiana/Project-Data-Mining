import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title("Silahkan Input Prediksi")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input ('Age')
    with col1:
        job = st.number_input ('Job')
    with col1:
        marital = st.number_input ('Marital')
    with col1:
        education = st.number_input ('Education')
    with col1:
        default = st.number_input ('Default')
    with col2:
        balance = st.number_input ('Balance')
    with col2:
        housing = st.number_input ('Housing')
    with col2:
        loan = st.number_input ('Loan')
    with col2:
        contact = st.number_input ('Contact')
    with col2:
        duration = st.number_input ('Duration')
    with col2:
        campaign = st.number_input ('Campaign')
    
    features = [age,job,marital,education,default,balance,housing,loan,contact,duration,campaign]

    #tombol prediksi
    if st.button('Prediksi'):
        prediction, score = predict(x,y, features)
        score = score
        st.info('Prediksi Sukses')

        if (prediction==1):
            st.warning("Nasabah Berpotensi Membuka Simpanan Deposito")
        else:
            st.success("Nasabah Tidak Berpotensi Membuka Simpanan Deposito")
        
        st.write("Akurasi", (score*100), "%")


