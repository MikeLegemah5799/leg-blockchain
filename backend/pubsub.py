import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-be4a94c1-bbcf-4252-b35c-6a614803564d'
pnconfig.publish_key = 'pub-c-1bfd86fa-1d8e-448c-a2fe-d445c3a84954'
pnconfig.user_id = 'mike-legemah'

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()


def main():
    pubsub = PubSub()
    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})


if __name__ == '__main__':
    main()
