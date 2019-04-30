def quad_residue(a, modulus):
    QR = 0

    for b in range(1, ((modulus - 1) // 2) + 1):
        if (b ** 2) % modulus == a:
            QR = 1

    return int(QR)

quad_residue(6, 11)

p = 1709
for i in range(100, 110):
    y_squared = (i*i*i + i + 1) % p
    qr = quad_residue(y_squared, p)
    if qr == 1:
        print(i, y_squared)

