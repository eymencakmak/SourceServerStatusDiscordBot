import discord
from discord.ext import commands
import a2s
import time
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def format_duration(seconds):
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

@bot.event
async def on_ready():
    print(f"✅ Bot is running: {bot.user}")

@bot.command()
async def server(ctx, ipport: str):
    try:
        await ctx.message.delete()

        ip, port = ipport.split(":")
        port = int(port)
    except:
        await ctx.send("❌ Please use the correct format: `!server IP:PORT` (example: `!server 31.56.0.10:27015`)")
        return

    if hasattr(bot, 'last_message') and bot.last_message is not None:
        try:
            await bot.last_message.delete()
        except:
            pass

    async def create_embed():
        try:
            start = time.time()
            info = a2s.info((ip, port))
            players = a2s.players((ip, port))
            ping = round((time.time() - start) * 1000)

            embed = discord.Embed(
                title=f"{info.server_name}",
                description=(
                    f"🗺️ Map: `{info.map_name}`\n"
                    f"👥 Players: `{info.player_count}/{info.max_players}`\n"
                    f"🌐 IP: `{ip}:{port}`\n"
                    f"📶 Ping: `{ping} ms`"
                ),
                color=0x00ff00
            )

            if players:
                player_list = ""
                for p in players:
                    name = p.name or "[No Name]"
                    duration = format_duration(p.duration)
                    line = f"• `{name}` – 🎮 {duration}\n"
                    if len(player_list) + len(line) > 1000:
                        break
                    player_list += line
                embed.add_field(name="🎮 Player List", value=player_list or "Could not load players", inline=False)
            else:
                embed.add_field(name="🎮 Player List", value="No players on the server.", inline=False)

            return embed

        except Exception as e:
            return discord.Embed(
                title="❌ Error Occurred",
                description=f"`{e}`",
                color=0xff0000
            )

    try:
        message = await ctx.send(embed=await create_embed())
        bot.last_message = message

        while True:
            await asyncio.sleep(10)
            try:
                await message.edit(embed=await create_embed())
            except Exception as e:
                print(f"Update error: {e}")
                break

    except Exception as e:
        await ctx.send(f"❌ An error occurred during the process: `{e}`")

bot.run("ENTER_TOKEN_HERE")
