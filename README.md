# 🛡️ CodeGuardian

**CodeGuardian** è uno strumento avanzato per l'analisi statica del codice Python, progettato per rilevare vulnerabilità di sicurezza e bug comuni nei progetti Python.

## 🔍 Funzionalità principali
- ✅ **Rilevamento vulnerabilità di sicurezza**:
  - SQL Injection
  - Remote Code Execution (RCE)
  - Path Traversal
  - Command Injection
  - Uso pericoloso di `exec()`, `eval()`, `os.system()`, `subprocess.run()`, ecc.

- 🐛 **Individuazione di bug nel codice**:
  - Variabili non definite
  - Funzioni senza `return` coerente
  - Uso generico di `except Exception`
  - Import non utilizzati
  - Errori di sintassi
  - Loop infiniti

- ⚡ **Veloce ed efficace**:
  - Analizza **interi progetti o singoli file**
  - **Non esegue il codice**, quindi è sicuro da usare
  - Genera un report chiaro con dettagli su ogni problema rilevato

## 💻 Installazione
Assicurati di avere **Python 3.8+** installato.

```bash
# Clona il repository
git clone https://github.com/tuo-repo/codeguardian.git
cd codeguardian

# Installazione delle dipendenze (se necessarie)
pip install -r requirements.txt
```

## 🚀 Come usarlo
1. **Avvia CodeGuardian**
   ```bash
   python codeguardian.py
   ```
2. **Inserisci il percorso del file o della cartella da analizzare**
3. **Ottieni un report dettagliato con le vulnerabilità e i bug trovati!**

## 📌 Esempio di utilizzo
```bash
📂 Inserisci il percorso del file o della cartella: C:/Users/Utente/Desktop/progetto
🔍 Scansionando C:/Users/Utente/Desktop/progetto/main.py...
⚠️ SQL Injection trovato alla linea 12: query = "SELECT * FROM users WHERE username = '" + input()
🐛 Variabile non definita usata: 'user_name' alla linea 27
✅ Nessuna vulnerabilità o bug trovata nel file config.py
```

## 🛠️ Contributi
Se vuoi contribuire a CodeGuardian:
1. Fai un **fork** del repository
2. Crea un **branch** per la tua modifica
3. Manda una **pull request** con le tue migliorie

## 📜 Licenza
CodeGuardian è distribuito sotto la licenza **MIT**.

---
🔐 **Proteggi il tuo codice con CodeGuardian!** 🚀

