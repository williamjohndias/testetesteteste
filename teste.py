import bisect

def pesquisa_binaria_bisect(A, item):
    """Implementa pesquisa binária usando bisect."""
    # Encontra o ponto onde o item deveria ser (ou está) inserido.
    i = bisect.bisect_left(A, item)
    # Testa se o item está na lista.
    return i if i < len(A) and A[i] == item else -1

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", pesquisa_binaria_bisect(A, 20))
print("Pesquisa com sucesso:", pesquisa_binaria_bisect(A, 0))
print("Pesquisa com sucesso:", pesquisa_binaria_bisect(A, 70))
print("Pesquisa com falha:", pesquisa_binaria_bisect(A, 100))
