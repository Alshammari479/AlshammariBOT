import discord
from discord.ext import commands
from discord import app_commands

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channels = {}  # {guild_id: channel_id}

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        
        if guild.id not in self.welcome_channels:
            return
        
        channel_id = self.welcome_channels[guild.id]
        channel = guild.get_channel(channel_id)
        
        if channel:
            embed = discord.Embed(
                title="👋 أهلاً وسهلاً!",
                description=f"مرحباً بك {member.mention} في سيرفرنا!",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="الأعضاء الآن", value=f"{guild.member_count}", inline=False)
            
            await channel.send(embed=embed)

    @app_commands.command(name="setup_welcome", description="تعيين قناة الترحيب")
    @app_commands.describe(channel="القناة المراد تعيينها")
    async def setup_welcome(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ ليس لديك الصلاحيات", ephemeral=True)
            return
        
        self.welcome_channels[interaction.guild.id] = channel.id
        
        embed = discord.Embed(
            title="✅ تم التعيين",
            description=f"تم تعيين {channel.mention} كقناة الترحيب",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))
