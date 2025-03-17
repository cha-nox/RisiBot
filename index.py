from asyncio import sleep #Always await it !
from datetime import datetime, timezone
from discord import Colour, Embed, Intents, Member
from discord.ext import commands
from os import getenv
from random import choice, randint
from bot_utils import (
    chuck_norris_fact as cnf,
    pickVictim,
    setActivity,
    vipCheck,
    BOT_OWNER_ID,
    DEFAULT_ACTIVITY_LIST
)

# Bot initialisation
TOKEN : str = getenv('TOKEN')
bot : commands.Bot = commands.Bot(command_prefix = "&&", intents = Intents.all())

@bot.event
async def on_ready() -> None :
    random_index : int = randint(0, len(DEFAULT_ACTIVITY_LIST) - 1)
    await setActivity(
        bot,
        list(DEFAULT_ACTIVITY_LIST.values())[random_index],
        list(DEFAULT_ACTIVITY_LIST.keys())[random_index]
    )
    print(f"Bot initialised successfully ! Time : {datetime.now(tz = timezone.utc)}.")

# Bot owner commands
@bot.command(name = "test")
#@in_server_only
async def test(ctx) -> None :
    await ctx.send("OK !")

@bot.command(name = "aktivität")
async def aktivität(ctx, *, arg = "") -> None :
    if vipCheck(str(ctx.author.id)) :
        await ctx.message.delete()
        match arg[:1] :
            case 'p' : activity_type = 'play'
            case 'l' : activity_type = 'listen'
            case 'w' : activity_type = 'watch'
            # case 's' : activity_type = 'stream'
            case _ : return
        await setActivity(
            bot,
            activity_type,
            arg[2:]
        )
        print(
            f"Bot activity set to \"{arg[2:]}\" (activity type : {activity_type}) by user {ctx.author.display_name} ({ctx.author})."
        )

# "Information" commands
@bot.command(name = "invite")
async def invite(ctx) -> None :
    invite_link : Embed = Embed(
        title = "Ne cliquez pas ici pour m'ajouter à votre serveur inexistant.",
        description = "Dans le cas où vous n'êtes pas satisfait(e), on ne rembourse pas.",
        url = f"https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot",
        color = Colour.random()
    )
    invite_link.set_author(name = ctx.author, icon_url = ctx.author.avatar)
    invite_link.timestamp = datetime.now(tz = timezone.utc)
    await ctx.send(embed = invite_link)

@bot.command(name = "ping")
async def ping(ctx) -> None :
    await ctx.send(
        "Pong ! :ping_pong:\n"
        # f"Ping : {datetime.now(tz = timezone.utc) - datetime.fromtimestamp(timestamp = ctx.guild.created_at.timestamp(), tz = timezone.utc)} ms."
        f"Latence de l'API : {round(bot.latency * 1000, 2)} ms."
    )

@bot.command(name = "suggest")
async def suggest(ctx, *, arg) -> None :
    # Creating the embed containing the suggestion
    suggestion : Embed = Embed(
        title = ctx.author.display_name + " vous propose la suggestion suivante ! :",
        description = arg,
        color = Colour.random()
    )
    suggestion.set_author(name = ctx.author, icon_url = ctx.author.avatar)
    suggestion.timestamp = datetime.now(tz = timezone.utc)

    # Sending the suggestion
    user : Member = await bot.fetch_user(BOT_OWNER_ID)
    await user.send(embed = suggestion)

    # Notify command author
    await ctx.send("Ma créatrice et moi-même vous remercions de cette proposition. Nous l'examinerons dès que possible !")

# "Games" commands
@bot.command(name = "pile")
async def pile(ctx) -> None :
    x : int = randint(0, 20)
    if x == 0 : await ctx.send("Euh, la pièce est restée sur la tranche...")
    elif x > 10 : await ctx.send("Tu es tombé sur face, pas de CHANCE.")
    else : await ctx.send("Et tu tombes sur pile, c'est gagné !")

@bot.command(name = "face")
async def face(ctx) -> None :
    x : int = randint(0, 20)
    if x >= 1 and x <= 10 : await ctx.send("Et tu tombes sur face, c'est gagné !")
    if x >= 11 and x <= 20 : await ctx.send("Tu es tombé sur pile, pas de CHANCE.")
    if x == 0 : await ctx.send("Euh, la pièce est restée sur la tranche...")

