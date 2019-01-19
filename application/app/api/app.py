import responder

api = responder.API()


@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


@api.route("/player/{id}")
def get_player_info(req, resp, *, id):
    resp.text = f"hello, world! {id}"


if __name__ == '__main__':
    api.run(address="0.0.0.0")
