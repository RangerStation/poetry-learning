from poetry_learning.data_collector import DataCollector


def test_ctor__instance_keeps_coin_str():
    # Given
    some_coin = "zcash"

    # When
    dc = DataCollector(some_coin)

    # Then
    assert dc.coin == "zcash"

def test_ctor__instance_uses_lowercase_str_of_coin():
    # Given
    some_coin = "ZCasH"

    # When
    dc = DataCollector(some_coin)

    # Then
    assert dc.coin == "zcash"