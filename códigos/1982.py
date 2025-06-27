from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        somas_atuais = sums
        resposta = []

        for i in range(n, 0, -1):

            somas_atuais.sort()
            diferenca = somas_atuais[1] - somas_atuais[0]
            frequencia = Counter(somas_atuais)
            proximas_somas = []
            
            for soma in somas_atuais:
                if frequencia[soma] == 0:
                    continue

                proximas_somas.append(soma)
                
                frequencia[soma] -= 1
                frequencia[soma + diferenca] -= 1

            if 0 in proximas_somas:
                resposta.append(diferenca)
                somas_atuais = proximas_somas
            else:
                resposta.append(-diferenca)
                somas_atuais = [s + diferenca for s in proximas_somas]

        return resposta