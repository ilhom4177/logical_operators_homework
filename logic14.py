def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b=a%10
    a//=10
    c = a % 10
    return (b+c)%2==1

print(main(45))