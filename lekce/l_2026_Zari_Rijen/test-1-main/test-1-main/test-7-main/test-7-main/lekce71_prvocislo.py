for i in range(2, 5):
    for x in range(2, i):
        print(f"Kontroluji číslo {i} dělené {x}")
        if i % x == 0:     # modulo, zbytek po dělení
            print(f"{i} se rovná {x} * {i//x}, takže není prvočíslo")
            break
    else:
        print(f"{i} ====== JE PRVOČÍSLO ======")
            