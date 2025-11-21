"""Safe math helpers for Project-Zero.

Provides a small helper `safe_division(a, b)` which avoids division-by-zero
errors. This module keeps the behaviour simple and deterministic so callers
can handle the `None` result explicitly.

Behaviour:
- If `b == 0` return `None` (caller should handle it).
- Otherwise return `a / b` as a float (or numeric type as Python computes).
"""
from __future__ import annotations
from typing import Optional

def safe_division(a: float, b: float) -> Optional[float]:
    """Return `a / b` or `None` if `b` is zero.

    This function does minimal validation and intentionally does not
    coerce non-numeric inputs. If `a` or `b` are not numeric, Python's
    normal exceptions will surface (TypeError).

    Examples:
    >>> safe_division(6, 3)
    2.0
    >>> safe_division(1, 0) is None
    True
    """
    try:
        if b == 0:
            return None
        return a / b
    except Exception:
        # Let callers see the error type for non-numeric inputs.
        raise