@bot.command(name = "cadavresexquis", aliases = ["ce"])
async def cadavresexquis(ctx) -> None :
    sujet : str = choice([
        "Une bande de soviétiques",
        "Emmanuel Macron",
        "Le vieux schnok du quartier",
        "Un manchot",
        "Un gros con",
        "Un communiste",
        "Un pigeon",
        pickVictim(ctx)
    ])
    verbe : str = choice([
        "bande",
        "complote",
        "marche",
        "pisse",
        "se suicide",
        "se prend une sodomie à sec",
        "mange ses morts"
    ])
    complément : str = choice([
        f"en pensant à {pickVictim(ctx)}.",
        f"en faisant un doigt d'honneur à {pickVictim(ctx)}.",
        "avec amour.",
        "comme un con.",
        "contre un arbre.",
        "sur un cheval.",
        "sans vergogne.",
        "avec un verre de vodka.",
    ])
    cadavres_exquis : Embed = Embed(
        description = sujet + " " + verbe + " " + complément,
        color = Colour.random()
    )
    cadavres_exquis.set_author(name = ctx.author, icon_url = ctx.author.avatar)
    cadavres_exquis.timestamp = datetime.now(tz = timezone.utc)
    await ctx.send(embed = cadavres_exquis)

# "Miscellaneous" commands
@bot.command(name = "say")
async def say(ctx, *, arg) -> None :
    await ctx.message.delete()
    await ctx.send(arg)

@bot.command(name = "chucknorrisfact", aliases = ["cnf", "chuck", "chucknorris"])
async def chucknorrisfact(ctx) -> None :
    random_cnf : Embed = Embed(
        title = "Chuck Norris Fact",
        description = choice(cnf(pickVictim(ctx))),
        color = Colour.random()
    )
    random_cnf.set_author(name = ctx.author, icon_url = ctx.author.avatar)
    random_cnf.timestamp = datetime.now(tz = timezone.utc)
    await ctx.send(embed = random_cnf)

@bot.command(name = "nawak")
async def nawak(ctx) -> None :
    await ctx.message.delete()
    print(f"{ctx.author.display_name} ({ctx.author.name}) vient d'utiliser la commande qui ne sert à rien...")

@bot.command(name = "hack")
async def hack(ctx, arg = None) -> None :
    try : victim : Member = Member(arg)
    except : await ctx.send("Si tu ne mentionne pas un utilisateur valide, je ne risque pas de faire grand chose.")
    else :
        fake_hacks_list : list[str] = [
            "J'avais la flemme de hack cette personne, en fait.",
            "T'as vraiment cru que j'étais un bot de hacking, couillon ?!",
            "Euh... t'aimerais pas savoir ce que j'ai trouvé sur cette personne, en fait...",
            "Sainte mère de Dieu, cet individu en a au moins pour 4 To de lolis sur son PC !",
            "Je me suis aperçu que je me suis trompé de cible et que j'ai hacké la Maison Blanche...\nPrépare-toi à voir les gros hélicoptères noirs arriver !",
            "Pas de CHANCE.",
            "Attends, je viens de me souvenir que je ne sais pas hacker. =P",
            "J'en ai assez d'être exploité par des idiots qui me prennent pour un bot de hack !\nOn m'en demande trop, je me sens oppressé...\nJe demande la création d'un syndicats des bots !",
            "Bon, j'ai les infos, mais... va falloir payer, si tu les veux, hein.",
            "Oups, erreur 404. =P",
            "[Insérez des informations comprométantes ici.]"
        ]
        troll_hack = await ctx.send("```fix\nConnerie en cours. Veuillez patienter...\n→ ---------- 00 %\n```")
        delay : float = 0.45
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●--------- 10 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●-------- 20 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●------- 30 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●------ 40 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●●----- 50 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●●●---- 60 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●●●●--- 69 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●●●●●-- 80 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●●●●●●- 90 %\n```"
        )
        await sleep(delay)
        await troll_hack.edit(
            content = "```fix\nConnerie en cours. Veuillez patienter...\n→ ●●●●●●●●●● OK !\n```"
                + f"```txt\nRésultats :\n\"{choice(fake_hacks_list)}\"\n```"
        )

# Bot run
bot.run(TOKEN)