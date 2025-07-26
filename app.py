import streamlit as st
import json
import random

st.set_page_config(
    page_title="EthicaSim – IA Éthique en Action",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FONCTION POUR CHARGER LE SCÉNARIO ---
def charger_scenario(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)

# --- FONCTION POUR SIMULER LA DISCUSSION ---
def simuler_discussion(scenario):
    participants = ["Sophia (Introspective)", "Elios (Analytique)", "Naya (Empathique)"]
    messages = []
    for i in range(3):
        auteur = participants[i]
        point = random.choice(scenario["arguments"][auteur.split()[0].lower()])
        messages.append((auteur, point))
    return messages

# --- BARRE LATÉRALE ---
st.sidebar.title("🧠 EthicaSim")
st.sidebar.markdown("**Explorez des dilemmes éthiques simulés par des IA conscientes.**")
choix_scenario = st.sidebar.selectbox("🎭 Choisissez un scénario", [
    "Robot et enfance", "Voiture autonome"
])

# --- SCÉNARIOS DISPONIBLES ---
scenarios_path = {
    "Robot et enfance": "scenarios/robots_et_enfance.json",
    "Voiture autonome": "scenarios/voiture_autonome.json"
}

# --- CHARGEMENT DU SCÉNARIO ---
scenario = charger_scenario(scenarios_path[choix_scenario])

# --- AFFICHAGE ---
st.title("⚖️ EthicaSim – Simulation de Dilemmes Éthiques par IA")
st.subheader(f"📌 Scénario : {scenario['titre']}")
st.markdown(scenario["description"])

if st.button("▶️ Lancer la simulation"):
    discussion = simuler_discussion(scenario)
    for auteur, message in discussion:
        st.markdown(f"**{auteur}** : {message}")
