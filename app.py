import numpy as np
import streamlit as st
import pickle

st.title('Prediksi Jaya Jaya Jaya Charge Rumah Sehat')

if 'model' not in st.session_state:
    model = pickle.load(open('dt_model_charges.sav', 'rb'))
    st.session_state['model'] = model

st.header('Masukkan Identitas Diri Anda!')
age_input = st.number_input('Masukkan umur ')
bmi_input = st.number_input('Masukkan BMI ')
children_input = st.number_input('Masukkan jumlah anak ')
sex_input = st.radio('Jenis kelamin ', ['Laki-laki','Perempuan'])
smoker_input = st.radio('Merokok? ', ['Ya','Tidak'])
region_input = st.radio('Wilayah Tempat Tinggal', ['Northeast','Northwest','Southeast','Southwest'])

sex_input_encoded = []
smoker_input_encoded = []
region_input_encoded = []

if(sex_input == 'Laki-laki'):
    sex_input_encoded = [0,1]
else:
    sex_input_encoded = [1,0]

if(smoker_input == 'Ya'):
    smoker_input_encoded = [0,1]
else:
    smoker_input_encoded = [1,0]

if(region_input == 'Northeast'):
    region_input_encoded = [1,0,0,0]
    
elif(region_input == 'Northwest'):
    region_input_encoded = [0,1,0,0]
elif(region_input == 'Southeast'):
    region_input_encoded = [0,0,1,0]
else:
    region_input_encoded = [0,0,0,1]

region_input_encoded = np.array(region_input_encoded)
sex_input_encoded = np.array(sex_input_encoded)
smoker_input_encoded = np.array(smoker_input_encoded)

data_encoded = np.concatenate([sex_input_encoded, smoker_input_encoded, region_input_encoded], axis=None)

if st.button('Prediksi Harga'):
    data_num = np.array([age_input, bmi_input, children_input])
    data = np.concatenate((data_num, data_encoded), axis=None).reshape(1,-1)
    # st.write(data)
    result = st.session_state['model'].predict(data)
    st.write(f'Perkiraan biaya rumah sakit Anda adalah: {result[0]}')
else:
    st.write('Masukkan data diri Anda dan model akan memprediksi biaya rumah sakit Anda!')