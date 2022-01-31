import joblib
import os
from utils import gcs_utils
import constants
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")

class online_score_api:
    def __init__(self):
        self.root_path = "/mnt/model"
        self.load()

    def load(self):
        local_model_path = os.path.join(self.root_path, constants.MODEL_FILE)
        logging.info("downloading model file")
        gcs_utils.download_file_from_gcs(gcs_bucket_name=constants.GCS_BUCKET_NAME, 
                                    gcs_blob_object=os.path.join(constants.GCS_BLOB_OBJECT, constants.MODEL_FILE),
                                    local_model_path=local_model_path)
        self._joblib = joblib.load(local_model_path)

    def init_metadata(self):
        logging.info("metadata method called")
        meta = {
            "name": "iris-sklearn",
            "versions": ["v0.0.1"],
            "platform": "seldon",
            "inputs": [
                {
                    "messagetype": "tensor",
                    "schema": {"names": ["a", "b", "c", "d"], "shape": [4]},
                }
            ],
            "outputs": [{"messagetype": "tensor", "schema": {"shape": [1]}}],
            "custom": {"author": "quandv", "extra": "information"},
        }
        return meta


    def predict(self, X, names=[], meta=[]):
        logging.info(f"model features: {X}")
        logging.info(f"model names: {names}")
        logging.info(f"model meta: {meta}")
        try:
            result = self._joblib.predict(X)
            return result
        except Exception as ex:
            logging.exception("Exception during predict")