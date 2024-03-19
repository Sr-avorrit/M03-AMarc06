def mitjana_cicles(nom: str, cognom: str, **ufs):
    total_hores = sum(hores for _, hores in ufs.values())
    nota_total = sum(nota * hores for nota, hores in ufs.values()) / total_hores
    max_uf, max_nota = max(ufs.items(), key=lambda x: x[1][0])
    min_uf, min_nota = min(ufs.items(), key=lambda x: x[1][0])
    print(f"{nom} {cognom} te una mitjana de {nota_total:.2f}")
    print(f"La UF amb la nota més alta és la {max_uf} amb un {max_nota[0]}")
    print(f"La UF amb la nota més baixa és la {min_uf} amb un {min_nota[0]}")


mitjana_cicles('Laura', 'Garcia', UF1=(6, 99), UF2=(8, 33), UF3=(5, 66), UF4=(7, 66))
