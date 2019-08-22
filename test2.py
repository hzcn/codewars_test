dna = 'ATCG'

dna = dna.replace('T','a')
dna = dna.replace('A','T')
dna = dna.replace('C','g')
dna = dna.replace('G','C')
result = dna.upper()
print(result)


