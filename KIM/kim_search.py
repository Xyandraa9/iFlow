import kaggle


def search_datasets(keyword):
    # Authenticate and construct the Kaggle API client
    kaggle.api.authenticate()
    # Search for datasets on Kaggle
    results = kaggle.api.dataset_list(search=keyword)
    # Extract the list of datasets
    # datasets = results[results']
    return results


# if __name__ == "__main__":
#     dataset = search_datasets("anime")
#     print(dataset)
