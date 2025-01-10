import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGSTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/Lutfia23/YOLO_v5_ObjectDetection/raw/refs/heads/main/English%20Sentences.v1i.yolov5pytorch.zip"



"""
Data validation related constant and with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yml"]
