# Overlap é um script que permite identificar
# onde se inicia e termina a sobreposição entre strings.
def overlap(a: str, b: str, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0

        if b.startswith(a[start:]):
            return len(a) - start

        start += 1
