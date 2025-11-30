import collections.abc as col
import typing as t

c = col.Callable
i = col.Iterable
it = col.Iterator
T = t.TypeVar("T")


def ft_filter(function: (c[[T], t.Any]) | None, iterable: i[T]) -> it[T]:
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return (i for i in iterable if i)
    return (i for i in iterable if function(i))
