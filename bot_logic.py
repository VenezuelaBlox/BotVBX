import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

# --- NUEVAS FUNCIONES ---

def gen_emoji():
    emojis = ["😀", "😂", "🚀", "🔥", "🎨", "🦊", "💻"]
    return random.choice(emojis)

def flip_coin():
    coin = ["Cara", "Cruz"]
    return random.choice(coin)

def obtener_arepa():
    # Probabilidades en porcentaje que suman 100%
    probabilidades = [33.0, 25.0, 18.0, 12.0, 7.0, 3.5, 1.3, 0.2]
    
    arepas = [
        {"nombre": "Arepa Viuda (Solo masa)", "rareza": "Común"},
        {"nombre": "Arepa con Queso Blanco", "rareza": "Poco Común"},
        {"nombre": "Arepa Catira (Pollo y queso amarillo)", "rareza": "Rara"},
        {"nombre": "Arepa Pelúa (Carne mechada y queso amarillo)", "rareza": "Épica"},
        {"nombre": "Arepa Reina Pepiada (Pollo, aguacate y mayo)", "rareza": "Mítica"},
        {"nombre": "Arepa Pabellón (Caraotas, carne, tajadas y queso)", "rareza": "Legendaria"},
        {"nombre": "Arepa de Perico con Chicharrón", "rareza": "Única"},
        {"nombre": "Arepa Sifrina Suprema con Extra Queso Frito dorada", "rareza": "Arepa Power"}
    ]
    
    # Selección aleatoria usando los pesos definidos
    arepa_obtenida = random.choices(arepas, weights=probabilidades, k=1)[0]
    
    return f"¡Has obtenido una **{arepa_obtenida['nombre']}**! 🫓 [Rareza: *{arepa_obtenida['rareza']}*]"
