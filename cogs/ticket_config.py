# Ticket Settings Configuration
# Format: {guild_id: {settings}}

ticket_settings = {
    # Example configuration
    # guild_id: {
    #     "title": "Support Tickets",
    #     "description": "Select a ticket type to create a support ticket",
    #     "image": "https://example.com/image.png",
    #     "category": channel_id,  # Category ID for tickets
    #     "options": [
    #         {
    #             "label": "General Support",
    #             "description": "For general questions",
    #             "emoji": "❓"
    #         },
    #         {
    #             "label": "Bug Report",
    #             "description": "Report a bug",
    #             "emoji": "🐛"
    #         },
    #         {
    #             "label": "Feature Request",
    #             "description": "Suggest a new feature",
    #             "emoji": "✨"
    #         }
    #     ]
    # }
}

def add_ticket_settings(guild_id, settings):
    """Add or update ticket settings for a guild"""
    ticket_settings[guild_id] = settings

def get_ticket_settings(guild_id):
    """Get ticket settings for a guild"""
    return ticket_settings.get(guild_id)

def remove_ticket_settings(guild_id):
    """Remove ticket settings for a guild"""
    if guild_id in ticket_settings:
        del ticket_settings[guild_id]
