import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class LoggingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channels = {}  # {guild_id: channel_id}

    @app_commands.command(name="setup_logs", description="تعيين قناة اللوق")
    @app_commands.describe(channel="قناة اللوق")
    async def setup_logs(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ ليس لديك صلاحيات", ephemeral=True)
            return
        
        self.log_channels[interaction.guild.id] = channel.id
        
        embed = discord.Embed(
            title="✅ تم التعيين",
            description=f"تم تعيين {channel.mention} كقناة اللوق",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    def get_log_channel(self, guild):
        if guild.id in self.log_channels:
            return guild.get_channel(self.log_channels[guild.id])
        return None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = self.get_log_channel(member.guild)
        if not log_channel:
            return
        
        embed = discord.Embed(
            title="👋 عضو دخل",
            description=f"{member.mention} دخل السيرفر",
            color=discord.Color.green()
        )
        embed.add_field(name="الاسم", value=member.name)
        embed.add_field(name="الـ ID", value=member.id)
        embed.add_field(name="التوقيت", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_thumbnail(url=member.avatar.url)
        
        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = self.get_log_channel(member.guild)
        if not log_channel:
            return
        
        embed = discord.Embed(
            title="👤 عضو خرج",
            description=f"{member.mention} ترك السيرفر",
            color=discord.Color.red()
        )
        embed.add_field(name="الاسم", value=member.name)
        embed.add_field(name="الـ ID", value=member.id)
        embed.add_field(name="التوقيت", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_thumbnail(url=member.avatar.url)
        
        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        
        log_channel = self.get_log_channel(message.guild)
        if not log_channel:
            return
        
        embed = discord.Embed(
            title="🗑️ رسالة محذوفة",
            description=f"**المُرسل:** {message.author.mention}\n**المحتوى:** {message.content[:100]}",
            color=discord.Color.orange()
        )
        embed.add_field(name="القناة", value=message.channel.mention)
        embed.add_field(name="التوقيت", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        
        if before.content == after.content:
            return
        
        log_channel = self.get_log_channel(before.guild)
        if not log_channel:
            return
        
        embed = discord.Embed(
            title="✏️ رسالة معدلة",
            description=f"**المُرسل:** {before.author.mention}",
            color=discord.Color.blue()
        )
        embed.add_field(name="قبل", value=before.content[:100], inline=False)
        embed.add_field(name="بعد", value=after.content[:100], inline=False)
        embed.add_field(name="القناة", value=before.channel.mention)
        embed.add_field(name="التوقيت", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LoggingCog(bot))
