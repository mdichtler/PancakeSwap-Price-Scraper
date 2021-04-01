import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bscfind-default-rtdb.europe-west1.firebasedatabase.app/'
})




class Firebase_Interface:
    def __init__(self, scraped_site):
        # As an admin, the app has access to read and write all data, regradless of Security Rules
        self.ref = db.reference(scraped_site)

    def save_data(self, pair, date, time, seconds, data):
        users_ref = self.ref.child(pair).child(date).child(time).child(seconds)
        users_ref.set(data)
