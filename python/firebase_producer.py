from python.firebase_helper import FirebaseHelper


class FirebaseProducer:
    products = [
        "meat", "fruit", "veg", "snack", "tins", "jars", "drinks"
    ]
    idx = 0

    def __init__(self):
        self.stream = FirebaseHelper.listen(
            "products",
            self.on_ack
        )

    def on_ack(self, product: str) -> None:
        print("NEW_PRODUCT: " + str(product))
        if len(product) == 0:
            self.make_product()

    def make_product(self):
        self.stream = FirebaseHelper.set("products", self.products[self.idx])
        self.idx = (1 + self.idx) % len(self.products)


if __name__ == '__main__':
    producer = FirebaseProducer()
    producer.make_product()
