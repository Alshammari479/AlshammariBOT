import discord
from discord.ext import commands
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="عرض جميع الأوامر")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🤖 أوامر AlshammariBOT",
            description="قائمة بجميع الأوامر المتاحة",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📋 الأوامر العامة",
            value="`/help` - عرض هذه الرسالة\n`/setup` - إعداد البوت",
            inline=False
        )
        
        embed.add_field(
            name="🛡️ أوامر الإدارة",
            value="`/ban` - حظر عضو\n`/kick` - طرد عضو\n`/timeout` - إيقاف مؤقت\n`/warn` - تحذير\n`/clear` - حذف رسائل",
            inline=False
        )
        
        embed.add_field(
            name="🎫 نظام التذاكر",
            value="`/create_ticket` - إنشاء تذكرة\n`/close_ticket` - إغلاق تذكرة",
            inline=False
        )
        
        embed.set_footer(text="AlshammariBOT © 2024")
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
