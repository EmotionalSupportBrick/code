ålder = int(input("hur gammal är du?"))

if ålder == 17:
    print("Du är 17 år gammal och får inte rösta i valet, jävla nöt")
    
if ålder != 43: 
    print("du är inte lika gammal som per")
else:
    print("du är lika gammal som per")
    
if ålder <= 13:
    print("du är för ung för att rösta, jävla barn")
elif ålder < 18:
    print("du får inte ta körkort ån, dröm vidare")
elif ålder < 20:
    print("du får ta körkort men inte gå på systemet")
else:
    print("snyggt, du får både ta körkort och gå på systemet")
          
namn = input("vad heter du?")

if namn == "Benjamin":
    print("Tjenare Benjamin, trevligt att ha dig här frfr")
elif namn == "Benne":
    print("Så stavar man inte, nöt")
else:
    print("Tjenare " + namn + ", trevligt att du är här men du är inte Benjamin")
    
if ålder == 17 and namn == "Benjamin":
    print("Benjamin, du må vara 17 men du får inte rösta, inte ta körkort B, inte gå på systemet så dröm vidare")