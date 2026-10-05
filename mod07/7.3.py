def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def main():
    while True:
        gallonat = float(input("Anna bensiinin määrä gallonoina: "))
        if gallonat < 0:
            break
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")

main()    