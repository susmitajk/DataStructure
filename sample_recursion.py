def func_three():
    print('Three')


def func_two():
    func_three()
    print('Two')


def func_one():
    func_two()
    print('one')


func_one()