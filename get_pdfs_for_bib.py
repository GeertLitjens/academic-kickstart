<<<<<<< HEAD
import os
import requests

base_url = 'https://rdwww.extern.umcn.nl/svn/literature/pdf/'
base_folder = "C:\\Code\\source\\personal_site\\content\\publication"
user, password = 'geert', '***REMOVED***'

pub_list = os.listdir(base_folder)
pub_list.remove("_index.md")

for pub in pub_list:
    pub_key = pub.capitalize().replace("-", "")
    pdf_url = base_url + pub_key + ".pdf"
    out_path = os.path.join(base_folder, pub, pub + ".pdf")
    if not os.path.isfile(out_path):
        resp = requests.get(pdf_url, auth=(user, password))
        if resp.ok:
            open(out_path, 'wb').write(resp.content)
            print("PDF found for " + pub)
        else:
=======
import os
import requests

base_url = 'https://rdwww.extern.umcn.nl/svn/literature/pdf/'
base_folder = "C:\\Code\\source\\personal_site\\content\\publication"
user, password = 'geert', '***REMOVED***'

pub_list = os.listdir(base_folder)
pub_list.remove("_index.md")

for pub in pub_list:
    pub_key = pub.capitalize().replace("-", "")
    pdf_url = base_url + pub_key + ".pdf"
    out_path = os.path.join(base_folder, pub, pub + ".pdf")
    if not os.path.isfile(out_path):
        resp = requests.get(pdf_url, auth=(user, password))
        if resp.ok:
            open(out_path, 'wb').write(resp.content)
            print("PDF found for " + pub)
        else:
>>>>>>> bcfd49f687b60ec5999b6624c85c5ce7cd0987e6
            print("No PDF found for " + pub)