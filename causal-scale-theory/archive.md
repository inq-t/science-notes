# Source Archive and Provenance

The canonical CST notes were synthesized from two now-retired local master modules and a reviewed audit layer. Their complete directory trees are preserved under `sources/legacy/` and treated as immutable evidence. The SHA-256 values below verify the identity of named files; they do not contain or recover a missing source. The repository state immediately before retirement is Git commit `8eef728d80704f6529150afab6e086c5ce58212c`.

## Primary local inputs

[[causal-scale-theory/sources/legacy/causal-scale-master/entry|Causal Scale Dynamics v7 distilled entry]] is the clean older modular library. Its reviewed SHA-256 is

```
2D7AF51509FA16B5920842D5C18C70EAD11BDEB4D45D7AFFEBB80634850394FF
```

[[causal-scale-theory/sources/legacy/causal-scale-master/latest/Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]] is the long-form source snapshot. Its reviewed SHA-256 is

```
D42D5545AD61DD9BE052A07676D6E750D49C80F66AD147C7F390CC25CAD57169
```

[[causal-scale-theory/sources/legacy/causal-scale-master-v8/entry|The v8 proposed synthesis]] is the cumulative generalization and audit overlay. Its reviewed SHA-256 is

```
7782372C28899CE64FE07B9E1702952CC60BCFAC970834099F2AFAE676F4F423
```

[[causal-scale-theory/sources/legacy/causal-scale-master-v8/revision-audit|The v8 revision audit]] records what was accepted and withheld from its raw proposal. Its reviewed SHA-256 is

```
F8EC2C73A899FF0F46049542F65F3C3D7CB8BDD0E45E556E25FD5DDFAD7871E2
```

[[causal-scale-theory/sources/legacy/causal-scale-master-v8/receipts/background.py|The reviewed v8 background receipt]] has SHA-256

```
246A83BF720585520797643B50D5D31FB224DBBD4B24D700CDFE210699CAC838
```

## Corrective local dependencies

[[scale-as-modular-observable/claim-audit|The scale-observable claim audit]] owns the fixed-reference free-energy counterexample and the modular-rescaling diagnostic.

[[wall-construction-interface/entry|The wall-construction interface]] owns the shared cross-fiber object, binary-channel obligation, and anti-circularity tests.

[[compatible-with-existing-physics/entry|Compatibility with existing physics]] owns the distinction between importing a local GR/QFT fiber, conservatively restricting it, recovering it, and deriving it.

[[conservation-of-causal-charge/entry|Conservation of causal charge]] owns the wider philosophical and group-theoretic interpretation of the binary Casimir balance.

## Refactor history

The AI-authored pre-synthesis inventory, salvage ledger, receipt plan, quarantine, and migration plan are preserved under `junk-drawer/refactor-plan/`. [[junk-drawer/refactor-plan/refactor-audit|The synthesis audit]] records how that planning packet was corrected; [[junk-drawer/refactor-plan/retirement-audit|the retirement audit]] records the final salvage, rejection, delegation, receipt, and preservation decisions.

The exact v7 legacy tree retains its loose `latest/` snapshot and the original `causal_scale_dynamics_master_v7_0.zip`. For easier review, `sources/legacy/unpacked-v7-package/` is a convenience mirror of the ZIP's 65 entries, including section notes, referee notes, figures, and JSON outputs; no chats were observed in that package. The ZIP and the exact moved source tree remain the provenance objects, while the unpacked tree is only an access copy. The v8 tree likewise retains its notes and receipts. These local files, not the fingerprints alone, are the reviewable archive.

## Active retirement

`causal-scale-master` and `causal-scale-master-v8` are retired as active workspace modules. New theory links should target the versionless CST graph; historical links should target the local legacy trees. Retirement changes ownership, not provenance: the legacy files are preserved rather than rewritten, while commit `8eef728d80704f6529150afab6e086c5ce58212c` fixes the complete pre-retirement repository state.
