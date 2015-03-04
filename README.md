morph
===

Code runs and modifies itself, remapping variable names while preserving execution semantics.

```
$   cp morph.py temp.py
$   sha1sum temp.py
15a20ce6132c62f45f3e2cd50c9578291e2581a5  temp.py
$   ./temp.py
done
$   sha1sum temp.py
c90c8de25e2a93f7fb28d57d85ca632bb7bcf282  temp.py
