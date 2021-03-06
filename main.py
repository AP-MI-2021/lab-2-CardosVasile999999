def is_palindrome(n):
    '''
    Problema 5:Determina daca un numar este palindrom
    Input:
    -n: int
    Output:
    boolean variable: True/False
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

def get_n_choose_k(n: int , k: int ):
    '''
    Problema 10: Calculeaza valoarea combinarilor de n luate de k ori
    Input:
    -n, k: numere intregi date
    Output:
    -Combinari de n luate cate k : numar intreg
    '''
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


def test_get_n_choose_k():
    assert get_n_choose_k(6, 2)==15
    assert get_n_choose_k(5, 3)==10
    assert get_n_choose_k(8, 4)==70
    assert get_n_choose_k(9, 3)==84
    assert get_n_choose_k(12, 5)==792
    assert get_n_choose_k(13, 2)==78


def get_age_in_days(dd, mm, yyyy):
    '''
    intput: ziua , luna, anul in care te-ai nascut
    output: numarul de zile pe care le ai
    '''
    aaaa=2021-yyyy
    aaaa=aaaa*365
    ll=10-mm
    ll=30*ll
    zz=365-dd
    return aaaa+ll+zz

def test_get_age_in_days():
    assert get_age_in_days(15, 1, 2003)==7190
    assert get_age_in_days(29, 8, 2004)==6601
    assert get_age_in_days(9, 6, 1985)==13616












def main():
    while True:
        print('1. Determină dacă un număr dat este palindrom.')
        print('2. Combinari de n luate cate k.')
        print('3. Determinati numarul de zile a unei persoane')
        print('x.Exit')
        optiune=input('Alege o optiune: ')
        if optiune=='1':
            nr=int(input('Dati numarul: '))
            if is_palindrome(nr)==True:
                print(f'{nr} este palindrom')
            else:
                print(f'{nr} nu este palindrom')
        elif optiune=='2':
            nn=int(input('Dati-l pe n: '))
            nk = int(input('Dati-l pe k: '))
            combinari=get_n_choose_k(nn, nk)
            print(f'Combinari de {nn} luate cate {nk} este {combinari}')
        elif optiune=='3':
            ziua=int(input('Dati ziua '))
            luna=int(input('Dati luna '))
            anul=int(input('Dati Anul '))
            v=get_age_in_days(ziua, luna, anul)
            print(f'omul are {v} zile')
        elif optiune=='x':
            break
        else:
            print('Optiune invalida')

    test_is_palindrome()
    test_get_n_choose_k()
    test_get_age_in_days()
if __name__ == '__main__':
    main()