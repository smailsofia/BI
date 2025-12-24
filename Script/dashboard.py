import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Configuration de la page
st.set_page_config(page_title="Tableau de Bord Excel", layout="wide", page_icon="📊")

# Titre principal
st.title("📊 Tableau de Bord Analytique - Multi-Fichiers")
st.markdown("---")

# Section d'upload pour les 4 fichiers
st.sidebar.header("📁 Importer vos fichiers Excel")
file_annee = st.sidebar.file_uploader("Fichier ANNEE", type=['xlsx', 'xls'], key="annee")
file_country = st.sidebar.file_uploader("Fichier COUNTRY", type=['xlsx', 'xls'], key="country")
file_customer = st.sidebar.file_uploader("Fichier CUSTOMER", type=['xlsx', 'xls'], key="customer")
file_employee = st.sidebar.file_uploader("Fichier EMPLOYEE", type=['xlsx', 'xls'], key="employee")

# Fonction pour charger les données
def load_data(file):
    if file is not None:
        try:
            return pd.read_excel(file)
        except Exception as e:
            st.error(f"Erreur de lecture: {e}")
            return None
    return None

# Charger tous les fichiers
df_annee = load_data(file_annee)
df_country = load_data(file_country)
df_customer = load_data(file_customer)
df_employee = load_data(file_employee)

# Vérifier si au moins un fichier est chargé
files_loaded = sum([df is not None for df in [df_annee, df_country, df_customer, df_employee]])

if files_loaded > 0:
    st.sidebar.success(f"✅ {files_loaded}/4 fichiers chargés")
else:
    st.sidebar.info("ℹ️ Veuillez importer vos fichiers Excel")

# Afficher un aperçu des données chargées
if files_loaded > 0:
    with st.expander("📋 Aperçu des données chargées"):
        col1, col2 = st.columns(2)
        
        if df_annee is not None:
            with col1:
                st.write("**Fichier ANNEE:**")
                st.dataframe(df_annee.head(), use_container_width=True)
        
        if df_country is not None:
            with col2:
                st.write("**Fichier COUNTRY:**")
                st.dataframe(df_country.head(), use_container_width=True)
        
        col3, col4 = st.columns(2)
        
        if df_customer is not None:
            with col3:
                st.write("**Fichier CUSTOMER:**")
                st.dataframe(df_customer.head(), use_container_width=True)
        
        if df_employee is not None:
            with col4:
                st.write("**Fichier EMPLOYEE:**")
                st.dataframe(df_employee.head(), use_container_width=True)

st.markdown("---")

# VISUALISATION 1: Graphique ANNEE (Feuille 3)
if df_annee is not None:
    st.subheader("📈 Analyse par Année")
    
    # Détecter automatiquement les colonnes
    cols = df_annee.columns.tolist()
    st.write(f"Colonnes disponibles: {', '.join(cols)}")
    
    # Essayer de trouver les bonnes colonnes
    col_annee = next((col for col in cols if 'ann' in col.lower() or 'year' in col.lower()), cols[0])
    col_livree = next((col for col in cols if 'livr' in col.lower() and 'no' not in col.lower()), None)
    col_nolivree = next((col for col in cols if 'no' in col.lower() or 'non' in col.lower()), None)
    
    if col_livree and col_nolivree:
        fig_annee = go.Figure()
        fig_annee.add_trace(go.Bar(
            x=df_annee[col_annee],
            y=df_annee[col_livree],
            name='Livree',
            marker_color='#3b82f6'
        ))
        fig_annee.add_trace(go.Bar(
            x=df_annee[col_annee],
            y=df_annee[col_nolivree],
            name='NO Livree',
            marker_color='#f59e0b'
        ))
        fig_annee.update_layout(
            barmode='group',
            height=400,
            xaxis_title="Année",
            yaxis_title="Valeur"
        )
        st.plotly_chart(fig_annee, use_container_width=True)
    else:
        st.warning("⚠️ Colonnes 'Livree' et 'NO Livree' non détectées automatiquement")
        
else:
    st.info("📁 Importez le fichier ANNEE pour voir ce graphique")

st.markdown("---")

# VISUALISATION 2: Graphique COUNTRY (Feuille 4)
col_left, col_right = st.columns(2)

