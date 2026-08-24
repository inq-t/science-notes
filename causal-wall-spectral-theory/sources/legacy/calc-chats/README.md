# Causal-Wall Calculation Chats

This directory preserves the unique provenance from the retired calculation side-module without promoting its conclusions. Original artifacts are copied byte-for-byte. The four chat-01 outputs already present in `causal-wall-spectral-theory/sources/legacy/v2-and-v2_1/` are intentionally not duplicated here.

The first frozen chat contains its [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-01-v2-referee/prompt|prompt]] and [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-01-v2-referee/response|response]]. Its [[causal-wall-spectral-theory/sources/legacy/v2-and-v2_1/verify_causal_wall_spectral_v2_1.py|original receipt script]], referee report, completion memo, and JSON output are preserved together as the v2.1 old version. The script is historical rather than a current receipt: it depends on third-party packages, writes to a session-specific path, and includes claims later revoked by version 3.

The second frozen chat contains its [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-02-a2-wall-attempt/prompt|prompt]], [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-02-a2-wall-attempt/response|response]], [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-02-a2-wall-attempt/outputs/a2-wall-calculation-v1|calculation memo]], [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-02-a2-wall-attempt/outputs/verify_a2_wall_v1.py|script]], and [[causal-wall-spectral-theory/sources/legacy/calc-chats/chat-02-a2-wall-attempt/outputs/a2_wall_receipts_v1.json|JSON output]]. [[a2-wall-rejection|The rejection note]] records why its classical $A_2$ arithmetic does not construct a causal wall.

## Integrity manifest

| Frozen artifact | SHA-256 |
|---|---|
| `chat-01-v2-referee/prompt.md` | `77199fed18f91df7a27854d5d0e9a5358546484b618c0c7a5be677ddc171795f` |
| `chat-01-v2-referee/response.md` | `ce9fd1926071315901744ca3b4ead45039192c3ff6bb5d59910acf6cec5497d3` |
| `chat-02-a2-wall-attempt/prompt.md` | `7c537e9dca6feb83dbd4429875e8d7fb06bb01d1817f3b517a7c92c86c1e1a47` |
| `chat-02-a2-wall-attempt/response.md` | `11fdec157cdeaabba1dcea484d4dd0e6b91d4c337dc551b419b9e8d55c418ab9` |
| `chat-02-a2-wall-attempt/outputs/a2-wall-calculation-v1.md` | `41499e60d438d9bfdc7fd1606147a53407e21b0f7620ed9d1b2bcbf1b46dda34` |
| `chat-02-a2-wall-attempt/outputs/verify_a2_wall_v1.py` | `6e035ebef5704ab88442f603329e7227883e6a4dca9b0964c1d6e54576b1754f` |
| `chat-02-a2-wall-attempt/outputs/a2_wall_receipts_v1.json` | `063b6dc3a6d695965dc06304c4d06ff5ccaa0ae6cd4d517cc570a39554b1eb08` |

These hashes identify the copied artifacts only. The present README and rejection note are later archival annotations.
