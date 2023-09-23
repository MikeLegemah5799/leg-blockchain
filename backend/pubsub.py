from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-be4a94c1-bbcf-4252-b35c-6a614803564d'
pnconfig.publish_key = 'pub-c-1bfd86fa-1d8e-448c-a2fe-d445c3a84954'
pubnub = PubNub(pnconfig)
