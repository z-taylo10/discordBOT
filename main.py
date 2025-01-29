import discord
from discord.ext import tasks
from config import TOKEN, GUILD_ID, ROLE_ID, MESSAGE_ID

EMOJI = "✅"

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True

class VerificationBot(discord.Client):
    async def setup_hook(self):
        self.keep_alive.start()

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    @tasks.loop(minutes=5)
    async def keep_alive(self):
        print("Bot is still running...")

    async def on_raw_reaction_add(self, payload):
        print(f"Reaction detected: {payload.emoji}")
        if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
            print(f"Correct message and emoji")
            guild = self.get_guild(GUILD_ID)
            if guild:
                print(f"Guild found: {guild.name}")
                member = guild.get_member(payload.user_id)
                if member:
                    print(f"Member found: {member.name}")
                    role = guild.get_role(ROLE_ID)
                    if role:
                        print(f"Role found: {role.name}")
                        try:
                            await member.add_roles(role)
                            print(f"Added {role.name} to {member.name}")
                        except Exception as e:
                            print(f"Error adding role: {e}")
                    else:
                        print("Role not found")
                else:
                    print("Member not found")
            else:
                print("Guild not found")

bot = VerificationBot(intents=intents)

if __name__ == '__main__':
    bot.run(TOKEN)
