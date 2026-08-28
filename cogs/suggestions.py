import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class SuggestionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.suggestion_channels = {}  # {guild_id: channel_id}
        self.suggestion_counter = 0

    @app_commands.command(name="setup_suggestions", description="تعيين قناة الاقتراحات")
    @app_commands.describe(channel="قناة الاقتراحات")
    async def setup_suggestions(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ ليس لديك صلاحيات", ephemeral=True)
            return
        
        self.suggestion_channels[interaction.guild.id] = channel.id
        
        embed = discord.Embed(
            title="✅ تم التعيين",
            description=f"تم تعيين {channel.mention} كقناة الاقتراحات",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="suggest", description="إرسال اقتراح")
    @app_commands.describe(suggestion="الاقتراح")
    async def suggest(self, interaction: discord.Interaction, suggestion: str):
        if interaction.guild.id not in self.suggestion_channels:
            await interaction.response.send_message(
                "❌ لم يتم تعيين قناة الاقتراحات بعد",
                ephemeral=True
            )
            return
        
        channel_id = self.suggestion_channels[interaction.guild.id]
        channel = interaction.guild.get_channel(channel_id)
        
        if not channel:
            await interaction.response.send_message(
                "❌ قناة الاقتراحات غير متاحة",
                ephemeral=True
            )
            return
        
        self.suggestion_counter += 1
        
        embed = discord.Embed(
            title=f"💡 اقتراح #{self.suggestion_counter}",
            description=suggestion,
            color=discord.Color.gold()
        )
        embed.add_field(name="المُقترح", value=interaction.user.mention)
        embed.add_field(name="التاريخ", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_thumbnail(url=interaction.user.avatar.url)
        
        msg = await channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        
        await interaction.response.send_message(
            f"✅ تم إرسال اقتراحك برقم #{self.suggestion_counter}",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(SuggestionsCog(bot))
