from dataclasses import dataclass

@dataclass
# class DataIngestionArtifact:
#     data_zip_file_path: str
#     feature_store_path: str  
class DataIngestionArtifact:
    def __init__(self, feature_store_path: str, data_zip_file_path: str): #validation_status: bool):
        self.feature_store_path = feature_store_path
        self.data_zip_file_path = data_zip_file_path
        #self.validation_status = validation_status



@dataclass
# class DataValidationArtifact:
#     validation_status: bool
class DataValidationArtifact:
    def __init__(self, validation_status: bool):
        self.validation_status = validation_status
