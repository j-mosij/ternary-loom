# Security

**Author: j-mosij**

## Strict rules for any copy or derivative

- The open shell check (`C == shell(A, B)`) must remain intact and visible.
- No `eval`, `exec`, `compile`, dynamic imports, or remote code loading may be added.
- The vehicle/container must remain write-free after construction.
- Attribution to j-mosij and this SECURITY.md must be retained.
- Public mirrors or forks that remove the integrity relation or add injection surfaces are unauthorized.

## Build integrity

- Pure Python standard library only at runtime.
- CI runs an injection scan on every push.
- No secrets, no private keys, no PQC private material are present (public integrity only).

## Reporting

Contact the author directly for security concerns. Do not open public issues with exploit details.
