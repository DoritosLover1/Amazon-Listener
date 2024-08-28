# p_name, p_star_rating, p_photo, p_url, p_delivery

class Products:
    def __init__(self):
        self.products_set = list()

    def __iter__(self):
        return iter(self.products_set)

    def setinformation(self, information):
        for element in information["data"]["products"]:
            self.products_set.append(element)
