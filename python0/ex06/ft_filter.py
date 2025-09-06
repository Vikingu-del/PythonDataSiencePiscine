import collections.abc as col
import typing as t

c = col.Callable
i = col.Iterable
it = col.Iterator
T = t.TypeVar("T")


def ft_filter(function: (c[[T], t.Any]) | None, iterable: i[T]) -> it[T]:
    """
    Filters the elements of an iterable for which the given
    function returns True.

    Args:
        function: A callable that returns True or False for each element.
        iterable: An iterable of elements to filter.

    Returns:
        A list of elements for which the function returned True.
    """
    if function is None:
        return (i for i in iterable if i)
    return (i for i in iterable if function(i))
