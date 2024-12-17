def formatar_mdx(mdx_bruto):
    resposta = ""
    for mdx in mdx_bruto:
        resposta += f"ID {mdx[0]} - Melhor de {mdx[1]} - PLACAR => {mdx[2]} x {mdx[3]}"
    return resposta
