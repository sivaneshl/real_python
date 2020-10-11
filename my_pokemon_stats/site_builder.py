import jinja2
import csv
import gspread
import webbrowser
from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import storage
from google.oauth2 import service_account

def download_data():
    """ download data using the google sheets api """

    print("Authorizing google apis...")
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    # get google drive api credentials from credentials.json
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scopes=scope)

    # use gspread to authorize google api
    client = gspread.authorize(credentials)

    # open the work book and read the values
    worksheet = client.open('my_pokemon_stats').get_worksheet(0)
    sheet_values = worksheet.get_all_values()

    print(f"Downloading data from {worksheet.title}...")
    with open("my_pokemon_stats.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(sheet_values)


def generate_site():
    """ generate site in local directory """

    print("Generating site...")

    # using jinja to get the template
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('template.html')

    # open the downloaded csv file and read the data
    with open('my_pokemon_stats.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    # generate the output html
    output = template.render(data=data)
    # write the output html to a index.html file
    with open('index.html', 'w') as f:
        f.write(output)


def upload_to_gcs():
    """ upload the index.html file to gcs """
    print("Uploading to GCS...")
    storage_credentials = service_account.Credentials.from_service_account_file('credentials.json')
    storage_client = storage.Client(project='braided-carport-274513', credentials=storage_credentials)
    bucket = storage_client.get_bucket('my_pokemon_stats')
    blob = bucket.get_blob('index.html')
    blob.upload_from_filename('index.html')
    print("Opening site...")
    webbrowser.open(f"http://storage.googleapis.com/my_pokemon_stats/index.html")


if __name__ == "__main__":
    download_data()
    generate_site()
    upload_to_gcs()