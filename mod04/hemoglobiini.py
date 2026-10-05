sukupuoli = input("Kerro biologinen sukupuolesi: ")
if sukupuoli == "mies":
    hemoglobiini = int(input("Kerro hemoglobiini arvosi: "))
    if (hemoglobiini <134):
     print("Hemoglobiini arvosi ovat alhaiset.")
    elif (hemoglobiini >195):
     print("Hemoglobiini arvosi ovat korkeat")
    else:
     print("hemoglobiini arvosi ovat normaalit")

   
elif sukupuoli == "nainen":
    hemoglobiini = int(input("Kerro hemoglobiini arvosi."))
if (hemoglobiini <117):
    print("Hemoglobiini arvosi ovat alhaiset.")
elif (hemoglobiini >175):
    print("Hemoglobiini arvosi ovat korkeat")
else:
    print("hemoglobiini arvosi ovat normaalit")
   


    
