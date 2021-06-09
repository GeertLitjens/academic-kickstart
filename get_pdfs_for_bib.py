import os
import shutil

source = 'C:\\Users\\geert\\Documents\\literature\\pdf'
destination = "C:\\Code\\source\\personal_site\\content\\publication"

pub_list = os.listdir(destination)
pub_list.remove("_index.md")

for pub in pub_list:
    pub_key = pub.capitalize().replace("-", "")
    pdf_path = os.path.join(source, pub_key + ".pdf")
    out_path = os.path.join(destination, pub, pub + ".pdf")
    if not os.path.isfile(out_path):
        if os.path.isfile(pdf_path):
            shutil.copyfile(pdf_path, out_path)
            print("PDF found for " + pub)
        else:
            print("No PDF found for " + pub)
