import requests


class MavenAPI:
    @staticmethod
    def search(query: str) -> requests.Response:
        url = "http://search.maven.org/solrsearch/select?q={query}&rows=20&wt=json".format(query=query)
        return requests.get(url)
