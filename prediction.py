import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sqlalchemy import create_engine

def main():
    # dataset
    data = pd.read_csv('dataset/employee_data.csv')

    # pisahkan fitur dan target
    features = data.drop('Attrition', axis=1)
    target = data['Attrition'].fillna(data['Attrition'].mode()[0])

    # One-hot encoding untuk fitur kategorikal
    features_encoded = pd.get_dummies(features)

    # ganti nama kolom hasil encoding
    features_encoded.columns = [col.replace('_', ' ').title() for col in features_encoded.columns]

    # Normalisasi fitur
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features_encoded)

    # Oversampling dengan SMOTE (optional)
    smote = SMOTE(random_state=42)
    features_resampled, target_resampled = smote.fit_resample(features_scaled, target)

    # load model yang telah dilatih
    model = joblib.load('model/xgboost_model.pkl')

    # prediksi menggunakan data yang sudah dinormalisasi
    predictions = model.predict(features_scaled)

    # tambahkan hasil prediksi ke DataFrame asli
    data['Predicted Attrition'] = predictions

    # ganti nama kolom untuk memastikan label yang jelas
    data.columns = [col.replace('_', ' ').title() for col in data.columns]

    # simpan hasil prediksi ke dalam PostgreSQL
    engine = create_engine('postgresql://postgres:root@localhost:5432/hr_attrition')
    data.to_sql('attrition_predictions', engine, if_exists='replace', index=False)

    print("Prediksi berhasil disimpan ke PostgreSQL.")

if __name__ == '__main__':
    main()