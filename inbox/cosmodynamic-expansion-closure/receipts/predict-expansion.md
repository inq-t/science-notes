# Expansion Closure Receipt

The script predict-expansion.py independently evaluates the provisional height--position--shape closure, integrates the dimensionless proper age, samples the expansion function, and verifies that radius, quasilocal mass, energy, horizon entropy, and canonical horizon temperature reconstruct one \(H\). Its default output is prediction.json.

Run it from the repository root with the bundled or any standard Python 3 interpreter:

    python inbox/cosmodynamic-expansion-closure/receipts/predict-expansion.py

A passing result establishes only formula implementation, quadrature convergence, regression against the canonical CST-B2 benchmark, and the horizon identities. The physical premises are not machine tests. Alternative arguments allow sensitivity calculations; `--output PATH` preserves such a run without overwriting the default benchmark, while `--no-write` prints it only. Nondefault fitted inputs must also declare `--omega-m-provenance` and `--omega-m-status`, which are written into the ledger so a provisional or conditional fit cannot masquerade as a generic prediction. The checked default is the frozen unit packet recorded in [[inbox/cosmodynamic-expansion-closure/prediction-ledger|the prediction ledger]].
