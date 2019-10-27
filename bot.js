//Pas touche aux premières constantes. Sinon, ça va moins bien marcher.
const Discord = require('discord.js');
const bot = new Discord.Client();
const token = process.env.token;
const prefix = '&';

bot.login(token);


bot.on("message", async message => {

//Catégorie "Divers" :

    //Commande pour faire un pile ou face :
    const args = message.content.slice(prefix.length).trim().split(/ +/g); 
    const command = args.shift().toLowerCase();
        {
            function random(min, max){
                min = Math.ceil(1);  //C'est le minimum qu'il peut choisir.
                max = Math.floor(3); //C'est le maximum qu'il peut choisir.
                randnum = Math.floor(Math.random() * (max - min +1) +min); //On définit le randnum : en gros, chaque random est numéroté.
            }
        if(command === "pile") {
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
        if(command === "face") {
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

    //Commande pour afficher une reverse card dans le salon. [&reverse] :
    if (command === "reverse") {
            var reverse = new Discord.RichEmbed()  //C'est le nom de l'embed, et chaque embed doit en avoir un distinct.
            .setColor('RANDOM')  
            .setImage("https://cdn.discordapp.com/attachments/389333591575756803/630076056824446976/yXEiYQ4.png")    //Tu as aussi .setTumbnail(" ") pour mettre l'image en mode portrait, en petit.
            message.channel.send(reverse);
        }; 

    //Commande temporaire pour troll. [&boobs] :
    if (command === "boobs") {
        var boobs = new Discord.RichEmbed()
        .setColor('RANDOM')  
        .setImage("https://media.discordapp.net/attachments/382605587034144778/637796109208518678/Blank_84137de241bbb5d823d4a467c98f0ca8.gif")
        message.channel.send(boobs);
    };

    //Commande pour afficher des Chuck Norris facts au hasard. [&chucknorrisfact] :
    {
        function random(min, max){
            min = Math.ceil(1);
            max = Math.floor(4);
            randnum = Math.floor(Math.random() * (max - min +1) +min);
        }
    if(command === "chucknorrisfact") {
    random();
        if (randnum == 1){
            message.channel.send("Chuck Norris peut claquer une porte fermée.");
        }
        if (randnum == 2){
            message.channel.send("Un jour, Chuck Norris a balancé une grenade sur 12 personnes, et les 12 personnes sont mortes. Puis la grenade a explosé après.");
        }
        if (randnum == 3){
            message.channel.send("Quand Chuck Norris joue à Pile ou face, la pièce peut rester sur la tranche...");
        if (randnum == 4){
            message.channel.send("Chuck Norris peut t'étrangler avec le fil d'un téléphone sans fil.")
        }
        }
    }} 

    //Commande pour faire dire quelque chose au bot. [&say] :
    if(command === "say") {
    const sayMessage = args.join(" ");
        message.delete().catch(O_o=>{}); 
        message.channel.send(sayMessage);
      }

});
