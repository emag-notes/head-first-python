def double(arg):
    print("実行前:", arg)
    print(id(arg))
    arg = arg * 2
    print("実行後:", arg)
    print(id(arg))


def change(arg):
    print("実行前:", arg)
    print(id(arg))
    arg.append("さらなるデータ")
    print("実行後:", arg)
    print(id(arg))
