import time
import argparse
from transformers import GreedyAssembler

# Argument Parser prepara como método de configurar
# inputs e outputs do nosso programa.

ap = argparse.ArgumentParser()
ap.add_argument(
    "-i",
    "--input",
    type=str,
    required=True,
    help="path to the input file"
    )
ap.add_argument(
    "-o",
    "--output",
    type=str,
    required=False,
    help="output filename"
    )
ap.add_argument(
    "-k",
    "--overlap",
    type=int,
    required=False,
    help="minimal number of overlapping residues for each read.",
)
args = vars(ap.parse_args())

# Nota:
# o script espera pelo menos dois argumentos:
# um path para o arquivo de input e
# um path para arquivo de output,
# além de permitir também definir
# o número minimo de sobreposições entre cada um dos reads.

# Instanciamos a classe GreedyAssembler, criada dentro dos transformers.
assembler = GreedyAssembler()

# Ler os inputs e carregar como uma lista dentro da variável reads.
reads = []
with open(args["input"], "r") as file:
    for line in file:
        reads.append(line.strip())

# Passamos as reads para o método assemble do GreedyAssembler,
# com número mínimo de sobreposições.
k = args['overlap'] if 'overlap' in args.keys() else 3

start_time = time.time()
assembly = assembler.assemble(reads, k)
end_time = time.time()

print("Finished in {} seconds.".format(end_time - start_time))


# Por fim, escrevemos os resultados em arquivo.
output_filename = args['output'] if 'output' in args.keys() else 'output.txt'
with open(output_filename, "w") as output:
    output.write(assembly)
