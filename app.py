import numpy as np
import pandas as pd
import streamlit as st
import pickle

st.title('Prediksi Jaya Jaya Jaya Charge Rumah Sehat')

if 'model' not in st.session_state:
    model = pickle.load(open('rf_model_charges.sav', 'rb'))
    st.session_state['model'] = model

st.header('Masukkan Identitas Diri Anda!')
age_input = st.number_input('Masukkan umur ')
bmi_input = st.number_input('Masukkan BMI ')
children_input = st.number_input('Masukkan jumlah anak ')
sex_input = st.radio('Jenis kelamin ', ['Laki-laki','Perempuan'])
smoker_input = st.radio('Merokok? ', ['Ya','Tidak'])
region_input = st.radio('Wilayah Tempat Tinggal', ['Northeast','Northwest','Southeast','Southwest']).lower()

# Kode jika model gapake ColumnTransformer

# sex_input_encoded = []
# smoker_input_encoded = []
# region_input_encoded = []

# if(sex_input == 'Laki-laki'):
#     sex_input_encoded = [0,1]
# else:
#     sex_input_encoded = [1,0]

# if(smoker_input == 'Ya'):
#     smoker_input_encoded = [0,1]
# else:
#     smoker_input_encoded = [1,0]

# if(region_input == 'northeast'):
#     region_input_encoded = [1,0,0,0]
    
# elif(region_input == 'northwest'):
#     region_input_encoded = [0,1,0,0]
# elif(region_input == 'southeast'):
#     region_input_encoded = [0,0,1,0]
# else:
#     region_input_encoded = [0,0,0,1]

# region_input_encoded = np.array(region_input_encoded)
# sex_input_encoded = np.array(sex_input_encoded)
# smoker_input_encoded = np.array(smoker_input_encoded)

# data_encoded = np.concatenate([sex_input_encoded, smoker_input_encoded, region_input_encoded], axis=None)

# Kode jika model pake ColumnTransformer

if(sex_input == 'Laki-laki'):
    sex_input = 'male'
else:
    sex_input = 'female'

if(smoker_input == 'Ya'):
    smoker_input = 'yes'
else:
    smoker_input = 'no'

if st.button('Prediksi Harga'):
    #Kode jika gapake ColumnTransformer
    # data_num = np.array([age_input, bmi_input, children_input])
    # data = np.concatenate((data_num, data_encoded), axis=None).reshape(1,-1)

    #Kode jika pake ColumnTransformer
    data_dict = {'age' : age_input, 'bmi' : bmi_input, 'children' : children_input, 'sex' : sex_input, 'smoker' : smoker_input, 'region' : region_input}
    data = pd.DataFrame(data_dict, index=[0])

    # st.write(data) # buat debugging
    result = st.session_state['model'].predict(data)
    st.write(f'Perkiraan biaya rumah sakit Anda adalah: ${result[0]}')
else:
    st.write('Masukkan data diri Anda dan model akan memprediksi biaya rumah sakit Anda!')
