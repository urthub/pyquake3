import pytest
from pyquake3 import Player
from pyquake3 import PyQuake3

GAMER = Player(3, 'Name', 5, 14, '1.1.1.1')
SERVER = PyQuake3('127.0.0.1:27960', 'password')


class TestClass(object):

    def test_player_num(self):
        assert GAMER.num == 3

    def test_player_name(self):
        assert str(GAMER) == 'Name'

    def test_player_ping(self):
        assert GAMER.ping == 14

    def test_player_frags(self):
        assert GAMER.frags == 5

    def test_player_ip_addr(self):
        assert GAMER.address == '1.1.1.1'

    def test_server_addr(self):
        assert SERVER.get_address() == '127.0.0.1:27960'

    def test_server_rcon(self):
        assert SERVER.rcon_password == 'password'

    def test_set_server_value_exception(self):
        with pytest.raises(ValueError):
            SERVER.set_server('2.2.2.2;27960')

    def test_set_server_exception(self):
        with pytest.raises(ValueError):
            SERVER.set_server('3.3.3.3')
