import pytest

from sample import my_fun

def test_my_fun():

	#assert pytest.raises(NotImplementedError)

	#assert pytest.raises(NotImplementedError)

	with pytest.raises(NotImplementedError):
		my_fun()





