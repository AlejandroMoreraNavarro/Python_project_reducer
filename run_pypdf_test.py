from pathlib import Path
from reducer_core import reduce_project, generate_reduction_report, compute_dir_hash

def main():
    project_dir = Path("external/pypdf").resolve()
    entry_point = project_dir / "pypdf" / "__init__.py"
    output_dir = Path("work/pypdf_reduced").resolve()
    
    print(f"--- 1. Hash initial de l'original ---")
    hash_before = compute_dir_hash(project_dir)
    print(f"Fichiers originaux scannés : {len(hash_before)}")
    
    print(f"\n--- 2. Génération du rapport de réduction ---")
    report = generate_reduction_report(project_dir, entry_point)
    print(f"Nécessaires (.py atteints) : {len(report['necessary'])}")
    print(f"Par précaution (non-.py/auxiliaires) : {len(report['precaution'])}")
    print(f"Supprimés (.py inatteignables) : {len(report['removed'])}")
    print(f"Incertains : {len(report['uncertain'])}")
    
    print(f"\n--- 3. Exécution de la réduction vers {output_dir} ---")
    copied = reduce_project(project_dir, entry_point, output_dir)
    print(f"Fichiers copiés dans la version réduite : {len(copied)}")
    
    print(f"\n--- 4. Vérification de l'intégrité de l'original ---")
    hash_after = compute_dir_hash(project_dir)
    assert hash_before == hash_after, "ERREUR : L'original a été modifié !"
    print("Succès : Le projet original est resté strictement intact.")
    
    # Vérification des fichiers essentiels dans la copie réduite
    reduced_files = {p.relative_to(output_dir).as_posix() for p in output_dir.rglob("*.py")}
    assert any("pypdf" in f for f in reduced_files), "Le package pypdf est absent de la version réduite."
    print("Succès : Les fichiers essentiels de pypdf sont présents dans la copie réduite.")

if __name__ == "__main__":
    main()
