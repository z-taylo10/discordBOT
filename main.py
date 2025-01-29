import discord
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", "1334224905553576030"))
ROLE_ID = int(os.getenv("ROLE_ID", "1334225373499625492"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID", "1334231259257507892"))
EMOJI = "✅"

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True

class VerificationBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
            guild = self.get_guild(GUILD_ID)
            if guild:
                member = guild.get_member(payload.user_id)
                if member:
                    role = guild.get_role(ROLE_ID)
                    if role:
                        await member.add_roles(role)
                        print(f"Added {role.name} to {member.name}")

bot = VerificationBot(intents=intents)
bot.run(TOKEN)