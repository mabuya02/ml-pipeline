import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from albumentations import Compose, HorizontalFlip, RandomBrightnessContrast, RandomCrop

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        data.drop_duplicates(inplace=True)
        for column in data.columns:
            if data[column].dtype == 'object':
                data[column].fillna(data[column].mode()[0], inplace=True)
            else:
                data[column].fillna(data[column].median(), inplace=True)
        logging.info("Data cleaning completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
        raise

def encode_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        data = pd.get_dummies(data, drop_first=True)
        logging.info("Data encoding completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error encoding data: {e}")
        raise

def scale_data(data: pd.DataFrame) -> pd.DataFrame:
    try:
        scaler = StandardScaler()
        numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
        data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
        logging.info("Data scaling completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error scaling data: {e}")
        raise

def feature_engineering(data: pd.DataFrame) -> pd.DataFrame:
    try:
        if 'date' in data.columns:
            data['year'] = pd.to_datetime(data['date']).dt.year
            data['month'] = pd.to_datetime(data['date']).dt.month
            data['day'] = pd.to_datetime(data['date']).dt.day
            data.drop('date', axis=1, inplace=True)
        logging.info("Feature engineering completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error in feature engineering: {e}")
        raise

def handle_imbalance(X, y):
    try:
        smote = SMOTE(random_state=42)
        X_res, y_res = smote.fit_resample(X, y)
        logging.info("Imbalanced data handled successfully with SMOTE.")
        return X_res, y_res
    except Exception as e:
        logging.error(f"Error handling imbalance: {e}")
        raise

def augment_data(images, augmentations=None):
    try:
        if augmentations is None:
            augmentations = Compose([HorizontalFlip(p=0.5), RandomBrightnessContrast(p=0.2), RandomCrop(224, 224)])
        augmented_images = [augmentations(image=img)['image'] for img in images]
        logging.info("Data augmentation completed successfully.")
        return augmented_images
    except Exception as e:
        logging.error(f"Error augmenting data: {e}")
        raise

def split_data(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42):
    try:
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        logging.info("Data splitting completed successfully.")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error(f"Error splitting data: {e}")
        raise
