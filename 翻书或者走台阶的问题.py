#共有n个台阶，每次只能上1个台阶或者2个台阶，共有多少种方法爬完台阶。
#共有n页书，每次只能翻1页或者2页书，共有多少种方法翻完全书。
#当n不大于2时，只有两种方法
#可以理解为当翻到n-2书页或走到n-2楼梯 时，只有两种方法n=1 or n=2
#类推可得 斐波那契数列
#实现代码
def A(n):
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    if n > 2:
        return A(n-1)+A(n-2)
print(A(10))
#ps:1.使用了递归
#   2.时间复杂度为指数级
#   3.斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........
#   这个数列从第3项开始，每一项都等于前两项之和。又称为“兔子数列”
