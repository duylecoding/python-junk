def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if (a * x) % m == 1:
            return x
    return 1

def find_lambda_of_one_point(x, y, a, n):
    top = 3 * x * x + a
    bot = 2 * y
    inv_bot = modInverse(bot, n)
    if inv_bot == 1:
        print("ANSWER: ", bot, gcd(bot, n))
    return (top * inv_bot) % n

def find_lambda_of_two_points(x1, y1, x2, y2, n):
    top = (y2 - y1)
    bot = (x2 - x1)
    inv_bot = modInverse(bot, n)
    if inv_bot == 1:
        print("ANSWER: ", bot, gcd(bot, n))
    return (top * inv_bot) % n

def find_x3_y3(lam, x1, x2, y1, n):
    x3 = (lam * lam - x1 - x2) % n
    y3 = (lam * (x1 - x3) - y1) % n
    return x3, y3


def fuck_471(x, y, a, n, iter):
    # y^2 = x^3 + Ax + B
    lam = find_lambda_of_one_point(x, y, a, n)
    new_x = find_x3_y3(lam, x, x, y, n)[0]
    new_y = find_x3_y3(lam, x, x, y, n)[1]

    #print(x, y, new_x, new_y)
    for i in range(2, iter):
        lam = find_lambda_of_two_points(x, y, new_x, new_y, n)
        new_y = find_x3_y3(lam, x, new_x, y, n)[1]
        new_x = find_x3_y3(lam, x, new_x, y, n)[0]

    print(new_x, new_y)


if __name__ == '__main__':
    n = 73
    a = 8
    k = 11
    x = 32
    y = 53
    fuck_471(x, y, a, n, k)

