
from shapely.geometry import Polygon
import requests

class PythonStac:
    def __init__(self):
        """ Constructor for this class."""

    def get_collection_ids(self):
        """
        Returns a list of collection IDs in the API
        """
        r = requests.get('https://earth-search.aws.element84.com/v0/collections')
        h = r.json()
        list_of_collection_ids = [c['id'] for c in h]
        return list_of_collection_ids

    def get_first_item(self, collection_id):
        """
        Get first item in a collection as a dictionary
        :return: Dictionary of first item
        """
        url = "https://earth-search.aws.element84.com/v0/collections/{collection_id}/items"\
            .format(collection_id=collection_id)
        r = requests.get(url)
        h = r.json()
        #get the first item and return it
        return h['features'][0]

    def num_intersecting_items(self, collection_id, poly):
        url = "https://earth-search.aws.element84.com/v0/search"

        coord = list(poly.exterior.coords)
        coord = [list(ele) for ele in coord]

        data = {
            "collections": [collection_id],
            "intersects": {
                "type": "Polygon",
                "coordinates": [coord]
            }
        }
        r = requests.post(url, params=data)
        h = r.json()
        return len(h)

# if __name__ == "__main__":
#     StacCollection = PythonStac()
#     collection_ids = StacCollection.get_collection_ids()
#     first_item = StacCollection.get_first_item(collection_ids[0])
#
#     #create a sample polygon
#     search_poly = Polygon([[-77.0824, 38.7886], [-77.0189, 38.7886],
#     [-77.0189, 38.8351], [-77.0824, 38.8351],
#     [-77.0824, 38.7886]])
#
#     #search number of items intersecting a polygon
#     num_items = StacCollection.num_intersecting_items(collection_ids[0], search_poly)