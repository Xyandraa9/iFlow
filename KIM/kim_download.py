import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# for single file


def download_data(dataset_name, file_name):
    check = api.dataset_download_file(
        dataset_name, file_name, force=True, quiet=False)
    if check == True:
        print("Downloaded")
    else:
        print("Error occured couldnt download")
    # print(api.dataset_download_file(dataset_name, file_name))


# for multiple file
def download_dataset(dataset_name, path_name=None):
    # api.dataset_download_files(dataset, path=None, force=False, quiet=True, unzip=False)
    api.dataset_download_files(
        dataset_name, path_name, force=True, quiet=False)


# checking function working or not
# download_data('abhi231092/uber-rides-data-bw-city-and-airport','Uber Request Data.csv')

# download_dataset('anshsarkar18/collatz-sequences-dataset', True)
# ds = api.dataset_list(sort_by='published',
#   search = 'patrickgendotti/udacity-course-catalog')
