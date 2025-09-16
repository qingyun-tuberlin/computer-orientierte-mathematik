# Der Ausdruck ist genau dann wahr, wenn aund b
# denselben Typ und dieselbe Bitfolge beinhalten.
print(2===2)
print(2===2.0)

# a == b : Der Ausdruck ist genau
# dann wahr, wenn aund b
# denselben Wert repräsentieren.
# Dies ist für verschiedene
# Kombinationen von Typen einzeln
# definiert.
print(2==2.0)

# isequal(a, b) : Wie== außer bei
# der Behandlung spezieller Werte
# (NaN, -0.0…).
print(isequal(NaN,-0.0))