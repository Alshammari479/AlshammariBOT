import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class AnnouncementsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.announcement_channels = {}  # {guild_id: channel_id}

    @app_commands.command(name="setup_announcements", description="تعيين قناة الإعلانات")
    @app_commands.describe(channel="قناة الإعلانات")
    async def setup_announcements(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ ليس لديك صلاحيات", ephemeral=True)
            return
        
        self.announcement_channels[interaction.guild.id] = channel.id
        
        embed = discord.Embed(
            title="✅ تم التعيين",
            description=f"تم تعيين {channel.mention} كقناة الإعلانات",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="announce", description="إرسال إعلان")
    @app_commands.describe(title="عنوان الإعلان", message="محتوى الإعلان")
    async def announce(self, interaction: discord.Interaction, title: str, message: str):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ ليس لديك صلاحيات",
                ephemeral=True
            )
            return
        
        if interaction.guild.id not in self.announcement_channels:
            await interaction.response.send_message(
                "❌ لم يتم تعيين قناة الإعلانات بعد",
                ephemeral=True
            )
            return
        
        channel_id = self.announcement_channels[interaction.guild.id]
        channel = interaction.guild.get_channel(channel_id)
        
        if not channel:
            await interaction.response.send_message(
                "❌ قناة الإعلانات غير متاحة",
                ephemeral=True
            )
            return
        
        embed = discord.Embed(
            title=f"📢 {title}",
            description=message,
            color=discord.Color.red()
        )
        embed.add_field(name="بواسطة", value=interaction.user.mention)
        embed.add_field(name="التاريخ", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else "")
        
        await channel.send(embed=embed)
        
        await interaction.response.send_message(
            "✅ تم إرسال الإعلان بنجاح",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(AnnouncementsCog(bot))
