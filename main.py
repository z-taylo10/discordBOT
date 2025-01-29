import discord
import os
import asyncio
from discord.ext import tasks

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", "1334224905553576030"))
ROLE_ID = int(os.getenv("ROLE_ID", "1334231259257507892"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID", "1334235802724466854"))
EMOJI = "✅"

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True

class VerificationBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.keep_alive.start()

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    @tasks.loop(minutes=5)  # Run every 5 minutes
    async def keep_alive(self):
        print("Bot is still running...")  # This will help keep the bot active

    async def on_raw_reaction_add(self, payload):
        print(f"Reaction detected: {payload.emoji}")  # Debug log
        if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
            print(f"Correct message and emoji")  # Debug log
            guild = self.get_guild(GUILD_ID)
            if guild:
                print(f"Guild found: {guild.name}")  # Debug log
                member = guild.get_member(payload.user_id)
                if member:
                    print(f"Member found: {member.name}")  # Debug log
                    role = guild.get_role(ROLE_ID)
                    if role:
                        print(f"Role found: {role.name}")  # Debug log
                        try:
                            await member.add_roles(role)
                            print(f"Added {role.name} to {member.name}")
                        except Exception as e:
                            print(f"Error adding role: {e}")  # Debug log
                    else:
                        print("Role not found")  # Debug log
                else:
                    print("Member not found")  # Debug log
            else:
                print("Guild not found")  # Debug log

bot = VerificationBot()

if __name__ == '__main__':
    bot.run(TOKEN)
