import pyrebase



config = {
    "apiKey": "CHANGEME",
    "authDomain": "CHANGEME",
    "databaseURL": "CHANGEME",
    "projectId": "CHANGEME",
    "storageBucket": "CHANGEME",
    "serviceAccount": "CHANGEME"
}
FIRMWARE_DOWNLOAD_FOLDER = '/tmp/'


class FirebaseHelper:
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    st = firebase.storage()
    __listen_list = {}

    @staticmethod
    def listen(key_: str, callback):
        try:
            FirebaseHelper.db.child(key_).stream(callback)
        except:
            pass

    @staticmethod
    def set(key_: str, data: any):
        FirebaseHelper.db.child(key_).set(data)

    @staticmethod
    def get_file(remote_file_name: str, local_path: str) -> bool:
        """
        Download file from firebase
        :param remote_file_name: The name of the file in firebase
        :param local_path: path where the file is downloaded
        :return: Returns true if downloaded correctly
        """
        try:
            FirebaseHelper.st.child(remote_file_name).download(
                local_path
            )
        except AttributeError:
            return False
        return True
