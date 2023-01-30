# python3 flow.py search <keyword> - this main file
# python3 flow.py download <url> -o <filename> -s true (-s is for standardize)

# add csv if not entereed, how to manage filenames
# datasets/<filename > .csv
# datasets/filename/filename_1.csv
# datasets/filename/<defaultname>
import kim_search
import click
import kim_download
import os


@click.group
def mycommands():
    pass


@click.command()
@click.option("--keyword")
# @click.option("--user")
# @click.option("--key")
def search(keyword):

    datasets = kim_search.search_datasets(keyword)
    click.echo("Datasets matching '{}':".format(keyword))
    for i in range(len(datasets)):
        click.echo(str(i+1) + " " + str(datasets[i]))


@click.command()
@click.option("--u")
@click.option("--d")
@click.option("--f")
def download(u, d, f):
    folder_name = f"{u}_{d}"
    os.chdir('../')
    os.makedirs("dataset")
    os.chdir('dataset')
    os.makedirs(folder_name, exist_ok=True)
    os.chdir(folder_name)
    kim_download.download_dataset(d, f)


mycommands.add_command(search)
mycommands.add_command(download)

if __name__ == "__main__":
    mycommands()


# username_datasetname
