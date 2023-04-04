from Database import Database
import click
from Logging import defaultLogging

global db

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def main():
    global db
    defaultLogging()
    db = Database(
        user="root",
        password="my-secret-pw",
        host="139.59.124.127",
        port=3306,
        database="SHOPAPP"
    )

@execution.command()
@click.argument('keywords')
@click.option('--exclude', "-e", default="", help="Exclude containing keywords")
@click.option('--questionbank', "-q", default=True, help="forceCreateQBSection", is_flag=True)
def bookletGeneration(keywords, exclude, byrecipe, datasource, docx, watermark, questionbank):
    pass

@execution.command()
def showAllShops():
    data = db.execute("""SELECT * FROM Shop""")
    print(data



if __name__ == '__main__':
    main()