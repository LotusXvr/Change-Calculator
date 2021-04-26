

while True:
    def change_calculation(cash):
        quinhentos = 0
        duzentos = 0
        cem = 0
        cinquenta = 0
        vinte = 0
        dez = 0
        cinco = 0
        dois = 0
        um = 0
        cinquenta_cents = 0
        vinte_cent = 0
        dez_cents = 0
        cinco_cent = 0
        dois_cents = 0
        um_cent = 0

        while cash >= 500.00:
            cash = round(cash, 3)
            cash -= 500.00
            quinhentos += 1
            cash = round(cash, 3)

        while cash < 500 and cash >= 200:
            cash = round(cash, 3)
            cash -= 200
            duzentos += 1
            cash = round(cash, 3)

        while cash < 200 and cash >= 100:
            cash = round(cash, 3)
            cash -= 100
            cem += 1
            cash = round(cash, 3)

        while cash < 100 and cash >= 50:
            cash = round(cash, 3)
            cash -= 50
            cinquenta += 1
            cash = round(cash, 3)

        while cash < 50 and cash >= 20:
            cash = round(cash, 3)
            cash -= 20
            vinte += 1
            cash = round(cash, 3)

        while cash < 20 and cash >= 10:
            cash = round(cash, 3)
            cash -= 10
            dez += 1
            cash = round(cash, 3)

        while cash < 10 and cash >= 5:
            cash = round(cash, 3)
            cash -= 5
            cinco += 1
            cash = round(cash, 3)

        while cash < 5 and cash >= 2:
            cash = round(cash, 3)
            cash -= 2
            dois += 1
            cash = round(cash, 3)

        while cash < 2 and cash >= 1:
            cash = round(cash, 3)
            cash -= 1
            um += 1
            cash = round(cash, 3)

        while cash < 1 and cash >= 0.50:
            cash = round(cash, 3)
            cash -= 0.50
            cinquenta_cents += 1
            cash = round(cash, 3)

        while cash < 0.50 and cash >= 0.20:
            cash = round(cash, 3)
            cash -= 0.20
            vinte_cent += 1
            cash = round(cash, 3)

        while cash < 0.20 and cash >= 0.10:
            cash = round(cash, 3)
            cash -= 0.10
            dez_cents += 1
            cash = round(cash, 3)

        while cash < 0.10 and cash >= 0.05:
            cash = round(cash, 3)
            cash -= 0.05
            cinco_cent += 1
            cash = round(cash, 3)

        while cash < 0.05 and cash >= 0.02:
            cash = round(cash, 3)
            cash -= 0.02
            dois_cents += 1
            cash = round(cash, 3)

        while cash < 0.02 and cash >= 0.01:
            cash = round(cash, 3)
            cash -= 0.01
            um_cent += 1
            cash = round(cash, 3)

        print("\nChange:")
        if quinhentos >= 1:
            print(f"500  - {quinhentos} bill(s)")
        if duzentos >= 1:
            print(f"200  - {duzentos} bill(s)")
        if cem >= 1:
            print(f"100  - {cem} bill(s)")
        if cinquenta >= 1:
            print(f"50   - {cinquenta} bill(s)")
        if vinte >= 1:
            print(f"20   - {vinte} bill(s)")
        if dez >= 1:
            print(f"10   - {dez} bill(s)")
        if cinco >= 1:
            print(f"5    - {cinco} bill(s)")
        if dois >= 1:
            print(f"2    - {dois} coin(s)")
        if um >= 1:
            print(f"1    - {um} coin(s)")
        if cinquenta_cents >= 1:
            print(f"0.50 - {cinquenta_cents} coin(s)")
        if vinte_cent >= 1:
            print(f"0.20 - {vinte_cent} coin(s)")
        if dez_cents:
            print(f"0.10 - {dez_cents} coin(s)")
        if cinco_cent >= 1:
            print(f"0.05 - {cinco_cent} coin(s)")
        if dois_cents >= 1:
            print(f"0.02 - {dois_cents} coin(s)")
        if um_cent >= 1:
            print(f"0.01 - {um_cent} coin(s)")


    def initiation():
        Amount_to_pay = float(input("\nAmount to pay: \n> "))
        Money_Given = float(input("Money given: \n> "))

        Troco = Money_Given - Amount_to_pay
        Troco = round(Troco, 3)
        print(f"\nThe change is {Troco}")

        if Troco < 0:
            print("The money given must be higher then the amount to pay.")
        else:
            change_calculation(Troco)


    prompt_continue = str(input("\nCalculate change? \ny/n \n> "))
    if prompt_continue in "sSyY1":
        initiation()
    else:
        break

