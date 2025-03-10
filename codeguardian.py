import os
import re
import ast

VULNERABILITIES = {
    "SQL Injection": r"(SELECT|INSERT|UPDATE|DELETE).*['\"]?\s*\+.*input",
    "Exec (RCE)": r"exec\(",
    "Eval (RCE)": r"eval\(",
    "Path Traversal": r"(open|os.path.join)\(.*input",
    "Command Injection": r"os\.system\(.*input|subprocess\.run\(.*input",
}
BUGS = {
    "Uso di except generico": r"except\s+Exception:",
    "Possibile variabile non definita": r"print\((\w+)\)|(\w+)\s*=",
    "Import non utilizzato": r"import\s+(\w+)",
}

def scan_file(filepath):
    if not os.path.isfile(filepath):
        print(f"❌ Errore: {filepath} non è un file valido.")
        return []

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            content = f.read()
    except PermissionError:
        print(f"❌ Errore: Permesso negato per {filepath}.")
        return []

    issues = []

    for i, line in enumerate(lines, start=1):
        for vuln_name, pattern in VULNERABILITIES.items():
            if re.search(pattern, line):
                issues.append(f"⚠️ {vuln_name} alla linea {i}: {line.strip()}")

    for i, line in enumerate(lines, start=1):
        for bug_name, pattern in BUGS.items():
            if re.search(pattern, line):
                issues.append(f"🐛 {bug_name} alla linea {i}: {line.strip()}")

    try:
        tree = ast.parse(content, filename=filepath)
        defined_vars = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        defined_vars.add(target.id)
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                if node.id not in defined_vars and node.id not in dir(__builtins__):
                    issues.append(f"🐛 Variabile non definita usata: '{node.id}' alla linea {node.lineno}")
            elif isinstance(node, ast.FunctionDef):
                has_return = any(isinstance(n, ast.Return) for n in ast.walk(node))
                if not has_return:
                    issues.append(f"🐛 Funzione '{node.name}' potrebbe non restituire un valore.")
            elif isinstance(node, ast.Try):
                for handler in node.handlers:
                    if isinstance(handler.type, ast.Name) and handler.type.id == "Exception":
                        issues.append(f"⚠️ Uso generico di 'except Exception' alla linea {node.lineno}")

    except SyntaxError as e:
        issues.append(f"❌ Errore di sintassi: {e}")

    return issues

def analyze_project(directory):
    if not os.path.exists(directory):
        print(f"❌ Errore: La cartella '{directory}' non esiste.")
        return
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                print(f"🔍 Scansionando {filepath}...")
                issues = scan_file(filepath)
                if issues:
                    print("\n".join(issues))
                else:
                    print("✅ Nessuna vulnerabilità o bug trovata.\n")

if __name__ == "__main__":
    path = input("📂 Inserisci il percorso del file o della cartella: ").strip()

    if os.path.isfile(path):
        print(f"🔍 Scansionando il file: {path}")
        issues = scan_file(path)
        if issues:
            print("\n".join(issues))
        else:
            print("✅ Nessuna vulnerabilità o bug trovata.")
    
    elif os.path.isdir(path):
        analyze_project(path)
    
    else:
        print(f"❌ Errore: '{path}' non è un file o una cartella valida.")