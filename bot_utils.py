from discord import Activity, ActivityType, Game
from discord.ext import commands
from os import getenv
from random import choice

BOT_OWNER_ID : str = getenv('BOT_OWNER_ID')
DEFAULT_ACTIVITY_LIST : dict[str, str] = {
    "engueuler une truite." : 'play',
    "pisser sur une télé." : 'play',
    "insulter une table." : 'play',
    "voler les cookies numériques préparés par Kagura." : 'play',
    "chasser des huîtres." : 'play',
    "étudier la congolexicomatisation des lois du marché." : 'play',
    "un match de quidditch." : 'watch'
}

def chuck_norris_fact(victim : str) -> list[str] :
    return [
        f"Chuck Norris détient la liste de tous les amateurs de Boku No Pico. D'ailleurs, il a remarqué que {victim} regarde très souvent.",
        f"Chuck Norris peut tuer les amis imaginaires de {victim}.",
        "Chuck Norris a déjà compté jusqu'à l'infini. Deux fois !",
        "Le Père Noël croît en Chuck Norris.",
        "Les extraterrestres ont peur de se faire capturer par Chuck Norris.",
        "Les suisses ne sont pas neutres. Ils attendent juste de savoir de quel côté est Chuck Norris.",
        "Quand il était petit, Chuck Norris n'envoyait pas de lettre au Père Noël. Il lui envoyait des ultimatums.",
        "Chuck Norris est né dans une maison en rondins qu'il a construite lui-même.",
        "Chuck Norris n'a pas de père. Personne ne nique la mère de Chuck Norris !",
        "Si Chuck Norris n'existait pas, il s'inventerait.",
        "Chuck Norris peut claquer une porte fermée.",
        "Un jour, Chuck Norris a balancé une grenade sur 12 personnes, et les 12 personnes sont mortes. Puis la grenade a explosé après.",
        "Quand Chuck Norris joue à Pile ou face, la pièce peut rester sur la tranche.",
        "Chuck Norris peut t'étrangler avec le fil d'un téléphone sans fil.",
        "Si c'était Chuck Norris qui codait ce bot, il fonctionnerait du premier coup et il n'y aurait pas d'erreurs.",
        "Quand Chuck Norris fume un joint, c'est le joint qui est défoncé.",
        "Chuck Norris a fini Super Mario Bros sans sauter.",
        "Chuck Norris joue à la console sans télé. Il trouve ça trop facile, sinon.",
        "En France, on dit aux petits enfants que le Grand Méchant Loup viendra les manger s'ils ne finissent pas leur assiette. Aux États-Unis, on leur parle de Chuck Norris. C'est pour ça qu'il y a autant d'enfants obèses en Amérique.",
        "Quand Chuck Norris utilise Windows, il ne plante pas.",
        "Un jour, Chuck Norris a perdu son alliance. Depuis, c'est le bordel sur la terre du milieu.",
        "Chuck Norris se souvient très bien de son futur.",
        "Un jour, Chuck Norris a fait un bras de fer contre One Punch Man ; le perdant devait se raser le crâne.",
        "Chuck Norris peut encercler dix hommes à lui seul.",
        "Les petits enfants portent des pyjamas Super Man. Super Man porte des pyjamas Chuck Norris.",
        "Chuck Norris est la raison pour laquelle Charlie se cache.",
        "La Lune tourne autour de la Terre pour échapper au regard de Chuck Norris.",
        "Chuck Norris peut tirer une balle de fusil à mains nues.",
        "Chuck Norris regarde la télé avec sa radio.",
        "Chuck Norris a inventé le lance-flammes en urinant sur la flamme d'un briquet.",
        "Chuck Norris a supprimé la corbeille de son PC Windows.",
        "La mort se demande souvent ce qu'il y a après Chuck Norris.",
        "Quand Chuck Norris entre dans une pièce sombre, il n'allume pas la lumière. Il éteint l'obscurité.",
        "Chuck Norris dort avec la lumière allumée. Pas parce qu'il a peur du noir, mais parce que le noir a peur de lui.",
        "Un jour, Chuck Norris a visité les Îles vierges. Depuis, elles s'appellent juste les Îles.",
        "Les amnésiques se souviennent quand-même de Chuck Norris.",
        "Les aveugles peuvent voir Chuck Norris.",
        "Chuck Norris apparaît en couleur sur les vieux écrans de télévision en noir et blanc.",
        "Quand Google ne sait pas quelque chose, il demande à Chuck Norris.",
        "Le seule endroit où tu peux taper Chuck Norris, c'est la barre de recherche de Google.",
        "Chuck Norris peut abattre 11 cibles sur les 10 qu'il a devant lui... et avec seulement 9 balles.",
        "Chuck Norris dort avec un oreiller sous son arme.",
        "Chuck Norris peut éteindre un incendie avec un bidon d'essence.",
        "Chuck Norris sait parler le braille.",
        "Chuck Norris peut entendre la langue des signes.",
        "Chuck Norris était censé mourrir il y a 20 ans, mais la Mort n'a jamais eu le courage de lui dire.",
        "Un jour, un serpent a mordu la jambe de Chuck Norris. Après avoir terriblement souffert pendant 4 jours, le serpent a fini par mourir.",
        "À la fin du livre des records, il est écrit que tous les records sont en réalité détenus par Chuck Norris, et que les performances citées dans le livre sont celles qui se rapproche le plus de celles de Chuck.",
        "Quand la nuit tombe, Chuck Norris la ramasse.",
        "Chuck Norris peut faire une roue avant avec un monocycle.",
        "La peur des araignées s'appelle l'arachnophobie. La peur des espaces publics s'appelle l'agoraphobie. La peur de Chuck Norris s'appelle la logique.",
        "Chuck Norris mange sa soupe avec une fourchette.",
        "Un jour, Chuck Norris est allé sur Mars. Depuis, il n'y a plus aucune trace de formes de vie sur la planète rouge.",
        "Voldemort a peur de prononcer le nom de Chu... de _vous savez qui_.",
        "Chuck Norris est le père de Dark Vador.",
        "La gravité, c'est ce qui fait que la Terre tient sous Chuck Norris.",
        "Chuck Norris joue à Pokemon Go avec un téléphone fixe.",
        "Chuck Norris joue à la roulette russe avec un chargeur plein. Et il gagne à chaque fois.",
        "Un jour, Chuck Norris à eu un 0/20 à un contrôle de Latin. Depuis, c'est une langue morte.",
        "Il n'y a pas de théorie de l'évolution. Il y a juste une liste d'espèces que Chuck Norris autorise à survivre.",
        "La seule chose qui arrive a la cheville de Chuck Norris, c'est sa chaussette.",
        "Les fantômes se racontent des histoires de Chuck Norris pour se faire peur.",
        "Chuck Norris ne ment pas. C'est la vérité qui se trompe.",
        "Le meunier fabrique de la farine avec du blé. Chuck Norris, lui, peut fabriquer du blé avec de la farine.",
        "Chuck Norris sait où se trouve le papa de Stromaé.",
        "Chuck Norris ne porte pas de montre. Il décide de l'heure qu'il est.",
        "Un jour, Chuck Norris a commandé un steak au restarant. Et le steak a obéï.",
        "Chuck Norris a inventé le code qui s'optimise lui-même.",
        "Chuck Norris peut tuer un cadavre.",
        "Tout ce que le roi Midas touche devient de l'or. Tout ce que Chuck Norris touche devient mort.",
        "Le journal intime de Chuck Norris s'appelle le Livre Guiness des records.",
        "Chuck Norris peut casser trois pattes à un canard.",
        "Chuck Norris peut faire un clic droit sur le curseur de sa souris."
    ]

def pickVictim(ctx) -> str :
    if ctx.guild == None : return ctx.author.mention
    random_member = choice([member for member in ctx.guild.members if not member.bot])
    return choice([random_member.mention, ctx.author.mention])

def vipCheck(ID : str) -> bool :
    return ID in [
        BOT_OWNER_ID
    ]

async def setActivity(bot : commands.Bot, activity_type : str, activity : str) -> None :
    match activity_type :
        case 'play' :
            await bot.change_presence(activity = Game(name = activity))

        case 'listen' :
            await bot.change_presence(activity = Activity(type = ActivityType.listening, name = activity))

        case 'watch' :
            await bot.change_presence(activity = Activity(type = ActivityType.watching, name = activity))

        # case 'stream' :
        #     await bot.change_presence(activity = Streaming(name = activity, url = twitch_url))

        case _ :
            raise Exception("Invalid activity type.")
        
# Decorators
# def in_server_only(command):
#     """
#     When applied to a command route as a decorator, ensure that the command can't be invoked in DMs.
#     """

#     @wraps(command)
#     def decorated_command(*args, **kwargs):
#         if command.ctx.guild is None :
#             print("Cette commande n'est pas disponible en messages privés.")
#             return

#         return command(*args, **kwargs)

#     return decorated_command