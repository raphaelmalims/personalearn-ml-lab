"""Forward-only DAG demo for Tue Study block."""

from value import Value


def parent_names(v: Value) -> list[str]:
    out = []
    for p in v._prev:
        out.append(p.label or str(p.data))
    return out


def show(v: Value) -> None:
    op = v._op or "(leaf)"
    print(f"{v.label or v.data}: data={v.data}, op={op}, parents={parent_names(v)}")


def main() -> None:
    a = Value(2.0, label="a")
    b = Value(3.0, label="b")
    c = a + b
    c.label = "c"
    d = a * b
    d.label = "d"
    e = c * d
    e.label = "e"

    for node in (a, b, c, d, e):
        show(node)
    print(f"\nroot e.data = {e.data}")


if __name__ == "__main__":
    main()
