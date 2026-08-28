import discord
from discord.ext import commands
from discord import app_commands

class TicketsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tickets = {}  # {guild_id: {ticket_id: info}}

    @app_commands.command(name="create_ticket", description="إنشاء تذكرة جديدة")
    @app_commands.describe(subject="موضوع التذكرة")
    async def create_ticket(self, interaction: discord.Interaction, subject: str):
        guild = interaction.guild
        
        # إنشاء روم التذكرة
        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            topic=f"التذكرة من: {interaction.user.mention}"
        )
        
        embed = discord.Embed(
            title="🎫 تذكرة جديدة",
            description=f"**الموضوع:** {subject}\n**المُنشئ:** {interaction.user.mention}",
            color=discord.Color.blue()
        )
        
        await ticket_channel.send(embed=embed)
        
        close_button = discord.ui.Button(label="إغلاق التذكرة", style=discord.ButtonStyle.danger)
        
        async def close_callback(button_interaction: discord.Interaction):
            await ticket_channel.delete()
        
        close_button.callback = close_callback
        view = discord.ui.View()
        view.add_item(close_button)
        
        await ticket_channel.send("اضغط الزر لإغلاق التذكرة:", view=view)
        
        await interaction.response.send_message(f"✅ تم إنشاء التذكرة: {ticket_channel.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(TicketsCog(bot))
