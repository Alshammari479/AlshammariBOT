import discord
from discord.ext import commands
from discord import app_commands
import datetime

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}  # {user_id: count}

    @app_commands.command(name="ban", description="حظر عضو من السيرفر")
    @app_commands.describe(member="العضو المراد حظره", reason="السبب")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("❌ ليس لديك صلاحيات الحظر", ephemeral=True)
            return
        
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="✅ تم الحظر",
                description=f"تم حظر {member.mention}\n**السبب:** {reason}",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ خطأ: {str(e)}", ephemeral=True)

    @app_commands.command(name="kick", description="طرد عضو من السيرفر")
    @app_commands.describe(member="العضو المراد طرده", reason="السبب")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("❌ ليس لديك صلاحيات الطرد", ephemeral=True)
            return
        
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="✅ تم الطرد",
                description=f"تم طرد {member.mention}\n**السبب:** {reason}",
                color=discord.Color.orange()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ خطأ: {str(e)}", ephemeral=True)

    @app_commands.command(name="timeout", description="إيقاف مؤقت لعضو")
    @app_commands.describe(member="العضو", minutes="عدد الدقائق", reason="السبب")
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, minutes: int, reason: str = "بدون سبب"):
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("❌ ليس لديك الصلاحيات", ephemeral=True)
            return
        
        try:
            duration = datetime.timedelta(minutes=minutes)
            await member.timeout(duration, reason=reason)
            embed = discord.Embed(
                title="⏱️ إيقاف مؤقت",
                description=f"تم إيقاف {member.mention} لمدة {minutes} دقيقة\n**السبب:** {reason}",
                color=discord.Color.yellow()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ خطأ: {str(e)}", ephemeral=True)

    @app_commands.command(name="warn", description="تحذير عضو")
    @app_commands.describe(member="العضو", reason="السبب")
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("❌ ليس لديك الصلاحيات", ephemeral=True)
            return
        
        self.warnings[member.id] = self.warnings.get(member.id, 0) + 1
        count = self.warnings[member.id]
        
        embed = discord.Embed(
            title="⚠️ تحذير",
            description=f"تم تحذير {member.mention}\n**السبب:** {reason}\n**التحذيرات:** {count}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="clear", description="حذف رسائل من القناة")
    @app_commands.describe(count="عدد الرسائل")
    async def clear(self, interaction: discord.Interaction, count: int):
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("❌ ليس لديك الصلاحيات", ephemeral=True)
            return
        
        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=count)
        await interaction.followup.send(f"✅ تم حذف {len(deleted)} رسالة")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
