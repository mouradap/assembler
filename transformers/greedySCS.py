import itertools
from .overlap import overlap

# A classe GreedyAssembler permite o cálculo
# de sobreposições por alinhamento global, 
# e retorna o menor construto contendo todas
# as possíveis sobreposições nos reads.
# Essa classe se baseia no algoritmo Greedy Common Superstring.

class GreedyAssembler:
    def __init__(self):
        pass

# Fazemos uma permutação entre cada string contida nos reads
# e calculamos as sobreposições entre elas.
# Retornamos as melhores sobreposições entre cada read.

    def pick_maximal_overlap(self, reads, k):
        reada, readb = None, None
        best_olen = 0
        permutations = itertools.permutations(reads, 2)
        for a, b in permutations:
            olen = overlap(a, b)
            if olen > best_olen:
                reada, readb = a, b
                best_olen = olen
        return reada, readb, best_olen

# O método assemble chama os demais métodos para a lista de reads de input
# encontra as melhores sobreposições entre cada read
# e itera até chegar ao menor superstring que contém todos os strings.
# Ao final, quando nenhum read tiver mais sobreposições, é retornado
# um superstring juntando cada um dos reads que foram possíveis construir.
    def assemble(self, reads, k):
        read_a, read_b, olen = self.pick_maximal_overlap(reads, k)
        while olen > 0:
            reads.remove(read_a)
            reads.remove(read_b)
            reads.append(read_a + read_b[olen:])

            read_a, read_b, olen = self.pick_maximal_overlap(reads, k)

        return "".join(reads)