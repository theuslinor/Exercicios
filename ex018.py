import math
ang = float(input('Digite um ângulo: '))
rad = math.radians(ang)
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem TANGENTE de {:.2f}'.format(ang, math.sin(rad), ang, math.cos(rad), ang, math.tan(rad)))