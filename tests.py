from pyquake3 import Player
from pyquake3 import PyQuake3


GAMER = Player(3, 'Name', 5, 14, '1.1.1.1')
SERVER = PyQuake3('127.0.0.1:27966', 'password')

def test_player_num():
    assert GAMER.num == 3

def test_player_name():
    assert str(GAMER) == 'Name'

def test_player_ping():
    assert GAMER.ping == 14

def test_player_frags():
    assert GAMER.frags == 5

def test_player_ip_addr():
    assert GAMER.address == '1.1.1.1'

def test_server_addr():
    assert SERVER.get_address() == '127.0.0.1:27966'

def test_server_rcon():
    assert SERVER.rcon_password == 'password'
