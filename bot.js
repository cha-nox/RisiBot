const Discord = require('discord.js')
const bot = new Discord.Client()
const token = process.env.token;

client.login(token);

bot.on('ready', function () {
console.log("Issou la chancla.")
})
