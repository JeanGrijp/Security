def getDiretorio():
    with open("diretorios.txt") as arquivo:
        var = arquivo.readlines()
        let = []
        for i in var:
            string = ""
            for j in range(0, len(i)-1):
                string += i[j]
            let.append(string)
            string = ""
        let[-1] = let[-1] + "e"
        return let
