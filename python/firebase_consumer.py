from python.firebase_helper import FirebaseHelper


class FirebaseConsumer:

    def __init__(self):
        self.stream = FirebaseHelper.listen(
            "products",
            self.on_new_product
        )

    @staticmethod
    def on_new_product(message: dict) -> None:
        print("NEW_PRODUCT: " + str(message))


if __name__ == '__main__':
    FirebaseConsumer()
