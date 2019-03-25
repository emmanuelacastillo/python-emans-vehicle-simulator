from wireless.sender_factory import sender_factory_impl

FAKE_DISTANCE: int = 40


class SenderFacade(object):

    @staticmethod
    def post_data(url: str, json: dict):
        sender = sender_factory_impl(FAKE_DISTANCE)
        sender.send(url, json)
