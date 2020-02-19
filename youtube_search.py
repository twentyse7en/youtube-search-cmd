import click
import webbrowser
import urllib.parse


@click.command()
@click.option('--keyword', prompt='Search', help='Keyword for youtube search')
def search(keyword):
    initial = 'https://www.youtube.com/results?'
    query = urllib.parse.urlencode({'search_query': keyword})
    url = initial+query
    webbrowser.open(url)


if __name__ == '__main__':
    search()
