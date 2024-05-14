import pandas as pd
import streamlit as st
import pickle

# Load model
with open('best_model.pkl', 'rb') as file:
    best_model = pickle.load(file)



def app():
    st.header('Silahkan Prediksi Harga Mobil Impian Anda!')
    st.image('gambar.jpeg', caption='Source = https://www.invygo.com', use_column_width=True)
    with st.form('Informasi Data Mobil'):
        brand = st.selectbox('Brand', ['Chrysler', 'Nissan', 'Hyundai', 'Honda', 'Toyota', 'Chevrolet',
       'Mercedes', 'MINI', 'Lexus', 'Land Rover', 'GMC', 'Mazda', 'Ford',
       'Kia', 'Genesis', 'Cadillac', 'Geely', 'MG', 'Jeep', 'INFINITI',
       'Dodge', 'Ferrari', 'Great Wall', 'Jaguar', 'GAC', 'Renault',
       'Suzuki', 'Peugeot', 'Changan', 'HAVAL', 'BMW', 'Rolls-Royce',
       'Porsche', 'Mitsubishi', 'Subaru', 'Zhengzhou', 'Lincoln',
       'Daihatsu', 'FAW', 'Chery', 'Isuzu', 'Audi', 'Bentley',
       'Aston Martin', 'Volkswagen', 'Fiat', 'Mercury', 'Classic',
       'Hummer', 'BYD', 'Maserati', 'Other', 'Lifan', 'Foton',
       'Victory Auto', 'Škoda', 'Iveco'])

        
        type = st.selectbox('Type', ['C300', 'Sunny', 'Elantra', 'Accord', 'Land Cruiser', 'Impala',
       'Yaris', 'Camry', 'Patrol', 'Tahoe', 'CLA', 'E', 'Corolla',
       'Copper', 'Prado', 'Civic', 'Furniture', 'RX', 'Range Rover',
       'Yukon', 'Bus Urvan', 'Aurion', 'Malibu', 'Rav4', 'CX9',
       'Expedition', 'ES', 'Cadenza', 'Tucson', 'Platinum', 'G80',
       'Accent', 'Sonata', 'LX', 'GX', 'Azera', 'CT-S', 'EC7', 'ZS',
       'Kona', 'Grand Cherokee', 'S', 'M', 'Charger', 'Taurus',
       'GTB 599 Fiorano', 'Royal', 'Picanto', 'Power', 'Datsun', 'F-Pace',
       'Hilux', 'Suburban', 'Explorer', 'FJ', 'Senta fe', 'Optima', 'GS8',
       'Maxima', 'Caprice', 'Challenger', 'Camaro', 'Symbol', 'Fluence',
       '6', 'RX5', 'Avalon', 'APV', '3008', 'Cerato', 'Traverse',
       'Sierra', 'F150', 'Genesis', 'NX', 'C', 'G70', 'Flex', 'UX',
       'Cores', 'Creta', 'Rio', 'Odyssey', 'Sylvian Bus', 'H1', 'Ciocca',
       'Land Cruiser Pickup', 'Cressida', 'Duster', 'Seven', 'GLC',
       'Carnival', 'EC8', 'H6', '300', 'The 7', 'Z370', 'Spark', 'Ghost',
       '911', 'Attrage', 'Focus', 'X-Trail', 'Forester', 'Pick up',
       'The 4', 'GS', 'Pajero', 'Acadia', 'City', 'Echo Sport', 'Vego',
       'The 5', 'Silverado', 'Cherokee', 'Altima', 'X', 'Navigator',
       'Wrangler', 'G', 'XT5', 'Cruze', 'Navara', 'Gran Max', 'Innova',
       'Aveo', 'Soul', 'Sportage', 'Montero', 'Prestige', 'Sentra',
       'Dokker', 'Veloster', 'Fusion', 'Land Cruiser 70', 'Pathfinder',
       'Seltos', 'Behbehani', 'Victoria', 'LS', 'CX5', 'Emgrand',
       'Carenz', 'SEL', 'The 6', 'Marquis', 'SL', 'H2', 'Talisman',
       'Mustang', '5008', 'A', 'T77', 'Optra', 'Safrane', 'QX', 'Tiggo',
       'Durango', 'Eado', 'MKS', 'CT5', 'Panamera', 'CS35', 'Coolray',
       'Countryman', 'D-MAX', 'Partner', 'Capture', '301', 'A6', 'Pilot',
       'Previa', 'X-Terra', 'Other', 'CS75', 'Flying Spur', 'Outlander',
       'Sorento', 'Vanquish', 'Touareg', 'Safari', 'K5', 'HRV', '3', 'Q5',
       'CT4', 'MKX', 'S5', 'X7', 'Rush', '2', 'Delta', 'VTC', 'IS',
       'Cayenne', 'Blazer', 'CS35 Plus', 'KICKS', 'Q', 'CS85', 'Armada',
       'Escalade', 'Echo', 'Avanza', 'Terios Ground', '5', 'CX3', 'S300',
       'Koleos', 'Compass', 'Edge', 'A8', 'Hiace', 'Lumina', 'ML', '500',
       'Macan', 'Passat', 'CLS', 'Stinger', 'Viano', 'A3', 'S8',
       'Vantage', 'RX8', 'RC', 'MKZ', 'CC', 'C-HR', 'Terrain', 'Mohave',
       'Savana', 'CL', 'Ram', 'Coaster', 'Vitara', 'Juke', 'C200', 'FX',
       'Fleetwood', 'Milan', 'Dyna', 'Cayman', 'Boxer', 'ATS', 'Cadillac',
       'Grand Marquis', 'H3', 'Trailblazer', 'Prius', 'CS95', 'F3', 'A5',
       'Gamble', 'The 3', 'L200', '360', 'Jimny', 'XJ', 'LF X60', 'Van',
       'Envoy', 'Patriot', 'GL', 'The M', 'Arnage', 'Cayenne S', 'ASX',
       'F Type', 'Golf', 'Coupe S', 'GLE', 'Camargue', 'Doblo',
       'Bus County', 'Ranger', 'H-2', 'Z', 'Avante', 'Discovery', 'B50',
       'Grand Vitara', 'Mini Van', 'Nativa', 'Beetle', 'Ertiga',
       '4Runner', 'GS3', 'Quattroporte', 'Azkarra', 'XF', 'A7', 'Gloria',
       'Tuscani', 'Kaptiva', 'Murano', 'DB9', 'Levante', 'Wingle',
       'Jetta', 'Opirus', 'CRV', 'Montero2', 'i40', 'Tiguan', 'Logan',
       'Town Car', 'Lancer', 'Abeka', 'Dzire', 'Terios', 'Cayenne Turbo',
       'Mini Cooper', 'Continental GT', 'Z350', 'Nitro', 'Van R',
       'Crosstour', 'SX4', 'Suvana', 'Liberty', 'Coupe', 'Prestige Plus',
       'X40', 'POS24', 'Colorado', 'CT6', 'Fabia', 'Megane', 'Bentayga',
       'Q7', 'Daily', 'Carens', 'A4', 'GC7', 'G330', 'Defender', 'H9',
       'Sedona', 'Cayenne Turbo GTS', 'SRT', 'HS', "D'max", 'Pegas',
       'DTS', 'Superb', 'Veracruz', '307', 'CX7', 'QQ', 'L300', 'Galant'])
        
        year = st.selectbox('Year', [1998, 1999, 2000, 2001,2002, 2003,2004,2005,2006,2007,2008, 2009,2010, 2011, 2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
        
        color = st.selectbox('Color',['Black', 'Silver', 'Grey', 'Navy', 'White', 'Bronze',
       'Another Color', 'Golden', 'Brown', 'Blue', 'Red', 'Oily', 'Green',
       'Orange', 'Yellow'])
        
        options = st.selectbox('Options', ['Full', 'Semi Full', 'Standard'])
        
        engine_size = st.slider('Engine Size (CC/1000)', 1.0, 10.0, 5.0)
        
        gear_type = st.selectbox('Gear Type', ['Automatic', 'Manual'])
        
        mileage = st.number_input('Mileage', min_value=0, max_value=999999)
        
        region = st.selectbox('Region',['Riyadh', 'Jeddah', 'Dammam', 'Al-Medina', 'Qassim', 'Makkah', 'Jazan', 'Tabouk', 'Aseer', 'Al-Ahsa', 'Taef', 'Sabya', 'Khobar', 'Abha', 'Al-Baha', 'Yanbu', 'Hail', 'Al-Namas', 'Jubail', 'Al-Jouf', 'Hafar Al-Batin', 'Najran', 'Arar', 'Wadi Dawasir', 'Besha', 'Qurayyat', 'Sakaka'] )
        
        submit = st.form_submit_button('Submit Data Mobil')
        
        if submit:
            dataInf = {
                'Brand': brand,
                'Type': type,
                'Year': year,
                'Color': color,
                'Options': options,
                'Engine Size': engine_size,
                'Gear Type': gear_type,
                'Mileage': mileage,
                'Region': region
            }

            dfInf = pd.DataFrame([dataInf])

            yPredInf = best_model.predict(dfInf)

            if yPredInf[0] < 0:
                st.write("Tidak ditemukan informasi mobil, periksa kembali informasi yang anda masukkan")
            else:
                st.write("Hasil Prediksi Harga Mobil Impian Anda adalah:", yPredInf[0])
