from ft_package.count_in_list import count_in_list


def test_count_in_list_simple():
    lst = ["toto", "tata", "toto"]
    assert count_in_list(lst, "toto") == 2
