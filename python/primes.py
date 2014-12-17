import itertools

# http://www.macdevcenter.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
def infinite_eratosthenes():
    composites = set()
    for i in itertools.count(2):
        if i not in composites:
            yield i
            composites.add(i * i)
