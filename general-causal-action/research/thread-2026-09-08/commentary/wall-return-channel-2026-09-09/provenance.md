# Wall Return Receipt Provenance

This directory preserves the eight files accompanying the Claude review received on 2026-09-09. Each file was copied byte for byte from the live inbox and its SHA-256 checked against that source. The scripts and stored outputs were inspected; none was executed during this review. The stored numerical claims remain claims of the incoming packet, assessed in [[../claude-2026-09-09-00H40-assessment|the commentary assessment]].

Source directory: `general-causal-action/research/thread-2026-09-08/claude-inbox/wall-return-channel/`. The associated text is preserved as [[../claude-2026-09-09-00H40-547d20fe3b08|the received review]], SHA-256 `547D20FE3B0840BAD044FCCC0F92FB2C0C8FFFEF7F3AF228D0E08806BEB011C9`.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `README.md` | 1186 | `EC5484ACBE957A2EB0C834D260A95C46A72C2A20395EC6315E4158F3F1A68AF4` |
| `wall_receipt.py` | 3330 | `E9DAA1E87932822042271C6C87E7BC094ABBD806ADBC88FA46E0969733330C29` |
| `wall_fermion_verify.py` | 3813 | `B20CE07950E1D8A121AE4C404FF25FF1B74D4963D58F3223B3B1D41CA5235421` |
| `wall_fermion_rate.py` | 3714 | `CCBA4C9199690FF1397C72B33736EB7FC014B2C3C1F9A6ACAB43060642896310` |
| `wall_fermion_controls.py` | 2531 | `6223FE78C08EB94C97817DA883BDCBCD3CFBB2517BDD40212C578CF81AB3EFB0` |
| `verify_output.txt` | 2080 | `95D670D6C64579833D13FD08E1AF55F2A70CA45B04A997A1F21E86178A94821F` |
| `rate_output.txt` | 3377 | `AB7E894A059378285592589067DD2AF3C3B9BC873E120E2CB992FCB61E995013` |
| `controls_output.txt` | 1113 | `E15846D0DC96E76697D8244F23765887FCAE928148F6D5DF401C848BE157AC37` |

The text changed while the live inbox was being read: an earlier observed revision had SHA-256 `A629A466042842CDB93945BEDAEB36D314FAF6ED240BA3B1B5BE12FD91AA2681`. That earlier revision was not copied before replacement. The preserved text and completed assessment use the later revision identified above. The prior round's three live inbox files were also replaced externally; their earlier immutable commentary copies remain in the repository.

The incoming `wall_fermion_controls.py` has one trailing space on line 4. It is retained to preserve the source hash; the authored mathematical notes and assessment pass their separate whitespace checks.
