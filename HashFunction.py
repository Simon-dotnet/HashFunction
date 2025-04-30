import sys

def hashFunc_blender(s: str) -> int:
    seed = 988787038669 # nombre premier
    MASK = 0xFFFFFFFFFFFFFFFF # masque appliqué aux opérations pour garder le résultat en 64 bits

    # coupe en 2 parties
    mid = len(s) // 2
    first, second = s[:mid], s[mid:]

    # fonction pour mélanger avec le seed + décalages de bits
    def blend_it(h, b):
        for _ in range(5):
            h = ((h << 8) ^ b) & MASK
            h = (h * seed) & MASK
            h ^= ((h >> 16) ^ b) & MASK
        return h
    
    # première moitié
    h1 = 0
    for c in first:
        b = ord(c)
        h1 = blend_it(h1, b)

    # seconde moitié
    h2 = 0
    for c in second:
        b = ord(c)
        h2 = blend_it(h2, b)

    return (h1 ^ h2) & MASK

def EvaluerUniformite(histogram): # Calcule la formule "Chi carré" pour évaluer le niveau d'uniformité du hachage. Formule : X² = ∑_{i=1}^(k-1) ((O_i - A_i)^2) / A_i
    total = sum(histogram)
    k = len(histogram)
    if k <= 0 or total == 0:
        return 0.0
    Ai = total / k
    chi2 = 0.0
    for Oi in histogram:
        chi2 += ((Oi - Ai) ** 2) / Ai
    return chi2

def printHistogram(histogram):
    for count in histogram:
        print(count)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <taille_histogramme>", file=sys.stderr)
        sys.exit(1)

    try:
        k = int(sys.argv[1])
    except ValueError:
        print("Erreur : la taille de l’histogramme doit être un entier.", file=sys.stderr)
        sys.exit(1)

    histogram = [0] * k

    for line in sys.stdin:
        s = line.rstrip('\n')
        h = hashFunc_blender(s)
        idx = h % k
        histogram[idx] += 1

    printHistogram(histogram)

    chi2 = EvaluerUniformite(histogram)
    print(f"Valeur d'uniformité : {chi2}", file=sys.stderr)

if __name__ == "__main__":
    main()
