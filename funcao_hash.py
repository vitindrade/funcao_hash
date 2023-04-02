from hashlib import sha256
from hashlib import md5


print("\n Gerador Hash \n")

escolha = str(input(" Escolha 'Mostrar exemplos' ou 'conferir codigo HASH':"))

if ((escolha == "Mostrar exemplos") or (escolha == "mostrar exemplos")):
    frase_1 ="A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP."
    hash_senha1 ="d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9"
    md5_senha1 ="c850e1a34a6ed572e0758ccd9c615bda"
    hash1_256 = str(sha256(frase_1.encode()).hexdigest())
    hash1_md5 = str(md5(frase_1.encode()).hexdigest())

    print("\n",hash_senha1," - exemplo","\n", hash1_256," - gerado")
    print("\n",md5_senha1," - exemplo","\n", hash1_md5," - gerado \n")

    if((hash_senha1==hash1_256 ) and (md5_senha1==hash1_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha1!=hash1_256 ) and (md5_senha1==hash1_md5)):
        print("Somente MD5 correto")
    if((hash_senha1==hash1_256 ) and (md5_senha1!=hash1_md5)):
        print("Somente SHA256 correto")
    if((hash_senha1!=hash1_256 ) and (md5_senha1!=hash1_md5)):
        print("Nenhum dos dois corretos")
    print("\n __________________________________________________________________________________ \n")

    frase_2 ="A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus"
    hash_senha2 ="6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337"
    md5_senha2 ="b710771da8d7521524f45233ea9dd9e1"
    hash2_256 = str(sha256(frase_2.encode()).hexdigest())
    hash2_md5 = str(md5(frase_2.encode()).hexdigest())

    print("\n",hash_senha2," - exemplo","\n", hash2_256," - gerado")
    print("\n",md5_senha2," - exemplo","\n", hash2_md5," - gerado \n")

    if((hash_senha2==hash2_256 ) and (md5_senha2==hash2_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha2!=hash2_256 ) and (md5_senha2==hash2_md5)):
        print("Somente MD5 correto")
    if((hash_senha2==hash2_256 ) and (md5_senha2!=hash2_md5)):
        print("Somente SHA256 correto")
    if((hash_senha2!=hash2_256 ) and (md5_senha2!=hash2_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")

    frase_3 ="Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial."
    hash_senha3 ="6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6"
    md5_senha3 ="55748c2cb669a9d9508677cb914cb025"
    hash3_256 = str(sha256(frase_3.encode()).hexdigest())
    hash3_md5 = str(md5(frase_3.encode()).hexdigest())

    print("\n",hash_senha3," - exemplo","\n", hash3_256," - gerado")
    print("\n",md5_senha3," - exemplo","\n", hash3_md5," - gerado \n")

    if((hash_senha3==hash3_256 ) and (md5_senha3==hash3_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha3!=hash3_256 ) and (md5_senha3==hash3_md5)):
        print("Somente MD5 correto")
    if((hash_senha3==hash3_256 ) and (md5_senha3!=hash3_md5)):
        print("Somente SHA256 correto")
    if((hash_senha3!=hash3_256 ) and (md5_senha3!=hash3_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")

    frase_4 ="A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente."
    hash_senha4 ="254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e"
    md5_senha4 ="f4a8a299fd4da2a5d70b374be2e48147"
    hash4_256 = str(sha256(frase_4.encode()).hexdigest())
    hash4_md5 = str(md5(frase_4.encode()).hexdigest())

    print("\n",hash_senha4," - exemplo","\n", hash4_256," - gerado")
    print("\n",md5_senha4," - exemplo","\n", hash4_md5," - gerado \n")

    if((hash_senha4==hash4_256 ) and (md5_senha4==hash4_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha4!=hash4_256 ) and (md5_senha4==hash4_md5)):
        print("Somente MD5 correto")
    if((hash_senha4==hash4_256 ) and (md5_senha4!=hash4_md5)):
        print("Somente SHA256 correto")
    if((hash_senha4!=hash4_256 ) and (md5_senha4!=hash4_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")


    frase_5 ="Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982"
    hash_senha5 ="d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0"
    md5_senha5 ="1c4ecc238571333ae507f82ff6a5e9e4"
    hash5_256 = str(sha256(frase_5.encode()).hexdigest())
    hash5_md5 = str(md5(frase_5.encode()).hexdigest())

    print("\n",hash_senha5," - exemplo","\n", hash5_256," - gerado")
    print("\n",md5_senha5," - exemplo","\n", hash5_md5," - gerado \n")

    if((hash_senha5==hash5_256 ) and (md5_senha5==hash5_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha5!=hash5_256 ) and (md5_senha5==hash5_md5)):
        print("Somente MD5 correto")
    if((hash_senha5==hash5_256 ) and (md5_senha5!=hash5_md5)):
        print("Somente SHA256 correto")
    if((hash_senha5!=hash5_256 ) and (md5_senha5!=hash5_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")

    frase_6 ="Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002."
    hash_senha6 ="faefb927a21dd282ee00effe42bc0688f649450677a61edce15863a15461b721"
    md5_senha6 ="98420532cbf1be32a98be579f592cd72"
    hash6_256 = str(sha256(frase_6.encode()).hexdigest())
    hash6_md5 = str(md5(frase_6.encode()).hexdigest())


    print("\n",hash_senha6," - exemplo","\n", hash6_256," - gerado")
    print("\n",md5_senha6," - exemplo","\n", hash6_md5," - gerado \n")

    if((hash_senha6==hash6_256 ) and (md5_senha6==hash6_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha6!=hash6_256 ) and (md5_senha6==hash6_md5)):
        print("Somente MD5 correto")
    if((hash_senha6==hash6_256 ) and (md5_senha6!=hash6_md5)):
        print("Somente SHA256 correto")
    if((hash_senha6!=hash6_256 ) and (md5_senha6!=hash6_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")

    frase_7 ="O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005."
    hash_senha7 ="da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6"
    md5_senha7 ="2e20bfbece6fdc62de4c4bb80a77ba1f"
    hash7_256 = str(sha256(frase_7.encode()).hexdigest())
    hash7_md5 = str(md5(frase_7.encode()).hexdigest())


    print("\n",hash_senha7," - exemplo","\n", hash7_256," - gerado")
    print("\n",md5_senha7," - exemplo","\n", hash7_md5," - gerado \n")

    if((hash_senha7==hash7_256 ) and (md5_senha7==hash7_md5)):
        print("SHA256 e MD5 corretos")
    if((hash_senha7!=hash7_256 ) and (md5_senha7==hash7_md5)):
        print("Somente MD5 correto")
    if((hash_senha7==hash7_256 ) and (md5_senha7!=hash7_md5)):
        print("Somente SHA256 correto")
    if((hash_senha7!=hash7_256 ) and (md5_senha7!=hash7_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")


    frase_8 ="Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050."
    hash_senha8 ="56f4ba0ea34d91fe386f09dc687f1c35c757009b0230a828fa43e48ac08f8d0c"
    md5_senha8 ="5cbf7c58bf9acd451c3bf1b48392a9e6"
    hash8_256 = str(sha256(frase_8.encode()).hexdigest())
    hash8_md5 = str(md5(frase_8.encode()).hexdigest())


    print("\n",hash_senha8," - exemplo","\n", hash8_256," - gerado")
    print("\n",md5_senha8," - exemplo","\n", hash8_md5," - gerado \n")

    if ((hash_senha8==hash8_256 ) and (md5_senha8==hash8_md5)):
        print("SHA256 e MD5 corretos")
    if ((hash_senha8!=hash8_256 ) and (md5_senha8==hash8_md5)):
        print("Somente MD5 correto")
    if ((hash_senha8==hash8_256 ) and (md5_senha8!=hash8_md5)):
        print("Somente SHA256 correto")
    if ((hash_senha8!=hash8_256 ) and (md5_senha8!=hash8_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")

    frase_9 ="Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação."
    hash_senha9 ="2707325bd4929bbbadb422851a2248615bf7998bf3607b6ad934168be6a45859"
    md5_senha9 ="a0a80cbc42bcd7b4b6ab317d0d2efa33"
    hash9_256 = str(sha256(frase_9.encode()).hexdigest())
    hash9_md5 = str(md5(frase_9.encode()).hexdigest())


    print("\n",hash_senha9," - exemplo","\n", hash9_256," - gerado")
    print("\n",md5_senha9," - exemplo","\n", hash9_md5," - gerado \n")

    if ((hash_senha9==hash9_256 ) and (md5_senha9==hash9_md5)):
        print("SHA256 e MD5 corretos")
    if ((hash_senha9!=hash9_256 ) and (md5_senha9==hash9_md5)):
        print("Somente MD5 correto")
    if ((hash_senha9==hash9_256 ) and (md5_senha9!=hash9_md5)):
        print("Somente SHA256 correto")
    if ((hash_senha9!=hash9_256 ) and (md5_senha9!=hash9_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")

    frase_10 ="Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação."
    hash_senha10 ="b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8"
    md5_senha10 ="0288b32001adf2f237ba8410f8415e50"
    hash10_256 = str(sha256(frase_10.encode()).hexdigest())
    hash10_md5 = str(md5(frase_10.encode()).hexdigest())


    print("\n",hash_senha10," - exemplo","\n", hash10_256," - gerado")
    print("\n",md5_senha10," - exemplo","\n", hash10_md5," - gerado \n")

    if ((hash_senha10==hash10_256 ) and (md5_senha10==hash10_md5)):
        print("SHA256 e MD5 corretos")
    if ((hash_senha10!=hash10_256 ) and (md5_senha10==hash10_md5)):
        print("Somente MD5 correto")
    if ((hash_senha10==hash10_256 ) and (md5_senha10!=hash10_md5)):
        print("Somente SHA256 correto")
    if ((hash_senha10!=hash10_256 ) and (md5_senha10!=hash10_md5)):
        print("Nenhum dos dois corretos")

    print("\n __________________________________________________________________________________ \n")


if ((escolha == "conferir codigo HASH")or(escolha == "Conferir codigo HASH")):
    frase = input("Frase a ser codificada:")
    sha_256 = str(input("Codigo Hash SHA256:"))
    md5_hash = str(input("Codigo Hash MD5:"))
    hash_256 = str(sha256(frase.encode()).hexdigest())
    hash_md5 = str(md5(frase.encode()).hexdigest())

    print("\n",sha_256," - exemplo","\n", hash_256," - gerado")
    print("\n",md5_hash," - exemplo","\n", hash_md5," - gerado \n")

    if ((sha_256==hash_256 ) and (md5_hash==hash_md5)):
        print("SHA256 e MD5 corretos")
    if ((sha_256!=hash_256 ) and (md5_hash==hash_md5)):
        print("Somente MD5 correto")
    if ((sha_256==hash_256 ) and (md5_hash!=hash_md5)):
        print("Somente SHA256 correto")
    if ((sha_256!=hash_256 ) and (md5_hash!=hash_md5)):
        print("Nenhum dos dois corretos")





