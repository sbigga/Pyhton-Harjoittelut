VUODENAJAT = (
    "talvi",   # tammikuu
    "talvi",   # helmikuu
    "kevät",   # maaliskuu
    "kevät",   # huhtikuu
    "kevät",   # toukokuu
    "kesä",    # kesäkuu
    "kesä",    # heinäkuu
    "kesä",    # elokuu
    "syksy",   # syyskuu
    "syksy",   # lokakuu
    "syksy",   # marraskuu
    "talvi",   # joulukuu
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(VUODENAJAT[kuukausi - 1])
else:
    print("Kuukauden numeron tulee olla välillä 1-12.")