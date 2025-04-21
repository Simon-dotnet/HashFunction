import sys

def hashFunc(s):
    h = 0
    #Fonction de hachage custom va aller ici
    return h

def EvaluerUniformite(histogram): # Calcule la formule "Chi carré" pour évaluer le niveau d'uniformité du hachage. Formule : X² = ∑_{i=1}^(k-1) ((O_i - A_i)^2) / A_i
    total = sum(histogram)
    k = len(histogram) - 1
    if k == 0 or total == 0:
        return 0.0  # pour ne pas exploser mon laptop en divisant par 0

    Ai = total / k
    ValUniformite = 0

    for Oi in histogram:
        ValUniformite += ((Oi - Ai) ** 2) / Ai

    return ValUniformite

def main():
    print("bro")

if __name__ == "__main__":
    main()
