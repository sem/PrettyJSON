<p align="center">
  <img width="400" alt="Screenshot 2021-09-27 at 21 54 16" src="https://user-images.githubusercontent.com/78478073/137600727-1384d300-c595-4efb-a0a3-87c80c9d0c27.png">
</p>

<p align="center">
<a href="https://discord.com/api/oauth2/authorize?client_id=899018611253989406&permissions=534723950656&scope=bot">Invite PrettyJSON to your Discord server</a>
</p>

# Table of contents
- [About the project](#about-the-project)
  - [What is JSON?](#what-is-json)
  - [What is pretty printing?](#what-is-pretty-printing)
- [How to use](#how-to-use)
  - [Input options](#input-options)
  - [Command](#command)
- [Installation](#installation)
- [How to invite](#how-to-invite)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## About the project
Since programming with other users on the group-chatting platform [Discord](https://discord.com) has become very popular, its use in bots has also increased. Several bots have already been released to make programming together within a community or group easier. For example, we have bots to compile code or to keep track of GitHub commits. Since you can often find yourself in a position where you use JSON data in your code, it could be helpful if this data is neatly formatted, but unfortunately this is not always the case. Usually the easiest way to quickly format your JSON data is by using an online website where you would paste your text and it would format it very nicely for you. With the lazy mindset of mine, I thought that it would be way easier and more convenient if this could be done through a Discord bot as well. And well, here we are.

### What is JSON?
JSON (**JavaScript Object Notation**) is a lightweight data-interchange format. It is easy for humans to read and write, and it's easy for machines to parse and generate. Although JSON is derived from JavaScript, it is supported either natively or through libraries in most major programming languages. JSON is commonly, but not exclusively, used to exchange information between web clients and web servers. It is a generic data format with a minimal number of value types: **strings**, **numbers**, **booleans**, **lists**, **objects**, and **null**.

>**Example:**
>```yaml
>{
>  "firstName": "Sem",
>  "lastName": "Moolenschot",
>  "student": true,
>  "pets": [
>    {
>      "name": "Bo",
>      "type": "Dog"
>    }
>  ]
>}
>```

### What is pretty printing?
Pretty printing is a form of stylistic formatting including indentation and colouring. It's important to have your JSON file formatted so it's easier for humans to read. The only disadvantage of pretty printing your JSON is that the size of the data will slightly increase, but in most cases people choose to have it pretty printed anyway so your data remains easy to read for humans.

>**Example of non-pretty printed JSON:**
>```yaml
>{"firstName": "Sem", "lastName": "Moolenschot", "student": true, "pets": [{"name": "Bo", "type": "Dog"}]}
>```
>
>**Previous example pretty printed using [PrettyJSON](https://discord.com/api/oauth2/authorize?client_id=899018611253989406&permissions=534723950656&scope=bot):**
>```yaml
>{
>  "firstName": "Sem",
>  "lastName": "Moolenschot",
>  "student": true,
>  "pets": [
>    {
>      "name": "Bo",
>      "type": "Dog"
>    }
>  ]
>}
>```

## How to use
There are a few different ways to give the bot your non-pretty printed JSON as input. Once the input is received by the bot, it will be pretty printed and sent back to the user. Keep in mind that if you pretty print JSON via a message you are dealing with a 2000 character limit, unless you have a Discord Nitro membership then this limit will be 4000.

### Input options:
- TXT files
- JSON files
- JSON URL
- Message

### Command:
- ``.pprint`` *input*

> **Example of a message as input:**
> <p align="left">
> <img width="455" alt="Screenshot 2021-10-17 at 21 39 39" src="https://user-images.githubusercontent.com/78478073/137642487-8f5f170b-0dcd-448a-8673-e905966efe0f.png">
> </p>
>
> **Example of a JSON file as input:**
> <p align="left">
> <img width="455" alt="Screenshot 2021-10-17 at 21 39 39" src="https://user-images.githubusercontent.com/78478073/137642847-cdab4e31-7e25-42dc-8dc3-71ba48625bcc.gif">
> </p>
> 
> If the output has less than 2000 characters, it will be sent back as text and a ``📁`` reaction will be added to the message. If you press this reaction, you will receive the output as a JSON file.

## Installation
If you don't want to host yourself, but wish to use the bot in your Discord server, then please look at [how to invite](#how-to-invite). If you would like to host the bot yourself, then you can check out the following steps. There is a docker image set up so you can run PrettyJSON yourself, here is a link to the [repository](https://hub.docker.com/repository/docker/moolenschot/bot_pretty_json) in case you need it.

1. Make sure you have your Discord application and your bot set up.
2. Go to your terminal and run ```docker run -e TOKEN=OTExNjM3ODk1NzQyMzg2MjS2.YZkS8w.CA8RORyQCaxHHBa7UAigQaVCrX0 -d moolenschot/bot_pretty_json``` *(example token, please make sure to use your own)*
3. Now the image is successfully pulled and being ran, so you're ready to go! 
4. To make sure the image has successfully ran, you can use ```docker ps```.

## How to invite
1. Go to PrettyJSON's [invitation link](https://discord.com/api/oauth2/authorize?client_id=899018611253989406&permissions=534723950656&scope=bot)
2. Select the server where you would like to add the bot
3. Make sure PrettyJSON has the right permissions
4. Authorize

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
sem@moolenschot.nl <br/>
[Reddit](https://www.reddit.com/user/moolenschot) <br/>
[Instagram](https://www.instagram.com/semmoolenschot)

## License
Distributed under the MIT License. See ```LICENSE``` for more information.