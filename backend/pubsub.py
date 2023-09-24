import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-be4a94c1-bbcf-4252-b35c-6a614803564d'
pnconfig.publish_key = 'pub-c-1bfd86fa-1d8e-448c-a2fe-d445c3a84954'
pnconfig.user_id = 'mike-legemah'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')


pubnub.add_listener(Listener())


def main():
    time.sleep(1)

    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()


if __name__ == '__main__':
    main()
