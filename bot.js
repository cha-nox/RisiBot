//Pas touche aux premières constantes. Sinon, ça va moins bien marcher.
const Discord = require('discord.js');
const bot = new Discord.Client();
const token = process.env.token;
const prefix = '&&';


bot.login(token);

//Boucle pour le statut Discord du bot :
bot.on("ready", () => {
    bot.user.setActivity(`Regarde le monde partir en steak.`);
});

//Boucle contenant les commandes :
bot.on("message", async message => {

const args = message.content.slice(prefix.length).trim().split(/ +/g); 
const command = args.shift().toLowerCase();

//Catégorie "Jeux" :

    //Commande pour faire un pile ou face [&&pile/&&face]:
        {
            function random(min, max){
                min = Math.ceil(1);  //C'est le minimum qu'il peut choisir.
                max = Math.floor(3); //C'est le maximum qu'il peut choisir.
                randnum = Math.floor(Math.random() * (max - min +1) +min); //On définit le randnum : en gros, chaque random est numéroté.
            }
        if(message.content.startsWith(prefix + "pile")) {
            random();  //On initialise le random.        
                if (randnum == 1){ //Chaque nouveau random est numéroté comme ça.
                    message.reply("Et tu tombes sur pile, c'est gagné !"); //Le message que tu envoies. (Réponse du bot, quoi.)
                }
                if (randnum == 2){   //idem
                    message.reply("Tu es tombé sur face, pas de CHANCE.");
                }
                if (randnum == 3){   //J'avais collé ça dans ma version sur calculatrice... xD
                    message.reply("Euh, la pièce est restée sur la tranche...");
                }
            }} 

        {
            function random(min, max){
                min = Math.ceil(1);
                max = Math.floor(3);
                randnum = Math.floor(Math.random() * (max - min +1) +min);
                }
    if(message.content.startsWith(prefix + "face")) {
        random(); 
            if (randnum == 1){
                message.reply("Et tu tombes sur face, c'est gagné !");
            }
            if (randnum == 2){
                message.reply("Tu es tombé sur pile, pas de CHANCE.");
            }
            if (randnum == 3){
                message.reply("Euh, la pièce est restée sur la tranche...");
        }
    }}

    //Commande pour faire un Either.io sur Discord. [&&either] :
    if(message.content.startsWith(prefix + "either")) {
        var either_list = [
            `:regional_indicator_a: ...être chauve ?
ou
:b: ...être manchot ?`,
            `:regional_indicator_a: ...le RisiBot ?
ou
:b: ... Kagura ?`
        ];

        var either = either_list[Math.floor(Math.random() * facts_list.length)];
        var either_embed = new Discord.RichEmbed()
        .setColor('RANDOM')
        .setTitle("**Est-ce que tu préfères...**")
        .setDescription(either)
        .addFooter("Répondre avec les réactions :regional_indicator_a: ou :b:.")
        .setTimestamp()
        message.channel.send(either)
        .then(function(message){
        message.react("✔")
        message.react("✖")  
        });
    }

//Catégorie "Divers" :

    //Commande temporaire pour troll. [&&boobs] :
        if(message.content.startsWith(prefix + "boobs")) {
            var boobs = new Discord.RichEmbed()
            .setColor('RANDOM')
            .setImage("https://media.discordapp.net/attachments/382605587034144778/637796109208518678/Blank_84137de241bbb5d823d4a467c98f0ca8.gif")
            message.channel.send(boobs);
        };

    //Commande de faux hacks. [&&hack <user>] :
        if(message.content.startsWith(prefix + "hack")) {
        
            let member = message.mentions.members.first();
            if(!member)
            return message.reply("Si tu ne mentionne pas un utilisateur valide, je ne risque pas de faire grand chose.");
 
            var fake_hacks_list = [
                "J'avais la flemme de hack ce type, en fait...",
                "T'as vraiment cru que j'étais un bot de hacking, couillon ?!",
                "Euh... t'aimerais pas savoir ce que j'ai trouvé sur cette personne, en fait...",
                "Sainte mère de Dieu, il en a au moins pour 4 Go de lolicons sur son PC !"
            ];

            var fake_hack = fake_hacks_list[Math.floor(Math.random() * fake_hacks_list.length)];
            const troll_hack = await message.channel.send(`_Connerie en cours. Veuillez patienter._
            → **---------- __0%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●--------- __10%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●-------- __20%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●------- __30%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●------ __40%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●●----- __50%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●●●---- __60%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●●●●--- __69%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●●●●●-- __80%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●●●●●●- __90%__**`);
            troll_hack.edit(`_Connerie en cours. Veuillez patienter._
            → **●●●●●●●●●● __100%__**`);
            troll_hack.edit(`_Voyons voir ce que ça donne..._`);
            troll_hack.edit(fake_hack);
        }

    //Commande pour afficher des Chuck Norris facts au hasard. [&&chucknorrisfact] :
        
        if(message.content.startsWith(prefix + "chucknorrisfact")) {
           
            var facts_list = [
                "Chuck Norris a déjà compté jusqu'à l'infini deux fois.",
                "La Mort se demande souvent ce qu'il y a après Chuck Norris",
                "Les extraterrestres ont peur de se faire capturer par Chuck Norris.",
                "Les suisses ne sont pas neutres. Ils attendent juste de savoir de quel côté est Chuck Norris.",
                "Quand il était petit, Chuck Norris n'envoyait pas de lettre au Père Noël. Il lui envoyait des ultimatums.",
                "Chuck Norris est né dans une maison en rondins qu'il a construite lui-même.",
                "Chuck Norris n'a pas de père. Personne ne nique la mère de Chuck Norris !",
                "Si Chuck Norris n'existait pas, il s'inventerait.",
                "Chuck Norris peut claquer une porte fermée.",
                "Un jour, Chuck Norris a balancé une grenade sur 12 personnes, et les 12 personnes sont mortes. Puis la grenade a explosé après.",
                "Quand Chuck Norris joue à Pile ou face, la pièce peut rester sur la tranche...",
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
                "Les petits enfants portent des pyjamas Super Man. Super Man porte des pyjamas Chuck Norris.",
                "Chuck Norris est la raison pour laquelle Charlie se cache.",
                "La Lune tourne autour de la Terre pour échapper au regard de Chuck Norris.",
                "Chuck Norris peut tirer une balle de fusil à mains nues.",
                "Chuck Norris envoie ses e-mails par la Poste.",
                "Chuck Norris regarde la télé avec sa radio.",
                "Chuck Norris a inventé le lance-flammes en pissant sur un briquet."
            ];

            var chucknorrisfact = facts_list[Math.floor(Math.random() * facts_list.length)];
            message.channel.send(chucknorrisfact);
        }

    //Commande pour faire dire quelque chose au bot. [&&say] :
        if(message.content.startsWith(prefix + "say")) {
            const sayMessage = args.join(" ");
            message.delete().catch(O_o=>{}); 
            message.channel.send(sayMessage);
        }

//Catégorie "Informations" :

    //Commande pour afficher la liste des commandes disponibles du bot. [&&help]
        if(message.content.startsWith(prefix + "help")) {
            var help = new Discord.RichEmbed()
            .setColor('RANDOM')
            .setTitle('Liste des commandes disponibles pour le RisiBot ! :')    
            .setDescription(`**__Informations :__**
            ● **&&help** _(Pour afficher la liste de toutes les commandes.)_

            **__Stickers :__**
            ● **&&reverse** _(Quand t'as besoin d'une reverse card bien placée parce que tu as la flemme d'avoir une bonne répartie.)_
            ● **&&respect** _(Quand tu sens que le respect est mort et que tu veux l'exprimer en beauté.)_

            **__Jeux :__**
            ● **&&pile / &&face** _(Pour jouer à Pile ou face.)_

            **__Divers :__**
            ● **&&chucknorrisfact** _(Pour afficher un Chuck Norris fact et en apprendre plus sur l'entité la plus puissante de l'univers.)_
            ● **&&say <texte>** _(Pour faire dire des conneries au bot.)_`)
            .setFooter("Cette liste n'est pas complète pour le moment. Elle s'agrandira a fur et à mesure du développement du bot.")
            message.channel.send(help);
        };
    //Commande de ping. [&&ping] :
        if(message.content.startsWith(prefix + "ping")) {
            message.channel.send(`Ping de \` ${new Date().getTime() - message.createdTimestamp} \` ms. \nAPI Latence de \` ${Math.round(bot.ping)} \` ms.`);
            }

//Catégorie "Stickers" :

    //Commande pour afficher une reverse card dans le salon. [&&reverse] :
        if(message.content.startsWith(prefix + "reverse")) {
            var reverse = new Discord.RichEmbed()  //C'est le nom de l'embed, et chaque embed doit en avoir un distinct.
            .setColor('RANDOM')
            .setImage("https://cdn.discordapp.com/attachments/389333591575756803/630076056824446976/yXEiYQ4.png") //Tu as aussi .setTumbnail(" ") pour mettre l'image en mode portrait, en petit.
            message.channel.send(reverse);
        }; 

    //Commande pour afficher un meme sur le manque de respect. [&&respect] :
        if(message.content.startsWith(prefix + "respect")) {
            var respect_links = [
                "https://cdn.discordapp.com/attachments/576854376451407873/639983272528707588/telechargement.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639964529031118879/Faut_retrouver_le_respect.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639919162545930271/18194982_2112951462264918_8985794969497464227_n.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639983266207760384/images_1.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639983269009555486/images.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639983264907657236/d6s9WS6z_400x400.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639983261296230446/1405.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639983256871239711/images_2.jpg",
                "https://cdn.discordapp.com/attachments/576854376451407873/639990280614969346/Alerte_Respect_Dispary.jpg"
            ];
        
            var respect_images = respect_links[Math.floor(Math.random() * respect_links.length)];
            var respect_embed = new Discord.RichEmbed()
            .setColor('RANDOM')
            .setImage(respect_images)
            message.channel.send(respect_embed);
        };
});
