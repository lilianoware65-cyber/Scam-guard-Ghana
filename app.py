# Scam Guard Ghana - By Dreama
# Detects MoMo fraud in Ghana

def check_scam(message):
    message = message.lower()
    scam_words = ["you have won", "send momo", "urgent", "blocked account", "verify your pin", "lottery", "prince", "giveaway", "claim now", "momo agent"]
    score = 0
    for word in scam_words:
        if word in message:
            score += 1
    if score >= 2:
        return "🚨 SCAM! This is 99% fraud. Do NOT send money!"
    elif score == 1:
        return "⚠️ SUSPICIOUS! Be careful, this looks like scam."
    else:
        return "✅ SAFE! Looks okay, but still be careful."

# Test it
print(check_scam("You have won 5000gh, send momo to claim"))
print(check_scam("Hello how are you"))
  
