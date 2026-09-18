import os
import unicodedata

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True,
                   allowed_mentions=discord.AllowedMentions.none())

OBJETOS = {
    "botella de plastico": {
        "tiempo": "Alrededor de 450 años (estimación educativa en ambiente marino).",
        "consejo": "Vacía la botella y entrégala al reciclaje si tu servicio local la acepta.",
        "nota": "Puede fragmentarse en microplásticos; esto no significa biodegradarse por completo.",
    },
    "lata de aluminio": {
        "tiempo": "Alrededor de 200 años (estimación educativa en ambiente marino).",
        "consejo": "Vacía la lata y sepárala para reciclaje.",
        "nota": "El metal se deteriora por corrosión; no se descompone como un resto de comida.",
    },
    "botella de vidrio": {
        "tiempo": "Indeterminado: no hay un plazo fiable de descomposición.",
        "consejo": "Devuélvela si es retornable o llévala a un punto que reciba envases de vidrio.",
        "nota": "Romperse en fragmentos no equivale a biodegradarse.",
    },
}

ALIAS = {"plastico": "botella de plastico", "aluminio": "lata de aluminio",
         "lata": "lata de aluminio", "vidrio": "botella de vidrio"}

def normalizar(texto):
    """Permite escribir con mayúsculas, tildes y espacios adicionales."""
    texto = unicodedata.normalize("NFD", texto.casefold())
    texto = "".join(letra for letra in texto if not unicodedata.combining(letra))
    return " ".join(texto.split())

# ⚠️ CORREGIDO: Se quitó "objetos" de los paréntesis
@bot.command()
async def descomposicion(ctx, *, objeto: str = ""):
    """Consulta un objeto: !descomposicion botella de plastico"""
    nombre = normalizar(objeto)
    if not nombre:
        await ctx.send("Escribe un objeto: `!descomposicion botella de plastico`. "
                       "Consulta la lista con `!objetos`.")
        return

    nombre = ALIAS.get(nombre, nombre)
    datos = OBJETOS.get(nombre)
    if datos is None:
        await ctx.send("No tengo información sobre ese objeto. Usa `!objetos` para ver la lista.")
        return

    await ctx.send(
        f"🌱 **{nombre.capitalize()}**\n"
        f"⏳ **Tiempo:** {datos['tiempo']}\n"
        f"♻️ **Qué hacer:** {datos['consejo']}\n"
        f"📌 {datos['nota']}\n\n"
        "Los tiempos cambian según el material, la luz, la temperatura y el ambiente. "
        "¡No abandones residuos en la naturaleza!"
    )

@bot.command()
async def objetos(ctx):
    """Muestra los objetos disponibles."""
    lista = "\n".join(f"• {nombre}" for nombre in OBJETOS)
    await ctx.send(f"**Objetos disponibles:**\n{lista}\n\n"
                   "Ejemplo: `!descomposicion lata de aluminio`")

@bot.event
async def on_ready():
    print(f"Bot conectado: {bot.user}. Prueba !objetos en Discord.")

if __name__ == "__main__":
    # Pega tu NUEVO token entre las comillas. ¡No lo compartas!
    token = "token" 
    bot.run(token)
