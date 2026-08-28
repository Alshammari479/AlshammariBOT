import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class RegistrationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.registrations = {}  # {user_id: {step, data}}
        self.registration_channels = {}  # {guild_id: channel_id}

    @app_commands.command(name="setup_registration", description="تعيين قناة التسجيل")
    @app_commands.describe(channel="قناة التسجيل")
    async def setup_registration(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ ليس لديك صلاحيات", ephemeral=True)
            return
        
        self.registration_channels[interaction.guild.id] = channel.id
        
        embed = discord.Embed(
            title="✅ تم التعيين",
            description=f"تم تعيين {channel.mention} كقناة التسجيل",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="register", description="التسجيل في السيرفر")
    async def register(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        
        # البيانات المطلوبة
        modal = RegisterModal()
        await interaction.response.send_modal(modal)
        
        await interaction.followup.send(
            "✅ تم فتح نموذج التسجيل. يرجى ملء البيانات.",
            ephemeral=True
        )

class RegisterModal(discord.ui.Modal, title="📋 نموذج التسجيل"):
    name = discord.ui.TextInput(
        label="الاسم الكامل",
        placeholder="أدخل اسمك الكامل",
        required=True
    )
    age = discord.ui.TextInput(
        label="العمر",
        placeholder="أدخل عمرك",
        required=True
    )
    country = discord.ui.TextInput(
        label="الدولة",
        placeholder="أدخل دولتك",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="✅ تم التسجيل بنجاح",
            description=f"مرحباً {self.name.value}!",
            color=discord.Color.green()
        )
        embed.add_field(name="الاسم", value=self.name.value)
        embed.add_field(name="العمر", value=self.age.value)
        embed.add_field(name="الدولة", value=self.country.value)
        embed.add_field(name="التاريخ", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
        # إرسال ملخص للمسؤولين
        if interaction.guild.id in [cog.registration_channels for cog in interaction.client.cogs.values() if hasattr(cog, 'registration_channels')]:
            # يمكن إضافة إرسال للقناة المعينة
            pass

async def setup(bot):
    await bot.add_cog(RegistrationCog(bot))
