def ft_filter(function: callable, iterable: list) -> list:
    """Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true."""
    if function is None:
        def function(x):
            return x
    return [item for item in iterable if function(item)]
