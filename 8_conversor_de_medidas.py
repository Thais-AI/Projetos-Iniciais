distancia = float(input("Digite uma distância em metros: "))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f"A medida de {distancia}m corresponde a:")
print(f"{km}km / quilômetro(s)")
print(f"{hm}hm / hectômetro(s)")
print(f"{dam}dam / decâmetro(s)") 
print(f"{dm:.0f}dm / decímetro(s)")
print(f"{cm:.0f}cm / centrímetro(s)")
print(f"{mm:.0f}mm / milímetro(s)")