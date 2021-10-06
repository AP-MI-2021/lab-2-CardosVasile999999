def is_palindrome(n):
    '''
    Problema 5:Determina daca un numar este palindrom
    Input:
    -n: int
    Output:
    boolean variable
    '''
    inv=0
    aux=n
    while n:
        inv=inv*10+n%10
        n=n//10
    if inv==aux:
        return True
    else:
        return False




def main():
    t=is_palindrome(123)
    print("3")
    main()