with col_left:
    if df_country is not None:
        st.subheader("🌍 Analyse par Pays")
        
        cols = df_country.columns.tolist()
        st.write(f"Colonnes: {', '.join(cols)}")
        
        col_country = next((col for col in cols if 'country' in col.lower() or 'pays' in col.lower()), cols[0])
        col_livree = next((col for col in cols if 'livr' in col.lower() and 'no' not in col.lower()), None)
        col_nolivree = next((col for col in cols if 'no' in col.lower() or 'non' in col.lower()), None)
        
        if col_livree and col_nolivree:
            fig_country = go.Figure()
            fig_country.add_trace(go.Bar(
                x=df_country[col_country],
                y=df_country[col_livree],
                name='Livree',
                marker_color='#3b82f6'
            ))
            fig_country.add_trace(go.Bar(
                x=df_country[col_country],
                y=df_country[col_nolivree],
                name='NO Livree',
                marker_color='#f59e0b'
            ))
            fig_country.update_layout(
                barmode='group',
                height=400,
                xaxis_title="Pays",
                yaxis_title="Valeur",
                xaxis_tickangle=-45
            )
            st.plotly_chart(fig_country, use_container_width=True)
        else:
            st.warning("⚠️ Colonnes non détectées")
    else:
        st.info("📁 Importez le fichier COUNTRY")

# VISUALISATION 3: Graphique CUSTOMER (Feuille 2)
with col_right:
    if df_customer is not None:
        st.subheader("🔵 Distribution Clients")
        
        cols = df_customer.columns.tolist()
        st.write(f"Colonnes: {', '.join(cols)}")
        
        col_customer = next((col for col in cols if 'customer' in col.lower() or 'client' in col.lower()), cols[0])
        col_livree = next((col for col in cols if 'livr' in col.lower() and 'no' not in col.lower()), None)
        col_nolivree = next((col for col in cols if 'no' in col.lower() or 'non' in col.lower()), None)
        
        if col_livree and col_nolivree:
            # Créer un graphique à barres groupées
            fig_customer = go.Figure()
            fig_customer.add_trace(go.Bar(
                x=df_customer[col_customer],
                y=df_customer[col_livree],
                name='Livree',
                marker_color='#3b82f6'
            ))
            fig_customer.add_trace(go.Bar(
                x=df_customer[col_customer],
                y=df_customer[col_nolivree],
                name='NO Livree',
                marker_color='#f59e0b'
            ))
            fig_customer.update_layout(
                barmode='group',
                height=400,
                xaxis_title="Customer ID",
                yaxis_title="Valeur",
                xaxis_tickangle=-45
            )
            st.plotly_chart(fig_customer, use_container_width=True)
        else:
            st.warning("⚠️ Colonnes non détectées")
    else:
        st.info("📁 Importez le fichier CUSTOMER")

st.markdown("---")

# VISUALISATION 4: Graphique EMPLOYEE (Feuille 1)
if df_employee is not None:
    st.subheader("👥 Performance Employés")
    
    cols = df_employee.columns.tolist()
    st.write(f"Colonnes disponibles: {', '.join(cols)}")
    
    col_employee = next((col for col in cols if 'employee' in col.lower() or 'employe' in col.lower()), cols[0])
    col_livre = next((col for col in cols if 'livr' in col.lower() and 'no' not in col.lower() and 'non' not in col.lower()), None)
    col_nonlivre = next((col for col in cols if 'no' in col.lower() or 'non' in col.lower()), None)
    
    if col_livre and col_nonlivre:
        fig_employee = go.Figure()
        fig_employee.add_trace(go.Bar(
            y=df_employee[col_employee].astype(str),
            x=df_employee[col_livre],
            name='Livre',
            orientation='h',
            marker_color='#3b82f6'
        ))
        fig_employee.add_trace(go.Bar(
            y=df_employee[col_employee].astype(str),
            x=df_employee[col_nonlivre],
            name='Non livre',
            orientation='h',
            marker_color='#f59e0b'
        ))
        fig_employee.update_layout(
            barmode='stack',
            height=500,
            xaxis_title="Valeur",
            yaxis_title="Employee ID"
        )
        st.plotly_chart(fig_employee, use_container_width=True)
    else:
        st.warning("⚠️ Colonnes 'Livre' et 'Non livre' non détectées")
else:
    st.info("📁 Importez le fichier EMPLOYEE pour voir ce graphique")

# Instructions
st.markdown("---")
st.markdown("""
### 📖 Guide d'utilisation

**Étape 1**: Dans la barre latérale (sidebar), importez vos 4 fichiers Excel:
- `ANNEE.xlsx` - Données par année
- `COUNTRY.xlsx` - Données par pays
- `CUSTOMER.xlsx` - Données clients
- `EMPLOYEE.xlsx` - Données employés

**Étape 2**: Les graphiques se génèrent automatiquement

**Étape 3**: Le script détecte automatiquement les colonnes contenant:
- Année/Year
- Country/Pays
- Customer/Client
- Employee/Employé
- Livree/Livre
- NO Livree/Non livree

💡 **Astuce**: Si les colonnes ne sont pas détectées, vérifiez leurs noms dans l'aperçu des données.
""")
