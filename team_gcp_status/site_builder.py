import jinja2
import csv
import gspread
import webbrowser
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import storage
from google.oauth2 import service_account


def generate_site():
    """ generate site in local directory """

    print("Generating site...")
    # using jinja to get the template
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('template.html')

    # open the downloaded csv file and read the data
    with open('team_gcp_status.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    # generate the output html
    output = template.render(data=data, date=datetime.date.today())
    # write the output html to a index.html file
    with open('index.html', 'w') as f:
        f.write(output)


def upload_to_gcs():
    """ upload the index.html file to gcs """
    print("Uploading to GCS...")
    storage_credentials = service_account.Credentials.from_service_account_file('credentials.json')
    storage_client = storage.Client(project='braided-carport-274513', credentials=storage_credentials)
    bucket = storage_client.get_bucket('team_gcp_status')
    blob = bucket.get_blob('index.html')
    blob.upload_from_filename('index.html')
    print("Opening site...")
    webbrowser.open(f"http://storage.googleapis.com/team_gcp_status/index.html")


if __name__ == "__main__":
    # download_data()
    generate_site()
    upload_to_gcs()