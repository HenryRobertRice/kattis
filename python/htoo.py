from string import ascii_uppercase
def main():
    mol_in, n = input().split()
    n = int(n)
    atoms_in = quantify(mol_in)
    for atom in atoms_in:
        atoms_in[atom] *= n
    atoms_out = quantify(input())
    print(convert(atoms_in, atoms_out))


def quantify(mol):
    atoms = {}
    for i in range(len(mol)):
        if mol[i] in ascii_uppercase:
            n = get_number(mol, i)
            if mol[i] not in atoms:
                atoms[mol[i]] = n
            else:
                atoms[mol[i]] += n
    return atoms


def get_number(mol, i):
    if i == len(mol) - 1:
        return 1
    buf = []
    for j in range(i + 1, len(mol)):
        if mol[j] not in ascii_uppercase:
            buf.append(mol[j])
        else:
            break
    if buf == []:
        return 1
    return int("".join(buf))


def convert(atoms_in, atoms_out):
    multiples = []
    for atom in atoms_out:
        if atom not in atoms_in:
            return 0
        multiples.append(atoms_in[atom] // atoms_out[atom])
    return min(multiples)



if __name__ == "__main__":
    main()
