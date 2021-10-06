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
def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(153) == False
    assert is_palindrome(2222) == True
    assert is_palindrome(1234321) ==True
    assert is_palindrome(5000) == False

def get_n_choose_k(n , k):
    factorial_n=1
    factorial_k=1
    factorial_n_minus_k=1
    for i in range(1, n+1):
        factorial_n=factorial_n*i
    for i in range(1, k+1):
        factorial_k=factorial_k*i

    for i in range(1, n-k+1):
        factorial_n_minus_k=factorial_n_minus_k*i

    return factorial_n//(factorial_k*factorial_n_minus_k)







def main():
    '''
    nr= int(input('Dati numarul: '))
    inversul=is_palindrome(nr)
    if inversul==True:
        print(f'{nr} este palindrom')
    else:
        print(f'{nr} nu este palindrom')
    '''
    nn=int(input('Dati-l pe n: '))
    nk=int(input('Dati-l pe k: '))
    numarul=get_n_choose_k(nn, nk)
    print(numarul)
main()