from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36 #TODO
	assert simple_work_calc(20, 3, 2) == 230 #TODO
	assert simple_work_calc(30, 4, 2) == 650 #TODO

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n)
	work_fn2 = lambda n: work_calc(n, 3, 2, lambda n: n*n)
	res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():
	# TODO
    span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: n)
    span_fn2 = lambda n: span_calc(n, 3, 2, lambda n: 1)
    res = compare_span(span_fn1, span_fn2)
    print_results(res)