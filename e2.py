while True:
    try:
        x,y,z = input("Δώσε τα μήκη των πλευρών(x,y,z):").split(',')
        x = float(x)
        y = float(y)
        z = float(z)
    except ValueError as sfalma:
        print("Σφάλμα:",sfalma)
        continue
    if x==0 and y==0 and z==0:
        break

    x,y,z = sorted((x,y,z), reverse=True)


    def iso(x,y,z):
        if x==y and x!=z or x==z and x!=y or y==z and y !=x:
            return 'Το τρίγωνο είναι ισοσκελές'
        elif x==y and y==z:
            return 'Το τρίγωνο είναι ισόπλευρο'
        else:
            return 'Το τρίγωνο είναι οξυγώνιο'

    def eidos(x,y,z):
        if x**2 == y**2 + z**2 :
            return 'Το τρίγωνο είναι ορθογώνιο'
        elif x**2 > y**2 + z**2 :
            return 'Το τρίγωνο είναι αμβλυγώνιο'
        else:
            return 'Το τρίγωνο είναι οξυγώνιο'

        
    if x >= y + z :
        print(f"Οι πλευρές με φθίνουσα σειρά μεγέθους είναι:",x,y,z,"\nΔεν ισχύει η τριγωνική ανισότητα")
    else:
        perimetros = x + y + z
        t = perimetros*(1/2)
        embado = (t*(t-x)*(t-y)*(t-z))**(1/2)
        print(f"Οι πλευρές με φθίνουσα σειρά μεγέθους είναι:",x,y,z,"\nΗ περίμετρος του τριγώνου είναι:",perimetros,"\nΤο εμβαδόν του τριγώνου είναι:",embado,'\n',iso(x,y,z),'\n',eidos(x,y,z))
        
