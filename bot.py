import json
import discord
from discord.utils import get
from discord.ext import commands
import arrow

name_to_unicode = {
    ":regional_indicator_a:": "\U0001F1E6",
    ":regional_indicator_b:": "\U0001F1E7",
    ":regional_indicator_c:": "\U0001F1E8",
    ":regional_indicator_d:": "\U0001F1E9",
    ":regional_indicator_e:": "\U0001F1EA",
    ":regional_indicator_f:": "\U0001F1EB",
    ":regional_indicator_g:": "\U0001F1EC",
    ":regional_indicator_h:": "\U0001F1ED",
    ":regional_indicator_i:": "\U0001F1EE",
    ":regional_indicator_j:": "\U0001F1EF",
    ":regional_indicator_k:": "\U0001F1F0",
    ":regional_indicator_l:": "\U0001F1F1",
    ":regional_indicator_m:": "\U0001F1F2",
    ":regional_indicator_n:": "\U0001F1F3",
    ":regional_indicator_o:": "\U0001F1F4",
    ":regional_indicator_p:": "\U0001F1F5",
    ":regional_indicator_q:": "\U0001F1F6",
    ":regional_indicator_r:": "\U0001F1F7",
    ":regional_indicator_s:": "\U0001F1F8",
    ":regional_indicator_t:": "\U0001F1F9",
    ":regional_indicator_u:": "\U0001F1FA",
    ":regional_indicator_v:": "\U0001F1FB",
    ":regional_indicator_w:": "\U0001F1FC",
    ":regional_indicator_x:": "\U0001F1FD",
    ":regional_indicator_q:": "\U0001F1FE",
    ":regional_indicator_z:": "\U0001F1FF"
}


bot = commands.Bot("!")

@bot.command(help="Create a vote.")
async def v(ctx, question, *args):
    author = ctx.message.author.name
    date = str(ctx.message.created_at)
    date = date[:len(date) - 7]

    # 刪掉原本的指令
    await ctx.message.delete()

    question_text = question
    options_text = []
    for arg in args:
        options_text.append(args[0])

    option_num = len(options_text)

    if option_num > 24:
        await ctx.send("你不能問這麼多問題，天啊。")
        return

    reactions = []
    for i in range(option_num):
        character = str(chr(ord('a') + i))
        reactions.append(f":regional_indicator_{character}:")

    for i in range(option_num):
        options_text[i] = f"{reactions[i]}：{options_text[i]}"
    
    des = ""
    for option in options_text:
        des += f"> {option}\n"

    embed = discord.Embed(
        title=question_text,
        description=des,
        color=discord.Color.blue())

    embed.set_footer(text=f"（這個問題由{author}在{date}時提出）")

    poll = await ctx.send(embed=embed)

    for react in reactions:
        try:
            await poll.add_reaction(name_to_unicode[react])
        except ex:
            print(ex)


with open("setting.json") as setting:
    text = setting.read()
    json_data = json.loads(text)
    token = json_data["token"]
    bot.run(token)
