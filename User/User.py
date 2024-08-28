from APISource.Access.Access import Access
from APISource.Product.Products import Products

class User:
    def __init__(self, query, country, sort, product_condition):
        self.item_name = query
        self.item_country = country
        self.sort_by = sort
        self.item_condition = product_condition

    def search(self):
        response = Access(self.item_name, self.item_country, self.sort_by, self.item_condition)
        output = response.responsefunc()
        setofelement = Products()

        setofelement.setinformation(output)
        return setofelement