# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from bing_image_downloader import downloader

query_strings= ["cytology diff quik cocci", "cytology diff quik rods", "cytology diff quik yeast"]

def main():
    for query_string in query_strings:
        try:
            downloader.download(query_string, limit=100, output_dir="dataset")
        except:
            continue
    # downloader.download("diff quick yeast", limit=1000, output_dir="dataset")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
