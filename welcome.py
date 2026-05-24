import requests

MY_TOKEN = os.environ.get("TELEGRAM_TOKEN")
MY_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")"

# שימוש בתגיות HTML נקיות כדי למנוע בעיות תווים בטלגרם
welcome_message = (
    "<b>📢 BIENVENUE SUR IMMOALERTS ISRAËL ! 🎯</b>\n\n"
    "Vous cherchez les meilleures opportunités immobilières en Israël sans perdre de temps ? Vous êtes au bon endroit.\n\n"
    "Ce canal utilise un algorithme d'automatisation avancé pour scanner en temps réel le marché immobilier israélien (basé sur les données officielles du Tabu et du Registre Foncier).\n\n"
    "<b>📍 Notre Mission :</b> Détecter instantanément les appartements vendus en dessous du prix moyen du marché dans les zones les plus recherchées par la communauté francophone : <b>Netanya, Ashdod, Tel Aviv et Jérusalem.</b>\n\n"
    "<b>💡 Pourquoi nous suivre ?</b>\n"
    "• ⚡ <b>100% Automatique :</b> Des alertes claires et immédiates, directement sur votre téléphone.\n"
    "• 📜 <b>Données Officielles :</b> Pas de spéculation ni de rumeurs, uniquement de vrais prix de clôture certifiés.\n"
    "• 🎯 <b>Rapidité Maximale :</b> Soyez le premier informé des opportunités exclusives avant qu'elles ne quittent le marché.\n\n"
    "📈 <i>Rejoignez notre communauté d'investisseurs et ne ratez plus jamais la bonne affaire !</i>"
)

url = f"https://api.telegram.org/bot{MY_TOKEN}/sendMessage"
# שינוי ה-parse_mode ל-HTML
payload = {"chat_id": MY_CHAT_ID, "text": welcome_message, "parse_mode": "HTML"}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("SUCCESS: The Bot has posted the welcome message to the channel!")
    else:
        print(f"FAILED: {response.text}")
except Exception as e:
    print(f"ERROR: {e}")
